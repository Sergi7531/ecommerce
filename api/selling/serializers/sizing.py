from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from selling.models import Product
from selling.models.sizing import Sizing


class SizingsSerializer(ModelSerializer):
    class Meta:
        model = Sizing
        fields = ('size_type', 'amount', 'size_short')


class SizingSerializer(ModelSerializer):
    class Meta:
        model = Sizing
        fields = '__all__'

    def validate(self, attrs):
        product = Product.objects.get(id=self.initial_data['product_id'])
        if not product.sizes.filter(size_type=attrs['size_type']) and product.sizes.all().count() > 0:
            raise ValidationError('Invalid sizing, all product sizes must be same kind')

        if attrs['size_short'] not in Sizing.choices_by_type(attrs['size_type'].id):
            raise ValidationError('Invalid sizing for size type')

        return attrs

