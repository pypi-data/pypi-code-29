from plico.utils.decorator import override, returnsNone, returns
from tipico.calibration.abstract_calibration_manager import \
    AbstractCalibrationManager
from tipico.types.encoder_calibration import EncoderCalibration



class InMemoryCalibrationManager(AbstractCalibrationManager):

    def __init__(self):
        self._encoderCalibrationDict= {}


    @override
    @returnsNone
    def saveEncoderCalibration(self, tag, encoderCalibration):
        self._encoderCalibrationDict[tag]= encoderCalibration


    @override
    @returns(EncoderCalibration)
    def loadEncoderCalibration(self, tag):
        return self._encoderCalibrationDict[str(tag)]
