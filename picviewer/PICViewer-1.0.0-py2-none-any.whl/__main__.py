import os
import sys
from PySide import QtCore, QtGui

def launch_gui():

    app = QtGui.QApplication(sys.argv)

    from picviewer.controller.mainwindow import MainWindow

    mainwindow = MainWindow()
    mainwindow.show()

    #print(mainwindow.field_panel)

    sys.exit(app.exec_())

if __name__ == '__main__':
    launch_gui()
