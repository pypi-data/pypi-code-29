import sys, os, glob

from picviewer.controller.mainwindow import MainWindow 
from picviewer.controller.initialization import Initialization
from picviewer.controller.time_controller import TimeController
from picviewer.controller.space_controller import SpaceController
from picviewer.controller.panel_controller import PanelController
from picviewer.controller.combobox_controller import ComboboxController
from picviewer.controller.slice_controller import SliceController
from picviewer.controller.mouse_controller import MouseController

from picviewer.dataloader.data_collector import DataCollector
from picviewer.dataplotter.prepare_plot import PreparePlot
from picviewer.dataplotter.prepare_localplot import PrepareLocalplot

from picviewer.configuration.config_loadsave import ConfigLoadsave


import threading
import time as tm


from PySide import QtCore, QtGui

class ControlCenter():
    """
        Main Controller
    """
    def __init__(self):
    
        self.main = MainWindow()
        self.main.show()

        # current folder
        self.main.filepath = os.getcwd()
        # Open data from the current folder
        filelist = glob.glob(self.main.filepath+'/*')
        direct_open = (any('data000' in myfile for myfile in filelist) or \
                      any('plt000' in myfile for myfile in filelist) or \
                      any('flds.tot.' in myfile for myfile in filelist))
        if direct_open:
            # Set window title
            self.main.setWindowTitle(os.getcwd())
            
        # Open data from a selected folder, self.main.filepath
        else:
            self.main.filepath = QtGui.QFileDialog.getExistingDirectory(
                            None, 'Select a folder:', './',
                            QtGui.QFileDialog.ShowDirsOnly)
            # Set window title
            self.main.setWindowTitle(self.main.filepath)

        # ------------------------------------------
        # Initialize classes
        # ------------------------------------------
        # Initialization class (read data and initialize)
        self.initialization = Initialization(self.main)
        # Time Controller class
        self.timecontroller = TimeController(self.main)
        # Space Controller class
        self.spacecontroller = SpaceController(self.main)
        # Panel Controller class
        self.panelcontroller = PanelController(self.main)
        # Create panel buttons
        self.panelcontroller.SetPanelButtons()
        # Combobox Controller class
        self.comboboxcontroller = ComboboxController(self.main)
        self.slicecontroller = SliceController(self.main)
        # Data collection class
        self.collectdata = DataCollector(self.main)
        # Plot class
        self.prepareplot = PreparePlot(self.main)
        # Mouse controller class
        self.mousecontroller = MouseController(self.main)
        # Local plot class
        self.preparelocalplot = PrepareLocalplot(self.main)
        # Configuration load/save class
        self.configloadsave = ConfigLoadsave(self.main)


        # time button
        self.main.backwardtimeButton.clicked.connect(self.backwardtimebutton)
        self.main.forwardtimeButton.clicked.connect(self.forwardtimebutton)
        # time slder
        self.main.timeSlider.valueChanged.connect(self.timeslider)

        # space slider
        self.main.x1minSlider.valueChanged.connect(self.x1minslider)
        self.main.x1maxSlider.valueChanged.connect(self.x1maxslider)
        self.main.x2minSlider.valueChanged.connect(self.x2minslider)
        self.main.x2maxSlider.valueChanged.connect(self.x2maxslider)
        # space slider release
        self.main.releaseButton.clicked.connect(self.releasebutton)

        # field & particle buttons
        QtCore.QObject.connect(self.main.fieldButton, QtCore.SIGNAL('clicked()'),self.fieldbutton)
        QtCore.QObject.connect(self.main.particleButton, QtCore.SIGNAL('clicked()'),self.particlebutton)
        # field combobox 
        self.main.fieldsComboBox.activated.connect(self.fieldcombobox)
        # species combobox
        self.main.speciesComboBox.activated.connect(self.speciescombobox)
        # pahse combobox
        self.main.phaseComboBox.activated.connect(self.phasecombobox)

        # slice (xy, xz, yz 2D plane) button in 3D
        QtCore.QObject.connect(self.main.xyButton, QtCore.SIGNAL('clicked()'),self.slicebutton)
        QtCore.QObject.connect(self.main.xzButton, QtCore.SIGNAL('clicked()'),self.slicebutton)
        QtCore.QObject.connect(self.main.yzButton, QtCore.SIGNAL('clicked()'),self.slicebutton)
        self.main.slicevalueSlider.sliderMoved.connect(self.sliceslider)
        self.main.strideSlider.sliderMoved.connect(self.strideslider)
       
        # Panel button signal
        for i in range(self.main.nrow):
            for j in range(self.main.ncolumn):
                QtCore.QObject.connect(self.main.panelbuttons[(i,j)], QtCore.SIGNAL('clicked()'),self.panelbutton)
  
        # Plot button
        self.main.plotButton.clicked.connect(self.plotbutton)
      
        # Aspect ratio checkbox
        #self.main.aspectCheckBox.clicked.connect(self.aspectcheckbox)
      
        # Line selection checkbox
        self.main.lineCheckBox.clicked.connect(self.linecheckbox)
        # Rectangle selection checkbox
        self.main.rectangleCheckBox.clicked.connect(self.rectanglecheckbox)
        
        # Save cofiguration button
        self.main.savepushButton.clicked.connect(self.saveconfig)

        # Load cofiguration button
        self.main.loadpushButton.clicked.connect(self.loadconfig)

         # Quit button
        self.main.quitpushButton.clicked.connect(self.quitpushbutton)

        # animation PushButton
        self.main.animationButton.clicked.connect(self.animationbutton)
        

        # Data load and plot
        self.collectdata.loaddatasync()
        self.prepareplot.plotsync()


    def backwardtimebutton(self):
        self.timecontroller.backwardtime()
     
    def forwardtimebutton(self):
        self.timecontroller.fowardtime()

    def timeslider(self):
        self.timecontroller.timeslider()

    def x1minslider(self):
        self.spacecontroller.x1minslider()

    def x1maxslider(self):
        self.spacecontroller.x1maxslider()

    def x2minslider(self):
        self.spacecontroller.x2minslider()

    def x2maxslider(self):
        self.spacecontroller.x2maxslider()

    def releasebutton(self):
        self.spacecontroller.releasebutton()

    def fieldbutton(self):
        self.comboboxcontroller.fieldbutton()

    def particlebutton(self):
        self.comboboxcontroller.particlebutton()

    def fieldcombobox(self):
        self.comboboxcontroller.fieldcombobox()

    def speciescombobox(self):
        self.comboboxcontroller.speciescombobox()

    def phasecombobox(self):
        self.comboboxcontroller.phasecombobox()
        
    def slicebutton(self):
        self.slicecontroller.slicebutton()

    def sliceslider(self):
        self.slicecontroller.sliceslider()

    def strideslider(self):
        self.slicecontroller.strideslider()

    def panelbutton(self):
        self.panelcontroller.panelbutton()

    def plotbutton(self):
        # re-create panel buttons if asked
        nrow = self.main.rowpanelSpinBox.value()
        ncolumn = self.main.columnpanelSpinBox.value()
        if self.main.nrow != nrow or self.main.ncolumn != ncolumn:
            self.panelcontroller.RecreatePanelButton()
        else:
            if self.main.field_select_panel[self.main.panelselect-1]:
                self.collectdata.loadfield()
                self.prepareplot.plotfield()
            else:
                self.collectdata.loadparticle()
                self.prepareplot.plotparticle()

        # save png image
        if self.main.pngCheckBox.isChecked():
            savedir = '../'
            tstep = self.main.tstep
            if self.main.synctimeBox.isChecked():
                filename = 'multi_plot'
                self.main.figure.savefig(savedir+filename+'%3.3d.png'%(tstep), format='png')

            else:
                filename = self.main.field_panel[self.main.panelselect-1]
                ax = self.main.axes[(self.main.panelselect-1)]
                extent = ax.get_window_extent().transformed(
                        self.main.figure.dpi_scale_trans.inverted())
                self.main.figure.savefig(savedir+filename+'%3.3d.png'%(tstep), format='png',
                        bbox_inches=extent.expanded(1.35, 1.25))

            print('created a file, %s'%(savedir+filename+'%3.3d.png'%(tstep)))

    def linecheckbox(self):
        self.preparelocalplot.linecheckbox()

    def rectanglecheckbox(self):
        self.preparelocalplot.rectanglecheckbox()

    def saveconfig(self):
        self.configloadsave.SaveConfig()
    
    def loadconfig(self):
        self.configloadsave.LoadConfig()
        
    def quitpushbutton(self):

        sys.exit(0)

    def animationbutton(self):

        self.c_thread=threading.Thread(target=self.myEventListener)
        self.c_thread.start()
           
    def myEventListener(self):
        tini = self.main.tiniSpinBox.value()
        tmax = self.main.tmaxSpinBox.value()
        step = self.main.stepSpinBox.value()

        if self.main.movieCheckBox.isChecked() or self.main.pngCheckBox.isChecked():
            savedir = '../images'
            os.system('mkdir '+savedir)

        s = 0
        for t in range(tini,tmax+1,step):
            self.main.tstep = t
            self.main.time = self.main.taxis[self.main.tstep-1]
            # updata time slider
            self.main.tstepLabel.setText("tstep %d" %self.main.tstep)
            self.main.timeLabel.setText("%6.1f fs" %self.main.time)
            self.main.timeSlider.setValue(self.main.tstep)

            if self.main.synctimeBox.isChecked():
                self.collectdata.loaddatasync()
                self.prepareplot.plotsync()

                if self.main.movieCheckBox.isChecked() or self.main.pngCheckBox.isChecked():
                    filename = 'multi_plot'
                    self.main.figure.savefig(savedir+'/'+filename+'%3.3d.png'%(s), format='png')
            else:
                if self.main.field_select_panel[self.main.panelselect-1]:
                    self.collectdata.loadfield()
                    self.prepareplot.plotfield()
                else:
                    self.collectdata.loadparticle()
                    self.prepareplot.plotparticle()

                if self.main.movieCheckBox.isChecked() or self.main.pngCheckBox.isChecked():
                    filename = self.main.field_panel[self.main.panelselect-1]
                    ax = self.main.axes[(self.main.panelselect-1)]
                    extent = ax.get_window_extent().transformed(
                            self.main.figure.dpi_scale_trans.inverted())

                    self.main.figure.savefig(savedir+'/'+filename+'%3.3d.png'%(s), format='png',
                            bbox_inches=extent.expanded(1.35, 1.25))
                tm.sleep(0.005)
            s+=1

        if self.main.movieCheckBox.isChecked():
            # ffmpeg create .mp4 file
            framerate = 4 #int(raw_input("Input a frame rate (#/second): "))
            command = "ffmpeg -framerate %d " %framerate + "-i "+savedir+"/"+filename+"%03d.png" \
                +" -c:v libx264 -pix_fmt yuv420p -vf scale=1280:-2 ./" + savedir+"/"+filename+".mp4"
            os.system(command)
            print('created %s'%(savedir+"/"+filename+".mp4"))

        self.main.movieCheckBox.setChecked(False)
        self.main.pngCheckBox.setChecked(False)
