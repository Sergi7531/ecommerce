from django.db import models


class ShoppingCartProduct(models.Model):
    cart = models.ForeignKey('selling.ShoppingCart', on_delete=models.CASCADE)
    product = models.ForeignKey('selling.Product', related_name='products', on_delete=models.CASCADE)
    sizing = models.ForeignKey('selling.Sizing', on_delete=models.CASCADE)
    amount = models.IntegerField()
