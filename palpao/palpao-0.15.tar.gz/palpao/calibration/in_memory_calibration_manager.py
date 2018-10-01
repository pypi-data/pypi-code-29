from plico.utils.decorator import override, returnsNone, returns
from palpao.types.modal_basis import ModalBasis
from palpao.calibration.abstract_calibration_manager import \
    AbstractCalibrationManager



__version__= "$Id: in_memory_calibration_manager.py 27 2018-01-27 08:48:07Z lbusoni $"


class InMemoryCalibrationManager(AbstractCalibrationManager):

    def __init__(self):
        self._modalBasisDict= {}


    @override
    @returnsNone
    def saveModalBasis(self, tag, modalBasis):
        self._modalBasisDict[tag]= modalBasis


    @override
    @returns(ModalBasis)
    def loadModalBasis(self, tag):
        return self._modalBasisDict[str(tag)]
