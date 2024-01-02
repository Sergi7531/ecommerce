import json

import requests

from resources.nude_project_scraping.nude_project_objs.nude_project_product import NudeProjectProduct


class EcommerceApi:
    base_url = 'http://localhost:8000/api/v1'

    def post_product(self, nude_project_product: NudeProjectProduct) -> int:
        payload = {
            "name": nude_project_product.name,
            "description": nude_project_product.description,
            "price": nude_project_product.price * 100,
            "tags": [],
            # TODO: Change this for "product_images_listing" and "product_images_detail":
            "image_url": nude_project_product.biggest_image_url,
            "sizes": nude_project_product.sizes
        }

        response = requests.post(f'{self.base_url}/products/', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        if response.status_code not in [200, 201]:
            print(f'Product {nude_project_product.name} failed. Response: {response.text}')

        return response.status_code
