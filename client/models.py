from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from common.managers import SoftDeletionManager
from common.models import SoftDeletionModel


class Client(AbstractBaseUser, SoftDeletionModel):
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=30, default=None, null=True)
    first_name = models.CharField(max_length=30, default=None, null=True)
    last_name = models.CharField(max_length=30, default=None, null=True)
    email = models.EmailField(max_length=190, null=False, blank=False, unique=True)

    is_staff = models.BooleanField(default=False)
    system_user = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)
    # updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # deleted_at = models.DateTimeField(auto_now_add=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)
