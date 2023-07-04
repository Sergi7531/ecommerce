from django.db import models
from django.utils import timezone

from client.models import EcommerceClient
from common.models import SoftDeletionModel
from selling.common.utils import SUBTOTAL_DECIMALS
from selling.models import Product


class ShoppingCart(SoftDeletionModel):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(EcommerceClient, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products')
    # discounts = models.ManyToManyField(Discount, related_name='discounts')

    @property
    def products_subtotal_no_discounts(self):
        return round(sum(product.price for product in self.products), SUBTOTAL_DECIMALS) or 0

    @property
    def discounts_subtotal(self):
        return round(sum(discount.price for discount in self.discounts), SUBTOTAL_DECIMALS) or 0

    @property
    def cart_subtotal(self):
        return self.products_subtotal_no_discounts - self.discounts_subtotal or 0

    @property
    def timedelta(self):
        return timezone.now() - self.updated_at

    @property
    def shopping_cart_owner(self):
        return self.user.full_name
