from resources.nude_project_scraping.nude_project_objs.nude_project_base_class import NudeProjectBaseClass
from resources.nude_project_scraping.nude_project_objs.nude_project_product_detail import NudeProjectProductDetail
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
        product_detail = NudeProjectProductDetail(self.product_detail_url)
        product_detail_images = product_detail.detail_images

        images = [
            {"type": self._IMAGE_TYPE_THUMBNAIL,
             "url": self.get_image_url(url=self._product_non_formatted_url, width=product_detail.biggest_image_width)
             }
        ]

        for url in product_detail_images:
            images.append({
                "type": self._IMAGE_TYPE_STOCK,
                "url": self.get_image_url(url, product_detail.biggest_image_width)
            })

        return images

    @property
    def biggest_image_width(self):
        return int(max(self.product_item.select_one('.ProductItem__Image')['data-widths'].strip('[]').split(',')))

    def get_image_url(self, url, width):
        return f'{url.format(width=width)}'

    @property
    def sizes(self):
        return NudeProjectSizing(self.product_item).sizes
