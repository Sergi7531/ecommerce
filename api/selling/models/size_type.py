from django.db import models


class SizeType(models.Model):
    ADULT_CLOTHING_ID = 1
    ADULT_SHOES_ID = 2
    KID_CLOTHING_ID = 3
    KID_SHOES_ID = 4
    ACCESSORIES_ID = 5

    name = models.CharField(max_length=20)
