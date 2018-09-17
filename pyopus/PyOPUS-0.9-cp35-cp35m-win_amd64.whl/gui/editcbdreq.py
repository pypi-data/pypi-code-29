from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .table import *
from .editbase import *


__all__ = [ 'QPEditCBDRequirements' ]

header = [ '', 'Name', 'Above', 'Below', 'Norm', 'Tradeoff Weight' ]

dfl = [ True, '', '', '', '', '' ]

class QPCBDRequirementsModel(QPTableModel):
	def __init__(self, data, parent=None, *args):
		QPTableModel.__init__(
			self, data, 
			header=header, 
			dfl=dfl, 
			sortingIndices=[], 
			parent=None, *args
		)
		
	def data(self, index, role):
		if not index.isValid():
			return None
		
		row=index.row()
		col=index.column()
			
		if role == Qt.DisplayRole or role == Qt.EditRole:
			if col==0 and role == Qt.EditRole:
				return QVariant(self.mylist[row][col])
			elif col>0 and col<len(header):
				return QVariant(self.mylist[row][col])
			else:
				return None
		elif role == Qt.CheckStateRole:
			if col==0:
				return Qt.Checked if self.mylist[row][0] is True else Qt.Unchecked
			else:
				return None
		else:
			return None
	
	def setData(self, index, value, role):
		row=index.row()
		col=index.column()
		if role==Qt.CheckStateRole:
			storeval=True if value==Qt.Checked else False
			if col==0 and self.mylist[row][0]!=storeval:
				self.mylist[row][0]=storeval
				self.dataChanged.emit(index, index)
			else:
				return False
		else:
			if col>=0 and col<len(header) and self.mylist[row][col]!=value:
				self.mylist[row][col]=value 
			else:
				return False
		
		self.dataChanged.emit(index, index)
		return True
	
	def flags(self, index):
		col=index.column()
		f=QPTableModel.flags(self, index)
		if col==0:
			f|=Qt.ItemIsUserCheckable
		return f
	
class QPEditCBDRequirements(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		self.model=QPCBDRequirementsModel(self.data, parent=self)
		self.table=QPTable(self.model, parent=self)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		layout.addWidget(QLabel("Design requirements", self))
		layout.addWidget(QLabel("Checked requirements are subject to optimization.", self))
		layout.addWidget(QLabel("Unchecked requirements are monitored if Above or Below is specified.", self))
		layout.addWidget(self.table)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.table)
		
