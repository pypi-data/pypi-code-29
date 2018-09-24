import numpy as np

from PySide import QtCore, QtGui

from picviewer.controller.slice_controller import SliceController
from picviewer.dataloader.data_collector import DataCollector
from picviewer.dataplotter.prepare_plot import PreparePlot


class PanelController():
    """
        panel control class
        
    """
    def __init__(self,Mainwindow):

        self.main = Mainwindow

        self.slicecontroller = SliceController(self.main)

        # Data collect class
        self.collectdata = DataCollector(self.main)
        # Plot class
        self.prepareplot = PreparePlot(self.main)


    def SetPanelButtons(self):
        """
        Create panel buttons
        """

        self.main.panelbuttons = {}
        self.main.panellayout = QtGui.QWidget(self.main.centralwidget)
        # Assign button locations
        button_height = 520
        button_left = 160
        x0 = -20*(self.main.ncolumn-2)+button_left
        w0 = 25*(self.main.ncolumn-2)+50
        y0 = (10./3)*(self.main.nrow-2)+button_height
        h0 = 20*(self.main.nrow-2)+60
        self.main.panellayout.setGeometry(QtCore.QRect(x0, y0, w0, h0))
        self.main.gridLayout = QtGui.QGridLayout(self.main.panellayout)
        self.main.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        for i in np.arange(self.main.nrow):
            for j in np.arange(self.main.ncolumn):
                self.main.panelbuttons[(i,j)] = QtGui.QRadioButton(self.main.panellayout)
                self.main.panelbuttons[(i,j)].setStyleSheet("")
                self.main.panelbuttons[(i,j)].setText("")
                self.main.gridLayout.addWidget(self.main.panelbuttons[(i,j)], i, j, 1, 1)
        self.main.panellayout.show()      
        
        i = (self.main.panelselect-1)/self.main.ncolumn
        j = np.mod((self.main.panelselect-1),self.main.ncolumn)
        self.main.panelbuttons[(i,j)].setChecked(True)


    def panelbutton(self):
        """
        Change the parameters to the saved ones in the selected panel

        """
        # self.panelselect is the index of a selected panel, i.e., 1, 2, 3, or ...
        for i in np.arange(self.main.nrow):
            for j in np.arange(self.main.ncolumn):
                if self.main.panelbuttons[(i,j)].isChecked():
                    self.main.panelselect = i*self.main.ncolumn+j+1

        # i.e., self.main.field_select_panel = [True, True, False, ....]
        if self.main.field_select_panel[self.main.panelselect-1]:
            self.main.fieldButton.setChecked(True)
            # i.e., self.main.field_panel = ['Bx', 'By', ...]
            field = self.main.field_panel[self.main.panelselect-1]
            index = self.main.field_list_indexed[field]
            self.main.fieldsComboBox.setCurrentIndex(index)
        else:
            self.main.particleButton.setChecked(True)
            # i.e., self.species_panel = ['elec', 'ions', ...]
            species = self.main.species_panel[self.main.panelselect-1]
            index = self.main.species_list_indexed[species]
            self.main.speciesComboBox.setCurrentIndex(index)
            # i.e., phase = ['px','x'], ['x','z'], ...
            phase = self.main.phase_panel[self.main.panelselect-1]        
            if self.main.dim == 2:
                index = self.main.phase_list1_indexed[phase]
            else:
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                    index = self.main.phase_list2_indexed[phase]
                    self.main.phaseComboBox.clear() 
                    for i in np.arange(len(self.main.phase_list2)):
                        self.main.phaseComboBox.addItem(self.main.phase_list2[i][0]+'-'+self.main.phase_list2[i][1], i)

                if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                    index = self.main.phase_list1_indexed[phase]
                    self.main.phaseComboBox.clear()
                    for i in np.arange(len(self.main.phase_list1)):
                        self.main.phaseComboBox.addItem(self.main.phase_list1[i][0]+'-'+self.main.phase_list1[i][1], i)

                if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                    index = self.main.phase_list3_indexed[phase]
                    self.main.phaseComboBox.clear() 
                    for i in np.arange(len(self.main.phase_list3)):
                        self.main.phaseComboBox.addItem(self.main.phase_list3[i][0]+'-'+self.main.phase_list3[i][1], i)

            self.main.phaseComboBox.setCurrentIndex(index)

        if self.main.aspect_panel[self.main.panelselect-1] == 'equal':
            self.main.aspectCheckBox.setChecked(True)
        else:
             self.main.aspectCheckBox.setChecked(False)

        if self.main.line_panel[self.main.panelselect-1] == True:
            self.main.lineCheckBox.setChecked(True)
        else:
            self.main.lineCheckBox.setChecked(False)

        if self.main.rectangle_panel[self.main.panelselect-1] == True:
            self.main.rectangleCheckBox.setChecked(True)
        else:
            self.main.rectangleCheckBox.setChecked(False)

        
        if self.main.dim == 3:
            # i.e., self.main.slicevalue_panel = [0, 0, 10, .. ] 
            # The number is between [0,30] and specifies the location
            # on the 3rd axis of the 2D slice plane.
            slicevalue = self.main.slicevalue_panel[self.main.panelselect-1]
            self.main.slicevalueSlider.setValue(slicevalue)
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                self.main.xyButton.setChecked(True)
                zvalue = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*slicevalue/30.
                self.main.slicevalueLabel.setText(str("z=%.2f" %zvalue))    

            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                self.main.xzButton.setChecked(True)
                yvalue = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*slicevalue/30.
                self.main.slicevalueLabel.setText(str("y=%.2f" %yvalue))

            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                self.main.xzButton.setChecked(True)
                yvalue = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*slicevalue/30.
                self.main.slicevalueLabel.setText(str("y=%.2f" %yvalue))

         # Call a function which updates the labeling in the range sliders
        self.slicecontroller.ChangeRangeSliderLabels()

    def RecreatePanelButton(self):

        nrow = self.main.rowpanelSpinBox.value()
        ncolumn = self.main.columnpanelSpinBox.value()
        # save old nrow and ncolumn
        nrow0 = self.main.nrow; ncolumn0 = self.main.ncolumn
        # update nrow and ncolumn
        self.main.nrow = nrow
        self.main.ncolumn = ncolumn
        # delete old panel buttons
        self.main.panellayout.deleteLater()

        if self.main.panelselect > (self.main.nrow*self.main.ncolumn): 
            # This is when the panel dimension is decreased.
            self.main.panelselect = self.main.nrow*self.main.ncolumn
        
        # Update the panel buttons
        self.SetPanelButtons()

        field_select_panel0 = self.main.field_select_panel
        field_panel0 = self.main.field_panel
        species_panel0 = self.main.species_panel
        phase_panel0 = self.main.phase_panel
        line_panel0 = self.main.line_panel
        rectangle_panel0 = self.main.rectangle_panel
        aspect_panel0 = self.main.aspect_panel
        if self.main.dim  == 3:
            sliceplane_panel0 = self.main.sliceplane_panel
            slicevalue_panel0 = self.main.slicevalue_panel
        xminloc_panel0 = self.main.xminloc_panel
        xmaxloc_panel0 = self.main.xmaxloc_panel
        if self.main.dim  == 3:
            yminloc_panel0 = self.main.yminloc_panel
            ymaxloc_panel0 = self.main.ymaxloc_panel
        zminloc_panel0 = self.main.zminloc_panel
        zmaxloc_panel0 = self.main.zmaxloc_panel
        
        # Re-initialize the panel parameter lists.
        self.main.field_panel = []
        self.main.species_panel = []
        self.main.phase_panel = []
        self.main.line_panel = []
        self.main.field_select_panel = []
        self.main.rectangle_panel = []
        self.main.aspect_panel = []
        self.main.sliceplane_panel = []
        self.main.slicevalue_panel = []
        self.main.xminloc_panel = []
        self.main.xmaxloc_panel = []
        self.main.yminloc_panel = []
        self.main.ymaxloc_panel = []
        self.main.zminloc_panel = []
        self.main.zmaxloc_panel = []

        for l in np.arange(self.main.nrow*self.main.ncolumn):
            self.main.field_panel.append(field_panel0[np.mod(l,nrow0*ncolumn0)])
            if l < nrow0*ncolumn0:
                self.main.field_select_panel.append(field_select_panel0[l])
                self.main.line_panel.append(line_panel0[l])
                self.main.rectangle_panel.append(rectangle_panel0[l])
                self.main.aspect_panel.append(aspect_panel0[l])
                self.main.species_panel.append(species_panel0[l])
                self.main.phase_panel.append(phase_panel0[l])
                if self.main.dim == 3:
                    self.main.sliceplane_panel.append(sliceplane_panel0[l])
                    self.main.slicevalue_panel.append(slicevalue_panel0[l])
                self.main.xminloc_panel.append(xminloc_panel0[l])
                self.main.xmaxloc_panel.append(xmaxloc_panel0[l])
                if self.main.dim == 3:
                    self.main.yminloc_panel.append(yminloc_panel0[l])
                    self.main.ymaxloc_panel.append(ymaxloc_panel0[l])
                self.main.zminloc_panel.append(zminloc_panel0[l])
                self.main.zmaxloc_panel.append(zmaxloc_panel0[l])
            else:
                self.main.field_select_panel.append('True')
                self.main.line_panel.append(False)
                self.main.rectangle_panel.append(False)
                self.main.aspect_panel.append('auto')
                self.main.species_panel.append(species_panel0[0])
                self.main.phase_panel.append(phase_panel0[0])
                if self.main.dim == 3:
                    self.main.sliceplane_panel.append('xz')
                    self.main.slicevalue_panel.append(15)
                self.main.xminloc_panel.append(0)
                self.main.xmaxloc_panel.append(100)
                if self.main.dim == 3:
                    self.main.yminloc_panel.append(0)
                    self.main.ymaxloc_panel.append(100)
                self.main.zminloc_panel.append(0)
                self.main.zmaxloc_panel.append(100)
                
        self.main.figure.clear()

        self.collectdata.loaddatasync()
        self.prepareplot.plotsync()

    
