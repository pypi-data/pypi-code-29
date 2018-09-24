import numpy as np

from picviewer.controller.panel_controller import PanelController
from picviewer.dataloader.data_collector import DataCollector
from picviewer.dataplotter.prepare_plot import PreparePlot

class MouseController():
    """
        mouse control class
        
    """
    def __init__(self,Mainwindow):

        self.main = Mainwindow

        self.main.canvas.mpl_connect('motion_notify_event', self.motion_notify)
        self.main.canvas.mpl_connect('button_press_event', self.onclick)
        self.main.canvas.mpl_connect('button_release_event', self.release_click)
        
        self.panelcontroller = PanelController(self.main)
        
        # Data collect class
        self.collectdata = DataCollector(self.main)
        # Plot class
        self.prepareplot = PreparePlot(self.main)

    def motion_notify(self,event):
        """
        mouse in motion
        """
        if not event.inaxes in self.main.axes.values(): return
        self.x_m, self.y_m = event.xdata, event.ydata
        self.main.coordLabel.setText("(x1,x2)=(%4.2f, %4.2f)" %(self.x_m, self.y_m)) 

    def onclick(self, event):
        """
        mouse pressed
        """
        # return if mouse click is outside panels
        if not event.inaxes in self.main.axes.values(): return

        self.main.pressed = True  # True if mouse is on-click
        # Select a panel by mouse clicking
        self.main.panelselect = np.where(np.array(self.main.axes.values()) == event.inaxes)[0][0]+1
        i = (self.main.panelselect-1)/self.main.ncolumn
        j = np.mod((self.main.panelselect-1),self.main.ncolumn)
        self.main.panelbuttons[(i,j)].setChecked(True)
        self.panelcontroller.panelbutton()

        self.x_o, self.y_o = event.xdata, event.ydata
        # to draw rectangle
        #self.pos1[0], self.pos1[1] = event.x, event.y
        #self.pos2[0], self.pos2[1] = event.x, event.y

        #self.xpix_o, self.ypix_o = event.x, event.y

        if self.main.line_panel[self.main.panelselect-1]:
            # remove previous line
            if self.main.panelselect-1 in self.main.line.keys():
                self.main.line[(self.main.panelselect-1)].remove()
                self.main.canvas.draw()
                 
        elif  self.main.rectangle_panel[self.main.panelselect-1]:
            # remove previous rectangle
            if self.main.panelselect-1 in self.main.rectangle1.keys():
                self.main.rectangle1[(self.main.panelselect-1)].remove()
                self.main.rectangle2[(self.main.panelselect-1)].remove()
                self.main.rectangle3[(self.main.panelselect-1)].remove()
                self.main.rectangle4[(self.main.panelselect-1)].remove()
                self.main.canvas.draw()

    def release_click(self, event):
        """
        mouse released

        """
        
        # Return if mouse click is outside panels.
        if not event.inaxes in self.main.axes.values(): return
        # return if mouse is released inside panel but pressed outside.
        if not self.main.pressed: return
        
        #QtGui.QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)
        # Return if mouse is pressed and released at the same position.
        self.x_r, self.y_r = event.xdata, event.ydata    
        if self.x_r == self.x_o and self.y_r == self.y_o: 
            self.main.pressed = False
            return

        # Zoom-in the image by mouse dragging
        if (not self.main.line_panel[self.main.panelselect-1]) and (not self.main.rectangle_panel[self.main.panelselect-1]):

            if self.main.dim == 3:
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                    x1axis = self.main.xaxis
                    x2axis = self.main.yaxis
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                    x1axis = self.main.zaxis
                    x2axis = self.main.xaxis
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                    x1axis = self.main.zaxis
                    x2axis = self.main.yaxis
            else:
                x1axis = self.main.zaxis
                x2axis = self.main.xaxis

            # Do not zoom in but return if mouse is pressed and released at very close points. 
            # This might be a mistake of clicking rather than intending to drag.
            if abs(self.x_r -self.x_o)/(x1axis[-1]-x1axis[0]) < 0.03 and \
                    abs(self.y_r -self.y_o)/(x1axis[-1]-x1axis[0]) < 0.03: 
                self.main.pressed = False
                return

            # Zoom in the image
            x1minloc = int((np.min([self.x_o,self.x_r])-x1axis[0])/(x1axis[-1]-x1axis[0])*100.)
            x1maxloc = int((np.max([self.x_o,self.x_r])-x1axis[0])/(x1axis[-1]-x1axis[0])*100.)
            x2minloc = int((np.min([self.y_o,self.y_r])-x2axis[0])/(x2axis[-1]-x2axis[0])*100.)
            x2maxloc = int((np.max([self.y_o,self.y_r])-x2axis[0])/(x2axis[-1]-x2axis[0])*100.)
            
            self.main.x1minSlider.setValue(x1minloc)
            self.main.x1maxSlider.setValue(x1maxloc)
            self.main.x2minSlider.setValue(x2minloc)
            self.main.x2maxSlider.setValue(x2maxloc)
            if self.main.field_select_panel[self.main.panelselect-1]:
                self.collectdata.loadfield()
                self.prepareplot.plotfield()
            else:
                self.collectdata.loadparticle()
                self.prepareplot.plotparticle()

        # line selection and local plot
        if self.main.line_panel[self.main.panelselect-1]:
                self.plot = self.main.figure.add_subplot(self.main.nrow,self.main.ncolumn,self.main.panelselect)
                self.main.line[(self.main.panelselect-1)], = self.plot.plot(
                        [self.x_o,self.x_r],[self.y_o,self.y_r], 
                        ':', linewidth=1.0, color='black')
                self.main.canvas.draw()

                #self.PrepareLocalplot()

        # rectangle selection and local plot
        elif  self.main.rectangle_panel[self.main.panelselect-1]:
                self.plot = self.main.figure.add_subplot(self.main.nrow,self.main.ncolumn,self.main.panelselect)
                self.main.rectangle1[(self.main.panelselect-1)], = self.plot.plot(
                        [self.x_o,self.x_r],[self.y_o,self.y_o], 
                        ':', linewidth=1.0, color='black')
                self.main.rectangle2[(self.main.panelselect-1)], = self.plot.plot(
                        [self.x_o,self.x_r],[self.y_m,self.y_r], 
                        ':', linewidth=1.0, color='black')
                self.main.rectangle3[(self.main.panelselect-1)], = self.plot.plot(
                        [self.x_o,self.x_o],[self.y_o,self.y_r], 
                        ':', linewidth=1.0, color='black')
                self.main.rectangle4[(self.main.panelselect-1)], = self.plot.plot(
                        [self.x_r,self.x_r],[self.y_o,self.y_r], 
                        ':', linewidth=1.0, color='black')
                self.main.canvas.draw()

                #self.PrepareLocalplot()

        self.main.pressed = False