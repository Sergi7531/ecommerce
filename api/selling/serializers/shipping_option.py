from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from selling.models import ShippingOption


class ShippingOptionSerializer(ModelSerializer):
    text = CharField(source='display_text')

    class Meta:
        model = ShippingOption
        fields = ('id', 'name', 'text', 'price')

