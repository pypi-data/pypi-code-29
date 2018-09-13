from ghostbot.core import Basis, Service
from ghostbot.utils.logger import Logger


class Inspector(Basis, Service):

    def __init__(self):
        super().__init__()
        self.logger = Logger(__name__)

    def startup(self):
        pass

    def shutdown(self):
        pass

    def execute(self, options=None):
        pass
