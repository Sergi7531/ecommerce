from django.db import models


class ShippingOption(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
