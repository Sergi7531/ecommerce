from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from client.models import EcommerceClient


class MeSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        exclude = ('password', 'is_staff')


class EcommerceClientSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')


class EcommerceClientCreationSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        read_only_fields = ('id',)


class EcommerceClientsSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name')
