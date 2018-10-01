#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
__all__ = ['PlotPsdController']

class PlotPsdController:

    """This class handles the interactions between the main program and the
       power spectrum distribution (PSD) waterfall plots.

    Attributes
    ----------
    psdXPlot : PsdWaterfallPlotWidget
        The instance of the waterfall plot for the PSD x coordinates.
    psdYPlot : PsdWaterfallPlotWidget
        The instance of the waterfall plot for the PSD y coordinates.
    """

    def __init__(self, psdx, psdy):
        """Initialize the class.

        Parameters
        ----------
        psdx : PsdWaterfallPlotWidget
            The instance of the waterfall plot for the PSD x coordinates.
        psdy : PsdWaterfallPlotWidget
            The instance of the waterfall plot for the PSD y coordinates.
        """
        self.psdXPlot = psdx
        self.psdYPlot = psdy

    def getPlotConfiguration(self):
        """Get the current camera configuration.

        Returns
        -------
        dict
            The set of current camera configuration parameters.
        """
        config = {}
        config['waterfall'] = self.psdXPlot.getConfiguration()
        return config

    def setPlotConfiguration(self, config):
        """Set a new configuration on the PSD plots.

        Parameters
        ----------
        config : dict
            The new configuration parameters.
        """
        self.psdXPlot.setConfiguration(config['waterfall'])
        self.psdYPlot.setConfiguration(config['waterfall'])

    def setup(self, arraySize, timeScale):
        """Setup the controller's internal information.

        Parameters
        ----------
        arraySize : int
            The vertical dimension of the PSD waterfall plot data.
        timeScale : float
            The total accumulation time from the buffer size and ROI FPS.
        """
        self.psdXPlot.setup(arraySize, timeScale, 'X')
        self.psdYPlot.setup(arraySize, timeScale, 'Y')

    def update(self, psdDataX, psdDataY, frequencies):
        """Update the controller's plot widgets with the data provided.

        NOTE: If NoneType data is provided, the updatePlot methods are not called.

        Parameters
        ----------
        psdDataX : numpy.array
            The array of the PSD x coordinate data.
        psdDataY : numpy.array
            The array of the PSD y coordinate data.
        frequencies : numpy.array
            The frequency array associated with the PSD data.
        """
        if psdDataX is None or psdDataY is None or frequencies is None:
            return

        self.psdXPlot.updatePlot(psdDataX, frequencies)
        self.psdYPlot.updatePlot(psdDataY, frequencies)

    def updateTimeScale(self, newTimeScale):
        """Update the stored timescale in the plot widgets.

        Parameters
        ----------
        newTimeScale : float
            The new timescale.
        """
        self.psdXPlot.setTimeScale(newTimeScale)
        self.psdYPlot.setTimeScale(newTimeScale)
