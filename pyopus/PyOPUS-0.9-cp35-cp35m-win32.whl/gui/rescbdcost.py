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

from ..evaluator.aggregate import *

from .indicators import *

__all__ = [ "QPCBDResultsCost" ]


class QPCBDResultsCost(QPResultsWidget):
	def __init__(self, treePath, logger=None, parent=None):
		QPResultsWidget.__init__(self, treePath, logger, parent)
		
		# Build table (it is static so why complicate things with a model)
		task=self.rec.auxData['task']
		cornerNames=task['cornerNames']
		aggregatorSetup=self.rec.auxData['aggregatorSetup']
		
		aggregatorData=self.rec.payload.aggregatorData
		
		cost=0.0
		tab=[]
		relval=[]
		constraints=[]
		for ii in range(len(aggregatorSetup)):
			setup=aggregatorSetup[ii]
			name=setup['measure']
			norm=setup['norm']
			typeChar=">" if type(norm)is Nabove else "<"
			if typeChar==">":
				constraints.append("above")
			else:
				constraints.append("below")
				
			goal=norm.goal
			normValue=norm.norm
			
			reqStr="%s%e" % (typeChar, goal)
			
			
			data=aggregatorData[ii]
			contrib=data['contribution']
			cost+=contrib
			strContrib="%e" % (contrib)
			
			failed=False
			if data['worst'] is None:
				failed=True
				failedCount=len(data['worst_corner_vector'])
				worstText="failed in %d corner(s)" % (failedCount, )
				relval.append(None)
				
				cornerList=[cornerNames[ci] for ci in data['worst_corner_vector']]
				if len(cornerList)>3:
					cornerText=(" ".join(cornerList[:3]))+" ..."
				else:
					cornerText=(" ".join(cornerList))
			else:
				worst=data['worst']
				worstText="%e" % (worst)
				relval.append((worst-goal)/normValue)
				cornerText=cornerNames[data['worst_corner']]
			
			tab.append([
				name, reqStr, worstText, "", strContrib, cornerText
			])
			
		model=QPTableModel(
			tab, 
			header=['Name', 'Requirement', 'Worst', 'Worst wrt. requirement', 'Contribution', 'Worst corner(s)'], parent=self
		)
		model.setReadOnly(True)
		self.table=QPTable(model, canDelete=False, canCreate=False, canMove=False, canPaste=False, parent=self)
		
		for ii in range(len(relval)):
			self.table.setIndexWidget(
				ii, 3, 
				QPPerformanceConstraint(relval[ii], constraint=constraints[ii])
			)
		
		l=QVBoxLayout(self)
		l.setSpacing(4)
		# l.setContentsMargins(0, 0, 0, 0)
		
		label=QLabel("Cost function value", self)
		costBox=QLineEdit(self)
		costBox.setText("%e" % (cost))
		costBox.setReadOnly(True)
		
		l.addWidget(label)
		l.addWidget(costBox)
		
		l.addSpacing(2*l.spacing())
		l.addWidget(self.table)
		
		l.addStretch(1)
		
		self.setLayout(l)
		
