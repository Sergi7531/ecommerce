from django.db import models

from selling.models.enums.adult_sizing import AdultSizing
from selling.models.enums.kid_sizing import KidSizing
from selling.models.size_type import SizeType


class ProductSizing(models.Model):
    _SIZE_TYPE_TO_CLASS = {
        SizeType.ADULT_CLOTHING: AdultSizing.ClothingSize,
        SizeType.ADULT_SHOES: AdultSizing.ShoeSize,
        SizeType.KID_CLOTHING: KidSizing.ClothingSize,
        SizeType.KID_SHOES: KidSizing.ShoeSize,
    }

    product = models.ForeignKey('selling.Product', on_delete=models.CASCADE)
    size_type = models.ForeignKey(SizeType, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    size_short = models.CharField(max_length=7)

    @property
    def choices_by_type(self):
        return self._SIZE_TYPE_TO_CLASS[self.size_type].values
