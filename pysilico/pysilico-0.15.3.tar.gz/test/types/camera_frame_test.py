#!/usr/bin/env python
import unittest
import numpy as np
from pysilico.types.camera_frame import CameraFrame


__version__ = "$Id: camera_frame_test.py 163 2016-12-03 21:41:27Z lbusoni $"


class CameraFrameTest(unittest.TestCase):

    def setUp(self):
        self._createCameraFrame()


    def _createCameraFrame(self):
        self._frame = np.arange(
            120* 100, dtype=np.uint8).reshape((120, 100))
        self._counter = 42
        self._cameraFrame = CameraFrame.fromNumpyArray(self._frame,
                                                       self._counter)

    def testNumpy(self):
        self._createCameraFrame()
        frame2 = self._cameraFrame.toNumpyArray()
        self.assertTrue(np.array_equal(self._frame, frame2))


    def testTypeIsFloat(self):
        self.assertEqual(np.float, self._cameraFrame.toNumpyArray().dtype)


    def testComparison(self):
        counter = 42
        cameraFrame2 = CameraFrame.fromNumpyArray(self._frame.copy(), counter)
        self.assertTrue(self._cameraFrame == cameraFrame2)


    def testStringRepresentation(self):
        self.assertEqual('frame-42', str(self._cameraFrame))


if __name__ == "__main__":
    unittest.main()
