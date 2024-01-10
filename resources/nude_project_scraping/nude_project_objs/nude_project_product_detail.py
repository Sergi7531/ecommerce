import requests
from bs4 import BeautifulSoup

from resources.nude_project_scraping.nude_project_objs.nude_project_base_class import NudeProjectBaseClass


class NudeProjectProductDetail(NudeProjectBaseClass):
    def __init__(self, detail_url):
        self.detail_url = detail_url

        self.soup = BeautifulSoup(requests.get(self.detail_url).text, 'html.parser')


    @property
    def images(self):
        image_urls = [img['data-src'] for img in self.soup.select('#desktopGallery img[data-src]')]

        return image_urls
