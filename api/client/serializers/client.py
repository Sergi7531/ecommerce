from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from client.models.ecommerce_client import EcommerceClient
from client.serializers.address import AddressSerializer


class MeSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        exclude = ('password', 'is_staff')


class EcommerceClientSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined', 'address')


class EcommerceClientCreationSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        read_only_fields = ('id',)


class EcommerceClientsSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name')
