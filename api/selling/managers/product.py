from common.managers import SoftDeletionManager


class ProductManager(SoftDeletionManager):

    def decrease_stock(self, instance):
        if instance.stock >= 0:
            instance.stock -= 1
        return instance.stock >= 0

    def add_to_cart(self):
        pass
