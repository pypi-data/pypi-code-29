import abc
from plico.utils.decorator import returns, returnsNone
from six import with_metaclass
from tipico.types.encoder_calibration import EncoderCalibration


__version__= "$Id: abstract_calibration_manager.py 25 2018-01-26 19:00:40Z lbusoni $"



class AbstractCalibrationManager(with_metaclass(abc.ABCMeta, object)):

    @abc.abstractmethod
    @returns(EncoderCalibration)
    def loadEncoderCalibration(self, tag):
        assert False


    @abc.abstractmethod
    @returnsNone
    def saveEncoderCalibration(self, tag, encoderCalibration):
        assert False


