from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .editgroup import *
from .table import *
from .values import simulators, blankHead, simulatorTranslator
from .delegates import QPComboBoxDelegate

__all__ = [ 'QPEditHeads' ]


class QPHeadsTableModel(QPGroupTableModel):
	def __init__(self, treePath, parent=None, *args):
		QPGroupTableModel.__init__(
			self, treePath, 
			header=[ "Setup name", "Simulator type", "Defined modules" ], 
			editable=[ treePath.canRenameChildren(), True, False ], 
			dfl=treePath.childTemplate(), 
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
				return QVariant(self.mylist[row][0])
			elif col==1:
				if role == Qt.DisplayRole:
					return QVariant(simulatorTranslator.toText(self.mylist[row][col]["simulator"]))
				else:
					return QVariant(self.mylist[row][col]["simulator"])
			elif col==2:
				return QVariant(", ".join([m[0] for m in self.mylist[row][1]["moddefs"]]))
			else:
				return None
		else:
			return None
	
	def setData(self, index, value, role):
		row=index.row()
		col=index.column()
		if col==0 and self.mylist[row][0]!=value:
			self.mylist[row][0]=value 
		elif col==1 and self.mylist[row][col]["simulator"]!=value:
			self.mylist[row][col]["simulator"]=value
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
	
	
class QPEditHeads(QPEditGroup):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditGroup.__init__(self, QPHeadsTableModel, treePath, logger, parent=parent, *args)
		
		layout = QVBoxLayout(self)
		
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.tab=QPGroupTable(
			self.model, 
			canDelete=treePath.canDeleteChildren(), 
			canCreate=treePath.canCreateChildren(), 
			canMove=treePath.canMoveChildren(),
			stretch=[ False, False, True ], 
			buttons=False, 
			parent=self
		)
		# Collect extra simulator types
		options=[entry for entry in simulators]
		simNames=set([entry[1] for entry in simulators])
		for head in self.data:
			if head[1]["simulator"] not in simNames:
				options.append([simulatorTranslator.toText(head[1]["simulator"]), head[1]["simulator"]])
		self.tab.setItemDelegateForColumn(
			1, QPComboBoxDelegate(options=options, parent=self)
		)
		
		layout.addWidget(QLabel("Simulator setups", self))
		layout.addWidget(self.tab)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.tab)
		
