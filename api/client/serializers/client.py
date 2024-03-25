from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from client.models.address import Address
from client.models.ecommerce_client import EcommerceClient
from client.serializers.address import AddressSerializer


class MeSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = EcommerceClient
        exclude = ('password', 'is_staff')


class EcommerceClientSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'address')

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if address_data:
            address_serializer = AddressSerializer(instance.address, data=address_data)
            address_serializer.is_valid(raise_exception=True)
            address_serializer.save()

        return instance


class EcommerceClientCreationSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        read_only_fields = ('id',)


class EcommerceClientsSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name')
