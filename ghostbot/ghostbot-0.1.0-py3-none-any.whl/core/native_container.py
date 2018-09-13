from ghostbot.utils.logger import Logger
from .container import Container


class NativeContainer(Container):

    def __init__(self, content=None):
        super().__init__()
        self.logger = Logger(__name__)
        self.content(content)
