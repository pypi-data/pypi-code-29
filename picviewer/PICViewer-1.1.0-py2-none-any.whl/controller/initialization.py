import os, glob
from PySide import QtCore, QtGui
import numpy as np

from picviewer.dataloader.get_datainfo import DataInfo

class Initialization():
    """
        Initialization after reading data information
    """
    def __init__(self, Mainwindow):

        self.main = Mainwindow

        # get data information
        self.datainfo = DataInfo()
        param_dic = self.datainfo.datainfo(self.main.filepath)

        self.main.iterations = param_dic['iterations']
        self.main.dataformat = param_dic['dataformat']
        self.main.dim = param_dic['dim']
        self.main.coord_system = param_dic['coord_system']
        self.main.xaxis = param_dic['xaxis']
        self.main.yaxis = param_dic['yaxis']
        self.main.zaxis = param_dic['zaxis']
        self.main.taxis = param_dic['taxis']
        self.main.time = self.main.taxis[-1]

        nx = param_dic['nx']
        nz = param_dic['nz']
        ny = param_dic['ny']
        self.main.dxfact = param_dic['dxfact']
        self.main.dzfact = param_dic['dzfact']
        self.main.dyfact = param_dic['dyfact']
        numpart_list = param_dic['numpart_list']
        self.main.dpfact_list = param_dic['dpfact_list'] 

        self.main.field_list = param_dic['field_list']
        self.main.species_list = param_dic['species_list']
        self.main.phase_list1 = param_dic['phase_list1']
        if self.main.dim == 3:
            self.main.phase_list2 = param_dic['phase_list2']
            self.main.phase_list3 = param_dic['phase_list3']
        self.main.mass_list = param_dic['mass_list']

        self.main.field_list_indexed = \
                {self.main.field_list[k]: k for k in np.arange(len(self.main.field_list))}
        self.main.species_list_indexed = \
                {self.main.species_list[k]: k for k in np.arange(len(self.main.species_list))}
        self.main.phase_list1_indexed = \
                {self.main.phase_list1[k]: k for k in np.arange(len(self.main.phase_list1))}
        if self.main.dim == 3:
            self.main.phase_list2_indexed = \
                {self.main.phase_list2[k]: k for k in np.arange(len(self.main.phase_list2))}
            self.main.phase_list3_indexed = \
                {self.main.phase_list3[k]: k for k in np.arange(len(self.main.phase_list3))}
        self.main.mass_list_indexed = \
                {self.main.mass_list[k]: k for k in np.arange(len(self.main.mass_list))}

        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Load %s %dD simulation data'%(self.main.dataformat, self.main.dim))
        print('Field data dims=',(len(self.main.xaxis),len(self.main.yaxis),len(self.main.zaxis)))
        print('dims from source', (nx,ny,nz),'--> downsample factor',(self.main.dxfact,self.main.dyfact,self.main.dzfact))
        print('field list', self.main.field_list)
        print('species list', self.main.species_list)
        print('species mass list', self.main.mass_list)
        print('particle number from source (/1e6)',np.array(numpart_list)/1e6)
        print('particle downsample factor',self.main.dpfact_list)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        self.main.tstep = len(self.main.taxis)
        # display simulation type
        self.main.simuLabel.setText('%dD %s'%(self.main.dim, self.main.dataformat))
        self.main.coordinateLabel.setText(self.main.coord_system)

        # time step slider
        self.main.tstepLabel.setText("tstep %d" %(len(self.main.iterations)))
        self.main.timeLabel.setText("%6.1f fs" % self.main.taxis[-1])
        self.main.timeSlider.setRange(1,len(self.main.iterations))
        self.main.timeSlider.setSingleStep(1)
        self.main.timeSlider.setValue(len(self.main.iterations))

        # time interval spinbox
        self.main.tiniSpinBox.setMinimum(1)
        self.main.tiniSpinBox.setMaximum(len(self.main.iterations))
        self.main.tiniSpinBox.setValue(np.min([2,len(self.main.iterations)]))
        self.main.tmaxSpinBox.setMinimum(1)
        self.main.tmaxSpinBox.setMaximum(len(self.main.iterations))
        self.main.tmaxSpinBox.setValue(len(self.main.iterations))
        
        # space range slider
        self.main.x1min.setText("zmin")
        self.main.x1minLabel.setText(str("%.1f"%(self.main.zaxis[0])))
        self.main.x1max.setText("zmax")
        self.main.x1maxLabel.setText(str("%.1f"%(self.main.zaxis[-1])))
        self.main.x2min.setText("xmin")
        self.main.x2minLabel.setText(str("%.1f"%(self.main.xaxis[0])))
        self.main.x2max.setText("xmax")
        self.main.x2maxLabel.setText(str("%.1f"%(self.main.xaxis[-1])))

        # field combo-boxes
        for i in np.arange(len(self.main.field_list)):
            self.main.fieldsComboBox.addItem(self.main.field_list[i], i)
        self.main.fieldsComboBox.setCurrentIndex(0)
        
        # species combo-boxes
        for i in np.arange(len(self.main.species_list)):
            self.main.speciesComboBox.addItem(self.main.species_list[i], i)
        self.main.speciesComboBox.setCurrentIndex(0)
        
        # phase combo-boxes
        for i in np.arange(len(self.main.phase_list1)):
            self.main.phaseComboBox.addItem(self.main.phase_list1[i][0]+'-'+self.main.phase_list1[i][1], i)
        self.main.phaseComboBox.setCurrentIndex(0)
  	
        for l in np.arange(self.main.nrow*self.main.ncolumn):
            # initialize parameters in each panel
            self.main.field_select_panel.append(True)
            self.main.field_panel.append(self.main.field_list[np.mod(l,len(self.main.field_list))])
            self.main.species_panel.append(self.main.species_list[0])
            self.main.phase_panel.append(self.main.phase_list1[0])
            self.main.line_panel.append(False)
            self.main.rectangle_panel.append(False)
            self.main.aspect_panel.append('auto')
            self.main.xminloc_panel.append(0)
            self.main.xmaxloc_panel.append(100)
            self.main.zminloc_panel.append(0)
            self.main.zmaxloc_panel.append(100)
            #self.shift_panel.append(False)
            if self.main.dim == 3:
                self.main.sliceplane_panel.append('xz')
                self.main.slicevalue_panel.append(15)
                self.main.yminloc_panel.append(0)
                self.main.ymaxloc_panel.append(99)

        if self.main.dim == 3:
            yvalue = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*15/30.
            self.main.slicevalueLabel.setText(str("y=%.2f" %yvalue))
            stride = self.main.strideSlider.value()
            self.main.strideLabel.setText(u'\u0394'+ "y=%.2f" %(stride/30.))