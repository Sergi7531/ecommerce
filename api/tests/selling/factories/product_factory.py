import random

import factory
from factory.django import DjangoModelFactory

from selling.models import Product

factory.Faker._DEFAULT_LOCALE = 'en_US'

class PredictableProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('text', max_nb_chars=100)
    description = factory.Faker('paragraph')
    price = random.randint(1000, 50000)
    published = factory.Faker('boolean')
