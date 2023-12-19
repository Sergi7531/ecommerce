from rest_framework.fields import FloatField, Field, CharField


class ShoppingCartBaseField(Field):

    def __init__(self, **kwargs):
        self.read_only = True
        super().__init__(**kwargs)


class ShoppingCartCharField(ShoppingCartBaseField, CharField):
    pass


class ShoppingCartPriceField(ShoppingCartBaseField, FloatField):
    pass
    # def get_value(self, dictionary):
    #     return super().get_value() / 100
