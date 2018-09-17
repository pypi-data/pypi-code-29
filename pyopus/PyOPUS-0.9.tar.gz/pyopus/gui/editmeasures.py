from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .editgroup import *
from .table import *
from .values import blankMeasure

__all__ = [ 'QPEditMeasures' ]


class QPMeasuresTableModel(QPGroupTableModel):
	def __init__(self, treePath, parent=None, *args):
		QPGroupTableModel.__init__(
			self, treePath, 
			header=[ "Measure name", "Analysis", "Above", "Below", "Norm"], 
			editable=[ treePath.canRenameChildren(), True, True, True, True ], 
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
				return QVariant(self.mylist[row][1]["analysis"])
			elif col==2:
				return QVariant(self.mylist[row][1]["lower"])
			elif col==3:
				return QVariant(self.mylist[row][1]["upper"])
			elif col==4:
				return QVariant(self.mylist[row][1]["norm"])
			else:
				return None
		else:
			return None
	
	def setData(self, index, value, role):
		row=index.row()
		col=index.column()
		if col==0 and self.mylist[row][0]!=value:
			self.mylist[row][0]=value 
		elif col==1 and self.mylist[row][1]["analysis"]!=value:
			self.mylist[row][1]["analysis"]=value
		elif col==2 and self.mylist[row][1]["lower"]!=value:
			self.mylist[row][1]["lower"]=value
		elif col==3 and self.mylist[row][1]["upper"]!=value:
			self.mylist[row][1]["upper"]=value
		elif col==4 and self.mylist[row][1]["norm"]!=value:
			self.mylist[row][1]["norm"]=value
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
	
	
class QPEditMeasures(QPEditGroup):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditGroup.__init__(self, QPMeasuresTableModel, treePath, logger, parent=parent, *args)
		
		layout = QVBoxLayout(self)
		
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.tab=QPGroupTable(
			self.model, 
			canDelete=treePath.canDeleteChildren(), 
			canCreate=treePath.canCreateChildren(), 
			canMove=treePath.canMoveChildren(),
			buttons=False, 
			parent=self
		)
		layout.addWidget(QLabel("Measures", self))
		layout.addWidget(self.tab)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.tab)
	
