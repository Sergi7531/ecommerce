from django.db import models

from common.models import SoftDeletionModel


class Address(SoftDeletionModel):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    road = models.CharField(max_length=100)
    number = models.IntegerField()
    extra_info = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
