from django.db import models


class SizeType(models.Model):
    ADULT_CLOTHING = 1
    ADULT_SHOES = 2
    KID_CLOTHING = 3
    KID_SHOES = 4
    ACCESSORIES = 5

    name = models.CharField(max_length=20)
