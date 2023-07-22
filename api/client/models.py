from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


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
