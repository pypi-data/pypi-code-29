from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .delegates import QPComboBox
from .table import *
from .editbase import *
from .values import optimizers

__all__ = [ 'QPEditCBDSettings' ]

settingsHeader = [ 'Name', 'Value' ]

paramsHeader = [ 'Name', 'Value' ]

modulesHeader = [ 'Label' ]

# Model of the head structure excluding data in tables
class QPCBDSettingsModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return len(self.columnNames)
	
	def rowCount(self, parent):
		return 1
	
	columnNames=[
		'failurepenalty', 'stopsatisfied', 'tradeoffmultiplier', 'method', 
		'maxiter', 'stoptol', 'initialstep', 'forwardsolution', 'relevantcorners',
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
			return self.data[self.columnNames[col]]
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		
		if self.data[self.columnNames[col]]!=value: 
			self.data[self.columnNames[col]]=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


class QPEditCBDSettings(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		self.evSettingsModel=QPTableModel(self.data['evaluatorsettings'], settingsHeader, dfl=[], parent=self)
		self.evSettingsWidget=QPTable(self.evSettingsModel, parent=self)
		
		self.agSettingsModel=QPTableModel(self.data['aggregatorsettings'], settingsHeader, dfl=[], parent=self)
		self.agSettingsWidget=QPTable(self.agSettingsModel, parent=self)
		
		self.optSettingsModel=QPTableModel(self.data['optimizersettings'], settingsHeader, dfl=[], parent=self)
		self.optSettingsWidget=QPTable(self.optSettingsModel, parent=self)
		
		self.failPenaltyBox=QLineEdit(self)
		self.stopSatisfiedCheckbox=QCheckBox(self)
		self.tradeoffMulBox=QLineEdit(self)
		
		self.forwardSolutionCheckbox=QCheckBox(self)
		self.relevantCornersCheckbox=QCheckBox(self)
		
		self.optBox=QPComboBox(self)
		for s in optimizers:
			self.optBox.addItem(s[0], QVariant(s[1]))
			
		# self.simBox.setEditable(True)
		self.optBox.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		
		self.initialStepBox=QLineEdit(self)
		self.maxiterBox=QLineEdit(self)
		self.tolBox=QLineEdit(self)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPCBDSettingsModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.failPenaltyBox, 0, b"text")
		self.dm.addMapping(self.stopSatisfiedCheckbox, 1)
		self.dm.addMapping(self.tradeoffMulBox, 2, b"text")
		self.dm.addMapping(self.optBox, 3, b"customData")
		self.dm.addMapping(self.maxiterBox, 4, b"text")
		self.dm.addMapping(self.tolBox, 5, b"text")
		self.dm.addMapping(self.initialStepBox, 6, b"text")
		self.dm.addMapping(self.forwardSolutionCheckbox, 7)
		self.dm.addMapping(self.relevantCornersCheckbox, 8)
		self.dm.toFirst()
		
		# QCheckBox and QPComboBox change trigger QDataWidgetMapper submit() immediately
		self.optBox.currentIndexChanged.connect(self.triggerSubmit)
		self.stopSatisfiedCheckbox.stateChanged.connect(self.triggerSubmit)
		self.forwardSolutionCheckbox.stateChanged.connect(self.triggerSubmit)
		self.relevantCornersCheckbox.stateChanged.connect(self.triggerSubmit)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		layout.addWidget(QLabel("Penalty for failed measure", self))
		layout.addWidget(self.failPenaltyBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(self.stopSatisfiedCheckbox, 0)
		self.stopSatisfiedCheckbox.setText("Stop when all requirements are satisfied")
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Tradeoff weight multiplier", self))
		layout.addWidget(self.tradeoffMulBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Optimization method", self))
		layout.addWidget(self.optBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Upper limit for the number of evaluated candidate circuits per pass", self))
		layout.addWidget(self.maxiterBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Initial step (relative to bounds) for local optimizers", self))
		layout.addWidget(self.initialStepBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Stop when step is smaller than", self))
		layout.addWidget(self.tolBox)
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(self.forwardSolutionCheckbox, 0)
		self.forwardSolutionCheckbox.setText("Use solution from previous pass as initial point")
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(self.relevantCornersCheckbox, 0)
		self.relevantCornersCheckbox.setText("Use only relevant corners in optimization")
		layout.addSpacing(2*layout.spacing())
		
		layout.addWidget(QLabel("Evaluator settings", self))
		layout.addWidget(self.evSettingsWidget)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Aggregator settings", self))
		layout.addWidget(self.agSettingsWidget)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Optimizer settings", self))
		layout.addWidget(self.optSettingsWidget)
		layout.addSpacing(2*layout.spacing())
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		self.registerModelView(self.evSettingsModel, self.evSettingsWidget)
		self.registerModelView(self.agSettingsModel, self.agSettingsWidget)
		self.registerModelView(self.optSettingsModel, self.optSettingsWidget)
	
	@pyqtSlot(int)
	def triggerSubmit(self, i):
		self.dm.submit()
	