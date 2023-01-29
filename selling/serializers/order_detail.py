from rest_framework.serializers import ModelSerializer

from selling.models import OrderDetail
from selling.serializers.order import OrdersSerializer
from selling.serializers.product import ProductsSerializer


class OrderDetailCreationSerializer(ModelSerializer):
    order = OrdersSerializer()
    order = ProductsSerializer()

    class Meta:
        model = OrderDetail
        fields = ('order', 'amount', 'product')
