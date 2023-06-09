from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from common.managers import SoftDeletionManager
from common.models import SoftDeletionModel


class Client(AbstractBaseUser, SoftDeletionModel):
    username = models.CharField(max_length=30, default=None, null=True)
    first_name = models.CharField(max_length=30, default=None, null=True)
    last_name = models.CharField(max_length=30, default=None, null=True)
    email = models.EmailField(max_length=190, null=False, blank=False, unique=True)
    # client = models.ForeignKey('selling.models.ShoppingCart', related_name='cart_client', on_delete=models.CASCADE)

    is_staff = models.BooleanField(default=False)
    system_user = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)
