import factory
from myapp.models import YourModel


class YourModelFactory(factory.Factory):
    class Meta:
        model = YourModel

    field1 = factory.Faker('word')
    field2 = factory.Faker('sentence')
