from common.managers import SoftDeletionManager


class ProductManager(SoftDeletionManager):

    def decrease_stock(self):
        pass

    def add_to_cart(self):
        return
