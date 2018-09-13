from abc import abstractmethod
from enum import Enum
from selenium.webdriver.common.keys import Keys as _
from .basis import Basis
from .asserter import Asserter


class Appearances(Enum):
    BLINK = "blink"
    STANDARD = "standard"
    HEADLESS = "headless"


class Directions(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    ABSOLUTE = "absolute"


class Formats(Enum):
    HTML = "html"
    JPEG = "jpeg"
    PNG = "png"
    PDF = "pdf"
    WEB = "web"


class Keys(Enum):
    ESCAPE = _.ESCAPE
    TAB = _.TAB
    CONTROL = _.CONTROL
    SHIFT = _.SHIFT
    SPACE = _.SPACE
    ALT = _.ALT
    OPTION = _.ALT
    COMMAND = _.COMMAND
    WINDOWS = _.META
    META = _.META
    BACKSPACE = _.BACKSPACE
    ENTER = _.ENTER
    HOME = _.HOME
    END = _.END
    ARROW_UP = _.ARROW_UP
    ARROW_DOWN = _.ARROW_DOWN
    ARROW_LEFT = _.ARROW_LEFT
    ARROW_RIGHT = _.ARROW_RIGHT
    F1 = _.F1
    F2 = _.F2
    F3 = _.F3
    F4 = _.F4
    F5 = _.F5
    F6 = _.F6
    F7 = _.F7
    F8 = _.F8
    F9 = _.F9
    F10 = _.F10
    F11 = _.F11
    F12 = _.F12


class MouseButtons(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    WHEEL = "wheel"


class PhysicalButtons(Enum):
    HOME = "home"
    BACK = "back"
    POWER = "power"
    VOLUME_UP = "volume_up"
    VOLUME_DOWN = "volume_down"


class Speeds(Enum):
    STANDARD = "standard"
    SLOW = "slow"
    VERY_SLOW = "very_slow"


class TouchFingers(Enum):
    ONE = "one"
    TWO = "two"
    THREE = "three"


class Agent(Basis, Asserter):

    def __init__(self, scenario=None, container=None, reactor=None):
        super().__init__()
        self._scenario = scenario
        self._container = container
        self._reactor = reactor
        self._options = None
        self._actions = []

    def actions(self, action=None):
        if action:
            self._actions.append(action)
        return self._actions

    def scenario(self, scenario=None):
        if scenario:
            self._scenario = scenario
        return self._scenario

    def container(self, container=None):
        if container:
            self._container = container
        return self._container

    def reactor(self, reactor=None):
        if reactor:
            self._reactor = reactor
        return self._reactor

    def options(self, options=None):
        if options:
            self._options = options
        return self._options

    @abstractmethod
    def startup(self, config=None):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    @abstractmethod
    def execute(self, options=None):
        pass
