from django.db import models
from django.utils import timezone


class ShoppingCartManager(models.Manager):
    class ShoppingCartQuerySet(models.QuerySet):

        def delete(self):
            return super().update(deleted_at=timezone.now())

        def hard_delete(self):
            return super().delete()

        def alive(self):
            return self.filter(deleted_at=None)

        def dead(self):
            return self.exclude(deleted_at=None)

    def __init__(self, *args, **kwargs):
        self.expired = kwargs.pop('expired', False)
        super(ShoppingCartManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.expired and self.expired is False:
            return ShoppingCartManager.ShoppingCartQuerySet(self.model).filter(expiry__gt=timezone.now())
        return ShoppingCartManager.ShoppingCartQuerySet(self.model)
