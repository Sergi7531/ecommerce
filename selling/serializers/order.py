from rest_framework.serializers import ModelSerializer

from selling.models import Order


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrdersSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = 'date_time'


class OrderCreationSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ('amount')