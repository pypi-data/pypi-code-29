from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .style import enableWidget
from .table import *
from .editbase import *

__all__ = [ 'QPEditMPI' ]


# Model of the head structure excluding data in tables
class QPMPIModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 5
	
	def rowCount(self, parent):
		return 1
	
	columnNames=[
		'processors', 'mirror', 'persistent', 'vmdebug', 'cosdebug'
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
			if col>=0 and col<=4:
				return self.data[self.columnNames[col]]
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col>=0 and col<=4 and self.data[self.columnNames[col]]!=value:
			self.data[self.columnNames[col]]=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


class QPEditMPI(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		self.processorsBox=QLineEdit(self)
		self.debugVMBox=QLineEdit(self)
		self.debugCOSBox=QLineEdit(self)
		self.mirrorCheckbox=QCheckBox(self)
		self.persistentCheckbox=QCheckBox(self)
		
		# Disable persistent storage checkbox when mirroring is disabled
		self.mirrorCheckbox.stateChanged.connect(self.onMirrorChanged)
		self.mirrorCheckbox.setCheckState(Qt.Checked)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPMPIModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.processorsBox, 0, b"text")
		self.dm.addMapping(self.mirrorCheckbox, 1)
		self.dm.addMapping(self.persistentCheckbox, 2)
		self.dm.addMapping(self.debugVMBox, 3, b"text")
		self.dm.addMapping(self.debugCOSBox, 4, b"text")
		self.dm.toFirst()
		
		# QCheckBox and QPComboBox change trigger QDataWidgetMapper submit() immediately
		self.mirrorCheckbox.stateChanged.connect(self.triggerSubmit)
		self.persistentCheckbox.stateChanged.connect(self.triggerSubmit)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		layout.addWidget(QLabel("Number of CPUs to allocate (leave empty to allocate all available CPUs)", self))
		layout.addWidget(self.processorsBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(self.mirrorCheckbox, 0)
		self.mirrorCheckbox.setText("Mirror files to local storage on hosts")
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(self.persistentCheckbox, 0)
		self.persistentCheckbox.setText("Persistent storage of mirrored data")
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("MPI debug level", self))
		layout.addWidget(self.debugVMBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Cooperative multitasking manager debug level", self))
		layout.addWidget(self.debugCOSBox)
		layout.addSpacing(2*layout.spacing())
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		
		# Take care of disabling widgets that need to be disabled
		self.onMirrorChanged
	
	@pyqtSlot(int)
	def onMirrorChanged(self, newVal):
		enableWidget(self.persistentCheckbox, newVal)
	
	@pyqtSlot(int)
	def triggerSubmit(self, i):
		self.dm.submit()
	
