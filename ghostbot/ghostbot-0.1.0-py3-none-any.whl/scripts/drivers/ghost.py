import re
from time import sleep
from bs4 import BeautifulSoup
from ghostbot.utils.network import HttpClient


class Ghost(object):

    def __init__(self):
        self._client = HttpClient()
        self._client.session()
        self._request = self._client.request()
        self._response = self._client.response()
        self._page_source = None
        self._html = None
        self._element = None

    @property
    def page_source(self):
        return self._page_source

    @property
    def window_handles(self):
        return []

    def get(self, url):
        self._client.get(url)
        if self._response.status_code == 200:
            self._page_source = self._response.content
            self._html = BeautifulSoup(self._response.content)
        else:
            raise Exception("HTTP access failed: status_code={} url={}".format(self._response.status_code, url))

    def find_element_by_id(self, ids):
        self._element = self._html.find(id=ids)
        return self._element

    def find_element_by_name(self, name):
        self._element = self._html.find(attrs={"name": name})
        return self._element

    def find_element_by_tag_name(self, tag_name):
        self._element = self._html.find(tag_name)
        return self._element

    def find_element_by_class_name(self, class_name):
        self._element = self._html.find(class_=class_name)
        return self._element

    def find_element_by_link_text(self, link_text):
        self._element = self._html.find("a", text=link_text)
        return self._element

    def find_element_by_partial_link_text(self, link_text):
        self._element = self._html.find("a", text=re.compile(link_text))
        return self._element

    def find_element_by_xpath(self, xpath):
        self._element = self._html.xpath(xpath)
        return self._element

    def find_element_by_css_selector(self, css_selector):
        self._element = self._html.select(css_selector)
        return self._element

    def find_elements_by_name(self, name):
        self._element = self._html.find_all(attrs={"name": name})
        return self._element

    def find_elements_by_tag_name(self, tag_name):
        self._element = self._html.find_all(tag_name)
        return self._element

    def find_elements_by_class_name(self, class_name):
        self._element = self._html.find_all(class_=class_name)
        return self._element

    def find_elements_by_link_text(self, link_text):
        self._element = self._html.find_all("a", text=link_text)
        return self._element

    def find_elements_by_partial_link_text(self, link_text):
        self._element = self._html.find_all("a", text=re.compile(link_text))
        return self._element

    def find_elements_by_xpath(self, xpath):
        self._element = self._html.xpath(xpath)
        return self._element

    def find_elements_by_css_selector(self, css_selector):
        self._element = self._html.select(css_selector)
        return self._element

    def implicitly_wait(self, seconds):
        sleep(seconds)

    def download(self, file, url):
        self._client.download(file, url)

    def close(self):
        if self._client:
            self._client.close()
        self._client = None
        self._request = None
        self._response = None
        self._html = None

    def quit(self):
        self.close()
