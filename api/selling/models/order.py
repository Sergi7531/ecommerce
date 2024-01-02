from django.db import models

from common.models import SoftDeletionModel


class Order(SoftDeletionModel):
    shopping_cart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE, related_name='orders')
    address = models.ForeignKey('client.Address', on_delete=models.CASCADE)
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE)
    # discount = models.ForeignKey('Discount', on_delete=models.CASCADE)
    shipping = models.ForeignKey('ShippingOption', on_delete=models.CASCADE)
