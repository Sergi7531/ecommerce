from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    relevance = models.IntegerField()

    related_tags = models.ManyToManyField('self', related_name='tags_related')

