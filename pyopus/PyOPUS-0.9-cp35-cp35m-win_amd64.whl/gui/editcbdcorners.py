from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .editgroup import *
from .table import *
from .values import blankCorner
from .wizgencorners import *

__all__ = [ 'QPEditCBDCorners' ]


class QPCornersTableModel(QPGroupTableModel):
	def __init__(self, treePath, parent=None, *args):
		QPGroupTableModel.__init__(
			self, treePath, 
			header=[ "Name", "Setups", "Modules", "Parameters" ], #, "Modules", "Parameters"], 
			editable=[treePath.canRenameChildren(), False, False, False], 
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
				return QVariant(
					", ".join(
						[m[0] for m in self.mylist[row][1]["heads"]]
					)
				)
			elif col==2:
				return QVariant(
					", ".join(
						[m[0] for m in self.mylist[row][1]["modules"]]
					)
				)
			elif col==3:
				return QVariant(
					", ".join(
						[p[0]+"="+str(p[1]) for p in self.mylist[row][1]["params"]]
					)
				)
			else:
				return None
		else:
			return None
	
	def setData(self, index, value, role):
		row=index.row()
		col=index.column()
		if col==0 and self.mylist[row][0]!=value:
			self.mylist[row][0]=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
	
	
class QPEditCBDCorners(QPEditGroup):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditGroup.__init__(self, QPCornersTableModel, treePath, logger, parent=parent, *args)
		
		self.genButton=QPushButton("Generate corners")
		
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
		hl=QHBoxLayout()
		hl.addWidget(self.genButton)
		hl.addStretch(1)
		layout.addLayout(hl)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Corners", self))
		layout.addWidget(self.tab)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		self.genButton.clicked.connect(self.generateCorners)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.tab)
		
	@pyqtSlot(bool)
	def generateCorners(self, checked):
		w=QPWizardCorners(self.rootData, self)
		w.setModal(True)
		w.exec_()
		
		corners = w.output()
		if corners is not None:
			#n=self.model.rowCount()
			#for ii in range(len(corners)):
			#	c=corners[ii]
			#	self.tab.addAfter(True)
			#	for jj in range(len(c)):
			#		self.model.setData(QModelIndex() n+ii,jj
			self.tab.extendData(corners)
					
