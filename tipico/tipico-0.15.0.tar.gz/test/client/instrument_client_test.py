#!/usr/bin/env python
import unittest
from tipico.client.instrument_client import InstrumentClient
from tipico.utils.timeout import Timeout
from plico.utils.decorator import override
from tipico.types.instrument_status import InstrumentStatus
from plico.rpc.dummy_remote_procedure_call import DummyRpcHandler
from plico.rpc.dummy_sockets import DummySockets



class TesterRpcHandler(DummyRpcHandler):

    def __init__(self):
        self._sendRequestHistory= []
        self._receivePickableHistory= []
        self._sendRequestCounter= 0
        self._receivePickableCounter= 0


    @override
    def sendRequest(self, socket, command, args, timeout=1):
        self._sendRequestHistory.append(
            (socket, command, args, timeout))
        self._sendRequestCounter += 1


    @override
    def receivePickable(self, socket, timeout=1):
        self._receivePickableCounter+= 1
        self._receivePickableHistory.append(
            (socket, timeout))
        return self._objToReturnWithReceivePickable


    def getLastSendRequestArguments(self):
        return self._sendRequestHistory[-1]


    def getLastReceivePickableArguments(self):
        return self._receivePickableHistory[-1]


    def wantsPickable(self, objToReturnWithReceivePickable):
        self._objToReturnWithReceivePickable= \
            objToReturnWithReceivePickable


class MyRpcHandler(TesterRpcHandler):
    pass


class MySockets(DummySockets):
    pass


class InstrumentClientTest(unittest.TestCase):


    def setUp(self):
        self._rpc= MyRpcHandler()
        self._sockets= MySockets()
        self._client= InstrumentClient(self._rpc, self._sockets)


    def tearDown(self):
        pass


    def testMoveTo(self):
        instrumentWantedPosition= 42
        self._client.moveTo(instrumentWantedPosition)
        self.assertEqual(
            self._rpc.getLastSendRequestArguments(),
            (self._sockets.serverRequest(),
             'moveTo',
             [instrumentWantedPosition],
             Timeout.INSTRUMENT_MOVE_TO))


    def testGetPosition(self):
        timeoutInSec= 12
        _= self._client.getPosition(timeoutInSec)
        self.assertEqual(
            self._rpc.getLastSendRequestArguments(),
            (self._sockets.serverRequest(),
             'getPosition',
             [],
             timeoutInSec))


    def testGetStatus(self):
        wantedInstrumentStatus= InstrumentStatus('foo', 'tux')
        self._rpc.wantsPickable(wantedInstrumentStatus)

        timeoutInSec= 22
        gotInstrumentStatus= self._client.getStatus(timeoutInSec)
        self.assertEqual(
            wantedInstrumentStatus, gotInstrumentStatus)

        self.assertEqual(
            self._rpc.getLastReceivePickableArguments(),
            (self._sockets.serverStatus(),
             timeoutInSec))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()