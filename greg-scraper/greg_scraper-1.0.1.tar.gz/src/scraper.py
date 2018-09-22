from bs4 import BeautifulSoup as Soup
from requests import request


class ScrapingException(Exception):
    pass


def get_part(tag):
    def _get_part(url):
        response = request("GET", url)

        if not response.status_code == 200 or "html" not in response.headers.get("Content-Type", "html"):
            raise ScrapingException()

        soup = Soup(response.content, "html.parser")
        return soup.select_one(tag).text
    return _get_part
