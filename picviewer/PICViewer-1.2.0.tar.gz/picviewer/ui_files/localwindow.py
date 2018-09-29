
import matplotlib
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas

from PySide import QtCore, QtGui
from matplotlib.figure import Figure
import localwindow_widget

class LocalPlot(QtGui.QMainWindow, localwindow_widget.Ui_MainWindow):
    def __init__(self, left,
                top,
                width,
                height):
        super(LocalPlot, self).__init__()
        self.setupUi(self)
                        
        self.setGeometry(QtCore.QRect(left, top, width, height))
    
        self.setWindowTitle('local plot window')

        self.LayoutWidget = QtGui.QWidget(self.centralwidget)
        self.LayoutWidget.setGeometry(QtCore.QRect(10, 10, width-20, height-20))
        self.plotwidget_layout = QtGui.QVBoxLayout(self.LayoutWidget)
        self.plotwidget_layout.setContentsMargins(0, 0, 0, 0)

        self.figure = Figure()
        self.canvas = Canvas(self.figure)
        self.plotwidget_layout.addWidget(self.canvas)
