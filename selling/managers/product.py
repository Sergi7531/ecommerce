from django.db import models

from common.managers import SoftDeletionManager


class ProductManager(SoftDeletionManager):

    def decrease_stock(self):
        pass
