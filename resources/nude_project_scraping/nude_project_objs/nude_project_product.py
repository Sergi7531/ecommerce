from resources.nude_project_scraping.nude_project_objs.nude_project_base_class import NudeProjectBaseClass
from resources.nude_project_scraping.nude_project_objs.nude_project_size import NudeProjectSizing


class NudeProjectProduct(NudeProjectBaseClass):
    _IMAGE_TYPE_THUMBNAIL = 1
    _IMAGE_TYPE_STOCK = 2

    def __init__(self, product_item):
        self.product_item = product_item

    @property
    def name(self):
        return self.product_item.select_one('.ProductItem__Title a').text.strip()

    @property
    def product_detail_url(self):
        return f"{self.base_website_url}{self.product_item.select_one('.ProductItem__Title a')['href']}"

    @property
    def description(self):
        return self.product_item.select_one('.ProductItem__Title a').text.strip()

    @property
    def price(self):
        return float(
            self.product_item.select_one('.ProductItem__Price').text.strip().replace('€', '').replace(',', '.'))

    @property
    def _product_non_formatted_url(self):
        return f"https:{self.product_item.select_one('.ProductItem__Image')['data-src']}"

    @property
    def all_product_images(self):
        all_image_sizes = self.product_item.select_one('.ProductItem__Image')['data-widths'].strip('[]').split(',')

        return [{"type": self._IMAGE_TYPE_THUMBNAIL, "url": self.biggest_image_url},
                *[{"type": self._IMAGE_TYPE_STOCK,
                  "url": self._product_non_formatted_url.format(width=int(width))} for width in all_image_sizes]
                ]

    @property
    def biggest_image_url(self):
        return self._product_non_formatted_url.format(
            width=int(max(self.product_item.select_one('.ProductItem__Image')['data-widths'].strip('[]').split(','))))

    @property
    def sizes(self):
        return NudeProjectSizing(self.product_item).sizes
