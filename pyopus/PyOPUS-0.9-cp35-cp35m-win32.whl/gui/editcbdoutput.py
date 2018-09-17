from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .delegates import QPComboBox
from .table import *
from .editbase import *
from .values import cbdSaveWaveforms

__all__ = [ 'QPEditCBDOutput' ]


# Model of the head structure excluding data in tables
class QPCBDOutputModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 8
	
	def rowCount(self, parent):
		return 1
	
	columnNames=[
		'simulatordebug', 'evaluatordebug', 'aggregatordebug', 
		'optimizerdebug', 'taskdebug', 'keepfiles', 'saveallresults', 'savewaveforms', 
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
			if col>=0 and col<=7:
				return self.data[self.columnNames[col]]
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col>=0 and col<=7 and self.data[self.columnNames[col]]!=value:
			self.data[self.columnNames[col]]=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


class QPEditCBDOutput(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		self.debugSimBox=QLineEdit(self)
		self.debugEvalBox=QLineEdit(self)
		self.debugAggBox=QLineEdit(self)
		self.debugOptBox=QLineEdit(self)
		self.debugTaskBox=QLineEdit(self)
		self.keepFilesCheckbox=QCheckBox(self)
		self.saveAllCheckbox=QCheckBox(self)
		
		self.saveWaveformsBox=QPComboBox(self)
		for s in cbdSaveWaveforms:
			self.saveWaveformsBox.addItem(s[0], QVariant(s[1]))
			
		self.saveWaveformsBox.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPCBDOutputModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.debugSimBox, 0, b"text")
		self.dm.addMapping(self.debugEvalBox, 1, b"text")
		self.dm.addMapping(self.debugAggBox, 2, b"text")
		self.dm.addMapping(self.debugOptBox, 3, b"text")
		self.dm.addMapping(self.debugTaskBox, 4, b"text")
		self.dm.addMapping(self.keepFilesCheckbox, 5)
		self.dm.addMapping(self.saveAllCheckbox, 6)
		self.dm.addMapping(self.saveWaveformsBox, 7, b"customData")
		self.dm.toFirst()
		
		# QCheckBox and QPComboBox change trigger QDataWidgetMapper submit() immediately
		self.saveWaveformsBox.currentIndexChanged.connect(self.triggerSubmit)
		self.keepFilesCheckbox.stateChanged.connect(self.triggerSubmit)
		self.saveAllCheckbox.stateChanged.connect(self.triggerSubmit)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		layout.addWidget(QLabel("Simulator debug level (overrides setting in simulator setup)", self))
		layout.addWidget(self.debugSimBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Evaluator debug level (overrides evaluator settings)", self))
		layout.addWidget(self.debugEvalBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Aggregator debug level (overrides aggregator settings)", self))
		layout.addWidget(self.debugAggBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Optimizer debug level (overrides optimizer setting)", self))
		layout.addWidget(self.debugOptBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Task debug level", self))
		layout.addWidget(self.debugTaskBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(self.keepFilesCheckbox, 0)
		self.keepFilesCheckbox.setText("Keep intermediate files on disk")
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(self.saveAllCheckbox, 0)
		self.saveAllCheckbox.setText("Save results for all evaluated circuits")
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Save waveforms", self))
		layout.addWidget(self.saveWaveformsBox)
		layout.addSpacing(2*layout.spacing())
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
	
	@pyqtSlot(int)
	def triggerSubmit(self, i):
		self.dm.submit()
	
