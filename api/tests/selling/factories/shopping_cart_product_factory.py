import random

import factory
from factory.django import DjangoModelFactory

from selling.models import Sizing, Product
from selling.models.shopping_cart_product import ShoppingCartProduct
from tests.selling.factories.product_factory import PredictableProductFactory


class ShoppingCartProductBuildableFactory(DjangoModelFactory):
    class Meta:
        model = ShoppingCartProduct

    product = factory.SubFactory(PredictableProductFactory)
    sizing = factory.Iterator(Sizing.objects.all())

    @factory.lazy_attribute
    def amount(self):
        return random.randint(0, self.product.total_stock)