from picviewer.dataloader.data_collector import DataCollector
from picviewer.dataplotter.prepare_plot import PreparePlot
from picviewer.dataloader.get_datainfo import DataInfo

class TimeController():
    """
        time control class
        
        Returns:
            None
    """
    def __init__(self,Mainwindow):

        self.main = Mainwindow
        
        self.datainfo = DataInfo()

        # Data collect class
        self.collectdata = DataCollector(self.main)
        # Plot class
        self.prepareplot = PreparePlot(self.main)

    def backwardtime(self):
        
        tstride = self.main.stepSpinBox.value()
        self.main.tstep = self.main.timeSlider.value()
        self.main.tstep = self.main.tstep - tstride
        if self.main.tstep < 1:
            self.main.tstep = self.main.tstep + tstride
        else:
            self.main.tstepLabel.setText("tstep %d" %self.main.tstep)
            self.main.time = self.main.taxis[self.main.tstep-1]
            self.main.timeLabel.setText("%6.1f fs" %self.main.time)
            self.main.timeSlider.setValue(self.main.tstep)

        # update domain axes
        #self.main.xaxis, self.main.yaxis, self.main.zaxis = \
        #        self.datainfo.update_domain_axes(
        #            self.main.filepath, self.main.dataformat, 
        #            self.main.dim, self.main.iterations[self.main.tstep-1])
        #self.main.ChangeRangeSliderLabels()

        if self.main.synctimeBox.isChecked():
            self.collectdata.loaddatasync()
            self.prepareplot.plotsync()
        else:
            if self.main.field_select_panel[self.main.panelselect-1]:
                self.collectdata.loadfield()
                self.prepareplot.plotfield()
            else:
                self.collectdata.loadparticle()
                self.prepareplot.plotparticle()

    def fowardtime(self):
        
        tstride = self.main.stepSpinBox.value()
        self.main.tstep = self.main.timeSlider.value()
        self.main.tstep = self.main.tstep + tstride
        if self.main.tstep > len(self.main.taxis):
            self.main.tstep = self.main.tstep - tstride
        else:
            self.main.tstepLabel.setText("tstep %d" %self.main.tstep)
            self.main.time = self.main.taxis[self.main.tstep-1]
            self.main.timeLabel.setText("%6.1f fs" %self.main.time)
            self.main.timeSlider.setValue(self.main.tstep)

        if self.main.synctimeBox.isChecked():
            self.collectdata.loaddatasync()
            self.prepareplot.plotsync()
        else:
            if self.main.field_select_panel[self.main.panelselect-1]:
                self.collectdata.loadfield()
                self.prepareplot.plotfield()
            else:
                self.collectdata.loadparticle()
                self.prepareplot.plotparticle()


    def timeslider(self):

        self.main.tstep = self.main.timeSlider.value()
        self.main.time = self.main.taxis[self.main.tstep-1]
        self.main.tstepLabel.setText("tstep %d" %self.main.tstep)
        self.main.timeLabel.setText("%6.1f fs" %self.main.time)
          