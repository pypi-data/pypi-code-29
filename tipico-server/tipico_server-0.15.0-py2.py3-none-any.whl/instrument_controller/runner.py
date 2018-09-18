import os
import time
from plico.utils.base_runner import BaseRunner
from plico.utils.logger import Logger
from plico.utils.decorator import override
from plico.utils.control_loop import FaultTolerantControlLoop
from plico.rpc.zmq_ports import ZmqPorts
from tipico_server.instrument_controller.simulated_instrument import \
    SimulatedInstrument
from tipico_server.instrument_controller.instrument_controller import InstrumentController


class Runner(BaseRunner):

    RUNNING_MESSAGE = "Instrument controller is running."

    def __init__(self):
        BaseRunner.__init__(self)


    def _createInstrumentDevice(self):
        instrumentDeviceSection= self.configuration.getValue(
            self.getConfigurationSection(), 'mirror')
        instrumentModel= self.configuration.deviceModel(
            instrumentDeviceSection)
        if instrumentModel == 'simulatedInstrumentOfAnotherType':
            self._createSimulatedInstrument(instrumentDeviceSection)
        elif instrumentModel == 'simulatedInstrument':
            self._createSimulatedInstrument(instrumentDeviceSection)
        else:
            raise KeyError(
                'Unsupported mirror model %s' % instrumentModel)


    def _createSimulatedInstrument(self, mirrorDeviceSection):
        serialNumber= self.configuration.getValue(
            mirrorDeviceSection, 'serial_number')
        self._instrument= SimulatedInstrument(serialNumber)


    def _setUp(self):
        self._logger= Logger.of("Instrument Controller runner")

        self._zmqPorts= ZmqPorts.fromConfiguration(
            self.configuration, self.getConfigurationSection())
        self._replySocket = self.rpc().replySocket(
            self._zmqPorts.SERVER_REPLY_PORT)
        self._statusSocket = self.rpc().publisherSocket(
            self._zmqPorts.SERVER_STATUS_PORT)

        self._logger.notice('reply socket on port %d' %
                            self._zmqPorts.SERVER_REPLY_PORT)
        self._logger.notice('status socket on port %d' %
                            self._zmqPorts.SERVER_STATUS_PORT)

        self._createInstrumentDevice()

        self._controller= InstrumentController(
            self.name,
            self._zmqPorts,
            self._instrument,
            self._replySocket,
            self._statusSocket,
            self.rpc())


    def _runLoop(self):
        self._logRunning()

        FaultTolerantControlLoop(
            self._controller,
            Logger.of("Tipico controller control loop"),
            time,
            0.01).start()
        self._logger.notice("Terminated")


    @override
    def run(self):
        self._setUp()
        self._runLoop()
        return os.EX_OK


    @override
    def terminate(self, signal, frame):
        self._controller.terminate()
