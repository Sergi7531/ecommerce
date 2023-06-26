from django.utils import timezone

from common.models import SoftDeletionModel
from selling.common.utils import SUBTOTAL_DECIMALS
from selling.models import Product
from selling.models.user import User


class ShoppingCart(SoftDeletionModel):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products')
    discounts = models.ManyToManyField(Discount, related_name='discounts')

    @property
    def products_subtotal(self):
        return round(sum(product.price for product in self.products), SUBTOTAL_DECIMALS)

    @property
    def discounts_subtotal(self):
        return round(sum(discount.price for discount in self.discounts), SUBTOTAL_DECIMALS)

    @property
    def cart_subtotal(self):
        return self.subtotal_no_discounts - self.subtotal_discounts

    @property
    def timedelta(self):
        return timezone.now() - self.updated_at

    @property
    def shopping_cart_owner(self):
        return self.user.full_name
