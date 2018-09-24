import os
import sys
from PySide import QtCore, QtGui

def launch_gui():

    app = QtGui.QApplication(sys.argv)

    from picviewer.controller.main_controller import ControlCenter

    maincontrol = ControlCenter()


    sys.exit(app.exec_())

if __name__ == '__main__':
    launch_gui()
