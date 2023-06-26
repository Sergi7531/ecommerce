from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from selling.common.fields import ShoppingCartPriceField, ShoppingCartCharField
from selling.models.shopping_cart import ShoppingCart


class ShoppingCartSerializer(ModelSerializer):
    products_subtotal = ShoppingCartPriceField(source='products_subtotal')
    discounts_subtotal = ShoppingCartPriceField(source='discounts_subtotal')
    cart_subtotal = ShoppingCartPriceField(source='cart_subtotal')
    last_updated_at = ShoppingCartCharField(source='timedelta')
    cart_owner = ShoppingCartCharField(source='shopping_cart_owner')

    class Meta:
        model = ShoppingCart
        fields = ('products_subtotal', 'discounts_subtotal', 'cart_subtotal', 'last_updated_at', 'cart_owner')


class ShoppingCartAddProductSerializer(Serializer):
    product = CharField()
