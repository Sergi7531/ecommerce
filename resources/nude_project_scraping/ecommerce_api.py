import requests

from resources.nude_project_scraping.nude_project_product import NudeProjectProduct


class EcommerceApi:
    base_url = 'http://localhost:8000/api/v1'

    def post_product(self, nude_project_product: NudeProjectProduct):
        payload = {
            "name": nude_project_product.name,
            "description": nude_project_product.description,
            "price": nude_project_product.price * 100,
            "tags": [],
            # TODO: Change this for "product_images_listing" and "product_images_detail":
            "image_url": nude_project_product.biggest_image_url,
            "sizes": nude_project_product.sizes
        }

        return requests.post(f'{self.base_url}/products/', data=payload).status_code
