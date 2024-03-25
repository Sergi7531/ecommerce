from uuid import uuid4

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from client.models.address import Address

factory.Faker._DEFAULT_LOCALE = 'es_ES'

faker_provider = Faker(locale='es_ES')

class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    id = factory.LazyFunction(uuid4)
    full_name = factory.Faker('name')
    email = factory.Faker('email')
    phone_number = factory.LazyAttribute(lambda n: faker_provider.phone_number()[:10])
    full_road = factory.Faker('street_address')
    extra_info = factory.Faker('secondary_address')
    zip_code = factory.Faker('postcode')
    city = factory.Faker('city')
    country = factory.Faker('country')
