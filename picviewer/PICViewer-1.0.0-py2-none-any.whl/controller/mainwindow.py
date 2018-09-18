import sys, os
import numpy as np
import matplotlib
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
from base import Ui_MainWindow
import localwindow
import threading
import csv

from PySide import QtCore, QtGui
from picviewer.dataloader.datainfo import DataInfo
from picviewer.dataloader.loaddata import LoadData
from picviewer.dataplotter.plotdata import DataPlot

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
         initialize GUI
         
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)
         
        # create plotwidget
        self.LayoutWidget = QtGui.QWidget(self.centralwidget)
        self.LayoutWidget.setGeometry(QtCore.QRect(400, 10, 591, 730))
        self.plotwidget_layout = QtGui.QVBoxLayout(self.LayoutWidget)
        self.plotwidget_layout.setContentsMargins(0, 0, 0, 0)

        # coordiates
        self.coordLabel.setText(str('(0,0)'))
        # default number of panels
        self.rowpanelSpinBox.setValue(2)
        self.rowpanelSpinBox.setMinimum(1)
        self.rowpanelSpinBox.setMaximum(6)
        self.columnpanelSpinBox.setValue(1)
        self.columnpanelSpinBox.setMinimum(1)
        self.columnpanelSpinBox.setMaximum(5)
        # time step stride
        self.stepSpinBox.setValue(1)
        self.stepSpinBox.setMinimum(1)
        # current directory
        self.setWindowTitle(os.getcwd())

        # logo
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        self.image = QtGui.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(10, 230, 80, 68))
        self.pixmap = QtGui.QPixmap(logo_path)
        self.image.setPixmap(self.pixmap)
        self.image.show()

        # time button
        self.backwardtimeButton.clicked.connect(self.backwardtimebutton)
        self.forwardtimeButton.clicked.connect(self.forwardtimebutton)

        # time slder
        self.timeSlider.valueChanged.connect(self.timeslider)

        # space slider
        self.x1minSlider.setValue(0)
        self.x1minSlider.setMinimum(-1)
        self.x1minSlider.setRange(0,100)
        self.x1minSlider.valueChanged.connect(self.x1minslider)
        self.x1maxSlider.setValue(100)
        self.x1maxSlider.setMaximum(101)
        self.x1maxSlider.setRange(0,100)
        self.x1maxSlider.valueChanged.connect(self.x1maxslider)
        self.x2minSlider.setValue(0)
        self.x2minSlider.setMinimum(-1)
        self.x2minSlider.setRange(0,100)
        self.x2minSlider.valueChanged.connect(self.x2minslider)
        self.x2maxSlider.setValue(100)
        self.x2maxSlider.setMaximum(101)
        self.x2maxSlider.setRange(0,100)
        self.x2maxSlider.valueChanged.connect(self.x2maxslider)

        # space slider release
        self.releaseButton.clicked.connect(self.releasebutton)

        # plot button
        self.plotButton.clicked.connect(self.plotbutton)
       
        # aspect ratio checkbox
        self.aspectCheckBox.setChecked(False)
        self.aspectCheckBox.clicked.connect(self.aspectcheckbox)

        self.synctimeBox.setChecked(False)
        # line selection checkbox
        self.lineCheckBox.setChecked(False)
        self.lineCheckBox.clicked.connect(self.linecheckbox)
        # rectangle selection checkbox
        self.rectangleCheckBox.setChecked(False)
        self.rectangleCheckBox.clicked.connect(self.rectanglecheckbox)

        # shift checkbox
        #self.shiftCheckBox.setChecked(False)
        #self.shiftCheckBox.clicked.connect(self.shiftcheckbox)

        # 2D slice for 3D data
        self.xzButton.setChecked(True)
        QtCore.QObject.connect(self.xyButton, QtCore.SIGNAL('clicked()'),self.slicebutton)
        QtCore.QObject.connect(self.xzButton, QtCore.SIGNAL('clicked()'),self.slicebutton)
        QtCore.QObject.connect(self.yzButton, QtCore.SIGNAL('clicked()'),self.slicebutton)
        
        # slice value slider
        self.slicevalueSlider.setRange(1,29)
        self.slicevalueSlider.setValue(15)
        self.slicevalueSlider.sliderMoved.connect(self.slicevalueslider)
        self.strideSlider.setRange(1,30) 
        # The stride size should be > 0, otherwise no data error
        self.x2maxSlider.setMinimum(3)
        self.strideSlider.setValue(10)
        self.strideSlider.sliderMoved.connect(self.strideslider)

        # animation PushButton
        self.animationButton.clicked.connect(self.animationbutton)
        
        # initial gui size
        self.width0 = self.geometry().width()
        self.height0 = self.geometry().height()
        # default panel arrays
        self.nrow=2
        self.ncolumn=1
        self.panelselect = 1

        # Save parameters in each window panel
        # Each panal can work independently by setting these parameters.
        # When you click a window panel, the paramaeter saved in each panel is loaded.

        # field  i.e., ['Bx', 'By', ...]
        self.field_panel = []
        # species i.e., ['elec', 'ions', ...]
        self.species_panel = []
        # phase for particles i.e., [('px','x'),('py','x'), ...]
        self.phase_panel = []
        # field select i.e., ['True', 'False', ...], 
        # to check whether field or particle is selected in a panel.
        self.field_select_panel = []
        # local line selection i.e., ['True', 'False', ...]
        self.line_panel = []
        # local rectangle selection i.e., ['True', 'False', ...]
        self.rectangle_panel = []
        # aspect ratio selection  i.e., ['auto', 'equal', ...]
        self.aspect_panel = []
        # 2D slice plane in 3D i.e., ['xy', 'yz', ...]
        self.sliceplane_panel = []
        # 3rd axis value in 2D slice: i.e., [15, 15, ...]  <-- range between (0,30)
        self.slicevalue_panel = []
        # xmin and xmax location in 2D slice: i.e., [10, 30, ...]  <-- range between (0,100)
        self.xminloc_panel = []
        self.xmaxloc_panel = []
        # ymin and ymax location in 2D slice: i.e., [10, 10, ...]  <-- range between (0,100)
        self.yminloc_panel = []
        self.ymaxloc_panel = []
        # zmin and zmax location in 2D slice: i.e., [10, 20, ...]  <-- range between (0,100)
        self.zminloc_panel = []
        self.zmaxloc_panel = []

        # shift position of the image
        #self.shift_panel = []

        # field data container has multiple key words, i.e.,
        # {('Bx', tstep) : data, ..... }
        self.fdata_container = {}

        # particle data container has multiple key words, i.e.,
        # {('elec', 'px', tstep) : data, ..... }
        self.pdata_container = {}

        # subpanel window
        #self.subplot = {}
        #self.subfieldplot = {}
        self.existingLocalplot = False
         
        # prepare matplotlib canvas
        self.MatplotlibCanvas()
        self.dataplot = DataPlot()

        # call methods from imported classes
        self.datainfo = DataInfo()
        self.loaddata = LoadData()
        
        self.initialization()
        self.SetPanelButtons()

        # interactive mouse
        self.pressed= False
        self.line = {}
        self.rectangle1 = {}
        self.rectangle2 = {}
        self.rectangle3 = {}
        self.rectangle4 = {}

         # save button
        self.savepushButton.clicked.connect(self.savepushbutton)

         # load button
        self.loadpushButton.clicked.connect(self.loadSavedConfig)

         # quit button
        self.quitpushButton.clicked.connect(self.quitpushbutton)


    def initialization(self):
        """
        Initialization after reading data information
        """

        # Load basic global parameteres
        global iterations, dataformat, coord_system, dim, taxis
        global field_list, species_list, mass_list
        global phase_list1, phase_list2, phase_list3
        global field_list_indexed, species_list_indexed, mass_list_indexed
        global phase_list1_indexed, phase_list2_indexed, phase_list3_indexed 

        param_dic = self.datainfo.datainfo()

        iterations = param_dic['iterations']
        dataformat = param_dic['dataformat']
        dim = param_dic['dim']
        coord_system = param_dic['coord_system']
        self.xaxis = param_dic['xaxis']
        self.yaxis = param_dic['yaxis']
        self.zaxis = param_dic['zaxis']
        taxis = param_dic['taxis']
        self.time = taxis[-1]

        field_list = param_dic['field_list']
        species_list = param_dic['species_list']
        phase_list1 = param_dic['phase_list1']
        if dim == 3:
            phase_list2 = param_dic['phase_list2']
            phase_list3 = param_dic['phase_list3']
        mass_list = param_dic['mass_list']

        field_list_indexed = {field_list[k]: k for k in np.arange(len(field_list))}
        species_list_indexed = {species_list[k]: k for k in np.arange(len(species_list))}
        phase_list1_indexed = {phase_list1[k]: k for k in np.arange(len(phase_list1))}
        if dim == 3:
            phase_list2_indexed = {phase_list2[k]: k for k in np.arange(len(phase_list2))}
            phase_list3_indexed = {phase_list3[k]: k for k in np.arange(len(phase_list3))}
        mass_list_indexed = {mass_list[k]: k for k in np.arange(len(mass_list))}

        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Load %s %dD simulation data'%(dataformat, dim))
        print('Field data dims=',(len(self.xaxis),len(self.yaxis),len(self.zaxis)))
        print('field list', field_list)
        print('species list', species_list)
        print('species mass list', mass_list)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


        self.tstep = len(taxis)
        # display simulation info to labels
        self.simuLabel.setText('%dD %s'%(dim, dataformat))
        # display coordinates to which mouse cursor points
        self.coordinateLabel.setText(coord_system)
   
        # field and particle select buttons for three plot panels
        self.fieldButton.setChecked(True)
        QtCore.QObject.connect(self.fieldButton, QtCore.SIGNAL('clicked()'),self.fieldbutton)
        QtCore.QObject.connect(self.particleButton, QtCore.SIGNAL('clicked()'),self.particlebutton)

        # field combo-boxes
        for i in np.arange(len(field_list)):
            self.fieldsComboBox.addItem(field_list[i], i)
        self.fieldsComboBox.setCurrentIndex(0)
        self.fieldsComboBox.activated.connect(self.fieldcombobox)

        # species combo-boxes
        for i in np.arange(len(species_list)):
            self.speciesComboBox.addItem(species_list[i], i)
        self.speciesComboBox.setCurrentIndex(0)
        self.speciesComboBox.activated.connect(self.speciescombobox)
        for i in np.arange(len(phase_list1)):
            self.phaseComboBox.addItem(phase_list1[i][0]+'-'+phase_list1[i][1], i)
        self.phaseComboBox.setCurrentIndex(0)
        self.phaseComboBox.activated.connect(self.phasecombobox)
  	
        # time label
        self.tstepLabel.setText("tstep %d" %(len(iterations)))
        self.timeLabel.setText("%6.1f fs" % taxis[-1])

        # timestep slider
        self.timeSlider.setRange(1,len(iterations))
        self.timeSlider.setSingleStep(1)
        self.timeSlider.setValue(len(iterations))
        
        # space slider
        self.x1min.setText("zmin")
        self.x1minLabel.setText(str("%.1f"%(self.zaxis[0])))
        self.x1max.setText("zmax")
        self.x1maxLabel.setText(str("%.1f"%(self.zaxis[-1])))
        
        self.x2min.setText("xmin")
        self.x2minLabel.setText(str("%.1f"%(self.xaxis[0])))
        self.x2max.setText("xmax")
        self.x2maxLabel.setText(str("%.1f"%(self.xaxis[-1])))

        self.tiniSpinBox.setMinimum(1)
        self.tiniSpinBox.setMaximum(len(iterations))
        self.tiniSpinBox.setValue(np.min([2,len(iterations)]))
        self.tmaxSpinBox.setMinimum(1)
        self.tmaxSpinBox.setMaximum(len(iterations))
        self.tmaxSpinBox.setValue(len(iterations))

        for l in np.arange(self.nrow*self.ncolumn):
            # initialize parameters in each panel
            self.field_select_panel.append(True)
            self.field_panel.append(field_list[np.mod(l,len(field_list))])
            self.species_panel.append(species_list[0])
            self.phase_panel.append(phase_list1[0])
            self.line_panel.append(False)
            self.rectangle_panel.append(False)
            self.aspect_panel.append('auto')
            self.xminloc_panel.append(0)
            self.xmaxloc_panel.append(100)
            self.zminloc_panel.append(0)
            self.zmaxloc_panel.append(100)
            #self.shift_panel.append(False)
            if dim == 3:
                self.sliceplane_panel.append('xz')
                self.slicevalue_panel.append(15)
                self.yminloc_panel.append(0)
                self.ymaxloc_panel.append(99)
                
        if dim == 3:
            yvalue = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*15/30.
            self.slicevalueLabel.setText(str("y=%.2f" %yvalue))
            stride = self.strideSlider.value()
            self.strideLabel.setText(u'\u0394'+ "y=%.2f" %(stride/30.))
     
        self.opendataSync()
        self.MakePlotSync()

        self.createlocalwindow()

    def SetPanelButtons(self):
        """
        Create panel buttons
        The number of the panel buttons is given manually.

        Returns:
            None
        """

        self.panelbuttons = {}
        self.panellayout = QtGui.QWidget(self.centralwidget)
        # Assign button locations
        button_height = 520
        button_left = 160
        x0 = -20*(self.ncolumn-2)+button_left
        w0 = 25*(self.ncolumn-2)+50
        y0 = (10./3)*(self.nrow-2)+button_height
        h0 = 20*(self.nrow-2)+60
        self.panellayout.setGeometry(QtCore.QRect(x0, y0, w0, h0))
        self.gridLayout = QtGui.QGridLayout(self.panellayout)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        for i in np.arange(self.nrow):
            for j in np.arange(self.ncolumn):
                self.panelbuttons[(i,j)] = QtGui.QRadioButton(self.panellayout)
                self.panelbuttons[(i,j)].setStyleSheet("")
                self.panelbuttons[(i,j)].setText("")
                self.gridLayout.addWidget(self.panelbuttons[(i,j)], i, j, 1, 1)
        self.panellayout.show()      
        
        i = (self.panelselect-1)/self.ncolumn
        j = np.mod((self.panelselect-1),self.ncolumn)
        self.panelbuttons[(i,j)].setChecked(True)

        for i in np.arange(self.nrow):
            for j in np.arange(self.ncolumn):
                QtCore.QObject.connect(self.panelbuttons[(i,j)], QtCore.SIGNAL('clicked()'),self.panelbutton)

    def panelbutton(self):
        """
        Change all the parameters displayed in the GUI window
        into the saved ones in each panel.

        Returns:
            None
        """
        # self.panelselect is the index of a selected panel, i.e., 1, 2, 3, or ...
        for i in np.arange(self.nrow):
            for j in np.arange(self.ncolumn):
                if self.panelbuttons[(i,j)].isChecked():
                    self.panelselect = i*self.ncolumn+j+1

        # i.e., self.field_select_panel = [True, True, False, ....]
        if self.field_select_panel[self.panelselect-1]:
            self.fieldButton.setChecked(True)
            # i.e., self.field_panel = ['Bx', 'By', ...]
            field = self.field_panel[self.panelselect-1]
            index = field_list_indexed[field]
            self.fieldsComboBox.setCurrentIndex(index)
        else:
            self.particleButton.setChecked(True)
            # i.e., self.species_panel = ['elec', 'ions', ...]
            species = self.species_panel[self.panelselect-1]
            index = species_list_indexed[species]
            self.speciesComboBox.setCurrentIndex(index)
            # i.e., phase = ['px','x'], ['x','z'], ...
            phase = self.phase_panel[self.panelselect-1]        
            if dim == 2:
                index = phase_list1_indexed[phase]
            else:
                if self.sliceplane_panel[self.panelselect-1] == 'xy':
                    index = phase_list2_indexed[phase]
                    self.phaseComboBox.clear() 
                    for i in np.arange(len(phase_list2)):
                        self.phaseComboBox.addItem(phase_list2[i][0]+'-'+phase_list2[i][1], i)

                if self.sliceplane_panel[self.panelselect-1] == 'xz':
                    index = phase_list1_indexed[phase]
                    self.phaseComboBox.clear()
                    for i in np.arange(len(phase_list1)):
                        self.phaseComboBox.addItem(phase_list1[i][0]+'-'+phase_list1[i][1], i)

                if self.sliceplane_panel[self.panelselect-1] == 'yz':
                    index = phase_list3_indexed[phase]
                    self.phaseComboBox.clear() 
                    for i in np.arange(len(phase_list3)):
                        self.phaseComboBox.addItem(phase_list3[i][0]+'-'+phase_list3[i][1], i)

            self.phaseComboBox.setCurrentIndex(index)

        if self.aspect_panel[self.panelselect-1] == 'equal':
            self.aspectCheckBox.setChecked(True)
        else:
             self.aspectCheckBox.setChecked(False)

        if self.line_panel[self.panelselect-1] == True:
            self.lineCheckBox.setChecked(True)
        else:
            self.lineCheckBox.setChecked(False)

        if self.rectangle_panel[self.panelselect-1] == True:
            self.rectangleCheckBox.setChecked(True)
        else:
            self.rectangleCheckBox.setChecked(False)

        # Call a function which updates the labeling in the range sliders
        self.ChangeRangeSliderLabels()

        if dim == 3:
            # i.e., self.slicevalue_panel = [0, 0, 10, .. ] 
            # The number is between [0,30] and specifies the location
            # on the 3rd axis of the 2D slice plane.
            slicevalue = self.slicevalue_panel[self.panelselect-1]
            self.slicevalueSlider.setValue(slicevalue)
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                self.xyButton.setChecked(True)
                zvalue = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*slicevalue/30.
                self.slicevalueLabel.setText(str("z=%.2f" %zvalue))    

            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                self.xzButton.setChecked(True)
                yvalue = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*slicevalue/30.
                self.slicevalueLabel.setText(str("y=%.2f" %yvalue))

            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                self.xzButton.setChecked(True)
                yvalue = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*slicevalue/30.
                self.slicevalueLabel.setText(str("y=%.2f" %yvalue))

    def MatplotlibCanvas(self):
        """
        Create matplotlib canvas for the window plot panels

        Returns:
            None
        """
        self.figure = Figure()
        self.canvas = Canvas(self.figure)
        self.plotwidget_layout.addWidget(self.canvas)
        self.canvas.mpl_connect('motion_notify_event', self.motion_notify)
        self.canvas.mpl_connect('button_press_event', self.onclick)
        self.canvas.mpl_connect('button_release_event', self.release_click)
        
    def createlocalwindow(self):
        """
        Create matplotlib canvas for local window plot panels

        Returns:
            None
        """
        # global mainleft, maintop, mainwidth, mainheight
        size = self.geometry()
        mainleft=size.left(); maintop=size.top()
        mainwidth=size.width(); mainheight=size.height()
        width = mainwidth
        height = mainheight
        #global totalpanels, currentpanel
        totalpanels = self.nrow*self.ncolumn
        currentpanel = self.panelselect
        # show subplot window
        
        #self.subfieldplot[(self.panelselect)] = subwindow.subPlot(
        self.localdataplot = localwindow.LocalPlot(
                mainleft+mainwidth,
                maintop,
                width,
                height)

    def resizeEvent(self,  event):
        """
        Resize plot widget when mouse drags the mainwindow edges

        Returns:
            None
        """
        width = event.size().width()
        height = event.size().height()
        wratio=1.*(width-400)/(self.width0-400)
        hratio=1.*height/self.height0
        self.LayoutWidget.setGeometry(QtCore.QRect(400, 10, 591*wratio, 730*hratio))

        size = self.geometry()
        mainleft=size.left(); maintop=size.top()
        mainwidth=size.width(); mainheight=size.height()

        self.localdataplot.setGeometry(QtCore.QRect(
                    mainleft+mainwidth, 
                    maintop, 
                    500*wratio, 
                    600*hratio))
        self.localdataplot.LayoutWidget.setGeometry(QtCore.QRect(
            10, 
            10, 
            500*wratio-20, 
            600*hratio))
       

    def opendataSync(self):
        """
        load field data for multi-panel windows

        Returns:
            None
        """
        
        for l in np.arange(self.nrow*self.ncolumn):

            # i.e., self.field_select_panel = [True, True, False, ....]
            # When a panel selects field data, it is True
            # but selects particle data, False
            if self.field_select_panel[l]:
                field = self.field_panel[l]
                self.openfield(field)
            else:
                species = self.species_panel[l]
                phase= self.phase_panel[l]

                self.openparticle(species, phase[0], phase[1])


    def openfield(self, field=None):
        """
        load field data for a selected window panel

        Returns:
            None
        """
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        if field is None: 
            field = self.field_panel[self.panelselect-1]
   
        if (field,self.tstep) in self.fdata_container.keys():
        # if the field data already exist in fdata_container, skip loading
            pass
        else:
            self.fdata_container[(field,self.tstep)] = \
                self.loaddata.loadfield(
                dataformat,
                dim,
                iterations[self.tstep-1],
                field)
        QtGui.QApplication.restoreOverrideCursor()

    def openparticle(self, species=None, phase1=None, phase2=None):
        """
        load particle data for a selected window panel

        Returns:
            None
        """

        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        if species == None: 
            species = self.species_panel[self.panelselect-1]

        # phase_panel is a list with a pair, i.e., [['px','x'], ['x','z']], ...
        if phase1 == None or phase2 == None: 
            phase = self.phase_panel[self.panelselect-1]
        else:
            phase = [phase1, phase2]

        position_variables = ['x','y','z']
        momentum_variables = ['px','py','pz']
        other_variables = ['ene', 'ang']
        # loop over the tuple elements
        for loc in np.arange(2):
            variable = phase[loc]
            if variable in momentum_variables:
                # load particle data 
                if (species,variable, self.tstep) in self.pdata_container.keys():
                    pass
                else:
                    self.pdata_container[(species,variable,self.tstep)] = \
                        self.loaddata.loadparticle(
                            dataformat,
                            dim,
                            iterations[self.tstep-1], 
                            species,
                            variable)

                if dim == 3: # In 3D, load all the position data, x, y, and z for slicing
                    for var in position_variables:
                        if (species,var, self.tstep) in self.pdata_container.keys():
                            pass
                        else:
                            self.pdata_container[(species,var,self.tstep)] = \
                                self.loaddata.loadparticle(
                                    dataformat,
                                    dim,
                                    iterations[self.tstep-1], 
                                    species,
                                    var)

            if variable in position_variables:
                if dim == 2:
                    if (species,variable, self.tstep) in self.pdata_container.keys():
                        pass
                    else:
                        self.pdata_container[(species,variable,self.tstep)] = \
                            self.loaddata.loadparticle(
                            dataformat,
                            dim,
                            iterations[self.tstep-1], 
                            species,
                            variable)
                
                else: # In 3D, load all the position data, x, y, and z for slicing
                    for var in position_variables:
                        if (species,var, self.tstep) in self.pdata_container.keys():
                            pass
                        else:
                            self.pdata_container[(species,var,self.tstep)] = \
                                self.loaddata.loadparticle(
                                dataformat,
                                dim,
                                iterations[self.tstep-1], 
                                species,
                                var)
                    
            # If the variable is energy, angles, etc.,
            # then load three momentum variables, 'px', 'py', and 'pz'. 
            elif variable in other_variables:
                for var in momentum_variables:
                    if (species,var,self.tstep) in self.pdata_container.keys():
                        pass
                    else:
                        self.pdata_container[(species,var,self.tstep)] = \
                            self.loaddata.loadparticle(
                            dataformat,
                            dim,
                            iterations[self.tstep-1], 
                            species,
                            var)
                    
        QtGui.QApplication.restoreOverrideCursor()
        
    def MakePlotSync(self):
        """
        Plot multi-window panels

        Returns:
            None
        """

        # Find which panels have field selection.
        # i.e., index = [0,1,3,5,..] --> panels 0, 1, 3, 5 .. have field plots.
        index = [i for i, yesfield in enumerate(self.field_select_panel) if yesfield]
        fields = [self.field_panel[i] for i in index]
        # i.e., field_keyworsd = [('Bx', 10), ('Ez', 10), ....]
        field_keywords =[(k,self.tstep) for k in fields]

        # Find which panels have particle selection.
        index = [i for i, yesfield in enumerate(self.field_select_panel) if not yesfield]
        species = [self.species_panel[i] for i in index]
        phase = [self.phase_panel[i] for i in index]
        particle_keywords0 =[(species[i], phase[i][0], self.tstep) for i in range(len(species))]
        particle_keywords1 =[(species[i], phase[i][1], self.tstep) for i in range(len(species))]
        # i.e., particle_keywords = [('elec', 'px', 10), ('elec', 'x', 10), .... ]
        particle_keywords = particle_keywords0 + particle_keywords1

        # Pass field and paricle data dictionary to the plot function
        if dim == 2:
            # self.axes: return value from each subpanel axis
            # self.cbars: return value from each subpanel colorbar
            self.axes, self.cbars = self.dataplot.makeplotsync2D(
                    self.figure,
                    {k:self.fdata_container[k] for k in field_keywords},
                    {k:self.pdata_container[k] for k in particle_keywords},
                    self.nrow, 
                    self.ncolumn,
                    self.field_select_panel,
                    self.field_panel, 
                    self.species_panel,
                    self.phase_panel,
                    self.tstep,
                    self.time,
                    self.xaxis,
                    self.zaxis,
                    self.xminloc_panel,
                    self.xmaxloc_panel,
                    self.zminloc_panel,
                    self.zmaxloc_panel,
                    self.aspect_panel)
        else:
            
            loc_container = self.getLocalparticleLoc()
            self.axes, self.cbars = self.dataplot.makeplotsync3D(
                    self.figure,
                    {k:self.fdata_container[k] for k in field_keywords},
                    {k:self.pdata_container[k] for k in particle_keywords},
                    loc_container,
                    self.nrow, 
                    self.ncolumn,
                    self.field_select_panel,
                    self.field_panel,
                    self.species_panel,
                    self.phase_panel,
                    self.tstep,
                    self.time,
                    self.sliceplane_panel,
                    self.slicevalue_panel,
                    self.xaxis,
                    self.yaxis,
                    self.zaxis,
                    self.xminloc_panel,
                    self.xmaxloc_panel,
                    self.yminloc_panel,
                    self.ymaxloc_panel,
                    self.zminloc_panel,
                    self.zmaxloc_panel,
                    self.aspect_panel)

        self.canvas.draw()

    def MakeFieldPlot(self):
        """
        Plot field data in a selected window panel

        Returns:
            None
        """

        # field is the field name in each panel, i.e., 'Bx', 'By', ...
        field = self.field_panel[self.panelselect-1]
        t = self.tstep  # current time step

        x1min, x1max, \
        x2min, x2max, \
        iloc1, iloc2, \
        jloc1, jloc2, \
        kloc1, kloc2 = self.getSpaceRanges()

        if dim == 2:

            self.cbars[(self.panelselect-1)] = self.dataplot.makeplot2D(
                self.figure, 
                self.fdata_container[(field,t)][jloc1:jloc2,iloc1:iloc2],
                self.nrow, 
                self.ncolumn,
                self.field_panel[self.panelselect-1],
                self.panelselect, 
                self.time,
                x1min,
                x1max,
                x2min,
                x2max,
                self.aspect_panel[self.panelselect-1],
                self.cbars[(self.panelselect-1)])

        else:   # 3D
            self.cbars[(self.panelselect-1)]=self.dataplot.makeplot3D(
                self.figure,
                self.fdata_container[(field,t)][iloc1:iloc2,jloc1:jloc2,kloc1:kloc2],
                self.nrow, 
                self.ncolumn,
                self.field_panel[self.panelselect-1],
                self.panelselect,
                self.time,
                self.sliceplane_panel[self.panelselect-1],
                x1min,
                x1max,
                x2min,
                x2max,
                self.aspect_panel[self.panelselect-1],
                self.cbars[(self.panelselect-1)])

        self.canvas.draw()

    def MakeParticlePlot(self):
        """
        Plot particle data in a selected window panel

        Returns:
            None
        """

        species = self.species_panel[self.panelselect-1]
        # variable is a pair element [x,px], [y,px], ...
        phase = self.phase_panel[self.panelselect-1]
        stride = self.strideSlider.value()

        # get space range of the current selected panel
        x1min, x1max, \
        x2min, x2max, \
        dummy, dummy, \
        dummy, dummy, \
        dummy, dummy = self.getSpaceRanges()

        if dim == 2:
            self.cbars[(self.panelselect-1)] = self.dataplot.makeparticleplot(
                    self.figure,
                    self.pdata_container[(species,phase[0],self.tstep)],
                    self.pdata_container[(species,phase[1],self.tstep)],
                    self.nrow, 
                    self.ncolumn,
                    species,
                    phase,
                    self.panelselect, 
                    self.time,
                    x1min,
                    x1max,
                    x2min,
                    x2max,
                    self.aspect_panel[self.panelselect-1],
                    self.cbars[(self.panelselect-1)])

        else:

            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                slicevalue = self.slicevalue_panel[self.panelselect-1]
                zvalue = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*(slicevalue/30.)
                width = (self.zaxis[-1]-self.zaxis[0])*(stride/30.)
                loc = np.where((self.pdata_container[(species,'z',self.tstep)] > zvalue-.5*width) & \
                       (self.pdata_container[(species,'z',self.tstep)] < zvalue+.5*width))[0]
                
            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                slicevalue = self.slicevalue_panel[self.panelselect-1]
                yvalue = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*(slicevalue/30.)
                width = (self.yaxis[-1]-self.yaxis[0])*(stride/30.)
                loc = np.where((self.pdata_container[(species,'y',self.tstep)] > yvalue-.5*width) & \
                       (self.pdata_container[(species,'y',self.tstep)] < yvalue+.5*width))[0]

            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                slicevalue = self.slicevalue_panel[self.panelselect-1]
                xvalue = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*(slicevalue/30.)
                width = (self.xaxis[-1]-self.xaxis[0])*(stride/30.)
                loc = np.where((self.pdata_container[(species,'x',self.tstep)] > xvalue-.5*width) & \
                       (self.pdata_container[(species,'x',self.tstep)] < xvalue+.5*width))[0]

            self.cbars[(self.panelselect-1)] = self.dataplot.makeparticleplot(
                    self.figure,
                    self.pdata_container[(species,phase[0],self.tstep)][loc],
                    self.pdata_container[(species,phase[1],self.tstep)][loc],
                    self.nrow, 
                    self.ncolumn,
                    species,
                    phase,
                    self.panelselect,
                    self.time,
                    x1min,
                    x1max,
                    x2min,
                    x2max,
                    self.aspect_panel[self.panelselect-1],
                    self.cbars[(self.panelselect-1)])

        self.canvas.draw()

    def motion_notify(self,event):
        """
        Mouse interaction on motion

        Returns:
            None
        """
        if not event.inaxes in self.axes.values(): return
        self.x_m, self.y_m = event.xdata, event.ydata
        self.coordLabel.setText("(x1,x2)=(%4.2f, %4.2f)" %(self.x_m, self.y_m)) 

        #if self.shift_panel[self.panelselect-1]:
        #    if self.pressed:

        #        self.xpix_m, self.ypix_m = event.x, event.y
        #        print(self.xpix_m-self.xpix_o, self.ypix_m-self.ypix_o)
        #        print(self.LayoutWidget.geometry())
        """
        x1minloc0 = zminloc_panel[self.panelselect-1]
        x1maxloc0 = zmaxloc_panel[self.panelselect-1]
        x2minloc0 = xminloc_panel[self.panelselect-1]
        x2maxloc0 = xmaxloc_panel[self.panelselect-1]

        if dim == 3:
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                x1axis = xaxis
                x2axis = yaxis
            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                x1axis = zaxis
                x2axis = xaxis
            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                x1axis = zaxis
                x2axis = yaxis
        else:
            x1axis = zaxis
            x2axis = xaxis

        if abs(self.x_m -self.x_o)/(x1axis[-1]-x1axis[0]) < 0.05 and \
                abs(self.y_m -self.y_o)/(x1axis[-1]-x1axis[0]) < 0.05: return

        self.x1shiftloc = int((self.x_o-self.x_m)/(x1axis[-1]-x1axis[0])*100.)
        self.x2shiftloc = int((self.y_o-self.y_m)/(x2axis[-1]-x2axis[0])*100.)
            
        self.zminloc_panel[self.panelselect-1] = x1minloc0+x1shiftloc
        self.zmaxloc_panel[self.panelselect-1] = x1maxloc0+x1shiftloc
        self.xminloc_panel[self.panelselect-1] = x2minloc0+x2shiftloc
        self.xmaxloc_panel[self.panelselect-1] = x2maxloc0+x2shiftloc
        self.MakePlot()
        """

    def onclick(self, event):
        """
        Mouse interaction on mouse pressed
        
        Returns:
            None
        """
        # return if mouse click is outside panels
        if not event.inaxes in self.axes.values(): return

        self.pressed = True  # True if mouse is on-click
        # Select panel by mouse click
        self.panelselect = np.where(np.array(self.axes.values()) == event.inaxes)[0][0]+1
        i = (self.panelselect-1)/self.ncolumn
        j = np.mod((self.panelselect-1),self.ncolumn)
        self.panelbuttons[(i,j)].setChecked(True)
        self.panelbutton()

        self.x_o, self.y_o = event.xdata, event.ydata

        #self.xpix_o, self.ypix_o = event.x, event.y

        if self.line_panel[self.panelselect-1]:
            # remove previous line
            if self.panelselect-1 in self.line.keys():
                self.line[(self.panelselect-1)].remove()
                self.canvas.draw()
                 
        elif  self.rectangle_panel[self.panelselect-1]:
            # remove previous rectangle
            if self.panelselect-1 in self.rectangle1.keys():
                self.rectangle1[(self.panelselect-1)].remove()
                self.rectangle2[(self.panelselect-1)].remove()
                self.rectangle3[(self.panelselect-1)].remove()
                self.rectangle4[(self.panelselect-1)].remove()
                self.canvas.draw()
            
    def release_click(self, event):
        """
        Mouse interaction on mouse released
        
        Returns:
            None
        """
        
        # Return if mouse click is outside panels.
        if not event.inaxes in self.axes.values(): return
        # return if mouse is released inside panel but pressed outside.
        if not self.pressed: return
        
        #QtGui.QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)
        # Return if mouse is pressed and released at the same position.
        self.x_r, self.y_r = event.xdata, event.ydata    
        if self.x_r == self.x_o and self.y_r == self.y_o: 
            self.pressed = False
            return

        # Zoom-in the image by mouse dragging
        if (not self.line_panel[self.panelselect-1]) and (not self.rectangle_panel[self.panelselect-1]):

            if dim == 3:
                if self.sliceplane_panel[self.panelselect-1] == 'xy':
                    x1axis = self.xaxis
                    x2axis = self.yaxis
                if self.sliceplane_panel[self.panelselect-1] == 'xz':
                    x1axis = self.zaxis
                    x2axis = self.xaxis
                if self.sliceplane_panel[self.panelselect-1] == 'yz':
                    x1axis = self.zaxis
                    x2axis = self.yaxis
            else:
                x1axis = self.zaxis
                x2axis = self.xaxis

            # Do not zoom in but return if mouse is pressed and released at very close points. 
            # This might be a mistake of clicking rather than intending to drag.
            if abs(self.x_r -self.x_o)/(x1axis[-1]-x1axis[0]) < 0.05 and \
                    abs(self.y_r -self.y_o)/(x1axis[-1]-x1axis[0]) < 0.05: 
                self.pressed = False
                return

            x1minloc = int((np.min([self.x_o,self.x_r])-x1axis[0])/(x1axis[-1]-x1axis[0])*100.)
            x1maxloc = int((np.max([self.x_o,self.x_r])-x1axis[0])/(x1axis[-1]-x1axis[0])*100.)
            x2minloc = int((np.min([self.y_o,self.y_r])-x2axis[0])/(x2axis[-1]-x2axis[0])*100.)
            x2maxloc = int((np.max([self.y_o,self.y_r])-x2axis[0])/(x2axis[-1]-x2axis[0])*100.)
            
            self.x1minSlider.setValue(x1minloc)
            self.x1maxSlider.setValue(x1maxloc)
            self.x2minSlider.setValue(x2minloc)
            self.x2maxSlider.setValue(x2maxloc)
            if self.field_select_panel[self.panelselect-1]:
                self.MakeFieldPlot()
            else:
                self.openparticle()
                self.MakeParticlePlot()
                
        if self.line_panel[self.panelselect-1]:
                self.plot = self.figure.add_subplot(self.nrow,self.ncolumn,self.panelselect)
                self.line[(self.panelselect-1)], = self.plot.plot(
                        [self.x_o,self.x_r],[self.y_o,self.y_r], 
                        ':', linewidth=1.0, color='grey')
                self.canvas.draw()

                self.PrepareLocalplot()

        elif  self.rectangle_panel[self.panelselect-1]:
                self.plot = self.figure.add_subplot(self.nrow,self.ncolumn,self.panelselect)
                self.rectangle1[(self.panelselect-1)], = self.plot.plot(
                        [self.x_o,self.x_r],[self.y_o,self.y_o], 
                        ':', linewidth=1.0, color='grey')
                self.rectangle2[(self.panelselect-1)], = self.plot.plot(
                        [self.x_o,self.x_r],[self.y_m,self.y_r], 
                        ':', linewidth=1.0, color='grey')
                self.rectangle3[(self.panelselect-1)], = self.plot.plot(
                        [self.x_o,self.x_o],[self.y_o,self.y_r], 
                        ':', linewidth=1.0, color='grey')
                self.rectangle4[(self.panelselect-1)], = self.plot.plot(
                        [self.x_r,self.x_r],[self.y_o,self.y_r], 
                        ':', linewidth=1.0, color='grey')
                self.canvas.draw()

                self.PrepareLocalplot()

        self.pressed = False
  
    def backwardtimebutton(self):
        """
        backward time button
        
        Returns:
            None
        """
        tstride = self.stepSpinBox.value()
        self.tstep = self.timeSlider.value()
        self.tstep = self.tstep - tstride
        if self.tstep < 1:
            self.tstep = self.tstep + tstride
        else:
            self.tstepLabel.setText("tstep %d" %self.tstep)
            self.time = taxis[self.tstep-1]
            self.timeLabel.setText("%6.1f fs" %self.time)
            self.timeSlider.setValue(self.tstep)

        # update domain axes
        self.xaxis, self.yaxis, self.zaxis = \
                self.datainfo.update_domain_axes(
                    dataformat, dim, iterations[self.tstep-1])
        self.ChangeRangeSliderLabels()

        if self.synctimeBox.isChecked():
            self.opendataSync()
            self.MakePlotSync()
        else:
            if self.fieldButton.isChecked():
                self.openfield()
                self.MakeFieldPlot()
            else:
                self.openparticle()
                self.MakeParticlePlot()

    def forwardtimebutton(self):
        """
        Foward time button
        
        Returns:
            None
        """
        tstride = self.stepSpinBox.value()
        self.tstep=self.timeSlider.value()
        self.tstep = self.tstep + tstride
        if self.tstep > len(taxis):
            self.tstep = self.tstep - tstride
        else:
            self.tstepLabel.setText("tstep %d" %self.tstep)
            self.time = taxis[self.tstep-1]    
            self.timeLabel.setText("%6.1f fs" %self.time)
            self.timeSlider.setValue(self.tstep)

        # update domain axes
            self.xaxis, self.yaxis, self.zaxis = \
                    self.datainfo.update_domain_axes(
                        dataformat, dim, iterations[self.tstep-1])
            self.ChangeRangeSliderLabels()
            
        if self.synctimeBox.isChecked():
            self.opendataSync()
            self.MakePlotSync()
        else:
            if self.fieldButton.isChecked():
                self.openfield()
                self.MakeFieldPlot()
            else:
                self.openparticle()
                self.MakeParticlePlot()

    def timeslider(self):
        """
        time slider
        
        Returns:
            None
        """
        self.tstep=self.timeSlider.value()
        self.time = taxis[self.tstep-1]
        self.tstepLabel.setText("tstep %d" %self.tstep)
        self.timeLabel.setText("%6.1f fs" %self.time)

    def x1minslider(self):
        """
        xaxis minimum slider
        
        Returns:
            None
        """
        x1minloc = self.x1minSlider.value()
        x1maxloc = self.x1maxSlider.value()
        if x1minloc > x1maxloc: 
            x1minloc = x1maxloc - 2
            self.x1minSlider.setValue(x1minloc)
        if dim == 3:
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                xmin = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*x1minloc/100. 
                self.x1minLabel.setText(str("%.1f" %xmin))
                self.xminloc_panel[self.panelselect-1] = x1minloc
            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                zmin = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*x1minloc/100.
                self.x1minLabel.setText(str("%.1f" %zmin))
                self.zminloc_panel[self.panelselect-1] = x1minloc
            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                zmin = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*x1minloc/100. 
                self.x1minLabel.setText(str("%.1f" %zmin))
                self.zminloc_panel[self.panelselect-1] = x1minloc
        else:
            zmin = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*(x1minloc)/100.
            self.x1minLabel.setText(str("%.1f" %zmin))
            self.zminloc_panel[self.panelselect-1] = x1minloc

        #self.MakePlot()

    def x1maxslider(self):
        """
        xaxis maximum slider
        
        Returns:
            None
        """
        x1minloc = self.x1minSlider.value()
        x1maxloc = self.x1maxSlider.value()
        if x1maxloc < x1minloc: 
            x1maxloc = x1minloc + 2
            self.x1maxSlider.setValue(x1maxloc)
        if dim == 3:
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                xmax = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*x1maxloc/100. 
                self.x1maxLabel.setText(str("%.1f" %xmax))
                self.xmaxloc_panel[self.panelselect-1] = x1maxloc
            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                zmax = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*x1maxloc/100. 
                self.x1maxLabel.setText(str("%.1f" %zmax))
                self.zmaxloc_panel[self.panelselect-1] = x1maxloc
            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                zmax = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*x1maxloc/100.
                self.x1maxLabel.setText(str("%.1f" %zmax))
                self.zmaxloc_panel[self.panelselect-1] = x1maxloc
        else:
            zmax = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*x1maxloc/100. 
            self.x1maxLabel.setText(str("%.1f" %zmax))
            self.zmaxloc_panel[self.panelselect-1] = x1maxloc

        #self.MakePlot()
            
    def x2minslider(self):
        """
        yaxis minimum slider
        
        Returns:
            None
        """
        x2minloc = self.x2minSlider.value()
        x2maxloc = self.x2maxSlider.value()
        if x2minloc > x2maxloc: 
            x2minloc = x2maxloc - 2
            self.x2minSlider.setValue(x2minloc)
        if dim == 3:
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                ymin = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*x2minloc/100. 
                self.x2minLabel.setText(str("%.1f" %ymin))
                self.yminloc_panel[self.panelselect-1] = x2minloc
            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                xmin = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*x2minloc/100. 
                self.x2minLabel.setText(str("%.1f" %xmin))
                self.xminloc_panel[self.panelselect-1] = x2minloc
            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                ymin = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*x2minloc/100. 
                self.x2minLabel.setText(str("%.1f" %ymin))
                self.yminloc_panel[self.panelselect-1] = x2minloc

        else:
            xmin = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*x2minloc/100. 
            self.x2minLabel.setText(str("%.1f" %xmin))
            self.xminloc_panel[self.panelselect-1] = x2minloc

        #self.MakePlot()
            
    def x2maxslider(self):
        """
        yaxis maximum slider
        
        Returns:
            None
        """
        x2minloc = self.x2minSlider.value()
        x2maxloc = self.x2maxSlider.value()
        if x2maxloc < x2minloc: 
            x2maxloc = x2minloc + 2
            self.x2maxSlider.setValue(x2maxloc)
        if dim == 3:
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                ymax = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*x2maxloc/100. 
                self.x2maxLabel.setText(str("%.1f" %ymax))
                self.ymaxloc_panel[self.panelselect-1] = x2maxloc
            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                xmax = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*x2maxloc/100. 
                self.x2maxLabel.setText(str("%.1f" %xmax))
                self.xmaxloc_panel[self.panelselect-1] = x2maxloc
            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                ymax = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*x2maxloc/100. 
                self.x2maxLabel.setText(str("%.1f" %ymax))
                self.ymaxloc_panel[self.panelselect-1] = x2maxloc
        else:
            xmax = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*x2maxloc/100. 
            self.x2maxLabel.setText(str("%.1f" %xmax))
            self.xmaxloc_panel[self.panelselect-1] = x2maxloc
        
        #self.MakePlot()

    def releasebutton(self):
        """
        Return to the original space range
        
        Returns:
            None
        """
        self.x1minSlider.setValue(0)
        self.x1maxSlider.setValue(100)
        self.x2minSlider.setValue(0)
        self.x2maxSlider.setValue(100)
        if self.fieldButton.isChecked():
            self.MakeFieldPlot()
        else:
            self.MakeParticlePlot()

    def fieldbutton(self):
        """
        Field selection button
        
        Returns:
            None
        """
        self.field_select_panel[self.panelselect-1] = True
        self.openfield()
        self.MakeFieldPlot()

    def fieldcombobox(self):
        """
        Field combo box
        
        Returns:
            None
        """
        self.fieldButton.setChecked(True)
        self.field_select_panel[self.panelselect-1] = True
        index=self.fieldsComboBox.currentIndex()
        self.field_panel[self.panelselect-1] = field_list[index]
        self.openfield()
        self.MakeFieldPlot()

    def particlebutton(self):
        """
        Particle selection button
        
        Returns:
            None
        """
        self.field_select_panel[self.panelselect-1] = False
        self.openparticle()
        self.MakeParticlePlot()

    def speciescombobox(self):
        """
        Species combo box
        
        Returns:
            None
        """
        self.particleButton.setChecked(True)
        self.field_select_panel[self.panelselect-1] = False
        index=self.speciesComboBox.currentIndex()
        self.species_panel[self.panelselect-1] = species_list[index]
        self.openparticle()
        self.MakeParticlePlot()

    def phasecombobox(self):
        """
        Phase space combo box
        
        Returns:
            None
        """
        self.particleButton.setChecked(True)
        self.field_select_panel[self.panelselect-1] = False
        index=self.phaseComboBox.currentIndex()
        if dim == 2:
            self.phase_panel[self.panelselect-1] = phase_list1[index]
        else:
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                self.phase_panel[self.panelselect-1] = phase_list2[index]
            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                self.phase_panel[self.panelselect-1] = phase_list1[index]
            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                self.phase_panel[self.panelselect-1] = phase_list3[index]

        self.openparticle()
        self.MakeParticlePlot()

    def loadSavedConfig(self):

        file = './configuration.txt'
        savedparam = {}
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if len(row) == 2:
                    savedparam[row[0].strip()] = row[1].strip()
                # below is for the panel parmaters
                if len(row) == 3:
                    savedparam[(row[0].strip(),row[1].strip())] = row[2].strip()
                elif len(row) == 4:
                    savedparam[(row[0].strip(),row[1].strip())] = (row[2].strip(),row[3].strip())
        
        self.nrow = int(savedparam['nrow'])
        self.ncolumn = int(savedparam['ncolumn'])

        self.rowpanelSpinBox.setValue(self.nrow)
        self.columnpanelSpinBox.setValue(self.ncolumn)

        self.panellayout.deleteLater()
        # Update the panel buttons
        self.SetPanelButtons()


        self.field_select_panel = []
        self.field_panel = []
        self.species_panel = []
        self.phase_panel = []
        self.line_panel = []
        self.rectangle_panel = []
        self.aspect_panel = []
        self.xminloc_panel = []
        self.xmaxloc_panel = []
        self.zminloc_panel = []
        self.zmaxloc_panel = []

        if dim == 3:
            self.sliceplane_panel = []
            self.slicevalue_panel = []
            self.yminloc_panel = []
            self.ymaxloc_panel = []

        for l in np.arange(self.nrow*self.ncolumn):
            
            self.field_select_panel.append(eval(savedparam[('field_select_panel',str(l))]))
            self.field_panel.append(savedparam[('field_panel',str(l))])
            self.species_panel.append(savedparam[('species_panel',str(l))])
            self.phase_panel.append(savedparam[('phase_panel', str(l))])
            self.line_panel.append(eval(savedparam[('line_panel', str(l))]))
            self.rectangle_panel.append(eval(savedparam[('rectangle_panel', str(l))]))
            self.aspect_panel.append(savedparam[('aspect_panel', str(l))])
            self.xminloc_panel.append(int(savedparam[('xminloc_panel', str(l))]))
            self.xmaxloc_panel.append(int(savedparam[('xmaxloc_panel', str(l))]))
            self.zminloc_panel.append(int(savedparam[('zminloc_panel', str(l))]))
            self.zmaxloc_panel.append(int(savedparam[('zmaxloc_panel', str(l))]))
            if dim == 3:
                self.sliceplane_panel.append(savedparam[('sliceplane_panel', str(l))])
                self.slicevalue_panel.append(int(savedparam[('slicevalue_panel', str(l))]))
                self.yminloc_panel.append(int(savedparam[('yminloc_panel', str(l))]))
                self.ymaxloc_panel.append(int(savedparam[('ymaxloc_panel', str(l))]))   

        self.opendataSync()
        self.MakePlotSync()


    def savepushbutton(self):

        f = open('configuration.txt','w')
        f.write('nrow, %d \n'%(self.nrow))
        f.write('ncolumn, %d \n'%(self.ncolumn)) 
        for l in np.arange(self.nrow*self.ncolumn):
            f.write('field_select_panel, %d, %r \n'%(l, self.field_select_panel[l]))
            f.write('field_panel, %d, %s \n'%(l, self.field_panel[l]))
            f.write('species_panel, %d, %s \n'%(l, self.species_panel[l]))
            f.write('phase_panel, %d, %s, %s \n'%(l, 
                        self.phase_panel[l][0], self.phase_panel[l][1]))
            f.write('line_panel, %d, %r \n'%(l, self.line_panel[l]))
            f.write('rectangle_panel, %d, %r \n'%(l, self.rectangle_panel[l]))
            f.write('aspect_panel, %d, %s \n'%(l, self.aspect_panel[l]))
            f.write('xminloc_panel, %d, %d \n'%(l, self.xminloc_panel[l]))
            f.write('xmaxloc_panel, %d, %d \n'%(l, self.xmaxloc_panel[l]))
            f.write('zminloc_panel, %d, %d \n'%(l, self.zminloc_panel[l]))
            f.write('zmaxloc_panel, %d, %d \n'%(l, self.zmaxloc_panel[l]))
            if dim == 3:
                f.write('sliceplane_panel, %d, %s \n'%(l, self.sliceplane_panel[l]))
                f.write('slicevalue_panel, %d, %d \n'%(l, self.slicevalue_panel[l]))
                f.write('yminloc_panel, %d, %d \n'%(l, self.yminloc_panel[l]))
                f.write('ymaxloc_panel, %d, %d \n'%(l, self.ymaxloc_panel[l]))
         

        print('configuration saved')
        f.close()


    def quitpushbutton(self):
        """
        Quit this program
        
        Returns:
            None
        """
        sys.exit(0)

    def slicebutton(self):
        """
        In 3D, select 2D slice plane, 'y-x', 'x-z', or 'y-x'.
        Returns:
            None
        """
        if dim == 3:    # only works for 3D
            
            if self.xyButton.isChecked():
                if self.sliceplane_panel[self.panelselect-1] == 'xy':
                    # if select the same button, return the slice value to the median
                    slicevalue = 15
                    self.slicevalueSlider.setValue(slicevalue)
                    self.slicevalue_panel[self.panelselect-1] = slicevalue
                else:
                    self.sliceplane_panel[self.panelselect-1] = 'xy'
                    slicevalue = self.slicevalue_panel[self.panelselect-1]
                    self.slicevalueSlider.setValue(slicevalue)
                    # change the space range labels
                    self.ChangeRangeSliderLabels()

                    # change the phase combo-box menus
                    index=self.phaseComboBox.currentIndex()
                    self.phase_panel[self.panelselect-1] = phase_list2[index]
                    self.phaseComboBox.clear() 
                    for i in np.arange(len(phase_list2)):
                        self.phaseComboBox.addItem(phase_list2[i][0]+'-'+phase_list2[i][1], i)
                    self.phaseComboBox.setCurrentIndex(index)
                
                zvalue = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*slicevalue/30.
                self.slicevalueLabel.setText(str("z=%.2f" %zvalue))
                stride = self.strideSlider.value()
                self.strideLabel.setText(u'\u0394'+ "z=%.2f" %(stride/30.))

                
            if self.xzButton.isChecked():
                if self.sliceplane_panel[self.panelselect-1] == 'xz':
                    # if select the same button, return the slice value to the median
                    slicevalue = 15
                    self.slicevalueSlider.setValue(slicevalue)
                    self.slicevalue_panel[self.panelselect-1] = slicevalue
                else:
                    self.sliceplane_panel[self.panelselect-1] = 'xz'
                    slicevalue = self.slicevalue_panel[self.panelselect-1]
                    self.slicevalueSlider.setValue(slicevalue)

                    # change the space range labels
                    self.ChangeRangeSliderLabels()

                    # change the phase combo-box menus
                    index=self.phaseComboBox.currentIndex()
                    self.phase_panel[self.panelselect-1] = phase_list1[index]
                    self.phaseComboBox.clear() 
                    for i in np.arange(len(phase_list1)):
                        self.phaseComboBox.addItem(phase_list1[i][0]+'-'+phase_list1[i][1], i)
                    self.phaseComboBox.setCurrentIndex(index)
                    
                yvalue = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*slicevalue/30.
                self.slicevalueLabel.setText(str("y=%.2f" %yvalue))
                stride = self.strideSlider.value()
                self.strideLabel.setText(u'\u0394'+ "y=%.2f" %(stride/30.))
   
            if self.yzButton.isChecked():        
                if self.sliceplane_panel[self.panelselect-1] == 'yz':
                    # if select the same button, return the slice value to the median
                    slicevalue = 15
                    self.slicevalueSlider.setValue(slicevalue)
                    self.slicevalue_panel[self.panelselect-1] = slicevalue
                else:
                    self.sliceplane_panel[self.panelselect-1] = 'yz'
                    slicevalue = self.slicevalue_panel[self.panelselect-1]
                    self.slicevalueSlider.setValue(slicevalue)

                    # change the space range labels
                    self.ChangeRangeSliderLabels()

                    # change the phase combo-box menus
                    index=self.phaseComboBox.currentIndex()
                    self.phase_panel[self.panelselect-1] = phase_list3[index]
                    self.phaseComboBox.clear() 
                    for i in np.arange(len(phase_list3)):
                        self.phaseComboBox.addItem(phase_list3[i][0]+'-'+phase_list3[i][1], i)
                    self.phaseComboBox.setCurrentIndex(index)

                xvalue = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*slicevalue/30.
                self.slicevalueLabel.setText(str("x=%.2f" %xvalue))
                stride = self.strideSlider.value()
                self.strideLabel.setText(u'\u0394'+ "x=%.2f" %(stride/30.))
                
            if self.field_select_panel[self.panelselect-1]:
                self.openfield()
                self.MakeFieldPlot()
            else:
                self.openparticle()
                self.MakeParticlePlot()

        else:
            self.xzButton.setChecked(True)

    def slicevalueslider(self):
        """
        Change the slider for 3rd axis in the 2D slice plane

        Returns:
            None
        """
        if dim == 3:
            slicevalue = self.slicevalueSlider.value()
            self.slicevalue_panel[self.panelselect-1] = slicevalue
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                zvalue = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*slicevalue/30.
                self.slicevalueLabel.setText(str("z=%.2f" %zvalue))
            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                yvalue = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*slicevalue/30.
                self.slicevalueLabel.setText(str("y=%.2f" %yvalue))
            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                xvalue = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*slicevalue/30.
                self.slicevalueLabel.setText(str("x=%.2f" %xvalue))

            if self.fieldButton.isChecked():
                self.MakeFieldPlot()
            else:
                self.MakeParticlePlot()
        else:
            self.slicevalueSlider.setValue(14)

    def strideslider(self):
        """
        Change the stride for 3rd axis in the 2D slice plane (only works for particles)

        Returns:
            None
        """
        if dim == 3:
            if self.particleButton.isChecked():
                stride = self.strideSlider.value()
                if self.sliceplane_panel[self.panelselect-1] == 'xy':
                    self.strideLabel.setText(u'\u0394'+ "z=%.2f" %(stride/30.))
                if self.sliceplane_panel[self.panelselect-1] == 'xz':
                    self.strideLabel.setText(u'\u0394'+ "y=%.2f" %(stride/30.))
                if self.sliceplane_panel[self.panelselect-1] == 'yz':
                    self.strideLabel.setText(u'\u0394'+ "x=%.2f" %(stride/30.))

                self.MakeParticlePlot()
        else:
            self.slicevalueSlider.setValue(15)

    def animationbutton(self):
        
        self.c_thread=threading.Thread(target=self.myEventListener)
        self.c_thread.start()
           
    def myEventListener(self):
        tini = self.tiniSpinBox.value()
        tmax = self.tmaxSpinBox.value()
        step = self.stepSpinBox.value()

        for t in np.arange(tini,tmax+1,step):
            self.tstep = t
            self.time = taxis[self.tstep-1]
            # updata time slider
            self.tstepLabel.setText("tstep %d" %self.tstep)
            self.timeLabel.setText("%6.1f fs" %self.time)
            self.timeSlider.setValue(self.tstep)

            # update domain axes
            self.xaxis, self.yaxis, self.zaxis = \
                    self.datainfo.update_domain_axes(
                        dataformat, dim, iterations[self.tstep-1])
            self.ChangeRangeSliderLabels()

            if self.synctimeBox.isChecked():
                self.opendataSync()
                self.MakePlotSync()
            else:
                if self.fieldButton.isChecked():
                    self.openfield()
                    self.MakeFieldPlot()
                else:
                    self.openparticle()
                    self.MakeParticlePlot()

        

    def plotbutton(self):
        """
        Plotbutton

        Returns:
            None
        """

        nrow = self.rowpanelSpinBox.value()
        ncolumn = self.columnpanelSpinBox.value()

        if self.nrow != nrow or self.ncolumn != ncolumn:
            #############################################
            # create new multi-panels if the panel dimension (nrow x ncolumn) is changed.
            #############################################
            nrow0 = self.nrow; ncolumn0 = self.ncolumn
            self.nrow = nrow
            self.ncolumn = ncolumn
            self.panellayout.deleteLater()

            if self.panelselect > (self.nrow*self.ncolumn): 
                # This is when the panel dimension is decreased.
                self.panelselect = self.nrow*self.ncolumn
            
            # Update the panel buttons
            self.SetPanelButtons()

            field_select_panel0 = self.field_select_panel
            field_panel0 = self.field_panel
            species_panel0 = self.species_panel
            phase_panel0 = self.phase_panel
            line_panel0 = self.line_panel
            rectangle_panel0 = self.rectangle_panel
            aspect_panel0 = self.aspect_panel
            if dim  == 3:
                sliceplane_panel0 = self.sliceplane_panel
                slicevalue_panel0 = self.slicevalue_panel
            xminloc_panel0 = self.xminloc_panel
            xmaxloc_panel0 = self.xmaxloc_panel
            if dim  == 3:
                yminloc_panel0 = self.yminloc_panel
                ymaxloc_panel0 = self.ymaxloc_panel
            zminloc_panel0 = self.zminloc_panel
            zmaxloc_panel0 = self.zmaxloc_panel
           
            # Re-initialize the panel parameter lists.
            self.field_panel = []
            self.species_panel = []
            self.phase_panel = []
            self.line_panel = []
            self.field_select_panel = []
            self.rectangle_panel = []
            self.aspect_panel = []
            self.sliceplane_panel = []
            self.slicevalue_panel = []
            self.xminloc_panel = []
            self.xmaxloc_panel = []
            self.yminloc_panel = []
            self.ymaxloc_panel = []
            self.zminloc_panel = []
            self.zmaxloc_panel = []

            for l in np.arange(self.nrow*self.ncolumn):
                self.field_panel.append(field_panel0[np.mod(l,nrow0*ncolumn0)])
                if l < nrow0*ncolumn0:
                    self.field_select_panel.append(field_select_panel0[l])
                    self.line_panel.append(line_panel0[l])
                    self.rectangle_panel.append(rectangle_panel0[l])
                    self.aspect_panel.append(aspect_panel0[l])
                    self.species_panel.append(species_panel0[l])
                    self.phase_panel.append(phase_panel0[l])
                    if dim == 3:
                        self.sliceplane_panel.append(sliceplane_panel0[l])
                        self.slicevalue_panel.append(slicevalue_panel0[l])
                    self.xminloc_panel.append(xminloc_panel0[l])
                    self.xmaxloc_panel.append(xmaxloc_panel0[l])
                    if dim == 3:
                        self.yminloc_panel.append(yminloc_panel0[l])
                        self.ymaxloc_panel.append(ymaxloc_panel0[l])
                    self.zminloc_panel.append(zminloc_panel0[l])
                    self.zmaxloc_panel.append(zmaxloc_panel0[l])
                else:
                    self.field_select_panel.append('True')
                    self.line_panel.append(False)
                    self.rectangle_panel.append(False)
                    self.aspect_panel.append('auto')
                    self.species_panel.append(species_panel0[0])
                    self.phase_panel.append(phase_panel0[0])
                    if dim == 3:
                        self.sliceplane_panel.append('xz')
                        self.slicevalue_panel.append(15)
                    self.xminloc_panel.append(0)
                    self.xmaxloc_panel.append(100)
                    if dim == 3:
                        self.yminloc_panel.append(0)
                        self.ymaxloc_panel.append(100)
                    self.zminloc_panel.append(0)
                    self.zmaxloc_panel.append(100)
                    
            self.figure.clear()
            self.opendataSync()
            self.MakePlotSync()

            self.localdataplot.figure.clear()

        else:   # just plot 
            if self.field_select_panel[self.panelselect-1]:
                self.openfield()
                self.MakeFieldPlot()
            else:
                self.openparticle()
                self.MakeParticlePlot()

    def aspectcheckbox(self):
        """
        aspect-ratio checkbox

        Returns:
            None
        """
        if self.aspectCheckBox.isChecked():
            self.aspect_panel[self.panelselect-1]='equal'
        else:
            self.aspect_panel[self.panelselect-1]='auto'

        if self.synctimeBox.isChecked():
            self.MakePlotSync()
        else:
            self.MakeFieldPlot()

    def linecheckbox(self):
        """
        Local line selection checkbox

        Returns:
            None
        """
        if self.lineCheckBox.isChecked():
            self.line_panel[self.panelselect-1]=True
            self.rectangleCheckBox.setChecked(False)
            self.rectangle_panel[self.panelselect-1]=False
            if self.panelselect-1 in self.rectangle1.keys():
                self.rectangle1[(self.panelselect-1)].remove()
                self.rectangle2[(self.panelselect-1)].remove()
                self.rectangle3[(self.panelselect-1)].remove()
                self.rectangle4[(self.panelselect-1)].remove()
                self.canvas.draw()
        else:
            self.line_panel[self.panelselect-1]=False
            if self.panelselect-1 in self.line.keys():
                self.line[(self.panelselect-1)].remove()
                self.canvas.draw()         

    def rectanglecheckbox(self):
        """
        Local rectangle selection checkbox

        Returns:
            None
        """
        if self.rectangleCheckBox.isChecked():
            self.rectangle_panel[self.panelselect-1]=True
            self.lineCheckBox.setChecked(False)
            self.line_panel[self.panelselect-1]=False
            if self.panelselect-1 in self.line.keys():
                self.line[(self.panelselect-1)].remove()
                self.canvas.draw()         
        else:
            self.rectangle_panel[self.panelselect-1]=False

            if self.panelselect-1 in self.rectangle1.keys():
                self.rectangle1[(self.panelselect-1)].remove()
                self.rectangle2[(self.panelselect-1)].remove()
                self.rectangle3[(self.panelselect-1)].remove()
                self.rectangle4[(self.panelselect-1)].remove()
                self.canvas.draw()

    def ChangeRangeSliderLabels(self):
        """
        Change the space range labels

        Returns:
            None
        """

        if dim == 3:
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                self.x1min.setText("xmin")
                self.x1max.setText("xmax")
                self.x2min.setText("ymin")
                self.x2max.setText("ymax")
                xminloc = self.xminloc_panel[self.panelselect-1]
                xmaxloc = self.xmaxloc_panel[self.panelselect-1]
                yminloc = self.yminloc_panel[self.panelselect-1]
                ymaxloc = self.ymaxloc_panel[self.panelselect-1]
                self.x1minSlider.setValue(xminloc)
                self.x1maxSlider.setValue(xmaxloc)
                self.x2minSlider.setValue(yminloc)
                self.x2maxSlider.setValue(ymaxloc)
                xmin=self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xminloc/100.
                xmax=self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xmaxloc/100.
                ymin=self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*yminloc/100.
                ymax=self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*ymaxloc/100.
                self.x1minLabel.setText(str("%.1f" %xmin))
                self.x1maxLabel.setText(str("%.1f" %xmax))
                self.x2minLabel.setText(str("%.1f" %ymin))
                self.x2maxLabel.setText(str("%.1f" %ymax))
                

            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                self.x1min.setText("zmin")
                self.x1max.setText("zmax")
                self.x2min.setText("xmin")
                self.x2max.setText("xmax")
                xminloc = self.xminloc_panel[self.panelselect-1]
                xmaxloc = self.xmaxloc_panel[self.panelselect-1]
                zminloc = self.zminloc_panel[self.panelselect-1]
                zmaxloc = self.zmaxloc_panel[self.panelselect-1]
                self.x1minSlider.setValue(zminloc)
                self.x1maxSlider.setValue(zmaxloc)
                self.x2minSlider.setValue(xminloc)
                self.x2maxSlider.setValue(xmaxloc)
                xmin=self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xminloc/100.
                xmax=self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xmaxloc/100.
                zmin=self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zminloc/100. 
                zmax=self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zmaxloc/100. 
                self.x1minLabel.setText(str("%.1f" %zmin))
                self.x1maxLabel.setText(str("%.1f" %zmax))
                self.x2minLabel.setText(str("%.1f" %xmin))
                self.x2maxLabel.setText(str("%.1f" %xmax))

            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                self.x1min.setText("zmin")
                self.x1max.setText("zmax")
                self.x2min.setText("ymin")
                self.x2max.setText("ymax")
                yminloc = self.yminloc_panel[self.panelselect-1]
                ymaxloc = self.ymaxloc_panel[self.panelselect-1]
                zminloc = self.zminloc_panel[self.panelselect-1]
                zmaxloc = self.zmaxloc_panel[self.panelselect-1]
                self.x1minSlider.setValue(zminloc)
                self.x1maxSlider.setValue(zmaxloc)
                self.x2minSlider.setValue(yminloc)
                self.x2maxSlider.setValue(ymaxloc)
                ymin=self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*yminloc/100. 
                ymax=self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*ymaxloc/100.
                zmin=self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zminloc/100. 
                zmax=self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zmaxloc/100. 
                self.x1minLabel.setText(str("%.1f" %zmin))
                self.x1maxLabel.setText(str("%.1f" %zmax))
                self.x2minLabel.setText(str("%.1f" %ymin))
                self.x2maxLabel.setText(str("%.1f" %ymax))

        else:
                xminloc = self.xminloc_panel[self.panelselect-1]
                xmaxloc = self.xmaxloc_panel[self.panelselect-1]
                zminloc = self.zminloc_panel[self.panelselect-1]
                zmaxloc = self.zmaxloc_panel[self.panelselect-1]
                self.x1minSlider.setValue(zminloc)
                self.x1maxSlider.setValue(zmaxloc)
                self.x2minSlider.setValue(xminloc)
                self.x2maxSlider.setValue(xmaxloc)
                xmin=self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xminloc/100.
                xmax=self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xmaxloc/100.
                zmin=self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zminloc/100. 
                zmax=self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zmaxloc/100. 
                self.x1minLabel.setText(str("%.1f" %zmin))
                self.x1maxLabel.setText(str("%.1f" %zmax))
                self.x2minLabel.setText(str("%.1f" %xmin))
                self.x2maxLabel.setText(str("%.1f" %xmax))

    def getSpaceRanges(self):
        """
        Get space range values

        Returns:
            None
        """
        if dim == 2:
            # xminloc, xmaxloc, ... are values in [0,99]
            xminloc = self.xminloc_panel[self.panelselect-1]
            xmaxloc = self.xmaxloc_panel[self.panelselect-1]
            zminloc = self.zminloc_panel[self.panelselect-1]
            zmaxloc = self.zmaxloc_panel[self.panelselect-1]
            # x1min, x1max, ... are coordinates
            x1min = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zminloc/100.
            x1max = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zmaxloc/100.
            x2min = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xminloc/100.
            x2max = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xmaxloc/100.
            # iloc1, iloc2, .. are grids
            jloc1 = int(len(self.xaxis)*xminloc/100.)
            jloc2 = int(len(self.xaxis)*xmaxloc/100.)
            iloc1 = int(len(self.zaxis)*zminloc/100.)
            iloc2 = int(len(self.zaxis)*zmaxloc/100.)

            kloc1 = 1
            kloc2 = 1
            
        else:   # 3D
            if self.sliceplane_panel[self.panelselect-1] == 'xy':
                xminloc = self.xminloc_panel[self.panelselect-1]
                xmaxloc = self.xmaxloc_panel[self.panelselect-1]
                yminloc = self.yminloc_panel[self.panelselect-1]
                ymaxloc = self.ymaxloc_panel[self.panelselect-1]
                x1min = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xminloc/100.
                x1max = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xmaxloc/100.
                x2min = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*yminloc/100.
                x2max = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*ymaxloc/100.
                iloc1 = int(len(self.xaxis)*xminloc/100.)
                iloc2 = int(len(self.xaxis)*xmaxloc/100.)
                jloc1 = int(len(self.yaxis)*yminloc/100.)
                jloc2 = int(len(self.yaxis)*ymaxloc/100.)
                kloc1 = int(1.0*len(self.zaxis)*self.slicevalue_panel[self.panelselect-1]/30)
                kloc2 = kloc1+1
                
            if self.sliceplane_panel[self.panelselect-1] == 'xz':
                xminloc = self.xminloc_panel[self.panelselect-1]
                xmaxloc = self.xmaxloc_panel[self.panelselect-1]
                zminloc = self.zminloc_panel[self.panelselect-1]
                zmaxloc = self.zmaxloc_panel[self.panelselect-1]
                x1min = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zminloc/100.
                x1max = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zmaxloc/100.
                x2min = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xminloc/100.
                x2max = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*xmaxloc/100.
                iloc1 = int(len(self.xaxis)*xminloc/100.)
                iloc2 = int(len(self.xaxis)*xmaxloc/100.)
                kloc1 = int(len(self.zaxis)*zminloc/100.)
                kloc2 = int(len(self.zaxis)*zmaxloc/100.)
                jloc1 = int(1.0*len(self.yaxis)*self.slicevalue_panel[self.panelselect-1]/30.)
                jloc2 = jloc1+1

            if self.sliceplane_panel[self.panelselect-1] == 'yz':
                yminloc = self.yminloc_panel[self.panelselect-1]
                ymaxloc = self.ymaxloc_panel[self.panelselect-1]
                zminloc = self.zminloc_panel[self.panelselect-1]
                zmaxloc = self.zmaxloc_panel[self.panelselect-1]
                x1min = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zminloc/100.
                x1max = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*zmaxloc/100.
                x2min = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*yminloc/100.
                x2max = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*ymaxloc/100.
                jloc1 = int(len(self.yaxis)*yminloc/100.)
                jloc2 = int(len(self.yaxis)*ymaxloc/100.)
                kloc1 = int(len(self.zaxis)*zminloc/100.)
                kloc2 = int(len(self.zaxis)*zmaxloc/100.)
                iloc1 = int(1.0*len(self.xaxis)*self.slicevalue_panel[self.panelselect-1]/30)
                iloc2 = iloc1+1

        return x1min, x1max, x2min, x2max, iloc1, iloc2, jloc1, jloc2, kloc1, kloc2

    def getLocalparticleLoc(self):
        """
        Select particle indices located within the particle stride of the 3rd axis

        Returns:
            None
        """
        loc_container = {}

        # Find which panels have particleselection.
        # i.e., index = [0,1,3,5,..] --> panels 0, 1, 3, 5 .. have particle plots.
        index = [i for i, yesfield in enumerate(self.field_select_panel) if not yesfield]
        stride = self.strideSlider.value()
        for l in index:
            species = self.species_panel[l]
            if self.sliceplane_panel[l] == 'xy':
                slicevalue = self.slicevalue_panel[l]
                zvalue = self.zaxis[0]+(self.zaxis[-1]-self.zaxis[0])*(slicevalue/30.)
                width = (self.zaxis[-1]-self.zaxis[0])*(stride/30.)
                loc = np.where((self.pdata_container[(species,'z',self.tstep)] > zvalue-.5*width) & \
                       (self.pdata_container[(species,'z',self.tstep)] < zvalue+.5*width))[0]
                
            if self.sliceplane_panel[l] == 'xz':
                slicevalue = self.slicevalue_panel[l]
                yvalue = self.yaxis[0]+(self.yaxis[-1]-self.yaxis[0])*(slicevalue/30.)
                width = (self.yaxis[-1]-self.yaxis[0])*(stride/30.)
                loc = np.where((self.pdata_container[(species,'y',self.tstep)] > yvalue-.5*width) & \
                       (self.pdata_container[(species,'y',self.tstep)] < yvalue+.5*width))[0]

            if self.sliceplane_panel[l] == 'yz':
                slicevalue = self.slicevalue_panel[l]
                xvalue = self.xaxis[0]+(self.xaxis[-1]-self.xaxis[0])*(slicevalue/30.)
                width = (self.xaxis[-1]-self.xaxis[0])*(stride/30.)
                loc = np.where((self.pdata_container[(species,'x',self.tstep)] > xvalue-.5*width) & \
                       (self.pdata_container[(species,'x',self.tstep)] < xvalue+.5*width))[0]

            loc_container[(l)] = loc

        return loc_container

    #def shiftcheckbox(self):
    #    if self.shiftCheckBox.isChecked():
    #        self.shift_panel[self.panelselect-1]=True
    #    else:
    #        self.shift_panel[self.panelselect-1]=False

    def PrepareLocalplot(self):

        if self.lineCheckBox.isChecked():
            self.MakelocallinePlot()
        if self.rectangleCheckBox.isChecked():
            self.MakelocalcontourPlot()

        self.localdataplot.show()

    def MakelocallinePlot(self):

        field = self.field_panel[self.panelselect-1]
        t = self.tstep
  
        if dim == 2:
            xL = int(min(self.x_o,self.x_r))
            xR = int(max(self.x_o,self.x_r))
            yL = int(min(self.y_o,self.y_r))
            yR = int(max(self.y_o,self.y_r))
            iL = np.where(self.zaxis > xL)[0][0]
            iR = np.where(self.zaxis > xR)[0][0]
            jL = np.where(self.xaxis > yL)[0][0]
            jR = np.where(self.xaxis > yR)[0][0]

            laxis = []
            ldata = []
            if np.abs(jR-jL) < np.abs(iR-iL):
                m = 1.*(jR-jL)/(iR-iL)
                if iL > iR:
                    step = -1
                else:
                    step = 1
                for i in np.arange(iL, iR, step):
                    j = m*(i-iL) + jL
                    j = int(j)
                    ldata.append(self.fdata_container[(field,t)][j,i])
                    length = (self.zaxis[i]-self.zaxis[iL])**2+(self.xaxis[j]-self.xaxis[jL])**2
                    length = length**.5
                    laxis.append(length)
            else:
                m = 1.*(iR-iL)/(jR-jL)
                if jL > jR:
                    step = -1
                else:
                    step = 1
                for j in np.arange(jL, jR, step):
                    i = m*(j-jL) + iL
                    i = int(i)
                    ldata.append(self.fdata_container[(field,t)][j,i])
                    length = (self.zaxis[i]-self.zaxis[iL])**2+(self.xaxis[j]-self.xaxis[jL])**2
                    length = length**.5
                    laxis.append(length)

            self.dataplot.locallineplot2D(
                self.localdataplot.figure,
                self.nrow, 
                self.ncolumn,
                field,
                self.panelselect,
                self.time,
                laxis, 
                ldata)

            self.localdataplot.canvas.draw()


    def MakelocalcontourPlot(self):

        field = self.field_panel[self.panelselect-1]
        t = self.tstep
  
        if dim == 2:
            xL = int(min(self.x_o,self.x_r))
            xR = int(max(self.x_o,self.x_r))
            yL = int(min(self.y_o,self.y_r))
            yR = int(max(self.y_o,self.y_r))
            iL = np.where(self.zaxis > xL)[0][0]
            iR = np.where(self.zaxis > xR)[0][0]
            jL = np.where(self.xaxis > yL)[0][0]
            jR = np.where(self.xaxis > yR)[0][0]
    
            self.dataplot.localcontourplot2D(
                self.localdataplot.figure,
                self.fdata_container[(field,t)][jL:jR,iL:iR], 
                self.nrow, 
                self.ncolumn,
                field,
                self.panelselect,
                self.time,
                xL,
                xR,
                yL,
                yR,
                self.aspect_panel[self.panelselect-1])

            self.localdataplot.canvas.draw()

