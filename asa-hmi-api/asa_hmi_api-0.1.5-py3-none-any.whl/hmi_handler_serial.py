a__all__ = ['HmiHandler']

import threading
import serial
import time
from .data_to_byte import *
from .decoder import *
from .util import *

class HmiHandler_serial(threading.Thread):
    pass

    def putArray(self, data):
        pass

    def putStruct(self, data):
        pass

    def putString(self, data):
        pass

    def putSync(self):
        pass

    def get(self):
        pass

    def getArray(self):
        pass

    def getStruct(self):
        pass

    def getString(self):
        pass

    def getAvailableDataNum(self):
        pass
