from django.db import models


class ShippingOption(models.Model):
    SHIPPING_OPTION_FREE_ID = 1
    SHIPPING_OPTION_STANDARD_ID = 2
    SHIPPING_OPTION_URGENT_ID = 3

    FREE_SHIPPING_MINIMUM_AMOUNT = 5000

    name = models.CharField(max_length=20)
    extra_text = models.CharField(max_length=50)
    price = models.IntegerField()

    @property
    def display_text(self):
        """
        Displays the shipping option information in a readable client-friendly way.
        """
        return f'{self.name} ({self.extra_text}).'