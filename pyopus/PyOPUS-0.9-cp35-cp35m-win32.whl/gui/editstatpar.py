from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .table import *
from .editbase import *
from .values import blankStatParam


__all__ = [ 'QPEditStatPar' ]

header = [ 'Name', 'Low', 'High', 'Distribution' ]
editable = [ True, True, True, False ]
stretch = [ False, False, False, True ]

class QPEditStatPar(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		self.model=QPTableModel(self.data, header, editable=editable, dfl=blankStatParam, parent=self)
		self.table=QPTable(self.model, stretch=stretch, parent=self)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		layout.addWidget(QLabel("Statistical parameters", self))
		layout.addWidget(self.table)
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.table)
		
