from datetime import timedelta, datetime

from rest_framework.exceptions import ValidationError
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


class AddToCartSerializer(Serializer):
    user = CharField()

    def validate_user(self, user):
        if not ShoppingCart.objects.filter(user=user, timestamp__gte=datetime.now() + timedelta(hours=1)):
            raise ValidationError("Shopping cart doesn't belong to user.")

        return user

    def validate(self, attrs):
        pass

