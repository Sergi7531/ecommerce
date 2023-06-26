from django.db import models

from api.common.models import SoftDeletionModel


class Brand(SoftDeletionModel):
    BRAND_NIKE_ID = 1
    BRAND_ADIDAS_ID = 2
    BRAND_CALVIN_KLEIN_ID = 3
    BRAND_THE_NORTH_FACE_ID = 4
    BRAND_PUMA_ID = 5
    BRAND_TOMMY_HILFIGER_ID = 6
    BRAND_VANS_ID = 7

    name = models.CharField(max_length=60)
    url_slug = models.SlugField()
    # categories = models.ManyToManyField('selling.Category', related_name='brand_category', blank=True)
