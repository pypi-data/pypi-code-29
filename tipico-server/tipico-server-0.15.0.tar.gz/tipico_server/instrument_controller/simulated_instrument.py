#!/usr/bin/env python

from plico.utils.decorator import override
from plico.utils.logger import Logger
from tipico_server.instrument_controller.abstract_instrument \
    import AbstractInstrument




class SimulatedInstrument(AbstractInstrument):


    def __init__(self, serialNumber):
        self._serialNumber= serialNumber
        self._logger= Logger.of('Simulated Deformable Mirror')
        self._command= 0


    @override
    def moveTo(self, command):
        self._command= command


    @override
    def getPosition(self):
        return self._command


    @override
    def serialNumber(self):
        return self._serialNumber
