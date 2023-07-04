import math

from django.db import models

from common.models import SoftDeletionModel
from selling.managers.product import ProductManager
from selling.models.brand import Brand


class Product(SoftDeletionModel):
    MEN = 'M'
    WOMEN = 'W'
    UNISEX = 'U'

    GENDER_CHOICES = (
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (UNISEX, 'Unisex'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    # IntegerField so we don't have to play with decimals in the backend.
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    published = models.BooleanField(default=False)

    tags = models.ManyToManyField('selling.Tag', related_name='products', blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    objects = ProductManager()

    @property
    def formatted_price(self):
        return math.ceil(self.price / 100)

    @property
    def trimmed_description(self):
        return f"{''.join(self.description.split()[:20])}..."
