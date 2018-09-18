import abc
import numpy
from plico.utils.decorator import returns
from six import with_metaclass




class AbstractInstrument(with_metaclass(abc.ABCMeta, object)):

    @abc.abstractmethod
    def moveTo(self):
        assert False


    @abc.abstractmethod
    @returns(numpy.ndarray)
    def getPosition(self):
        assert False


    @abc.abstractmethod
    @returns(str)
    def serialNumber(self):
        assert False
