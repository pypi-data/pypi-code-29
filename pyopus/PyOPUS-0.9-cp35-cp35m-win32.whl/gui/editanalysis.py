from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .delegates import QPComboBox
from .table import *
from .editbase import *
from .delegates import QPComboBoxDelegate
from .values import saveTypes, saveTypeTranslator, blankSave

__all__ = [ 'QPEditAnalysis' ]

optionsHeader = [ 'Name', 'Value' ]

modulesHeader = [ 'Label' ]

paramHeader = [ 'Name', 'Value' ]

# Override 
class QPSavesTableModel(QPTableModel):
	def __init__(self, data, parent=None, *args):
		QPTableModel.__init__(
			self, data, 
			header=[ 'Type', 'Nodes/Devices/Devices;Properties/Expression' ], 
			dfl=blankSave, 
			sortingIndices=[], 
			parent=None, *args
		)
	
	# For display role the text is used, but otherwise codes are stored
	# Need to override these two because we are accessing stuff deeper in the data structure
	def data(self, index, role):
		if not index.isValid():
			return None
		elif role == Qt.DisplayRole or role == Qt.EditRole:
			row=index.row()
			col=index.column()
			if col==0:
				if role == Qt.DisplayRole:
					return QVariant(saveTypeTranslator.toText(self.mylist[row][col]))
				else:
					return QVariant(self.mylist[row][col])
			elif col==1:
				return QVariant(self.mylist[row][col])
			else:
				return None
		else:
			return None
	
	def setData(self, index, value, role):
		row=index.row()
		col=index.column()
		if col>=0 and col<=1 and self.mylist[row][col]!=value:
			self.mylist[row][col]=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
	
	
# Model of the head structure excluding data in tables
class QPAnalysisModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 3
	
	def rowCount(self, parent):
		return 1
	
	columnNames=['name', 'head', 'command']
	
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
				return self.data[1]['head']
			elif col==2:
				return self.data[1]['command']
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col==0 and self.data[0]!=value:
			self.data[0]=value 
		elif col==1 and self.data[1]['head']!=value :
			self.data[1]['head']=value 
		elif col==2 and self.data[1]['command']!=value :
			self.data[1]['command']=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

class QPEditAnalysis(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		optionsModel=QPTableModel(self.data[1]['options'], optionsHeader, dfl=[], parent=self)
		self.optionsWidget=QPTable(optionsModel, parent=self)
		
		modulesModel=QPTableModel(self.data[1]['modules'], modulesHeader, dfl=[], parent=self)
		self.modulesWidget=QPTable(modulesModel, parent=self)
		
		paramModel=QPTableModel(self.data[1]['params'], paramHeader, dfl=[], parent=self)
		self.paramWidget=QPTable(paramModel, parent=self)
		
		savesModel=QPSavesTableModel(self.data[1]['saves'], parent=self)
		self.savesWidget=QPTable(savesModel, parent=self)
		self.savesWidget.setItemDelegateForColumn(
			0, QPComboBoxDelegate(options=saveTypes, parent=self)
		)
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.nameBox=QLineEdit(self)
		
		self.headBox=QLineEdit(self)
		
		self.commandBox=QLineEdit(self)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPAnalysisModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.nameBox, 0, b"text")
		self.dm.addMapping(self.headBox, 1, b"text")
		self.dm.addMapping(self.commandBox, 2, b"text")
		self.dm.toFirst()
		
		layout.addWidget(QLabel("Analysis name", self))
		layout.addWidget(self.nameBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Simulator setup", self))
		layout.addWidget(self.headBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Simulator options", self))
		layout.addWidget(self.optionsWidget)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Input file modules", self))
		layout.addWidget(self.modulesWidget)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Parameters", self))
		layout.addWidget(self.paramWidget)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Simulator output directives", self))
		layout.addWidget(self.savesWidget)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Command", self))
		layout.addWidget(self.commandBox)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		self.registerModelView(optionsModel, self.optionsWidget)
		self.registerModelView(modulesModel, self.modulesWidget)
		self.registerModelView(paramModel, self.paramWidget)
		self.registerModelView(savesModel, self.savesWidget)
		
		# Handle dataChanged() signal from the model to notify parent about name change 
		self.model.dataChanged.connect(self.onDataChanged)
	
	
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def onDataChanged(self, topLeft, bottomRight, roles):
		# Change in analysis name
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
	sa.setWindowTitle("Analysis editor demo")
	sa.setWidgetResizable(True)
	
	# Add widget
	win=QPEditAnalysis(sampledata.data['analyses'][0])
	sa.setWidget(win)
	
	# Show and run
	sa.show()
	app.exec_()
	
	# Print data
	pprint(sampledata.data)
	
	

