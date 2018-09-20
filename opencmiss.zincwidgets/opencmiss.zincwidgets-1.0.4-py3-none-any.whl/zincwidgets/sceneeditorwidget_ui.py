# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sceneeditorwidget.ui'
#
# Created: Thu May 14 11:53:32 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SceneEditorWidget(object):
    def setupUi(self, SceneEditorWidget):
        SceneEditorWidget.setObjectName("SceneEditorWidget")
        SceneEditorWidget.resize(227, 736)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SceneEditorWidget.sizePolicy().hasHeightForWidth())
        SceneEditorWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(SceneEditorWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphics_listview = QtGui.QListView(SceneEditorWidget)
        self.graphics_listview.setObjectName("graphics_listview")
        self.verticalLayout.addWidget(self.graphics_listview)
        self.frame = QtGui.QFrame(SceneEditorWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 7, 0, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_graphics_combobox = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_graphics_combobox.sizePolicy().hasHeightForWidth())
        self.add_graphics_combobox.setSizePolicy(sizePolicy)
        self.add_graphics_combobox.setObjectName("add_graphics_combobox")
        self.add_graphics_combobox.addItem("")
        self.add_graphics_combobox.addItem("")
        self.add_graphics_combobox.addItem("")
        self.add_graphics_combobox.addItem("")
        self.add_graphics_combobox.addItem("")
        self.add_graphics_combobox.addItem("")
        self.add_graphics_combobox.addItem("")
        self.add_graphics_combobox.addItem("")
        self.add_graphics_combobox.addItem("")
        self.add_graphics_combobox.addItem("")
        self.horizontalLayout.addWidget(self.add_graphics_combobox)
        self.delete_graphics_button = QtGui.QPushButton(self.frame)
        self.delete_graphics_button.setObjectName("delete_graphics_button")
        self.horizontalLayout.addWidget(self.delete_graphics_button)
        self.verticalLayout.addWidget(self.frame)
        self.graphics_editor = GraphicsEditorWidget(SceneEditorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphics_editor.sizePolicy().hasHeightForWidth())
        self.graphics_editor.setSizePolicy(sizePolicy)
        self.graphics_editor.setObjectName("graphics_editor")
        self.verticalLayout.addWidget(self.graphics_editor)

        self.retranslateUi(SceneEditorWidget)
        QtCore.QObject.connect(self.graphics_listview, QtCore.SIGNAL("clicked(QModelIndex)"), SceneEditorWidget.graphicsListItemClicked)
        QtCore.QObject.connect(self.add_graphics_combobox, QtCore.SIGNAL("currentIndexChanged(QString)"), SceneEditorWidget.addGraphicsEntered)
        QtCore.QObject.connect(self.delete_graphics_button, QtCore.SIGNAL("clicked()"), SceneEditorWidget.deleteGraphicsClicked)
        QtCore.QMetaObject.connectSlotsByName(SceneEditorWidget)

    def retranslateUi(self, SceneEditorWidget):
        SceneEditorWidget.setWindowTitle(QtGui.QApplication.translate("SceneEditorWidget", "Scene Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(0, QtGui.QApplication.translate("SceneEditorWidget", "Add...", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(1, QtGui.QApplication.translate("SceneEditorWidget", "---", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(2, QtGui.QApplication.translate("SceneEditorWidget", "point", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(3, QtGui.QApplication.translate("SceneEditorWidget", "node points", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(4, QtGui.QApplication.translate("SceneEditorWidget", "data points", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(5, QtGui.QApplication.translate("SceneEditorWidget", "element points", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(6, QtGui.QApplication.translate("SceneEditorWidget", "lines", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(7, QtGui.QApplication.translate("SceneEditorWidget", "surfaces", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(8, QtGui.QApplication.translate("SceneEditorWidget", "contours", None, QtGui.QApplication.UnicodeUTF8))
        self.add_graphics_combobox.setItemText(9, QtGui.QApplication.translate("SceneEditorWidget", "streamlines", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_graphics_button.setText(QtGui.QApplication.translate("SceneEditorWidget", "Delete", None, QtGui.QApplication.UnicodeUTF8))

from .graphicseditorwidget import GraphicsEditorWidget
