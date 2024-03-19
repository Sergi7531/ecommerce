from uuid import uuid4

import factory

from factory.django import DjangoModelFactory

from client.models import EcommerceClient
from tests.client.factories.address import AddressFactory

factory.Faker._DEFAULT_LOCALE = 'es_ES'

class EcommerceClientFactory(DjangoModelFactory):
    class Meta:
        model = EcommerceClient

    id = factory.LazyFunction(uuid4)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    address = factory.SubFactory(AddressFactory)
    password = factory.django.Password(factory.Faker('password'))


class EcommerceClientPredictableLoginFactory(EcommerceClientFactory):
    class Meta:
        model = EcommerceClient
        skip_postgeneration_save = True

    email = 'test123456789@example.com'
    password = factory.PostGenerationMethodCall('set_password', 'testing_password123')


class EcommerceClientWithoutAddressFactory(EcommerceClientPredictableLoginFactory):
    class Meta:
        model = EcommerceClient
        skip_postgeneration_save = True

    address = None