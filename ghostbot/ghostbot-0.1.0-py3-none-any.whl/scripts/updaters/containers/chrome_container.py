from ghostbot.core import WebContainer
from ghostbot.utils.logger import Logger


class ChromeContainer(WebContainer):

    def __init__(self, agent=None):
        super().__init__(agent)
        self.logger = Logger(__name__)
