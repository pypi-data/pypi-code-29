from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .delegates import QPComboBox
from .table import *
from .editbase import *
from . import values

__all__ = [ 'QPEditPostAxes' ]


# Model of the head structure excluding data in tables
class QPAxesModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 16
	
	def rowCount(self, parent):
		return 1
	
	columnNames=[
		'name', 'title', 'xlabel', 'ylabel', 'type', 
		'xpos', 'ypos', 'xspan', 'yspan', 
		'xlo', 'xhi', 'ylo', 'yhi', 'aspect', 'xgrid', 'ygrid' 
	]
	
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
			elif col>=1 and col<=15:
				return self.data[1][self.columnNames[col]]
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col==0 and self.data[0]!=value :
			self.data[0]=value 
		elif col>=1 and col<=15 and self.data[1][self.columnNames[col]]!=value:
			self.data[1][self.columnNames[col]]=value
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

class QPEditPostAxes(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.nameBox=QLineEdit(self)
		self.titleBox=QLineEdit(self)
		self.xlabelBox=QLineEdit(self)
		self.ylabelBox=QLineEdit(self)
		self.xposBox=QLineEdit(self)
		self.xspanBox=QLineEdit(self)
		self.yposBox=QLineEdit(self)
		self.yspanBox=QLineEdit(self)
		self.xloBox=QLineEdit(self)
		self.xhiBox=QLineEdit(self)
		self.yloBox=QLineEdit(self)
		self.yhiBox=QLineEdit(self)
		
		self.typeBox=QPComboBox(self)
		for s in values.axesTypes:
			self.typeBox.addItem(s[0], QVariant(s[1]))
		if self.typeBox.findData(self.data[1]['type'])<0:
			self.typeBox.addItem(values.axesTypeTranslator.toText(self.data[1]['type']), QVariant(self.data[1]['type']))
		self.typeBox.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		self.typeBox.currentIndexChanged.connect(self.triggerSubmit)
		
		self.aspectCheckbox=QCheckBox(self)
		self.aspectCheckbox.stateChanged.connect(self.triggerSubmit)
		
		self.xgridCheckbox=QCheckBox(self)
		self.xgridCheckbox.stateChanged.connect(self.triggerSubmit)
		
		self.ygridCheckbox=QCheckBox(self)
		self.ygridCheckbox.stateChanged.connect(self.triggerSubmit)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPAxesModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.nameBox, 0, b"text")
		self.dm.addMapping(self.titleBox, 1, b"text")
		self.dm.addMapping(self.xlabelBox, 2, b"text")
		self.dm.addMapping(self.ylabelBox, 3, b"text")
		self.dm.addMapping(self.typeBox, 4, b"customData")
		self.dm.addMapping(self.xposBox, 5, b"text")
		self.dm.addMapping(self.yposBox, 6, b"text")
		self.dm.addMapping(self.xspanBox, 7, b"text")
		self.dm.addMapping(self.yspanBox, 8, b"text")
		self.dm.addMapping(self.xloBox, 9, b"text")
		self.dm.addMapping(self.xhiBox, 10, b"text")
		self.dm.addMapping(self.yloBox, 11, b"text")
		self.dm.addMapping(self.yhiBox, 12, b"text")
		self.dm.addMapping(self.aspectCheckbox, 13)
		self.dm.addMapping(self.xgridCheckbox, 14)
		self.dm.addMapping(self.ygridCheckbox, 15)
		self.dm.toFirst()
		
		layout.addWidget(QLabel("Axes name", self))
		layout.addWidget(self.nameBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Title", self))
		layout.addWidget(self.titleBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("X label", self))
		layout.addWidget(self.xlabelBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Y label", self))
		layout.addWidget(self.ylabelBox)
		layout.addSpacing(2*layout.spacing())
		
		hl=QHBoxLayout()
		layout.addLayout(hl)
		
		hl.addWidget(self.typeBox)
		hl.addSpacing(2*layout.spacing())
		self.aspectCheckbox.setText("Lock 1:1 aspect ratio")
		hl.addWidget(self.aspectCheckbox)
		hl.addStretch(1)
		layout.addSpacing(2*layout.spacing())
		
		hl1=QHBoxLayout()
		layout.addLayout(hl1)
		
		self.xgridCheckbox.setText("Show x grid lines")
		hl1.addWidget(self.xgridCheckbox)
		hl1.addSpacing(2*layout.spacing())
		self.ygridCheckbox.setText("Show y grid lines")
		hl1.addWidget(self.ygridCheckbox)
		hl1.addStretch(1)
		layout.addSpacing(2*layout.spacing())
		
		glayout1=QGridLayout()
		layout.addLayout(glayout1)
		
		glayout1.addWidget(QLabel("Horizontal position", self), 0, 0)
		glayout1.addWidget(self.xposBox, 0, 1)
		glayout1.addWidget(QLabel("Span", self), 0, 2)
		glayout1.addWidget(self.xspanBox, 0, 3)
		glayout1.addWidget(QLabel("Vertical position", self), 1, 0)
		glayout1.addWidget(self.yposBox, 1, 1)
		glayout1.addWidget(QLabel("Span", self), 1, 2)
		glayout1.addWidget(self.yspanBox, 1, 3)
		glayout1.setColumnStretch(4, 1)
		
		layout.addSpacing(2*layout.spacing())
		
		glayout2=QGridLayout()
		layout.addLayout(glayout2)
		
		glayout2.addWidget(QLabel("X lower limit", self), 0, 0)
		glayout2.addWidget(self.xloBox, 0, 1)
		glayout2.addWidget(QLabel("X upper limit", self), 0, 2)
		glayout2.addWidget(self.xhiBox, 0, 3)
		glayout2.addWidget(QLabel("Y lower limit", self), 1, 0)
		glayout2.addWidget(self.yloBox, 1, 1)
		glayout2.addWidget(QLabel("Y upper limit", self), 1, 2)
		glayout2.addWidget(self.yhiBox, 1, 3)
		glayout2.setColumnStretch(4, 1)
		
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
	

	
	

