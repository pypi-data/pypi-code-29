m# -*- coding: utf-8 -*-

from . import general

__all__  = ['Packet']

class Packet():
    _seq = int(0)
    _isContinued = False
    _addr = int(0)
    _func = int(0)
    _data = bytes([])

    def __init__(self):
        pass

    def toByte(self):
        seq     = self._seq + (int(self._isContinued)<<5)
        dataLen = len(self._data)
        b  = general.HEADER
        b += bytes([self._addr>>8, self._addr&0xFF])
        b += bytes([seq])
        b += bytes([self._func])
        b += bytes([dataLen>>8, dataLen&0xFF])
        b += self._data
        chksum = sum(b) - int(general.HEADER[0])
        b += bytes([chksum])
        return b

    def setAddr(self, addr):
        if addr<65535 :
            self._addr = addr
        else:
            raise ValueError(str(addr) + ' excceds max value of address (65535).')

    def setSeq(self, seq):
        if seq<31 :
            self._seq = seq
            self._isContinued = True
        else:
            raise ValueError(str(seq) + ' excceds max num of seq (31).')

    def setNonContinue(self):
        self._seq = 0
        self._isContinued = False

    def setFunc(self, func):
        self._func = func

    def setData(self, data):
        self._data = data

    def setAsAck(self):
        self._func = 2
        self.setNonContinue()
        self._data = bytes([])

    def setAsNack(self):
        self._func = 3
        self.setNonContinue()
        self._data = bytes([])
