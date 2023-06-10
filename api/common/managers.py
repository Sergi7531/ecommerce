from django.db import models
from django.utils import timezone


class SoftDeletionManager(models.Manager):
    class SoftDeletionQuerySet(models.QuerySet):

        def delete(self):
            return super().update(deleted_at=timezone.now())

        def hard_delete(self):
            return super().delete()

        def alive(self):
            return self.filter(deleted_at=None)

        def dead(self):
            return self.exclude(deleted_at=None)

    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionManager.SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionManager.SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()

    def get_by_id(self, id):
        return self.get(id=id)
