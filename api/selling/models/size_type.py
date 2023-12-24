from django.db import models


class SizeType(models.Model):
    ADULT_CLOTHING_ID = 1
    ACCESSORIES_ID = 2

    name = models.CharField(max_length=20)
