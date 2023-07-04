from rest_framework.serializers import ModelSerializer

from client.models import EcommerceClient


class EcommerceClientSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        exclude = ('password', 'updated_at', 'deleted_at', 'is_staff', 'system_user', 'is_deleted')


class EcommerceClientCreationSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        read_only_fields = ('id',)


class EcommerceClientsSerializer(ModelSerializer):
    class Meta:
        model = EcommerceClient
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login')
