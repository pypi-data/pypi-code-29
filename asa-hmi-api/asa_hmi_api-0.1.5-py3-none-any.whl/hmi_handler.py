__all__ = ['HmiHandler']

import threading
import serial
import time
from .data_to_byte import *
from .decoder import *
from .util import *

class HmiHandler(threading.Thread):
    _ser = serial.Serial()
    _dataBuffer = list()
    _timeout = int()

    def __init__(
        self,
        port=None,
        baudrate=38400,
        timeout=None,
        bytedelay=0
    ):
        super(HmiHandler, self).__init__(name = 'hmi')
        self._ser.port = port
        self._ser.baudrate = baudrate
        self._ser.timeout = 0.01
        self._timeout = timeout
        self.lock = threading.Lock()
        self.setDaemon(True)

        self.eventGetString = threading.Event()
        self.eventGetArray  = threading.Event()
        self.eventGetStruct = threading.Event()

        self._bytedelay = bytedelay

    def setSerial(
        port,
        baudrate=38400,
    ):
        self._ser.port = port
        self._ser.baudrate = baudrate

    def run(self):
        de = Decoder()
        self._dataBuffer = list()
        self._ser.open()

        while (self._ser.isOpen()):
            try:
                self.lock.acquire()
                ch = self._ser.read(1)
                self.lock.release()
            except serial.serialutil.SerialException as e:
                raise AsaHmiException()
            else:
                if ch != b'':
                    self.lock.acquire()
                    de.add_text(ch)
                    type, data = de.get()
                    if type is 0:
                        pass
                    else:
                        self._dataBuffer.append((type, data))
                        if type == 0:
                            self.eventGetString.set()
                        elif type == 1:
                            self.eventGetArray.set()
                        elif type == 2:
                            self.eventGetStruct.set()
                    self.lock.release()

    def ser_write(self, data):
        for ch in data:
            print(ch)
            self._ser.write(bytes([ch]))
            time.sleep(self._bytedelay)

    def putArray(self, data):
        b = encodeArToPac(data)
        self.ser_write(b)

    def putStruct(self, data):
        b = encodeStToPac(data)
        self.ser_write(b)

    def putString(self, data):
        if type(data) is bytes:
            self.ser_write(data)
        elif type(data) is str:
            b = data.encode('utf-8')
            self.ser_write(b)

    def putSync(self):
        self.ser_write(b'sync\n')

    def get(self):
        if not self._ser.is_open:
            raise SerialNotOpenException
        if self._timeout is not None and self._timeout != 0:
            timeout = time.time() + self._timeout
        else:
            timeout = None
        data = None
        while self._ser.is_open:
            if len(self._dataBuffer) >= 1:
                data = self._dataBuffer.pop(0)
                break
            # check for timeout now, after data has been read.
            # useful for timeout = 0 (non blocking) read
            if timeout and time.time() > timeout:
                break
        return data

    def getArray(self):
        if not self._ser.is_open:
            raise SerialNotOpenException
        if self._timeout is not None and self._timeout != 0:
            timeout = time.time() + self._timeout
        else:
            timeout = None
        data = None
        while self._ser.is_open:
            if len(self._dataBuffer) >= 1:
                if self._dataBuffer[0][0] == 1:
                    data = self._dataBuffer.pop(0)
                    break
                else:
                    break
            # check for timeout now, after data has been read.
            # useful for timeout = 0 (non blocking) read
            if timeout and time.time() > timeout:
                break
        return data

    def getStruct(self):
        if not self._ser.is_open:
            raise SerialNotOpenException
        if self._timeout is not None and self._timeout != 0:
            timeout = time.time() + self._timeout
        else:
            timeout = None
        data = None
        while self._ser.is_open:
            if len(self._dataBuffer) >= 1:
                if self._dataBuffer[0][0] == 2:
                    data = self._dataBuffer.pop(0)
                    break
                else:
                    break
            # check for timeout now, after data has been read.
            # useful for timeout = 0 (non blocking) read
            if timeout and time.time() > timeout:
                break
        return data

    def getString(self):
        if not self._ser.is_open:
            raise SerialNotOpenException
        if self._timeout is not None and self._timeout != 0:
            timeout = time.time() + self._timeout
        else:
            timeout = None
        data = None
        while self._ser.is_open:
            if len(self._dataBuffer) >= 1:
                if len(self._dataBuffer) >= 1:
                    if self._dataBuffer[0][0] == 3:
                        data = self._dataBuffer.pop(0)
                        break
                    else:
                        break
            # check for timeout now, after data has been read.
            # useful for timeout = 0 (non blocking) read
            if timeout and time.time() > timeout:
                break
        return data

    def getAvailableDataNum(self):
        return len(self._dataBuffer)
