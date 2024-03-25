from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from knox.models import AuthToken

from client.models.address import Address
from selling.models.shopping_cart import ShoppingCart


class EcommerceClient(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=256)

    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

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

    @property
    def shopping_cart(self):
        shopping_cart, _ = ShoppingCart.objects.get_or_create(user=self)

        return shopping_cart
