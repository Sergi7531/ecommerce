import random
import faker_commerce

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from selling.models import Product

factory.Faker._DEFAULT_LOCALE = 'en_US'


custom_faker = Faker()
custom_faker.add_provider(faker_commerce.Provider)

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product


    name = custom_faker.ecommerce_name()
    description = factory.Faker('paragraph')
    price = random.randint(1000, 50000)
    published = factory.Faker('boolean')
