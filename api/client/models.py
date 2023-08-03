from uuid import uuid4

from django.contrib.auth import user_logged_in
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from knox.models import AuthToken
from rest_framework import request, status
from rest_framework.response import Response


class EcommerceClient(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = False

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def set_password(self, raw_password):
        super(EcommerceClient, self).set_password(raw_password)
        self.save()

    def has_token(self, auth_token):
        token_key = auth_token[:7]
        return bool(list(AuthToken.objects.filter(user_id=self.id,
                                                  token_key=token_key)))

    def remove_token(self, auth_token):
        token_key = auth_token[:7]
        return AuthToken.objects.filter(user_id=self.id,
                                        token_key=token_key).delete()
