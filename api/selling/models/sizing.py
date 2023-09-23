from django.db import models

from selling.models.enums.adult_sizing import AdultSizing
from selling.models.enums.kid_sizing import KidSizing
from selling.models.size_type import SizeType


class Sizing(models.Model):
    _SIZE_TYPE_TO_CLASS = {
        SizeType.ADULT_CLOTHING_ID: AdultSizing.ClothingSize,
        SizeType.ADULT_SHOES_ID: AdultSizing.ShoeSize,
        SizeType.KID_CLOTHING_ID: KidSizing.ClothingSize,
        SizeType.KID_SHOES_ID: KidSizing.ShoeSize,
    }

    size_type = models.ForeignKey(SizeType, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    size_short = models.CharField(max_length=7)

    @classmethod
    def choices_by_type(cls, size_type):
        return cls._SIZE_TYPE_TO_CLASS[size_type].values
