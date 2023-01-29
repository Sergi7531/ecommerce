from django.db import models


class ProductManager(models.Manager):

    def decrease_stock(self):
        pass