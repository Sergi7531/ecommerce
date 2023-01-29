from django.contrib.auth.models import User
from django.db import models

from common.models import SoftDeletionModel
from selling.managers.product import ProductManager


class Product(SoftDeletionModel):
    name = models.CharField(max_length=100)
    # IntegerField so we don't have to play with decimals in the backend. The front will be in charge of formatting the text
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()


class ShoppingCart(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    client = models.ForeignKey('client.Client', related_name='cart_client', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('Product', related_name='products_in_order')
    # total_pvp = models.IntegerField()

