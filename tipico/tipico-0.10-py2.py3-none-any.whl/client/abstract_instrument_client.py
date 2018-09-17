import abc
from plico.utils.decorator import returnsNone, returns, returnsForExample
from tipico.types.instrument_status import InstrumentStatus
from six import with_metaclass


__version__= "$Id: abstract_deformable_mirror_client.py 26 2018-01-26 19:06:25Z lbusoni $"


class SnapshotEntry(object):
    COMMAND_COUNTER= "COMMAND_COUNTER"
    SERIAL_NUMBER= "SERIAL_NUMBER"
    STEP_COUNTER= "STEP_COUNTER"



class AbstractInstrumentClient(with_metaclass(abc.ABCMeta, object)):


    @abc.abstractmethod
    @returnsNone
    def moveTo(self, actuatorPosition):
        assert False


    @abc.abstractmethod
    def getPosition(self):
        assert False


    @abc.abstractmethod
    @returnsForExample({'MY_INSTRUMENT.COMMAND_COUNTER': 42})
    def getSnapshot(self, prefix):
        assert False


    @abc.abstractmethod
    @returns(InstrumentStatus)
    def getStatus(self):
        assert False
