#!/usr/bin/env python

from plico.client.hackerable_client import HackerableClient
from tipico.client.abstract_instrument_client import \
    AbstractInstrumentClient
from plico.rpc.abstract_remote_procedure_call import \
    AbstractRemoteProcedureCall
from plico.utils.logger import Logger
from plico.utils.decorator import override, returns
from tipico.utils.timeout import Timeout
from tipico.types.instrument_status import InstrumentStatus
from plico.client.serverinfo_client import ServerInfoClient



class InstrumentClient(AbstractInstrumentClient,
                       HackerableClient,
                       ServerInfoClient):

    def __init__(self,
                 rpcHandler,
                 sockets):
        assert isinstance(rpcHandler, AbstractRemoteProcedureCall)

        self._rpcHandler= rpcHandler
        self._requestSocket= sockets.serverRequest()
        self._statusSocket= sockets.serverStatus()
        self._logger= Logger.of('Instrument client')

        HackerableClient.__init__(self,
                                  self._rpcHandler,
                                  self._requestSocket,
                                  self._logger)
        ServerInfoClient.__init__(self,
                                  self._rpcHandler,
                                  self._requestSocket,
                                  self._logger)



    @override
    def moveTo(self,
               actuatorPosition,
               timeoutInSec=Timeout.INSTRUMENT_MOVE_TO):
        return self._rpcHandler.sendRequest(
            self._requestSocket,
            'moveTo', [actuatorPosition],
            timeout=timeoutInSec)
        pass


    @override
    def getPosition(self, timeoutInSec=Timeout.MIRROR_GET_ZONAL_COMMAND):
        return self._rpcHandler.sendRequest(
            self._requestSocket,
            'getPosition', [],
            timeout=timeoutInSec)



    @override
    @returns(InstrumentStatus)
    def getStatus(self, timeoutInSec=Timeout.MIRROR_GET_STATUS):
        return self._rpcHandler.receivePickable(
            self._statusSocket,
            timeoutInSec)


    @override
    def getSnapshot(self,
                    prefix,
                    timeoutInSec=Timeout.MIRROR_GET_STATUS):
        return self._rpcHandler.sendRequest(
            self._requestSocket,
            'getSnapshot', [prefix],
            timeout=timeoutInSec)
