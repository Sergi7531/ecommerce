from django.db import models

from common.models import SoftDeletionModel
from selling.models.enums.accessories import AccessoriesSize
from selling.models.enums.adult_sizing import AdultSizing
from selling.models.size_type import SizeType


class Sizing(SoftDeletionModel):
    _SIZE_TYPE_TO_CLASS = {
        SizeType.ADULT_CLOTHING_ID: AdultSizing.ClothingSize,
        SizeType.ACCESSORIES_ID: AccessoriesSize
    }

    size_type = models.ForeignKey(SizeType, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    size_short = models.CharField(max_length=8)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='sizes')

    class Meta:
        unique_together = ('product', 'size_type', 'size_short')

    @classmethod
    def choices_by_type(cls, size_type):
        return cls._SIZE_TYPE_TO_CLASS[size_type].values
