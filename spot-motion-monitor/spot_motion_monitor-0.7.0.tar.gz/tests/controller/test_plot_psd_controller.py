#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.controller import PlotPsdController
from spot_motion_monitor.views import PsdWaterfallPlotWidget

class TestPlotPsdController:

    def setup_class(cls):
        cls.arraySize = 5
        cls.timeScale = 10

    def test_parametersAfterContruction(self, qtbot):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        pfc = PlotPsdController(psdx, psdy)
        assert pfc.psdXPlot is not None
        assert pfc.psdYPlot is not None

    def test_parametersAfterSetup(self, qtbot):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        pfc = PlotPsdController(psdx, psdy)
        pfc.setup(self.arraySize, self.timeScale)
        assert pfc.psdXPlot.arraySize == self.arraySize
        assert pfc.psdYPlot.arraySize == self.arraySize

    def test_update(self, qtbot, mocker):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        pfc = PlotPsdController(psdx, psdy)
        pfc.setup(self.arraySize, self.timeScale)

        np.random.seed(3000)
        psdDataX = np.random.random(7)
        psdDataY = np.random.random(7)
        freqs = np.random.random(7)

        mockPsdXPlotUpdatePlot = mocker.patch.object(pfc.psdXPlot, 'updatePlot')
        mockPsdYPlotUpdatePlot = mocker.patch.object(pfc.psdYPlot, 'updatePlot')
        pfc.update(psdDataX, psdDataY, freqs)

        assert mockPsdXPlotUpdatePlot.call_count == 1
        assert mockPsdYPlotUpdatePlot.call_count == 1

    def test_badFftData(self, qtbot, mocker):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        pfc = PlotPsdController(psdx, psdy)
        pfc.setup(self.arraySize, self.timeScale)

        mockPsdXPlotUpdatePlot = mocker.patch.object(pfc.psdXPlot, 'updatePlot')
        mockPsdYPlotUpdatePlot = mocker.patch.object(pfc.psdYPlot, 'updatePlot')
        pfc.update(None, None, None)

        assert mockPsdXPlotUpdatePlot.call_count == 0
        assert mockPsdYPlotUpdatePlot.call_count == 0

    def test_updateTimeScale(self, qtbot, mocker):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        pfc = PlotPsdController(psdx, psdy)
        pfc.setup(self.arraySize, self.timeScale)

        mockPsdXPlotSetTimeScale = mocker.patch.object(pfc.psdXPlot, 'setTimeScale')
        mockPsdYPlotSetTimeScale = mocker.patch.object(pfc.psdYPlot, 'setTimeScale')
        pfc.updateTimeScale(100)

        assert mockPsdXPlotSetTimeScale.call_count == 1
        assert mockPsdYPlotSetTimeScale.call_count == 1

    def test_getPlotConfiguration(self, qtbot):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        pfc = PlotPsdController(psdx, psdy)
        pfc.setup(self.arraySize, self.timeScale)

        currentConfig = pfc.getPlotConfiguration()
        assert len(currentConfig) == 1
        assert list(currentConfig.keys()) == ['waterfall']

    def test_setPlotConfiguration(self, qtbot, mocker):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        pfc = PlotPsdController(psdx, psdy)
        pfc.setup(self.arraySize, self.timeScale)

        mockPsdXWaterfallSetConfig = mocker.patch.object(pfc.psdXPlot, 'setConfiguration')
        mockPsdYWaterfallSetConfig = mocker.patch.object(pfc.psdYPlot, 'setConfiguration')

        truthConfig = {'waterfall': {'numBins': 10, 'colorMap': None}}
        pfc.setPlotConfiguration(truthConfig)

        assert mockPsdXWaterfallSetConfig.call_count == 1
        assert mockPsdYWaterfallSetConfig.call_count == 1
