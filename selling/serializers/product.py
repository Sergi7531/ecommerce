from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField, CharField, ListField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from selling.models import Product, Tag


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'published', 'tags')


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'deleted_at')


class ProductCreationSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'description', 'tags')


class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ('id', 'created_at', 'updated_at', 'deleted_at')


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

    def validate(self, attrs):
        self.validate_prices(attrs)
        return attrs
