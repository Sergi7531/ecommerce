
class NudeProjectSizing:
    _SIZE_AMOUNT_CORRESPONDENCE = {
        'XS': 50,
        'S': 100,
        'M': 120,
        'L': 110,
        'XL': 40,
        'XXL': 25,
    }

    SIZE_TYPE_CLOTHING = 1
    SIZE_TYPE_ACCESSORIES = 2

    def __init__(self, product):
        self.product = product

    @property
    def sizes(self):
        """
        Sizes will be returned API-friendly format:
        {
            "size_type": (Depending on the product has sizes or not),
            "amount": Generated depending on the size. Check dict SIZE_AMOUNT_CORRESPONDENCE.
            "size_short": The size itself (for example: XS, S, M...)
        }
        """

        sizes = []

        sizes_container = self.product.select_one('.SizeSwatchList')

        if self.product.select_one(".SoldOut"):
            return sizes

        if sizes_container and not 'ONE SIZE' in sizes_container.text.strip():
            for size_short, amount in self._SIZE_AMOUNT_CORRESPONDENCE.items():
                sizes.append({"size_type": self.SIZE_TYPE_CLOTHING,
                              "size_short": size_short,
                              "amount": amount})
        else:
            sizes.append({"size_type": self.SIZE_TYPE_ACCESSORIES,
                          "size_short": "ONE SIZE",
                          "amount": 100})

        return sizes

    @staticmethod
    def size_short(size_element):
        size_short = size_element.text.strip()
        return size_short if len(size_short) <= 3 else size_element.select_one('a')['data-title']
