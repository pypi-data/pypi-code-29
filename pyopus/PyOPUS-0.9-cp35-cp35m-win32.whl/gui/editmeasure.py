from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .style import enableWidget, styleWidget
from .delegates import QPComboBox
from .table import *
from .editbase import *
from .delegates import QPComboBoxDelegate
from .values import blankSave, blankDepends

__all__ = [ 'QPEditMeasure' ]

dependsHeader=[ 'Name' ]

	
# Model of the head structure excluding data in tables
class QPMeasureModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 8
	
	def rowCount(self, parent):
		return 1
	
	columnNames=['name', 'analysis', 'vector', 'components', 'expression', 'lower', 'upper', 'norm']
	
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
				return self.data[1]['analysis']
			elif col==2:
				return self.data[1]['vector']
			elif col==3:
				return self.data[1]['components']
			elif col==4:
				return self.data[1]['expression']
			elif col==5:
				return self.data[1]['lower']
			elif col==6:
				return self.data[1]['upper']
			elif col==7:
				return self.data[1]['norm']
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col==0 and self.data[0]!=value:
			self.data[0]=value 
		elif col==1 and self.data[1]['analysis']!=value:
			self.data[1]['analysis']=value 
		elif col==2 and self.data[1]['vector']!=value:
			self.data[1]['vector']=value 
		elif col==3 and self.data[1]['components']!=value:
			self.data[1]['components']=value 
		elif col==4 and self.data[1]['expression']!=value:
			self.data[1]['expression']=value
		elif col==5 and self.data[1]['lower']!=value:
			self.data[1]['lower']=value 
		elif col==6 and self.data[1]['upper']!=value:
			self.data[1]['upper']=value 
		elif col==7 and self.data[1]['norm']!=value:
			self.data[1]['norm']=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


class QPEditMeasure(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.dependsModel=QPTableModel(self.data[1]['depends'], dependsHeader, dfl=blankDepends, parent=self)
		self.dependsWidget=QPTable(self.dependsModel, parent=self)
		
		self.nameBox=QLineEdit(self)
		
		self.lowerBox=QLineEdit(self)
		self.upperBox=QLineEdit(self)
		self.normBox=QLineEdit(self)
		
		self.analysisBox=QLineEdit(self)
		
		self.vecnamesBox=QPlainTextEdit(self)
		styleWidget(self.vecnamesBox, ['monospace'])
		
		self.expressionBox=QPlainTextEdit(self)
		styleWidget(self.expressionBox, ['monospace'])
		
		self.vectorCheckbox=QCheckBox(self)
			
		# Enable/disable widgets
		self.analysisBox.textChanged.connect(self.onSimulatorChanged)
		self.vectorCheckbox.stateChanged.connect(self.onTypeChanged)
		
		self.onSimulatorChanged(self.analysisBox.text())
		self.onTypeChanged(self.vectorCheckbox.checkState())
				
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPMeasureModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.nameBox, 0, b"text")
		self.dm.addMapping(self.analysisBox, 1, b"text")
		self.dm.addMapping(self.vectorCheckbox, 2)
		self.dm.addMapping(self.vecnamesBox, 3, b"plainText")
		self.dm.addMapping(self.expressionBox, 4, b"plainText")
		self.dm.addMapping(self.lowerBox, 5, b"text")
		self.dm.addMapping(self.upperBox, 6, b"text")
		self.dm.addMapping(self.normBox, 7, b"text")
		self.dm.toFirst()
		
		# QCheckBox and QPComboBox change trigger QDataWidgetMapper submit() immediately
		self.vectorCheckbox.stateChanged.connect(self.triggerSubmit)
		
		layout.addWidget(QLabel("Measure name", self))
		layout.addWidget(self.nameBox)
		layout.addSpacing(2*layout.spacing())
		
		hl=QHBoxLayout()
		hl.addWidget(QLabel("Above", self))
		hl.addWidget(self.lowerBox)
		hl.addSpacing(2*layout.spacing())
		hl.addWidget(QLabel("Below", self))
		hl.addWidget(self.upperBox)
		hl.addSpacing(2*layout.spacing())
		hl.addWidget(QLabel("Norm", self))
		hl.addWidget(self.normBox)
		hl.addStretch(1)
		layout.addLayout(hl)
		
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Analysis name", self))
		layout.addWidget(self.analysisBox)
		layout.addSpacing(2*layout.spacing())
		self.vectorCheckbox.setText("Measure returns a vector")
		layout.addWidget(self.vectorCheckbox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Vector component names list", self))
		layout.addWidget(self.vecnamesBox, stretch=1)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Names of measures this expression/script depends on", self))
		layout.addWidget(self.dependsWidget)
		
		# layout.addWidget(self.dependsBox, stretch=0)
		
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Measure definition expression/script", self))
		layout.addWidget(self.expressionBox, stretch=3)
		
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		self.registerModelView(self.dependsModel, self.dependsWidget)
		
		# Handle dataChanged() signal from the model to notify parent about name change 
		self.model.dataChanged.connect(self.onDataChanged)
	
	@pyqtSlot(int)
	def triggerSubmit(self, i):
		self.dm.submit()
	
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def onDataChanged(self, topLeft, bottomRight, roles):
		# Change in measure name
		if topLeft.column()<=0 and bottomRight.column()>=0:
			self.dataChanged.emit()
	
	@pyqtSlot(str)
	def onSimulatorChanged(self, txt):
		enableWidget(self.dependsWidget, len(txt)==0)
		
	@pyqtSlot(int)
	def onTypeChanged(self, newVal):
		enableWidget(self.vecnamesBox, newVal==Qt.Checked, ['monospace'])
		
			
if __name__=='__main__':
	from pprint import pprint
	import sip 
	import sys
	import sampledata
	sip.setdestroyonexit(True)

	app = QApplication(sys.argv)
	
	# Create scroll area
	sa=QScrollArea()
	sa.setWindowTitle("Measure editor demo")
	sa.setWidgetResizable(True)
	
	# Add widget
	win=QPEditMeasure(sampledata.data['measures'][0])
	sa.setWidget(win)
	
	# Show and run
	sa.show()
	app.exec_()
	
	# Print data
	pprint(sampledata.data)
	
	


