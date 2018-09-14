#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import Centroid1dPlotWidget

class TestCentroid1dPlotWidget():

    def test_parametersAfterConstruction(self, qtbot):
        c1dpw = Centroid1dPlotWidget()
        qtbot.addWidget(c1dpw)
        assert c1dpw.plot is None
        assert c1dpw.curve is None
        assert c1dpw.dataSize is None
        assert c1dpw.data is None
        assert c1dpw.timeRange is None
        assert c1dpw.dataCounter == 0
        assert c1dpw.rollArray is False
        assert c1dpw.roiFps is None
        assert c1dpw.yRange is None
        assert c1dpw.pixelRangeAddition == 5
        assert c1dpw.numAccumFrames == 15

    def test_parametersAfterSetup(self, qtbot):
        c1dpw = Centroid1dPlotWidget()
        qtbot.addWidget(c1dpw)
        arraySize = 1000
        roiFps = 40
        c1dpw.setup(arraySize, 'X', roiFps)
        assert c1dpw.plot is not None
        assert c1dpw.curve is not None
        assert c1dpw.dataSize == arraySize
        assert c1dpw.data.size == arraySize
        assert c1dpw.timeRange.size == arraySize
        assert c1dpw.rollArray is False
        assert c1dpw.roiFps == roiFps

    def test_updatePlot(self, qtbot, mocker):
        c1dpw = Centroid1dPlotWidget()
        c1dpw.show()
        qtbot.addWidget(c1dpw)
        arraySize = 3
        currentFps = 2
        c1dpw.numAccumFrames = 2
        c1dpw.setup(arraySize, 'X', currentFps)
        timeRange = [0.0, 0.5, 1.0]
        assert c1dpw.timeRange.tolist() == timeRange
        mockSetData = mocker.patch.object(c1dpw.curve, 'setData')
        values = [254.43, 254.86, 253.91, 254.21]
        c1dpw.updatePlot(values[0])
        assert c1dpw.data.tolist() == [values[0]] + 2 * [0.0]
        assert c1dpw.dataCounter == 1
        assert c1dpw.yRange is None
        c1dpw.updatePlot(values[1])
        assert c1dpw.data.tolist() == [values[0], values[1], 0.0]
        assert c1dpw.yRange == [249, 259]
        c1dpw.updatePlot(values[2])
        assert c1dpw.data.tolist() == values[:-1]
        assert c1dpw.dataCounter == arraySize
        assert c1dpw.rollArray is True
        c1dpw.updatePlot(values[3])
        assert c1dpw.data.tolist() == values[1:]
        assert c1dpw.dataCounter == arraySize
        assert c1dpw.rollArray is True
        assert mockSetData.call_count == len(values)

    def test_updateRoiFps(self, qtbot):
        c1dpw = Centroid1dPlotWidget()
        c1dpw.show()
        qtbot.addWidget(c1dpw)
        arraySize = 1024
        c1dpw.setup(arraySize, 'X', 40)
        newRoiFps = 90
        c1dpw.setRoiFps(newRoiFps)
        assert c1dpw.timeRange.shape[0] == arraySize
        assert c1dpw.timeRange[-1] == (arraySize - 1) / newRoiFps

    def test_updateArraySize(self, qtbot):
        c1dpw = Centroid1dPlotWidget()
        c1dpw.show()
        qtbot.addWidget(c1dpw)
        arraySize = 1024
        roiFps = 40
        c1dpw.setup(arraySize, 'X', roiFps)
        c1dpw.rollArray = True
        newArraySize = 2048
        c1dpw.setArraySize(newArraySize)
        assert c1dpw.dataSize == newArraySize
        assert c1dpw.data.shape[0] == newArraySize
        assert c1dpw.timeRange.shape[0] == newArraySize
        assert c1dpw.timeRange[-1] == (newArraySize - 1) / roiFps
        assert c1dpw.rollArray is False
