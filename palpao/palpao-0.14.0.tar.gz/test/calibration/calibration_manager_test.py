#!/usr/bin/env python
import os
import unittest
import shutil

import numpy as np
from palpao.calibration.calibration_manager import CalibrationManager,\
    CalibrationManagerException
from palpao.types.modal_basis import ModalBasis


__version__= "$Id: calibration_manager_test.py 26 2018-01-26 19:06:25Z lbusoni $"


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


    def _createModalBasis(self):
        return ModalBasis(np.arange(6).reshape((3, 2)))


    def testStorageOfModalBasis(self):
        result= self._createModalBasis()

        self.calibMgr.saveModalBasis("foo", result)
        self.assertTrue(os.path.exists(
            os.path.join(self.CALIB_DIR, "modal_basis", "foo.fits")))

        loaded= self.calibMgr.loadModalBasis("foo")
        self.assertTrue(np.array_equal(
            result.modalToZonalMatrix, loaded.modalToZonalMatrix))


    def testInvalidTag(self):
        res= self._createModalBasis()
        self.assertRaises(
            CalibrationManagerException,
            self.calibMgr.saveModalBasis,
            None, res)
        self.assertRaises(
            CalibrationManagerException,
            self.calibMgr.saveModalBasis,
            "", res)

        self.assertRaises(
            CalibrationManagerException,
            self.calibMgr.loadModalBasis, None)
        self.assertRaises(
            CalibrationManagerException,
            self.calibMgr.loadModalBasis, "")





if __name__ == "__main__":
    unittest.main()
