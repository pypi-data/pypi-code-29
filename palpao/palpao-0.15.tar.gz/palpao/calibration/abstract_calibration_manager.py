import abc
from plico.utils.decorator import returns, returnsNone
from palpao.types.modal_basis import ModalBasis
from six import with_metaclass


__version__= "$Id: abstract_calibration_manager.py 27 2018-01-27 08:48:07Z lbusoni $"



class AbstractCalibrationManager(with_metaclass(abc.ABCMeta, object)):

    @abc.abstractmethod
    @returns(ModalBasis)
    def loadModalBasis(self, tag):
        assert False


    @abc.abstractmethod
    @returnsNone
    def saveModalBasis(self, tag, modalBasis):
        assert False


