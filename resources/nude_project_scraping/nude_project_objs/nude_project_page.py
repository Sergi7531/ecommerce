import requests
from bs4 import BeautifulSoup

from resources.nude_project_scraping.nude_project_objs.nude_project_base_class import NudeProjectBaseClass


class NudeProjectSource(NudeProjectBaseClass):
    def __init__(self, url, page_number):
        self.url = url
        self.page_number = page_number

        self.soup = BeautifulSoup(requests.get(self.complete_url).text, 'html.parser')

    @property
    def complete_url(self):
        return f"{self.url.split('?')[0]}?page={self.page_number}"

    @property
    def product_items(self):
        return self.soup.select('.product-container')

    @property
    def url_page(self):
        return int(self.url.split('page=')[1][0])
