from rest_framework.serializers import ModelSerializer

from selling.models import Order


class OrderInputSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('shopping_cart', 'address', 'payment_method', 'shipping')