from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .table import *
from .editbase import *


__all__ = [ 'QPEditCBDCorner' ]

headsHeader = [ 'Name' ]

paramsHeader = [ 'Name', 'Value' ]

modulesHeader = [ 'Label' ]


# Model of the head structure excluding data in tables
class QPCBDCornerModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 1
	
	def rowCount(self, parent):
		return 1
	
	columnNames=['name']
	
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
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col==0 and self.data[0]!=value:
			self.data[0]=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


class QPEditCBDCorner(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		
		self.hmodel=QPTableModel(self.data[1]['heads'], headsHeader, dfl=[], parent=self)
		self.htable=QPTable(self.hmodel, parent=self)
		
		self.mmodel=QPTableModel(self.data[1]['modules'], modulesHeader, dfl=[], parent=self)
		self.mtable=QPTable(self.mmodel, parent=self)
		
		self.pmodel=QPTableModel(self.data[1]['params'], paramsHeader, dfl=[], parent=self)
		self.ptable=QPTable(self.pmodel, parent=self)
		
		self.nameBox=QLineEdit(self)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPCBDCornerModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.nameBox, 0, b"text")
		self.dm.toFirst()
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		layout.addWidget(QLabel("Corner name", self))
		layout.addWidget(self.nameBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Simulator setups", self))
		layout.addWidget(self.htable)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Input modules", self))
		layout.addWidget(self.mtable)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Parameters", self))
		layout.addWidget(self.ptable)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		self.registerModelView(self.hmodel, self.htable)
		self.registerModelView(self.mmodel, self.mtable)
		self.registerModelView(self.pmodel, self.ptable)
		