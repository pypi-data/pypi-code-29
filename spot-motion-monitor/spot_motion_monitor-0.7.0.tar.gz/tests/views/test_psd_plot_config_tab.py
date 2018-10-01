#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import PsdPlotConfigTab

class TestPsdPlotConfigTab:

    def test_parametersAfterConstruction(self, qtbot):
        configTab = PsdPlotConfigTab()
        qtbot.addWidget(configTab)
        assert configTab.name == 'PSD'

    def test_setParametersFromConfiguration(self, qtbot):
        configTab = PsdPlotConfigTab()
        qtbot.addWidget(configTab)

        config = {'waterfall': {'numBins': 15, 'colorMap': None}}
        configTab.setConfiguration(config)
        assert int(configTab.waterfallNumBinsLineEdit.text()) == config['waterfall']['numBins']
        assert configTab.waterfallColorMapComboBox.currentText() == ''

    def test_getParametersFromConfiguration(self, qtbot):
        configTab = PsdPlotConfigTab()
        qtbot.addWidget(configTab)
        truthConfig = {'waterfall': {'numBins': 35, 'colorMap': None}}
        configTab.waterfallNumBinsLineEdit.setText(str(truthConfig['waterfall']['numBins']))
        config = configTab.getConfiguration()
        assert config == truthConfig
