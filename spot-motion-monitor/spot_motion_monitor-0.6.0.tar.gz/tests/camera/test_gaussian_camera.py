#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.camera.gaussian_camera import GaussianCamera

class TestGaussianCamera():

    def setup_class(self):
        self.camera = GaussianCamera()

    def test_parametersAfterConstruction(self):
        assert self.camera.seed is None
        assert self.camera.height == 480
        assert self.camera.width == 640
        assert self.camera.spotSize == 20
        assert self.camera.fpsFullFrame == 24
        assert self.camera.fpsRoiFrame == 40
        assert self.camera.roiSize == 50
        assert self.camera.postageStamp is None
        assert self.camera.xPoint is None
        assert self.camera.yPoint is None

    def test_parametersAfterStartup(self):
        self.camera.startup()
        assert self.camera.postageStamp is not None
        assert self.camera.xPoint is not None
        assert self.camera.yPoint is not None

    def test_getFullFrame(self):
        self.camera.seed = 1000
        self.camera.startup()
        frame = self.camera.getFullFrame()
        assert frame.shape == (480, 640)
        max_point1, max_point2 = np.where(frame == np.max(frame))
        assert max_point1[0] == 225
        assert max_point2[0] == 288

    def test_getRoiFrame(self):
        self.camera.seed = 1000
        self.camera.startup()
        frame = self.camera.getRoiFrame()
        assert frame.shape == (50, 50)
        max_point1, max_point2 = np.where(frame == np.max(frame))
        assert max_point1[0] == 25
        assert max_point2[0] == 24

    def test_getOffset(self):
        self.camera.seed = 1000
        self.camera.startup()
        offset = self.camera.getOffset()
        assert offset == (264, 200)
