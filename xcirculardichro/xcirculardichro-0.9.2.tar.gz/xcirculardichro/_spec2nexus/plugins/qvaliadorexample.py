'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QApplication
from PyQt5.QtGui import QDoubleValidator
import math
import sys
from PyQt5.Qt import QValidator

class MyWidget(QWidget):
    
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        
        layout = QGridLayout()
        self.line = QLineEdit(str(math.pi))
        
        layout.addWidget(self.line)
        self.validator = QDoubleValidator(-2*math.pi, 2*math.pi, 3, self)
        self.line.setValidator(self.validator)
        self.line.textChanged.connect(self.numberChanged)
        #self.line.editingFinished.connect(self.handleChange)
        self.setLayout(layout)
        
    def handleChange(self):
        print("New Value %f" % float(self.line.text()))
        
    def numberChanged(self, newText):
        
        state = self.validator.validate(newText, 0)[0]
        if state == QValidator.Acceptable:
            color = "#c4df9b"
        elif  state == QValidator.Intermediate:
            color = "#fff79a"
        elif  state == QValidator.Invalid:
            color = "#f6989d"
        else:
            color = "white"
        self.line.setStyleSheet("QLineEdit {background-color: %s}" % color)


app = QApplication(sys.argv)
myWidget = MyWidget()
myWidget.show()
app.exec()
        