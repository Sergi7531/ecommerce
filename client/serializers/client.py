from rest_framework.serializers import ModelSerializer

from client.models import Client


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        exclude = ('password', 'updated_at', 'deleted_at', 'is_staff', 'system_user', 'is_deleted')


class ClientCreationSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        read_only_fields = ('id', )

class ClientsSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login')
