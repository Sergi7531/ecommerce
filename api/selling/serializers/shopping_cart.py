from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer, Serializer

from selling.common.fields import ShoppingCartPriceField, ShoppingCartCharField
from selling.models import Product
from selling.models.shopping_cart import ShoppingCart
from selling.models.shopping_cart_product import ShoppingCartProduct
from selling.models.sizing import Sizing
from selling.serializers.product import ProductSerializer
from selling.serializers.sizing import SizingSerializer


class ShoppingCartProductSerializer(ModelSerializer):
    product = ProductSerializer()
    sizing = SizingSerializer()

    class Meta:
        model = ShoppingCartProduct
        fields = ('product', 'sizing', 'amount')


class ShoppingCartSerializer(ModelSerializer):
    products = ShoppingCartProductSerializer(many=True)
    products_subtotal = ShoppingCartPriceField(source='products_subtotal_no_discounts')
    discounts_subtotal = ShoppingCartPriceField()
    cart_subtotal = ShoppingCartPriceField()
    last_updated_at = ShoppingCartCharField(source='updated_at')
    cart_owner = ShoppingCartCharField(source='shopping_cart_owner')

    class Meta:
        model = ShoppingCart
        fields = ('products', 'products_subtotal', 'discounts_subtotal',
                  'cart_subtotal', 'last_updated_at', 'cart_owner')


class AddToCartSerializer(Serializer):
    product = serializers.UUIDField()
    sizing = serializers.UUIDField()

    def _validate_product(self, product):
        return get_object_or_404(Product.objects.all(), id=product)

    def _validate_sizing(self, sizing):
        return get_object_or_404(Sizing.objects.filter(product=self.product), id=sizing)

    # def validate(self, attrs):
    #     product = attrs['product']
    #
    #     if not self._validate_product(product) and self._validate_sizing(sizing=attrs['sizing'], product=product):
    #         raise
    #
    #     return attrs
