from knox.views import LoginView
from django.contrib.auth import user_logged_in
from django.db.models.manager import BaseManager
from django.utils import timezone
from knox.models import AuthToken
from rest_framework.exceptions import ValidationError


class KnoxAuthManager(BaseManager):
    view_class = LoginView()

    def __init__(self, request, client):
        self.request = request
        self.client = client

    def knox_login(self):
        token_ttl = self.view_class.get_token_ttl()

        instance, token = AuthToken.objects.create(self.client, token_ttl)
        user_logged_in.send(sender=self.client.__class__,
                            request=self.request, user=self.client)

        return token
