from datetime import timedelta

from django.db import models
from django.utils import timezone

from client.models.ecommerce_client import EcommerceClient
from common.models import SoftDeletionModel
from selling.common.utils import SUBTOTAL_DECIMALS
from selling.managers.shopping_cart import ShoppingCartManager
from selling.models import Product
from selling.models.shopping_cart_product import ShoppingCartProduct


class ShoppingCart(SoftDeletionModel):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(EcommerceClient, on_delete=models.CASCADE)
    products = models.ManyToManyField('ShoppingCartProduct', related_name='products_in_cart')
    # discounts = models.ManyToManyField(Discount, related_name='discounts')

    objects = ShoppingCartManager(expired=False)
    all_objects = ShoppingCartManager()

    @property
    def products_subtotal_no_discounts(self):
        return round(sum(cart_product.product.price * cart_product.amount for cart_product in self.products.all()), SUBTOTAL_DECIMALS) or 0

    @property
    def discounts_subtotal(self):
        return 0
        # return round(sum(discount.price for discount in self.discounts), SUBTOTAL_DECIMALS) or 0

    @property
    def total_products_amount(self):
        return sum(product.amount for product in self.products.all())

    @property
    def cart_subtotal(self):
        return self.products_subtotal_no_discounts - self.discounts_subtotal or 0

    @property
    def shopping_cart_owner(self):
        return self.user.full_name

    @property
    def expiry(self):
        return self.updated_at + timedelta(hours=2)

    def add_product_to_cart(self, product, sizing, amount=1):
        cart_product, created = ShoppingCartProduct.objects.get_or_create(
            cart=self,
            product=product,
            sizing=sizing,
            defaults={'amount': amount}
        )

        self.products.add(cart_product)

        # If the product already exists in the cart, increment the amount
        if not created:
            cart_product.amount += amount
            cart_product.save()

        return cart_product
