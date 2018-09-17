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

__all__ = [ "QPCBDResultsParameters" ]


class QPCBDResultsParameters(QPResultsWidget):
	def __init__(self, treePath, logger=None, parent=None):
		QPResultsWidget.__init__(self, treePath, logger, parent)
		
		# Build table (it is static so why complicate things with a model)
		task=self.rec.auxData['task']
		pConfig=task['parameters']
		tab=[]
		relval=[]
		for name in task['parameterNames']:
			lo=pConfig[name]['lo']
			hi=pConfig[name]['hi']
			value=self.rec.payload.parameters[name]
			if lo is not None and hi is not None:
				relval.append((value-lo)/(hi-lo))
			else:
				relval.append(None)
			tab.append([ name, str(value), "" ])

		model=QPTableModel(tab, header=['Name', 'Value', 'Value wrt. bounds'], parent=self)
		model.setReadOnly(True)
		self.table=QPTable(model, canDelete=False, canCreate=False, canMove=False, canPaste=False, parent=self)
		
		for ii in range(len(relval)):
			if relval[ii] is not None:
				self.table.setIndexWidget(ii, 2, QPRelativePosition(relval[ii]))
		
		l=QVBoxLayout(self)
		l.setSpacing(4)
		l.addWidget(self.table)
		# l.setContentsMargins(0, 0, 0, 0)
		
		l.addStretch(1)
		
		self.setLayout(l)
		
