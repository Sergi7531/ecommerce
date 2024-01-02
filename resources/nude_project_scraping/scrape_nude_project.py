from resources.nude_project_scraping.ecommerce_api import EcommerceApi
from resources.nude_project_scraping.nude_project_objs.nude_project_page import NudeProjectSource
from resources.nude_project_scraping.nude_project_objs.nude_project_product import NudeProjectProduct


def scrape_products(url: str) -> None:
    """
    This function will perform web scraping over a gallery of products from the known clothing brand "Nude Project".
    This is completely for database population and will never be used in a real project.
    :param url: The URL from the product gallery that must be scraped.
    """
    page_number = 1

    ecommerce_api = EcommerceApi()

    while True:
        page_source = NudeProjectSource(url, page_number)

        if not page_source.product_items:
            break

        for product_item in page_source.product_items:
            ecommerce_api.post_product(NudeProjectProduct(product_item))

        print(f'Page {page_number} done.')
        page_number += 1


if __name__ == '__main__':
    all_products_url = 'https://nude-project.com/collections/all-products?page=1'

    scrape_products(all_products_url)
