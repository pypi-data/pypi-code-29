from enum import Enum
from ghostbot.core import Appearances
from .agent import Agent


class NativeDevices(Enum):
    ANDROID = "android"
    IOS = "ios"


class NativeWidgets(Enum):
    IMAGE = "image"
    TEXT = "text"
    CHECK_BOX = "check_box"
    RADIO_BUTTON = "radio_button"
    BUTTON = "button"
    UNKNOWN = "unknown"


class NativeAgent(Agent):

    def __init__(self, options=None):
        if options is None:
            self.device = NativeDevices.DEFAULT
            self.mode = Appearances.NORMAL
        self.application = None
        self.uri = None

    def configure(self, options=None):
        pass

    def execute(self, options=None):
        pass
