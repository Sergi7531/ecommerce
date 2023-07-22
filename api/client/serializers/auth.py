from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import Serializer


class LoginSerializer(Serializer):
    email = EmailField()
    password = CharField()

