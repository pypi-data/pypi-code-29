#!/usr/bin/env python
import os
import unittest
import shutil

import numpy as np
from tipico.calibration.calibration_manager import CalibrationManager,\
    CalibrationManagerException
from tipico.types.encoder_calibration import EncoderCalibration




class CalibrationManagerTest(unittest.TestCase):

    CALIB_DIR= "./calib_tmp"


    def _removeCalibrationDir(self):
        if os.path.exists(self.CALIB_DIR):
            shutil.rmtree(self.CALIB_DIR)


    def setUp(self):
        self._removeCalibrationDir()
        self.calibMgr= CalibrationManager(self.CALIB_DIR)


    def tearDown(self):
        self._removeCalibrationDir()


    def _createCalibration(self):
        return EncoderCalibration(np.array([12, 3.14]))


    def testStorageOfEncoderCalibration(self):
        result= self._createCalibration()

        self.calibMgr.saveEncoderCalibration("foo", result)
        self.assertTrue(os.path.exists(
            os.path.join(self.CALIB_DIR,
                         "encoder_calibration",
                         "foo.fits")))

        loaded= self.calibMgr.loadEncoderCalibration("foo")
        self.assertTrue(np.array_equal(
            result.coefficients, loaded.coefficients))


    def testInvalidTag(self):
        res= self._createCalibration()
        self.assertRaises(
            CalibrationManagerException,
            self.calibMgr.saveEncoderCalibration,
            None, res)
        self.assertRaises(
            CalibrationManagerException,
            self.calibMgr.saveEncoderCalibration,
            "", res)

        self.assertRaises(
            CalibrationManagerException,
            self.calibMgr.loadEncoderCalibration, None)
        self.assertRaises(
            CalibrationManagerException,
            self.calibMgr.loadEncoderCalibration, "")





if __name__ == "__main__":
    unittest.main()
