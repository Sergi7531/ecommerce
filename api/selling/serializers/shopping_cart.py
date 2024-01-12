from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField
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
    products_subtotal = ShoppingCartPriceField(source='products_subtotal_no_discounts', read_only=True)
    discounts_subtotal = ShoppingCartPriceField(read_only=True)
    cart_subtotal = ShoppingCartPriceField(read_only=True)
    last_updated_at = ShoppingCartCharField(source='updated_at', read_only=True)
    cart_owner = ShoppingCartCharField(source='shopping_cart_owner', read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ('id', 'total_products_amount', 'products', 'products_subtotal', 'discounts_subtotal',
                  'cart_subtotal', 'last_updated_at', 'cart_owner')


class AddToCartSerializer(Serializer):
    product_id = serializers.UUIDField()
    sizing_id = serializers.UUIDField()
    amount = IntegerField()

    def _validate_product(self, product):
        return get_object_or_404(Product.objects.all(), id=product)

    def _validate_sizing(self, sizing):
        return get_object_or_404(Sizing.objects.filter(product=self.product), id=sizing)




class CartUpdateSerializer(ModelSerializer):
    products = AddToCartSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = ('products',)

    def update(self, instance, validated_data):
        cart_products = validated_data.pop('products', [])
        cart = super().update(instance, validated_data)
        # product_ids = [cart_product['product'] for cart_product in cart_products]
        ShoppingCartProduct.objects.filter(cart=cart).delete()

        for cart_product in cart_products:
            cart_product['product_id'] = cart_product.pop('product_id')
            cart_product['sizing_id'] = cart_product.pop('sizing_id')
            cart_product_data = {**cart_product, **{'cart': cart}}
            shopping_cart_product, _ = ShoppingCartProduct.objects.get_or_create(**cart_product_data)
            cart.products.add(shopping_cart_product)
            cart.save()

        return cart
