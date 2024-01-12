import requests
from bs4 import BeautifulSoup

from resources.nude_project_scraping.nude_project_objs.nude_project_base_class import NudeProjectBaseClass


class NudeProjectProductDetail(NudeProjectBaseClass):
    _secure_host = 'https:'

    def __init__(self, detail_url):
        self.detail_url = detail_url

        self.soup = BeautifulSoup(requests.get(self.detail_url).text, 'html.parser')

    @property
    def biggest_image_width(self):
        return sorted(
            map(int, self.soup.select_one('#desktopGallery img[data-src]')['data-widths'].strip('[]').split(',')),
            reverse=True)[0]

    @property
    def detail_images(self):
        image_urls = [f"{self._secure_host}{img['data-src']}" for img in
                      self.soup.select('#desktopGallery img[data-src]')][1:]

        return image_urls
