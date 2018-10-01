#!/usr/bin/env python

import unittest
import numpy as np
from palpao.calibration.in_memory_calibration_manager import \
    InMemoryCalibrationManager
from palpao.types.modal_basis import ModalBasis

__version__= "$Id: in_memory_calibration_manager_test.py 26 2018-01-26 19:06:25Z lbusoni $"


class InMemoryCalibrationManagerTest(unittest.TestCase):

    def setUp(self):
        self.calibMgr= InMemoryCalibrationManager()


    def testModalBasisStorage(self):
        tag= "20140909_110800"
        originalObject= ModalBasis(np.arange(8).reshape((4, 2)))
        self.calibMgr.saveModalBasis(tag, originalObject)
        storedObject= self.calibMgr.loadModalBasis(tag)
        self.assertEqual(storedObject, originalObject)



if __name__ == "__main__":
    unittest.main()
