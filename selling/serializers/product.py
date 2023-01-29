from rest_framework.serializers import ModelSerializer

from selling.models import Product


class ProductsSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreationSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'price', 'stock')


class ProductUpdateSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ('id', 'created_at', 'updated_at', 'deleted_at')
