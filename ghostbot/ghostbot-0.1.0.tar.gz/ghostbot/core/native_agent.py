from ghostbot.constants import Appearances, NativeDevices
from .agent import Agent


class NativeAgent(Agent):

    def __init__(self, options=None):
        if options is None:
            self.device = NativeDevices.DEFAULT
            self.mode = Appearances.NORMAL
        self.application = None
        self.uri = None

    def shutdown(self):
        pass

    def startup(self, config=None):
        pass

    def configure(self, options=None):
        pass

    def execute(self, options=None):
        pass
