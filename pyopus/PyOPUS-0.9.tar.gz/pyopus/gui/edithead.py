from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .delegates import QPComboBox
from .table import *
from .editbase import *
from .values import simulators, simulatorTranslator


__all__ = [ 'QPEditHead' ]

settingsHeader = [ 'Name', 'Value' ]

optionsHeader = [ 'Name', 'Value' ]

paramHeader = [ 'Name', 'Value' ]

inputsHeader = [ 'Label', 'File name', 'Section' ]


# Model of the head structure excluding data in tables
class QPHeadModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 2
	
	def rowCount(self, parent):
		return 1
	
	columnNames=['name', 'simulator']
	
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
				return self.data[1]['simulator']
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col==0 and self.data[0]!=value :
			self.data[0]=value 
		elif col==1 and self.data[1]['simulator']!=value:
			self.data[1]['simulator']=value
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

class QPEditHead(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		settingsModel=QPTableModel(self.data[1]['settings'], settingsHeader, dfl=[], parent=self)
		self.settingsWidget=QPTable(settingsModel, parent=self)
		
		optionsModel=QPTableModel(self.data[1]['options'], optionsHeader, dfl=[], parent=self)
		self.optionsWidget=QPTable(optionsModel, parent=self)
		
		paramModel=QPTableModel(self.data[1]['params'], paramHeader, dfl=[], parent=self)
		self.paramWidget=QPTable(paramModel, parent=self)
		
		inputsModel=QPTableModel(self.data[1]['moddefs'], inputsHeader, dfl=[], parent=self)
		self.inputsWidget=QPTable(inputsModel, parent=self)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.nameBox=QLineEdit(self)
		
		self.simBox=QPComboBox(self)
		for s in simulators:
			self.simBox.addItem(s[0], QVariant(s[1]))
		if self.simBox.findData(self.data[1]['simulator'])<0:
			self.simBox.addItem(simulatorTranslator.toText(self.data[1]['simulator']), QVariant(self.data[1]['simulator']))
			
		# self.simBox.setEditable(True)
		self.simBox.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPHeadModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.nameBox, 0, b"text")
		self.dm.addMapping(self.simBox, 1, b"customData")
		self.dm.toFirst()
		
		# QCheckBox and QPComboBox change trigger QDataWidgetMapper submit() immediately
		self.simBox.currentIndexChanged.connect(self.triggerSubmit)
		
		layout.addWidget(QLabel("Simulator setup name", self))
		layout.addWidget(self.nameBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Simulator", self))
		layout.addWidget(self.simBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Simulator settings", self))
		layout.addWidget(self.settingsWidget)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Simulation options", self))
		layout.addWidget(self.optionsWidget)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Parameters", self))
		layout.addWidget(self.paramWidget)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Input modules", self))
		layout.addWidget(self.inputsWidget)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		self.registerModelView(settingsModel, self.settingsWidget)
		self.registerModelView(optionsModel, self.optionsWidget)
		self.registerModelView(paramModel, self.paramWidget)
		self.registerModelView(inputsModel, self.inputsWidget)
		
		# Handle dataChanged() signal from the model to notify parent about name change 
		self.model.dataChanged.connect(self.onDataChanged)
	
	@pyqtSlot(int)
	def triggerSubmit(self, i):
		self.dm.submit()
	
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def onDataChanged(self, topLeft, bottomRight, roles):
		# Change in head name
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
	sa.setWindowTitle("Head editor demo")
	sa.setWidgetResizable(True)
	
	# Add widget
	win=QPEditHead(sampledata.data['heads'][0])
	sa.setWidget(win)
	
	# Show and run
	sa.show()
	app.exec_()
	
	# Print data
	pprint(sampledata.data)
	
	

