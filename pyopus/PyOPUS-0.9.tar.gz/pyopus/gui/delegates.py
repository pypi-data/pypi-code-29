from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

__all__ = [ 'QPComboBox', 'QPComboBoxDelegate' ]

# Need to do this so that currentData behaves as a settable property
class QPComboBox(QComboBox):
	def __init__(self, *args, **kwargs):
		QComboBox.__init__(self, *args, **kwargs)
	
	#@pyqtProperty(QVariant)
	#def customData(self):
	#	return QPComboBox.currentData(self)
	
	#@customData.setter
	#def customData(self, userData):
	#	QPComboBox.setCurrentIndex(self, QPComboBox.findData(self, userData))
	
	def getCustomData(self):
		return QPComboBox.currentData(self)
	
	def setCustomData(self, userData):
		QPComboBox.setCurrentIndex(self, QPComboBox.findData(self, userData))
	
	customData=pyqtProperty(QVariant, getCustomData, setCustomData)
	

class QPComboBoxDelegate(QStyledItemDelegate):
	def __init__(self, options, parent=None, *args):
		QStyledItemDelegate.__init__(self, parent=parent, *args)
		self.options=options
	
	def createEditor(self, parent, option, index):
		editor=QPComboBox(parent)
		for item in self.options:
			editor.addItem(item[0], QVariant(item[1]))
		return editor
	
	def setEditorData(self, editor, index):
		value=index.model().data(index, Qt.EditRole)
		editor.customData=value.value()
			
	def setModelData(self, editor, model, index):
		value=editor.customData
		model.setData(index, value, Qt.EditRole)
		
	def updateEditorGeometry(self, editor, option, index):
		editor.setGeometry(option.rect)
