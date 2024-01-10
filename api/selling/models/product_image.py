from django.db import models

from common.models import SoftDeletionModel


class ProductImage(SoftDeletionModel):
    class ImageType(models.IntegerChoices):
        THUMBNAIL = 1, "Thumbnail"
        STOCK = 2, "Stock"

    product = models.ForeignKey('selling.Product', on_delete=models.CASCADE, related_name='images')
    type = models.IntegerField(choices=ImageType.choices)
    url = models.URLField()

    class Meta:
        ordering = ['type']
