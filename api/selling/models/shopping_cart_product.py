from django.db import models


class ShoppingCartProduct(models.Model):
    cart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name='products', on_delete=models.CASCADE)
    sizing = models.ForeignKey('Sizing', on_delete=models.CASCADE)
    amount = models.IntegerField()
