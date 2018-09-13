import html2text
from bs4 import BeautifulSoup
from ghostbot.utils.logger import Logger
from .reactor import Reactor


class WebReactor(Reactor):
    DEFAULT_PARSER = "lxml"

    def __init__(self, agent=None):
        super().__init__(agent)
        self.logger = Logger(__name__)

    def markdown(self, html):
        content = BeautifulSoup(html, self.DEFAULT_PARSER)
        for tag in ["script", "style", "font", "em"]:
            [s.decompose() for s in content(tag)]
        for attr in ["style", "xmlns"]:
            content = self._remove_attrs(content, attr)
        return html2text.html2text(content)

    @staticmethod
    def _remove_attrs(content, target):
        for tag in content.find_all(True):
            for attr in [attr for attr in tag.attrs if attr == target]:
                del tag[attr]
        return content
