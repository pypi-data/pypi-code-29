from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .style import styleWidget
from .table import *
from .editbase import *


__all__ = [ 'QPEditVariable' ]

# Model of the head structure excluding data in tables
class QPVariableModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 2
	
	def rowCount(self, parent):
		return 1
	
	columnNames=['name', 'value']
	
	def headerData(self, ii, orientation, role):
		if orientation == Qt.Horizontal and role == Qt.DisplayRole:
			return self.columnNames[ii]
		elif orientation == Qt.Vertical and role == Qt.DisplayRole:
			return ii+1
		return None
	
	def data(self, index, role):
		if not index.isValid():
			return None
		elif role == Qt.DisplayRole or role == Qt.EditRole:
			col=index.column()
			if col==0:
				return self.data[0]
			elif col==1:
				return self.data[1]
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col>=0 and col<=1 and self.data[col]!=value:
			self.data[col]=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

class QPEditVariable(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.nameBox=QLineEdit(self)
		
		self.valueBox=QPlainTextEdit(self)
		styleWidget(self.valueBox, ['monospace'])
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPVariableModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.nameBox, 0, b"text")
		self.dm.addMapping(self.valueBox, 1, b"plainText")
		self.dm.toFirst()
		
		layout.addWidget(QLabel("Variable name", self))
		layout.addWidget(self.nameBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Value", self))
		layout.addWidget(self.valueBox)
		
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		
		# Handle dataChanged() signal from the model to notify parent about name change 
		self.model.dataChanged.connect(self.onDataChanged)
		
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def onDataChanged(self, topLeft, bottomRight, roles):
		# Change in variable name
		if topLeft.column()<=0 and bottomRight.column()>=0:
			self.dataChanged.emit()
		
			
if __name__=='__main__':
	from pprint import pprint
	import sip 
	import sys
	import sampledata
	sip.setdestroyonexit(True)

	app = QApplication(sys.argv)
	
	# Create scroll area
	sa=QScrollArea()
	sa.setWindowTitle("Variable editor demo")
	sa.setWidgetResizable(True)
	
	# Add widget
	win=QPEditVariable(sampledata.data['variables'][0])
	sa.setWidget(win)
	
	# Show and run
	sa.show()
	app.exec_()
	
	# Print data
	pprint(sampledata.data)
	
	

