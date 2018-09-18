#!/usr/bin/env python
import unittest
import numpy as np
from tipico.client.abstract_instrument_client import SnapshotEntry
from tipico_server.instrument_controller.instrument_controller \
    import InstrumentController
from tipico_server.instrument_controller.simulated_instrument \
    import SimulatedInstrument



class MyReplySocket():
    pass


class MyPublisherSocket():
    pass


class MyRpcHandler():

    def handleRequest(self, obj, socket, multi):
        pass


class InstrumentControllerTest(unittest.TestCase):

    def setUp(self):
        self._serverName= 'server description'
        self._ports= None
        self._dmSerialNumber= '0123456'
        self._instrument= SimulatedInstrument(self._dmSerialNumber)
        self._rpcHandler= MyRpcHandler()
        self._replySocket= MyReplySocket()
        self._statusSocket= MyPublisherSocket()
        self._ctrl= InstrumentController(
            self._serverName,
            self._ports,
            self._instrument,
            self._replySocket,
            self._statusSocket,
            self._rpcHandler)


    def testGetSnapshot(self):
        snapshot= self._ctrl.getSnapshot('baar')
        serialNumberKey= 'baar.%s' % SnapshotEntry.SERIAL_NUMBER
        self.assertEqual(self._dmSerialNumber, snapshot[serialNumberKey])


    def testMoveToGetPositionCommands(self):
        actuatorCommands= np.arange(12) * 3.14
        self._ctrl.moveTo(actuatorCommands)
        actualPosition= self._ctrl.getPosition()
        self.assertTrue(np.allclose(actuatorCommands, actualPosition))


if __name__ == "__main__":
    unittest.main()
