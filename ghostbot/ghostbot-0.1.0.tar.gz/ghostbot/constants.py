from enum import Enum
from selenium.webdriver.common.keys import Keys as _


class Appearances(Enum):
    BLINK = "blink"
    STANDARD = "standard"
    HEADLESS = "headless"


class Architectures(Enum):
    UNKNOWN = "unknown"
    ARCH32 = "32bit"
    ARCH64 = "64bit"


class CPU(Enum):
    UNKNOWN = "unknown"
    INTEL = "intel"
    ARM = "arm"
    MIPS = "mips"


class Directions(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    ABSOLUTE = "absolute"


class Formats(Enum):
    HTML = "html"
    PNG = "png"
    PDF = "pdf"
    HTML_PNG = "html_png"


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
    PAGE_UP = _.PAGE_UP
    PAGE_DOWN = _.PAGE_DOWN
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


class OperatingSystems(Enum):
    UNKNOWN = "unknown"
    ANDROID = "android"
    IOS = "ios"
    LINUX = "linux"
    MACOS = "macos"
    WINDOWS = "windows"


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


class Weekdays(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class WebDrivers(Enum):
    DEFAULT = "default"
    GHOST = "ghost"
    CHROME = "chrome"
    EDGE = "edge"
    FIREFOX = "firefox"
    SAFARI = "safari"


class WebWidgets(Enum):
    IMAGE = "image"
    LINK = "link"
    TEXT = "text"
    LIST_BOX = "list_box"
    LIST_ITEM = "list_item"
    INPUT_BOX = "input_box"
    CHECK_BOX = "check_box"
    RADIO_BUTTON = "radio_button"
    BUTTON = "button"
    UNKNOWN = "unknown"
