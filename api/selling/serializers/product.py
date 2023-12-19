from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField, CharField
from rest_framework.serializers import ModelSerializer, Serializer

from selling.models import Product
from selling.models.sizing import Sizing
from selling.serializers.sizing import SizingSerializer


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'published', 'tags', 'trimmed_description')


class ProductSerializer(ModelSerializer):
    sizes = SizingSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'published', 'image_url', 'tags', 'sizes')


class ProductCreateUpdateSerializer(ModelSerializer):
    sizes = SizingSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'tags', 'image_url', 'sizes', 'published')

    def validate_sizes(self, sizes):
        product = self.instance
        all_size_types = set(size['size_type'].id for size in sizes)

        invalid_sizing_msg = 'Invalid sizing, all product sizes must be same kind'

        if product:
            if not product.sizes.filter(size_type__in=all_size_types) and product.sizes.count() > 0:
                raise ValidationError(invalid_sizing_msg)
        else:
            if len(all_size_types) > 1:
                raise ValidationError(invalid_sizing_msg)

        for size in sizes:
            if size['size_short'] not in Sizing.choices_by_type(size['size_type'].id):
                raise ValidationError('Invalid sizing for size type')

        return sizes

    def create(self, validated_data):
        sizings = validated_data.pop('sizes', [])

        product = super().create(validated_data)

        for sizing in sizings:
            sizing_data = {**sizing, **{'product': product}}
            Sizing(**sizing_data).save()

        return product

    def update(self, instance, validated_data):
        sizings = validated_data.pop('sizes', [])
        product = super().update(instance, validated_data)
        Sizing.objects.filter(product=product).delete()

        for sizing in sizings:
            sizing_data = {**sizing, **{'product': product}}
            Sizing(**sizing_data).save()

        return product


class ProductsQueryParamsSerializer(Serializer):
    min_price = IntegerField(required=False, default=None)
    max_price = IntegerField(required=False, default=None)
    name = CharField(required=False, default=None)
    # TODO: Fix only 1 PK allowed, when more than 1 entered (1,2 for example) field validation error is raised.
    tags = CharField(required=False, default=None)

    def validate_prices(self, attrs):
        if attrs['min_price'] is not None and attrs['max_price'] is not None:
            if not attrs['min_price'] <= attrs['max_price']:
                raise ValidationError('Minimum price must be lower than maximum price.')
