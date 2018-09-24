import sys, os, glob
import numpy as np
import matplotlib
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
from picviewer.ui_files.base import Ui_MainWindow
import localwindow
import threading
import csv

import picviewer

from PySide import QtCore, QtGui


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
         initialize GUI
         
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)
         
        # create plotwidget
        self.LayoutWidget = QtGui.QWidget(self.centralwidget)
        self.LayoutWidget.setGeometry(QtCore.QRect(400, 10, 610, 740))
        self.plotwidget_layout = QtGui.QVBoxLayout(self.LayoutWidget)
        self.plotwidget_layout.setContentsMargins(0, 0, 0, 0)

        # coordiates
        self.coordLabel.setText('(x1,x2)=(%d,%d)'%(0,0))
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
        
        # logo icon
        logo_path = os.path.dirname(__file__)
        logo_path = logo_path[:-10] + 'images/logo.png'
        self.imageButton = QtGui.QPushButton(self.centralwidget)
        self.imageButton.setIcon(QtGui.QIcon(logo_path))
        self.imageButton.setIconSize(QtCore.QSize(80, 68))
        self.imageButton.setGeometry(QtCore.QRect(10, 230, 80, 68))   
        self.imageButton.clicked.connect(self.imagebutton)     

        # logo
        #logo_path = os.path.dirname(__file__)
        #logo_path = logo_path[:-10] + 'images/logo.png'
        #self.image = QtGui.QLabel(self.centralwidget)
        #self.image.setGeometry(QtCore.QRect(10, 230, 80, 68))
        #self.pixmap = QtGui.QPixmap(logo_path)
        #self.image.setPixmap(self.pixmap)
        #self.image.show()

        # field button
        self.fieldButton.setChecked(True)

        # 2D slice for 3D data
        self.xzButton.setChecked(True)

        # space slider
        self.x1minSlider.setValue(0)
        self.x1minSlider.setRange(0,100)
        self.x1maxSlider.setValue(100)
        self.x1maxSlider.setRange(0,100)
        self.x2minSlider.setValue(0)
        self.x2minSlider.setRange(0,100)
        self.x2maxSlider.setValue(100)
        self.x2maxSlider.setRange(0,100)

        # slice value slider
        self.slicevalueSlider.setRange(1,29)
        self.slicevalueSlider.setValue(15)
        self.strideSlider.setRange(1,30) 
        self.strideSlider.setMinimum(1)
        self.strideSlider.setValue(10)

        # aspect ratio checkbox
        self.aspectCheckBox.setChecked(False)

        # line selection checkbox
        self.lineCheckBox.setChecked(False)

        # rectangle selection checkbox
        self.rectangleCheckBox.setChecked(False)

        # sync time checkbox
        self.synctimeBox.setChecked(False)

      
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
         
        
        # interactive mouse
        self.pressed= False
        self.line = {}
        self.rectangle1 = {}
        self.rectangle2 = {}
        self.rectangle3 = {}
        self.rectangle4 = {}
        # mouse drag rectangle
        self.pos1 = [0,0]
        self.pos2 = [0,0]

        # create Matplotlib window
        self.figure = Figure()
        self.canvas = Canvas(self.figure)
        self.plotwidget_layout.addWidget(self.canvas)

    def resizeEvent(self,  event):

        width = event.size().width()
        height = event.size().height()
        wratio=1.*(width-400)/(self.width0-400)
        hratio=1.*height/self.height0
        self.LayoutWidget.setGeometry(QtCore.QRect(400, 10, 610*wratio, 740*hratio))

    def imagebutton(self):

        logo_path = os.path.dirname(__file__)
        logo_path = logo_path[:-10] + 'images/logo.png'

        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)

        msg.setIconPixmap(QtGui.QPixmap(logo_path))
        version = picviewer.__version__
        #msg.setWindowTitle("Visualization toolkit for PIC simulations")
        msg.setText( "<br><br><br>" 
		               + 'PICViewer' + " v" + version+ "<br>" 
		               + "(c) 10/2018 LBNL <br><br>")
		               #+ "<a href='{0}'>{0}</a><br><br>".format(website)
		               #+ "<a href='mailto:{0}'>{0}</a><br><br>".format(email) 
		               #+ "License: <a href='{0}'>{1}</a>".format(license_link, 
                       #license_name) )
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        #msg.buttonClicked.connect(msgbtn)  
        msg.exec_()
          