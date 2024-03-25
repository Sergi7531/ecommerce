from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from client.serializers.address import AddressSerializer
from client.serializers.client import EcommerceClientSerializer
from selling.models.order import Order
from selling.models.shipping_option import ShippingOption
from selling.serializers.payment_method import PaymentMethodSerializer
from selling.serializers.shipping_option import ShippingOptionSerializer
from selling.serializers.shopping_cart import ShoppingCartSerializer


class OrderInputSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('shopping_cart', 'address', 'payment_method', 'shipping')

    def validate(self, attrs):
        if attrs['shipping'].id == ShippingOption.SHIPPING_OPTION_FREE_ID and \
                not attrs['shopping_cart'].cart_subtotal >= ShippingOption.FREE_SHIPPING_MINIMUM_AMOUNT:
            raise ValidationError('Your order is not elegible for free shipping.')

        return attrs


class OrderOutputSerializer(ModelSerializer):
    order_id = CharField(source='id')
    shopping_cart = ShoppingCartSerializer()
    user = EcommerceClientSerializer(source='shopping_cart.user')
    address = AddressSerializer()
    payment_method = PaymentMethodSerializer()
    shipping = ShippingOptionSerializer()

    class Meta:
        model = Order
        fields = ('order_id', 'shopping_cart', 'user', 'address', 'payment_method', 'shipping')
