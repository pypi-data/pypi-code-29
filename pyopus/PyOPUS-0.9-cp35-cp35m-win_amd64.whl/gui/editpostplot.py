from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .delegates import QPComboBox
from .table import *
from .editbase import *


__all__ = [ 'QPEditPostPlot' ]


# Model of the head structure excluding data in tables
class QPPlotModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 2
	
	def rowCount(self, parent):
		return 1
	
	columnNames=['name', 'title']
	
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
				return self.data[1]['title']
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col==0 and self.data[0]!=value :
			self.data[0]=value 
		elif col==1 and self.data[1]['title']!=value:
			self.data[1]['title']=value
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

class QPEditPostPlot(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.nameBox=QLineEdit(self)
		self.titleBox=QLineEdit(self)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPPlotModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.nameBox, 0, b"text")
		self.dm.addMapping(self.titleBox, 1, b"text")
		self.dm.toFirst()
		
		layout.addWidget(QLabel("Plot name", self))
		layout.addWidget(self.nameBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Title", self))
		layout.addWidget(self.titleBox)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		
		# Handle dataChanged() signal from the model to notify parent about name change 
		self.model.dataChanged.connect(self.onDataChanged)
	
	# For combo boxes and checkboxes, should be triggered on change
	@pyqtSlot(int)
	def triggerSubmit(self, i):
		self.dm.submit()
	
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def onDataChanged(self, topLeft, bottomRight, roles):
		# Change in head name
		if topLeft.column()<=0 and bottomRight.column()>=0:
			self.dataChanged.emit()
	

	
	

