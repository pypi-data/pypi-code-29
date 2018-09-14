#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.utils import FullFrameInformation, NO_DATA_VALUE, RoiFrameInformation
from spot_motion_monitor.views import CameraDataWidget

class TestCameraDataWidget():

    def formatFloatText(self, value):
        return "{:.2f}".format(value)

    def test_defaulTextValues(self, qtbot):
        cdw = CameraDataWidget()
        cdw.show()
        qtbot.addWidget(cdw)

        assert cdw.accumPeriodValueLabel.text() == NO_DATA_VALUE
        assert cdw.fluxValueLabel.text() == NO_DATA_VALUE
        assert cdw.maxAdcValueLabel.text() == NO_DATA_VALUE
        assert cdw.centroidXLabel.text() == NO_DATA_VALUE
        assert cdw.centroidYLabel.text() == NO_DATA_VALUE
        assert cdw.rmsXLabel.text() == NO_DATA_VALUE
        assert cdw.rmsYLabel.text() == NO_DATA_VALUE

    def test_FullFramePassedValues(self, qtbot):
        cdw = CameraDataWidget()
        cdw.show()
        qtbot.addWidget(cdw)

        ffi = FullFrameInformation(200, 342, 4032.428492, 170.482945)
        cdw.updateFullFrameData(ffi)

        assert cdw.accumPeriodValueLabel.text() == NO_DATA_VALUE
        assert cdw.centroidXLabel.text() == str(ffi.centerX)
        assert cdw.centroidYLabel.text() == str(ffi.centerY)
        assert cdw.fluxValueLabel.text() == self.formatFloatText(ffi.flux)
        assert cdw.maxAdcValueLabel.text() == self.formatFloatText(ffi.maxAdc)
        assert cdw.rmsXLabel.text() == NO_DATA_VALUE
        assert cdw.rmsYLabel.text() == NO_DATA_VALUE

    def test_RoiFramePassedValues(self, qtbot):
        cdw = CameraDataWidget()
        cdw.show()
        qtbot.addWidget(cdw)

        rfi = RoiFrameInformation(243.23, 354.97, 2763.58328, 103.53245, 1.4335, 1.97533, (1000, 25.0))
        cdw.updateRoiFrameData(rfi)

        assert cdw.accumPeriodValueLabel.text() == self.formatFloatText(rfi.validFrames[1])
        assert cdw.centroidXLabel.text() == self.formatFloatText(rfi.centerX)
        assert cdw.centroidYLabel.text() == self.formatFloatText(rfi.centerY)
        assert cdw.fluxValueLabel.text() == self.formatFloatText(rfi.flux)
        assert cdw.maxAdcValueLabel.text() == self.formatFloatText(rfi.maxAdc)
        assert cdw.rmsXLabel.text() == self.formatFloatText(rfi.rmsX)
        assert cdw.rmsYLabel.text() == self.formatFloatText(rfi.rmsY)

    def test_NoneForRoiFramePassedValues(self, qtbot):
        cdw = CameraDataWidget()
        cdw.show()
        qtbot.addWidget(cdw)

        rfi = None
        cdw.updateRoiFrameData(rfi)

        assert cdw.accumPeriodValueLabel.text() == NO_DATA_VALUE
        assert cdw.fluxValueLabel.text() == NO_DATA_VALUE
        assert cdw.maxAdcValueLabel.text() == NO_DATA_VALUE
        assert cdw.centroidXLabel.text() == NO_DATA_VALUE
        assert cdw.centroidYLabel.text() == NO_DATA_VALUE
        assert cdw.rmsXLabel.text() == NO_DATA_VALUE
        assert cdw.rmsYLabel.text() == NO_DATA_VALUE
