from picviewer.dataloader.data_collector import DataCollector
from picviewer.dataplotter.prepare_plot import PreparePlot


class SpaceController():
    """
        space control class
        
    """
    def __init__(self,Mainwindow):

        self.main = Mainwindow

        # Data collect class
        self.collectdata = DataCollector(self.main)
        # Plot class
        self.prepareplot = PreparePlot(self.main)
        
    def x1minslider(self):

        x1minloc = self.main.x1minSlider.value()
        x1maxloc = self.main.x1maxSlider.value()
        if x1minloc > x1maxloc: 
            x1minloc = x1maxloc - 2
            self.main.x1minSlider.setValue(x1minloc)
        if self.main.dim == 3:
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                xmin = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*x1minloc/100. 
                self.main.x1minLabel.setText(str("%.1f" %xmin))
                self.main.xminloc_panel[self.main.panelselect-1] = x1minloc
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                zmin = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*x1minloc/100.
                self.main.x1minLabel.setText(str("%.1f" %zmin))
                self.main.zminloc_panel[self.main.panelselect-1] = x1minloc
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                zmin = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*x1minloc/100. 
                self.main.x1minLabel.setText(str("%.1f" %zmin))
                self.main.zminloc_panel[self.main.panelselect-1] = x1minloc
        else:
            zmin = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*(x1minloc)/100.
            self.main.x1minLabel.setText(str("%.1f" %zmin))
            self.main.zminloc_panel[self.main.panelselect-1] = x1minloc

    
    def x1maxslider(self):

        x1minloc = self.main.x1minSlider.value()
        x1maxloc = self.main.x1maxSlider.value()
        if x1maxloc < x1minloc: 
            x1maxloc = x1minloc + 2
            self.main.x1maxSlider.setValue(x1maxloc)
        if self.main.dim == 3:
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                xmax = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*x1maxloc/100. 
                self.main.x1maxLabel.setText(str("%.1f" %xmax))
                self.main.xmaxloc_panel[self.main.panelselect-1] = x1maxloc
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                zmax = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*x1maxloc/100.
                self.main.x1maxLabel.setText(str("%.1f" %zmax))
                self.main.zmaxloc_panel[self.main.panelselect-1] = x1maxloc
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                zmax = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*x1maxloc/100. 
                self.main.x1maxLabel.setText(str("%.1f" %zmax))
                self.main.zmaxloc_panel[self.main.panelselect-1] = x1maxloc
        else:
            zmax = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*(x1maxloc)/100.
            self.main.x1maxLabel.setText(str("%.1f" %zmax))
            self.main.zmaxloc_panel[self.main.panelselect-1] = x1maxloc

    def x2minslider(self):

        x2minloc = self.main.x2minSlider.value()
        x2maxloc = self.main.x2maxSlider.value()
        if x2minloc > x2maxloc: 
            x2minloc = x2maxloc - 2
            self.main.x2minSlider.setValue(x2minloc)
        if self.main.dim == 3:
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                ymin = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*x2minloc/100. 
                self.main.x2minLabel.setText(str("%.1f" %ymin))
                self.main.yminloc_panel[self.main.panelselect-1] = x2minloc
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                xmin = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*x2minloc/100.
                self.main.x2minLabel.setText(str("%.1f" %xmin))
                self.main.xminloc_panel[self.main.panelselect-1] = x2minloc
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                ymin = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*x2minloc/100. 
                self.main.x2minLabel.setText(str("%.1f" %ymin))
                self.main.yminloc_panel[self.main.panelselect-1] = x2minloc
        else:
            xmin = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*(x2minloc)/100.
            self.main.x2minLabel.setText(str("%.1f" %xmin))
            self.main.xminloc_panel[self.main.panelselect-1] = x2minloc

    
    def x2maxslider(self):

        x2minloc = self.main.x2minSlider.value()
        x2maxloc = self.main.x2maxSlider.value()
        if x2maxloc < x2minloc: 
            x2maxloc = x2minloc + 2
            self.main.x2maxSlider.setValue(x2maxloc)
        if self.main.dim == 3:
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                ymax = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*x2maxloc/100. 
                self.main.x2maxLabel.setText(str("%.1f" %ymax))
                self.main.ymaxloc_panel[self.main.panelselect-1] = x2maxloc
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                xmax = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*x2maxloc/100. 
                self.main.x2maxLabel.setText(str("%.1f" %xmax))
                self.main.xmaxloc_panel[self.main.panelselect-1] = x2maxloc
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                ymax = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*x2maxloc/100. 
                self.main.x2maxLabel.setText(str("%.1f" %ymax))
                self.main.ymaxloc_panel[self.main.panelselect-1] = x2maxloc
        else:
            xmax = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*x2maxloc/100. 
            self.main.x2maxLabel.setText(str("%.1f" %xmax))
            self.main.xmaxloc_panel[self.main.panelselect-1] = x2maxloc

    def releasebutton(self):
        """
        Return to the original space range

        """
        self.main.x1minSlider.setValue(0)
        self.main.x1maxSlider.setValue(100)
        self.main.x2minSlider.setValue(0)
        self.main.x2maxSlider.setValue(100)

        if self.main.field_select_panel[self.main.panelselect-1]:
            self.collectdata.loadfield()
            self.prepareplot.plotfield()
        else:
            self.collectdata.loadparticle()
            self.prepareplot.plotparticle()



