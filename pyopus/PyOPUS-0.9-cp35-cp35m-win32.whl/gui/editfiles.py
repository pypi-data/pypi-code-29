from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .fstools import fileInfo
from .editgroup import *
from .table import *
from .values import blankFile

__all__ = [ 'QPEditFiles' ]


class QPFilesTableModel(QPGroupTableModel):
	def __init__(self, treePath, parent=None, *args):
		QPGroupTableModel.__init__(
			self, treePath, 
			header=[ "Name", "External", "" ], 
			editable=[ treePath.canRenameChildren(), True, False ], 
			dfl=treePath.childTemplate(), 
			sortingIndices=[], 
			parent=None, *args
		)
		
	def data(self, index, role):
		if not index.isValid():
			return None
		
		row=index.row()
		col=index.column()
			
		if role == Qt.DisplayRole or role == Qt.EditRole:
			if col==0:
				return QVariant(self.mylist[row][0])
			if col==2:
				if self.mylist[row][1]['external']:
					info=fileInfo(self.mylist[row][0])
					txt=''
					if info['type']==None:
						txt+='not found'
					else:
						if info['symlink']:
							txt+='link to '
						if info['type']=='dir':
							txt+='folder'
						else:
							txt+='file'
					return QVariant(txt)
				else:
					return QVariant('')
			else:
				return None
		elif role == Qt.CheckStateRole:
			if col==1:
				return Qt.Checked if self.mylist[row][1]['external'] is True else Qt.Unchecked
			else:
				return None
		else:
			return None
	
	def setData(self, index, value, role):
		row=index.row()
		col=index.column()
		if role==Qt.CheckStateRole:
			setval=True if value==Qt.Checked else False
			if col==1 and self.mylist[row][1]["external"]!=setval:
				self.mylist[row][1]["external"]=setval
			else:
				return False
		else:
			if col==0 and self.mylist[row][0]!=value:
				self.mylist[row][0]=value 
			else:
				return False
		
		# Refresh whole row if columns 0 or 1 are changed
		self.dataChanged.emit(self.index(row, 0, QModelIndex()), self.index(row, self.columnCount()-1, QModelIndex()))
		
		return True
	
	def flags(self, index):
		col=index.column()
		f=QPTableModel.flags(self, index)
		if col==1:
			f|=Qt.ItemIsUserCheckable
		return f
	
	
class QPEditFiles(QPEditGroup):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditGroup.__init__(self, QPFilesTableModel, treePath, logger, parent=parent, *args)
		
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
		
		layout.addWidget(QLabel("Files and folders", self))
		layout.addWidget(self.tab)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.tab)
	