from django.conf import settings
from knox.models import AuthToken
from rest_framework.fields import CharField, EmailField, UUIDField
from rest_framework.serializers import Serializer


class LoginSerializer(Serializer):
    email = EmailField()
    password = CharField()


class LogoutSerializer(Serializer):
    token = CharField(max_length=settings.REST_KNOX['AUTH_TOKEN_CHARACTER_LENGTH'])

    def validate_token(self, token):
        return AuthToken.objects.filter(token=token)
