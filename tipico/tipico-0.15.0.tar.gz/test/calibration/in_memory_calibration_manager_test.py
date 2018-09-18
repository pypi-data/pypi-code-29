#!/usr/bin/env python

import unittest
import numpy as np
from tipico.calibration.in_memory_calibration_manager import \
    InMemoryCalibrationManager
from tipico.types.encoder_calibration import EncoderCalibration



class InMemoryCalibrationManagerTest(unittest.TestCase):

    def setUp(self):
        self.calibMgr= InMemoryCalibrationManager()


    def testEncoderCalibrationStorage(self):
        tag= "20140909_110800"
        originalObject= EncoderCalibration(np.array([1, 23]))
        self.calibMgr.saveEncoderCalibration(tag, originalObject)
        storedObject= self.calibMgr.loadEncoderCalibration(tag)
        self.assertEqual(storedObject, originalObject)



if __name__ == "__main__":
    unittest.main()
