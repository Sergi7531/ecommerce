import random

import factory
from factory.django import DjangoModelFactory

from selling.models import Product
from selling.models.shopping_cart import ShoppingCart
from tests.client.factories.ecommerce_client import EcommerceClientFactory
from tests.selling.factories.shopping_cart_product_factory import ShoppingCartProductBuildableFactory


class ShoppingCartFactory(DjangoModelFactory):
    class Meta:
        model = ShoppingCart

    user = factory.SubFactory(EcommerceClientFactory)


    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product in extracted:
                self.products.add(ShoppingCartProductBuildableFactory(cart=self, product=product))
        else:
            existing_products = Product.objects.all()
            for i in range(random.randint(1, 5)):
                self.products.add(ShoppingCartProductBuildableFactory(cart=self,
                                                                      product=random.choice(existing_products)))
