# -*- coding: utf-8 -*-

from . import general
from . import packet
import enum

__all__  = ['Decoder']

class _Status(enum.IntEnum):
    header = 0
    addr   = 1
    seq    = 2
    func   = 3
    byte   = 4
    data   = 5
    chksum = 6

class Decoder():

    class _State():
        status = _Status(_Status.header)
        addr   = int(0)
        seq    = int(0)
        func   = int(0)
        dbytes = int(0)
        data   = bytes()

        chksum = int(0)
        count = int(0)

    _text    = bytes([])
    _usedNum = int(0)

    def __init__(self):
        pass

    def putText(self, text):
        self._text += text

    def _get_ch(self):
        if self._usedNum+1 <= len(self._text):
            self._usedNum = self._usedNum + 1
            return self._text[self._usedNum-1]
        else:
            raise IndexError('get ch out of range')

    def de(self):
        for i in range(len(self._text)-self._usedNum):
            res = self._step()
            if res:
                return True
        return False

    def _step(self):
        ch = self._get_ch()
        if self._State.status == _Status.header:
            self._State.chksum = 0
            self._State.count  = 0
            self._State.status = _Status.addr

        elif self._State.status == _Status.addr:
            self._State.chksum += ch
            self._State.count  += 1
            if self._State.count == 1:
                self._State.addr = ch
            else:
                self._State.addr = (self._State.addr<<8) + ch
                self._State.count = 0
                self._State.status = _Status.seq

        elif self._State.status == _Status.seq:
            self._State.chksum += ch
            self._State.seq    = ch
            self._State.status  = _Status.func

        elif self._State.status == _Status.func:
            self._State.chksum += ch
            self._State.func   = ch
            self._State.status = _Status.byte

        elif self._State.status == _Status.byte:
            self._State.chksum += ch
            self._State.count  += 1
            if self._State.count == 1:
                self._State.dbytes = ch
            else:
                self._State.dbytes = (self._State.dbytes<<8) + ch
                self._State.count = 0

                if self._State.dbytes != 0:
                    self._State.data   = bytes([])
                    self._State.status = _Status.data
                else:
                    self._State.status = _Status.chksum

        elif self._State.status == _Status.data:
            self._State.chksum += ch
            self._State.count  += 1
            self._State.data   += bytes([ch])
            if self._State.count == self._State.dbytes:
                self._State.count = 0
                self._State.status = _Status.chksum

        elif self._State.status == _Status.chksum:
            if self._State.chksum&0xFF == ch:
                self._State.status = _Status.header
                return True
            else:
                self._State.status = _Status.header
        return False

    def getPac(self):
        en = packet.Packet()
        en.setAddr(self._State.addr)
        en.setSeq (self._State.seq )
        en.setFunc(self._State.func)
        en.setData(self._State.data)
        return en
