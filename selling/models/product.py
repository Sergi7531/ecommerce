from django.contrib.auth.models import User
from django.db import models

from common.models import SoftDeletionModel
from selling.managers.product import ProductManager


class Product(SoftDeletionModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # IntegerField so we don't have to play with decimals in the backend.
    # The front will be in charge of formatting the text
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    published = models.BooleanField(default=False)

    tags = models.ManyToManyField('selling.Tag', related_name='products_matching', blank=True)

    objects = ProductManager()
