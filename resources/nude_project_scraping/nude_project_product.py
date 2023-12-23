from resources.nude_project_scraping.nude_project_base_class import NudeProjectBaseClass
from resources.nude_project_scraping.nude_project_size import NudeProjectSizing


class NudeProjectProduct(NudeProjectBaseClass):
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
        return int(self.product_item.select_one('.ProductItem__Price').text.strip().replace('€', ''))

    @property
    def _product_non_formatted_url(self):
        return f"https:{self.product_item.select_one('.ProductItem__Image')['data-src']}"

    @property
    def product_images_listing(self):
        # Converting a string-ed list to a native python list without eval() to prevent code injection:
        all_image_sizes = self.product_item.select_one('.ProductItem__Image')['data-widths'].strip('[]').split(',')

        return [self._product_non_formatted_url.format(width=int(width)) for width in all_image_sizes]

    @property
    def biggest_image_url(self):
        return self._product_non_formatted_url.format(
            width=int(max(self.product_item.select_one('.ProductItem__Image')['data-widths'].strip('[]').split(','))))

    @property
    def sizes(self):
        return NudeProjectSizing(self.product_item).sizes
