from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .table import *
from .widgets import *
from ..design.sqlite import *
from . import resources
from .style import styleWidget
from .resbase import *

import datetime

from .indicators import *

__all__ = [ "QPCBDResultsCorners" ]

class QPColoredTableModel(QPTableModel):
	def __init__(self, colorIndices, *args, **kwargs):
		QPTableModel.__init__(self, *args, **kwargs)
		self.colorIndices=set(colorIndices)
		
	def data(self, index, role):
		if role==Qt.BackgroundColorRole:
			row=index.row()
			col=index.column()
			
			if (row,col) in self.colorIndices:
				return QColor(Qt.red).lighter(180)
			else:
				return QPTableModel.data(self, index, role)
		else:
			return QPTableModel.data(self, index, role)

class QPCBDResultsCorners(QPResultsWidget):
	def __init__(self, treePath, logger=None, parent=None):
		QPResultsWidget.__init__(self, treePath, logger, parent)
		
		# Build table (it is static so why complicate things with a model)
		task=self.rec.auxData['task']
		
		corners=self.rec.payload.measureCorners
		addedCorners=self.rec.payload.addedCorners
		
		nameList=task['requirementNames']
		
		tab=[]
		row=0
		colorIndices=[]
		for name in nameList:
			tab.append([name]+corners[name])
			for ii in range(len(corners[name])):
				acl=set(addedCorners[name])
				if corners[name][ii] in acl:
					colorIndices.append((row,ii+1))
			row+=1		
		
		# Make all rows the same length
		m=0
		for row in tab:
			l=len(row)
			if l>m:
				m=l 
		for row in tab:
			l=len(row)
			if l<m:
				row.extend(['']*(m-l))
			
		model=QPColoredTableModel(colorIndices, tab, header=['Name']+list(range(1,m)), parent=self)
		model.setReadOnly(True)
		self.table=QPTable(model, canDelete=False, canCreate=False, canMove=False, canPaste=False, parent=self)
		
		l=QVBoxLayout(self)
		l.setSpacing(4)
		l.addWidget(self.table)
		# l.setContentsMargins(0, 0, 0, 0)
		
		l.addStretch(1)
		
		self.setLayout(l)
		
