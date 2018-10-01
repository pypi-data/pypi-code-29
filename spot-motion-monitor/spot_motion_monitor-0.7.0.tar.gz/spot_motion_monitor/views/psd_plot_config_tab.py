#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTabWidget

import spot_motion_monitor.utils as utils
from spot_motion_monitor.views.ui_psd_plots_config import Ui_PsdPlotConfigForm

__all__ = ['PsdPlotConfigTab']

class PsdPlotConfigTab(QTabWidget, Ui_PsdPlotConfigForm):
    """Class that handles the Power Spectrum Distribution plot configuration
       tab.

    Attributes
    ----------
    name : str
        The name for the tab widget.
    """

    def __init__(self, parent=None):
        """Summary

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.waterfallNumBinsLineEdit.setValidator(QIntValidator(1, 1000))
        self.name = 'PSD'

    def getConfiguration(self):
        """Get the current configuration parameters from the tab's widgets.

        Returns
        -------
        dict
            The current set of configuration parameters.
        """
        config = {}
        config['waterfall'] = {}
        config['waterfall']['numBins'] = int(self.waterfallNumBinsLineEdit.text())
        config['waterfall']['colorMap'] = None
        return config

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : dict
            The current set of configuration parameters.
        """
        self.waterfallNumBinsLineEdit.setText(str(config['waterfall']['numBins']))
        value = utils.noneToDefaultOrValue(config['waterfall']['colorMap'])
        self.waterfallColorMapComboBox.setCurrentText(value)
