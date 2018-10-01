# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/psd_plots_config.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PsdPlotConfigForm(object):
    def setupUi(self, PsdPlotConfigForm):
        PsdPlotConfigForm.setObjectName("PsdPlotConfigForm")
        PsdPlotConfigForm.resize(271, 293)
        self.verticalLayout = QtWidgets.QVBoxLayout(PsdPlotConfigForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.autoScaleX1dCheckBox = QtWidgets.QCheckBox(PsdPlotConfigForm)
        self.autoScaleX1dCheckBox.setEnabled(False)
        self.autoScaleX1dCheckBox.setObjectName("autoScaleX1dCheckBox")
        self.verticalLayout.addWidget(self.autoScaleX1dCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.x1dMaximumLabel = QtWidgets.QLabel(PsdPlotConfigForm)
        self.x1dMaximumLabel.setEnabled(False)
        self.x1dMaximumLabel.setObjectName("x1dMaximumLabel")
        self.horizontalLayout.addWidget(self.x1dMaximumLabel)
        self.x1dMaximumLineEdit = QtWidgets.QLineEdit(PsdPlotConfigForm)
        self.x1dMaximumLineEdit.setEnabled(False)
        self.x1dMaximumLineEdit.setObjectName("x1dMaximumLineEdit")
        self.horizontalLayout.addWidget(self.x1dMaximumLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.autoScaleY1dCheckBox = QtWidgets.QCheckBox(PsdPlotConfigForm)
        self.autoScaleY1dCheckBox.setEnabled(False)
        self.autoScaleY1dCheckBox.setObjectName("autoScaleY1dCheckBox")
        self.verticalLayout.addWidget(self.autoScaleY1dCheckBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.y1dMaximumLabel = QtWidgets.QLabel(PsdPlotConfigForm)
        self.y1dMaximumLabel.setEnabled(False)
        self.y1dMaximumLabel.setObjectName("y1dMaximumLabel")
        self.horizontalLayout_2.addWidget(self.y1dMaximumLabel)
        self.y1dMaximumLineEdit = QtWidgets.QLineEdit(PsdPlotConfigForm)
        self.y1dMaximumLineEdit.setEnabled(False)
        self.y1dMaximumLineEdit.setObjectName("y1dMaximumLineEdit")
        self.horizontalLayout_2.addWidget(self.y1dMaximumLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.waterfallNumBinsLabel = QtWidgets.QLabel(PsdPlotConfigForm)
        self.waterfallNumBinsLabel.setEnabled(True)
        self.waterfallNumBinsLabel.setObjectName("waterfallNumBinsLabel")
        self.horizontalLayout_3.addWidget(self.waterfallNumBinsLabel)
        self.waterfallNumBinsLineEdit = QtWidgets.QLineEdit(PsdPlotConfigForm)
        self.waterfallNumBinsLineEdit.setObjectName("waterfallNumBinsLineEdit")
        self.horizontalLayout_3.addWidget(self.waterfallNumBinsLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.waterfallColorMapLabel = QtWidgets.QLabel(PsdPlotConfigForm)
        self.waterfallColorMapLabel.setEnabled(False)
        self.waterfallColorMapLabel.setObjectName("waterfallColorMapLabel")
        self.horizontalLayout_4.addWidget(self.waterfallColorMapLabel)
        self.waterfallColorMapComboBox = QtWidgets.QComboBox(PsdPlotConfigForm)
        self.waterfallColorMapComboBox.setEnabled(False)
        self.waterfallColorMapComboBox.setObjectName("waterfallColorMapComboBox")
        self.horizontalLayout_4.addWidget(self.waterfallColorMapComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(PsdPlotConfigForm)
        QtCore.QMetaObject.connectSlotsByName(PsdPlotConfigForm)

    def retranslateUi(self, PsdPlotConfigForm):
        _translate = QtCore.QCoreApplication.translate
        PsdPlotConfigForm.setWindowTitle(_translate("PsdPlotConfigForm", "Form"))
        self.autoScaleX1dCheckBox.setText(_translate("PsdPlotConfigForm", "Auto Scale X 1D"))
        self.x1dMaximumLabel.setText(_translate("PsdPlotConfigForm", "X 1D Maximum:"))
        self.autoScaleY1dCheckBox.setText(_translate("PsdPlotConfigForm", "Auto Scale Y 1D"))
        self.y1dMaximumLabel.setText(_translate("PsdPlotConfigForm", "Y 1D Maximum:"))
        self.waterfallNumBinsLabel.setText(_translate("PsdPlotConfigForm", "Waterfall Number of Bins:"))
        self.waterfallColorMapLabel.setText(_translate("PsdPlotConfigForm", "Waterfall Color Map:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PsdPlotConfigForm = QtWidgets.QWidget()
    ui = Ui_PsdPlotConfigForm()
    ui.setupUi(PsdPlotConfigForm)
    PsdPlotConfigForm.show()
    sys.exit(app.exec_())

