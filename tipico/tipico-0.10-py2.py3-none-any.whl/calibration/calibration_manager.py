
import os
import pyfits
from tipico.calibration.abstract_calibration_manager import \
    AbstractCalibrationManager
from plico.utils.decorator import override, returnsNone, returns, cacheResult
from tipico.types.encoder_calibration import EncoderCalibration
from plico.utils.fits_file_based_calibration_manager import \
    FitsFileBasedCalibrationManager


__version__= "$Id: calibration_manager.py 25 2018-01-26 19:00:40Z lbusoni $"


class CalibrationManagerException(Exception):
    pass


class CalibrationManager(AbstractCalibrationManager,
                         FitsFileBasedCalibrationManager):

    def __init__(self, calibrationRootDir):
        self._calibRootDir = calibrationRootDir


    def _checkTag(self, tag):
        if tag is None:
            raise CalibrationManagerException(
                "A tag must be given but is None")
        if len(tag) == 0:
            raise CalibrationManagerException(
                "A tag name must be valid but it is '%s'" % (tag))


    def getEncoderCalibrationFileName(self, tag):
        return os.path.join(self._calibRootDir,
                            "encoder_calibration",
                            "%s.fits" % tag)


    @override
    @returnsNone
    def saveEncoderCalibration(self, tag, encoderCalibration):
        self._checkTag(tag)
        fileName= self.getEncoderCalibrationFileName(tag)
        self._createFoldersIfMissing(fileName)
        pyfits.writeto(fileName,
                       encoderCalibration.coefficients,
                       clobber=False)


    @override
    @returns(EncoderCalibration)
    @cacheResult
    def loadEncoderCalibration(self, tag):
        self._checkTag(tag)
        fileName= self.getEncoderCalibrationFileName(tag)
        hduList= pyfits.open(fileName)
        return EncoderCalibration(hduList[0].data)
