from enum import Enum
from collections import OrderedDict
from ghostbot.core import Basis
from ghostbot.utils.logger import Logger
from ghostbot.utils.datetime import Timer


class Priorities(Enum):
    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"


class Scheduler(object):
    ONCE = "once"
    REPEAT = "repeat"

    def __init__(self):
        self.execution_at = None

    def setup(self):
        pass


class Task(object):
    UNKNOWN = "unknown"
    QUEUEING = "queueing"
    RUNNING = "running"
    WAITING = "waiting"
    FINISHED = "finished"

    def __init__(self):
        self.status = self.UNKNOWN
        self.history = OrderedDict()
        self.scheduler = None
        self.agent = None
        self.options = None

    def setup(self, scheduler=None):
        pass

    def queueing(self):
        self.status = self.QUEUEING
        self.history[self.status] = Timer.now()

    def running(self):
        self.status = self.RUNNING
        self.history[self.status] = Timer.now()

    def waiting(self):
        self.status = self.WAITING
        self.history[self.status] = Timer.now()

    def finished(self):
        self.status = self.FINISHED
        self.history[self.status] = Timer.now()


class Scheduler(Basis):

    def __init__(self):
        self.logger = Logger(__name__)
        self._high = []
        self._normal = []
        self._low = []

    def register(self, task, priority=Priorities.NORMAL):
        pass

    def execute(self):
        pass
