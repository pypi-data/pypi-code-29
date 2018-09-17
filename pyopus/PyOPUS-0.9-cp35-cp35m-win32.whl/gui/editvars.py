from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .editgroup import *
from .table import *
from .values import blankVariable

__all__ = [ 'QPEditVariables' ]


class QPVariablesTableModel(QPGroupTableModel):
	def __init__(self, treePath, parent=None, *args):
		QPGroupTableModel.__init__(
			self, treePath, 
			header=[ "Variable name", "Value"], 
			editable=[ treePath.canRenameChildren(), True ], 
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
	
	
class QPEditVariables(QPEditGroup):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditGroup.__init__(self, QPVariablesTableModel, treePath, logger, parent=parent, *args)
		
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
		layout.addWidget(QLabel("Predefined variables", self))
		layout.addWidget(self.tab)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.tab)
	
	