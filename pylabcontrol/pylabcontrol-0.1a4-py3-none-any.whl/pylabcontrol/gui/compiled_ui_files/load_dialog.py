# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Dialog():
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(857, 523)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(509, 476, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 436, 841, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(1, 4, 0, 4)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tree_infile = QtWidgets.QTreeView(Dialog)
        self.tree_infile.setGeometry(QtCore.QRect(270, 30, 256, 261))
        self.tree_infile.setAcceptDrops(True)
        self.tree_infile.setDragEnabled(True)
        self.tree_infile.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tree_infile.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tree_infile.setUniformRowHeights(True)
        self.tree_infile.setWordWrap(True)
        self.tree_infile.setObjectName("tree_infile")
        self.tree_loaded = QtWidgets.QTreeView(Dialog)
        self.tree_loaded.setGeometry(QtCore.QRect(10, 30, 256, 261))
        self.tree_loaded.setAcceptDrops(True)
        self.tree_loaded.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tree_loaded.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tree_loaded.setDragEnabled(True)
        self.tree_loaded.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tree_loaded.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tree_loaded.setWordWrap(True)
        self.tree_loaded.setObjectName("tree_loaded")
        self.lbl_info = QtWidgets.QLabel(Dialog)
        self.lbl_info.setGeometry(QtCore.QRect(540, 30, 311, 261))
        self.lbl_info.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_info.setWordWrap(True)
        self.lbl_info.setObjectName("lbl_info")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 241, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 241, 16))
        self.label_2.setObjectName("label_2")
        self.btn_open = QtWidgets.QPushButton(Dialog)
        self.btn_open.setGeometry(QtCore.QRect(774, 440, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        self.btn_open.setObjectName("btn_open")
        self.lbl_probe_log_path = QtWidgets.QLabel(Dialog)
        self.lbl_probe_log_path.setGeometry(QtCore.QRect(10, 440, 22, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_probe_log_path.sizePolicy().hasHeightForWidth())
        self.lbl_probe_log_path.setSizePolicy(sizePolicy)
        self.lbl_probe_log_path.setObjectName("lbl_probe_log_path")
        self.txt_probe_log_path = QtWidgets.QLineEdit(Dialog)
        self.txt_probe_log_path.setGeometry(QtCore.QRect(39, 440, 728, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_probe_log_path.sizePolicy().hasHeightForWidth())
        self.txt_probe_log_path.setSizePolicy(sizePolicy)
        self.txt_probe_log_path.setObjectName("txt_probe_log_path")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 241, 16))
        self.label_3.setObjectName("label_3")
        self.tree_script_sequence = QtWidgets.QTreeView(Dialog)
        self.tree_script_sequence.setGeometry(QtCore.QRect(10, 310, 261, 121))
        self.tree_script_sequence.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tree_script_sequence.setAcceptDrops(True)
        self.tree_script_sequence.setDragEnabled(True)
        self.tree_script_sequence.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tree_script_sequence.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tree_script_sequence.setObjectName("tree_script_sequence")
        self.btn_script_sequence = QtWidgets.QPushButton(Dialog)
        self.btn_script_sequence.setGeometry(QtCore.QRect(280, 380, 111, 41))
        self.btn_script_sequence.setObjectName("btn_script_sequence")
        self.cmb_looping_variable = QtWidgets.QComboBox(Dialog)
        self.cmb_looping_variable.setGeometry(QtCore.QRect(280, 350, 111, 22))
        self.cmb_looping_variable.setObjectName("cmb_looping_variable")
        self.txt_info = QtWidgets.QTextEdit(Dialog)
        self.txt_info.setGeometry(QtCore.QRect(540, 300, 301, 131))
        self.txt_info.setObjectName("txt_info")
        self.txt_script_sequence_name = QtWidgets.QLineEdit(Dialog)
        self.txt_script_sequence_name.setGeometry(QtCore.QRect(280, 320, 113, 20))
        self.txt_script_sequence_name.setObjectName("txt_script_sequence_name")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Loading..."))
        self.lbl_info.setText(_translate("Dialog", "info"))
        self.label.setText(_translate("Dialog", "Selected"))
        self.label_2.setText(_translate("Dialog", "Not Selected"))
        self.btn_open.setText(_translate("Dialog", "open"))
        self.lbl_probe_log_path.setText(_translate("Dialog", "Path"))
        self.txt_probe_log_path.setText(_translate("Dialog", "Z:\\Lab\\Cantilever\\Measurements"))
        self.label_3.setText(_translate("Dialog", "Script Sequence"))
        self.btn_script_sequence.setText(_translate("Dialog", "Add Script Sequence"))
        self.txt_info.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Enter docstring here</span></p></body></html>"))
        self.txt_script_sequence_name.setText(_translate("Dialog", "DefaultName"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

