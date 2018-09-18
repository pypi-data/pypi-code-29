import threading
from plico.utils.logger import Logger
from plico.utils.decorator import override, synchronized
from plico.utils.timekeeper import TimeKeeper
from plico.utils.stepable import Stepable
from plico.utils.snapshotable import Snapshotable
from plico.utils.hackerable import Hackerable
from plico.utils.serverinfoable import ServerInfoable
from tipico.client.abstract_instrument_client import SnapshotEntry
from tipico.types.instrument_status import InstrumentStatus


class InstrumentController(Stepable, Snapshotable, Hackerable,
                           ServerInfoable):

    def __init__(self,
                 servername,
                 ports,
                 instrument,
                 replySocket,
                 statusSocket,
                 rpcHandler):
        self._instrument= instrument
        self._replySocket= replySocket
        self._statusSocket= statusSocket
        self._rpcHandler= rpcHandler
        self._logger= Logger.of('InstrumentController')
        Hackerable.__init__(self, self._logger)
        ServerInfoable.__init__(self, servername,
                                ports,
                                self._logger)
        self._isTerminated= False
        self._stepCounter= 0
        self._commandCounter= 0
        self._timekeep = TimeKeeper()
        self._instrumentStatus= None
        self._mutexStatus= threading.RLock()


    @override
    def step(self):
        self._rpcHandler.handleRequest(self, self._replySocket, multi=True)
        self._publishStatus()
        if self._timekeep.inc():
            self._logger.notice(
                'Stepping at %5.2f Hz' % (self._timekeep.rate))
        self._stepCounter+= 1


    def _getStepCounter(self):
        return self._stepCounter


    def terminate(self):
        self._logger.notice("Got request to terminate")
        try:
            self._instrument.deinitialize()
        except Exception as e:
            self._logger.warn("Could not deinitialize mirror: %s" %
                              str(e))
        self._isTerminated= True


    @override
    def isTerminated(self):
        return self._isTerminated


    def moveTo(self, actuatorCommands):
        self._instrument.moveTo(actuatorCommands)
        self._command= actuatorCommands
        self._commandCounter+= 1
        with self._mutexStatus:
            self._instrumentStatus= None


    def getPosition(self):
        return self._instrument.getPosition()


    def getSnapshot(self, prefix):
        status= self._getInstrumentStatus()
        snapshot= {}
        snapshot[SnapshotEntry.COMMAND_COUNTER]= status.commandCounter()
        snapshot[SnapshotEntry.SERIAL_NUMBER]= \
            self._getInstrumentSerialNumber()
        snapshot[SnapshotEntry.STEP_COUNTER]= self._getStepCounter()
        return Snapshotable.prepend(prefix, snapshot)


    def _getInstrumentSerialNumber(self):
        return self._instrument.serialNumber()



    @synchronized("_mutexStatus")
    def _getInstrumentStatus(self):
        if self._instrumentStatus is None:
            self._logger.debug('get InstrumentStatus')
            self._instrumentStatus= InstrumentStatus(
                self._instrument.getPosition(),
                self._commandCounter)
        return self._instrumentStatus


    def _publishStatus(self):
        self._rpcHandler.publishPickable(self._statusSocket,
                                         self._getInstrumentStatus())
