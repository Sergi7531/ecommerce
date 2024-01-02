from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from client.models import Address


class AddressSerializer(ModelSerializer):
    id = CharField(read_only=True)

    class Meta:
        model = Address
        fields = ('id', 'full_name', 'email', 'phone_number', 'full_road', 'extra_info', 'zip_code', 'city', 'country')
