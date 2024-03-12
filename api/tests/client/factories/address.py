from uuid import uuid4

import factory
from factory.django import DjangoModelFactory

from client.models import Address

factory.Faker._DEFAULT_LOCALE = 'es_ES'


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    id = factory.LazyFunction(uuid4)
    full_name = factory.Faker('name')
    email = factory.Faker('email')
    phone_number = factory.Faker('phone_number')
    full_road = factory.Faker('street_address')
    extra_info = factory.Faker('secondary_address')
    zip_code = factory.Faker('postcode')
    city = factory.Faker('city')
    country = factory.Faker('country')
