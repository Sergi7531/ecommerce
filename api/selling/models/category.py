from django.db import models

from api.common.models import SoftDeletionModel


class Category(SoftDeletionModel):
    name = models.CharField(max_length=80)
    relevance = models.IntegerField()

