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
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'deleted_at')


class ProductCreateUpdateSerializer(ModelSerializer):
    sizes = SizingSerializer(source='sizings', many=True, required=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'tags', 'image_url', 'sizes', 'published')

    def validate_sizes(self, sizes):
        product = self.instance
        all_size_types = set(size['size_type'].id for size in sizes)

        if not product.sizes.filter(size_type__in=all_size_types) and product.sizes.count() > 0 or \
                len(all_size_types) > 1:
            raise ValidationError('Invalid sizing, all product sizes must be same kind')

        for size in sizes:
            if size['size_short'] not in Sizing.choices_by_type(size['size_type'].id):
                raise ValidationError('Invalid sizing for size type')

        return sizes


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
