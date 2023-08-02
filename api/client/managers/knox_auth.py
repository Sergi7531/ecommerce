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
        self.check_tokens()
        token_ttl = self.view_class.get_token_ttl()

        instance, token = AuthToken.objects.create(self.client, token_ttl)
        user_logged_in.send(sender=self.client.__class__,
                            request=self.request, user=self.client)

        return token

    def check_tokens(self):
        token_limit_per_user = self.view_class.get_token_limit_per_user()
        if token_limit_per_user is not None:
            now = timezone.now()
            token = self.client.auth_token_set.filter(expiry__gt=now)
            if token.count() >= token_limit_per_user:
                raise ValidationError('The maximum amount of tokens for this user has been exceeded.')
