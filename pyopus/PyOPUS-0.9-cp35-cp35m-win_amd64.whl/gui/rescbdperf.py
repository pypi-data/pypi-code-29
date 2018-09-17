from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .table import *
from .widgets import *
from ..design.sqlite import *
from . import resources
from .style import styleWidget
from .delegates import QPComboBox
from .resbase import *
import datetime
import numpy as np

from ..evaluator.aggregate import *

from .indicators import *

__all__ = [ "generateTable", "QPCBDResultsPerformance" ]

def generateTable(constraints, ev, compNames, isVector, perfNameList, cornerNames, reqFailed, parent):
	# Build table (it is static so why complicate things with a model)
	relval=[]
	tab=[]
	
	widgets=[]
	for mName in perfNameList:
		if mName not in ev:
			continue
		
		evMeas=ev[mName]
		if mName in constraints:
			con=constraints[mName]
			conLo=con["lo"]
			conHi=con["hi"]
			conNorm=con["norm"]
		else:
			conLo=None
			conHi=None
			conNorm=None
			
		for cName in cornerNames:
			if cName not in evMeas:
				continue
			
			measVal=evMeas[cName]
			
			if isVector[mName]:
				# Handle possible vector
				if type(measVal) is np.ndarray:
					# Vector
					for ii in range(measVal.shape[0]):
						lst=compNames[mName] if mName in compNames else None
						if lst is not None and len(lst)>ii:
							compName=lst[ii]
						else:
							compName="%d" % (ii)
						
						val=measVal[ii]
						
						w=createWidget(val, conLo, conHi, conNorm)
						if reqFailed and w.failed is False:
							continue
						widgets.append(w)
						tab.append([
							mName, cName, compName, ("%e" % (val)), ""
						])
				else:
					# Scalar posing as a vector
					# Also failed vector measurement
					lst=compNames[mName] if mName in compNames else None
					if lst is not None and len(lst)>0:
						compName=lst[0]
					else:
						compName="%d" % (0)
						
					val=measVal
					if val is None:
						valTxt="Failed"
					else:
						valTxt="%e" % (val)
					
					w=createWidget(val, conLo, conHi, conNorm)
					if reqFailed and w.failed is False:
						continue
					widgets.append(w)
					tab.append([
						mName, cName, compName, valTxt, ""
					])
			else:
				# Handle scalar
				val=measVal
				if val is None:
					valTxt="Failed"
				else:
					valTxt="%e" % (val)
				
				w=createWidget(val, conLo, conHi, conNorm)
				if reqFailed and w is not None and w.failed is False:
					continue
				tab.append([
					mName, cName, "", valTxt, ""
				])
				widgets.append(w)
			
	model=QPTableModel(
		tab, 
		header=['Name', 'Corner', 'Component', 'Value', 'Value wrt. requirements'], parent=parent
	)
	model.setReadOnly(True)
	table=QPTable(
		model, canDelete=False, canCreate=False, canMove=False, canPaste=False, parent=parent
	)
	
	for ii in range(len(widgets)):
		w = widgets[ii]
		if w is not None:
			table.setIndexWidget(ii, 4, w)
	
	return table
	
def createWidget(value, lo, hi, norm):
	if lo is not None and hi is None:
		relval=(value-lo)/norm if value is not None else None
		return QPPerformanceConstraint(relval, "above")
	elif lo is None and hi is not None:
		relval=(value-hi)/norm if value is not None else None
		return QPPerformanceConstraint(relval, "below")
	elif lo is not None and hi is not None:
		return QPPerformanceRange(value, lo, hi, norm, "inside")
	else:
		return None


class QPCBDResultsPerformance(QPResultsWidget):
	def __init__(self, treePath, logger=None, parent=None):
		QPResultsWidget.__init__(self, treePath, logger, parent)
		
		self.project=self.rec.auxData['project']
		self.task=self.rec.auxData['task']
		self.cornerNames=self.task['cornerNames']
		self.ev=self.rec.payload.evaluatorData
		self.componentNames=self.rec.payload.componentNames
		
		# Collect constraints and norms from task setup
		self.constraints={}
		for name in self.task['requirementNames']:
			if name not in self.constraints:
				self.constraints[name]={
					'lo': None, 
					'hi': None, 
				}
			dflNormList=[]
			if name in self.task['requirements']['lower']:
				con=self.task['requirements']['lower'][name]
				self.constraints[name]['lo']=con
				dflNormList.append(np.abs(con))
			if name in self.task['requirements']['upper']:
				con=self.task['requirements']['upper'][name]
				self.constraints[name]['hi']=con
				dflNormList.append(np.abs(con))
			
			if name in self.task['requirements']['norm']:
				self.constraints[name]['norm']=self.task['requirements']['norm'][name]
			else:
				# Repeat the default norm computation also implemented in cbd
				# If lower or upper given
				#   norm=max(abs(lover), abs(upper))
				# else
				#   norm=1.0
				# if norm==0
				#   norm=1
				if len(dflNormList)<1:
					dflNormList.append(1.0)
				dflNorm=max(dflNormList)
				if dflNorm==0.0:
					dflNorm=1.0
				self.constraints[name]['norm']=dflNorm
		
		# List only those measures that are in the aggregator setup
		self.nameList=[]
		for name in self.task['requirementNames']:
			if name in self.constraints:
				self.nameList.append(name)
		
		# Layout
		self.layout=QVBoxLayout(self)
		self.layout.setSpacing(4)
		# self.layout.setContentsMargins(0, 0, 0, 0)
		
		h=QHBoxLayout()
		self.layout.addLayout(h)
		
		# Control
		self.perfList=QPComboBox(self)
		self.perfList.addItem("All measures", None)
		for name in self.nameList:
			self.perfList.addItem(name, name)
		
		self.cornerList=QPComboBox(self)
		self.cornerList.addItem("All corners", None)
		for name in self.cornerNames:
			self.cornerList.addItem(name, name)
		
		self.failedOnly=QCheckBox(self)
		self.failedOnly.setCheckState(Qt.Unchecked)
		self.failedOnly.setText("Failures only")
		self.failedOnly.setLayoutDirection(Qt.RightToLeft)

		h.addWidget(self.perfList)
		h.addWidget(self.cornerList)
		h.addWidget(self.failedOnly)
		
		self.perfList.currentIndexChanged.connect(self.handlePerfChange)
		self.cornerList.currentIndexChanged.connect(self.handleCornerChange)
		self.failedOnly.stateChanged.connect(self.handleFailedOnlyChange)
		
		# Dummy table
		self.table=QWidget(None)
		self.layout.addWidget(self.table)
		
		# Stretch
		self.layout.addStretch(1)
		
		self.setLayout(self.layout)
		
	@pyqtSlot(int)
	def handlePerfChange(self, state):
		self.createTable()
	
	@pyqtSlot(int)
	def handleCornerChange(self, state):
		self.createTable()
	
	@pyqtSlot(int)
	def handleFailedOnlyChange(self, state):
		self.createTable()
	
	def viewerConfig(self):
		ndx=self.perfList.currentIndex()
		if ndx==0: 
			perf=None
		else:
			perf=self.nameList[ndx-1]
		
		ndx=self.cornerList.currentIndex()
		if ndx==0: 
			corner=None
		else:
			corner=self.cornerNames[ndx-1]
			
		return {
			'failedOnly': self.failedOnly.checkState()==Qt.Checked, 
			'perf': perf, 
			'corner': corner
		}
	
	def setViewerConfig(self, cfg):
		if 'failedOnly' in cfg:
			if cfg['failedOnly']:
				self.failedOnly.setCheckState(Qt.Checked)
			else:
				self.failedOnly.setCheckState(Qt.Unchecked)
		if 'perf' in cfg:
			if cfg['perf'] is None:
				self.perfList.setCurrentIndex(0)
			else:
				try:
					ndx=self.nameList.index(cfg['perf'])
					self.perfList.setCurrentIndex(ndx+1)
				except ValueError:
					pass
		if 'corner' in cfg:
			if cfg['corner'] is None:
				self.cornerList.setCurrentIndex(0)
			else:
				try:
					ndx=self.cornerNames.index(cfg['corner'])
					self.cornerList.setCurrentIndex(ndx+1)
				except ValueError:
					pass
		self.createTable()
		
	def createTable(self):
		isVector={ mName:self.project['measures'][mName]['vector'] for mName in self.nameList }
		
		ndx=self.perfList.currentIndex()
		if ndx==0:
			perfNameList=self.nameList
		else:
			perfNameList=[self.nameList[ndx-1]]
		
		ndx=self.cornerList.currentIndex()
		if ndx==0:
			cornerNames=self.cornerNames
		else:
			cornerNames=[self.cornerNames[ndx-1]]
		
		reqFailed=self.failedOnly.checkState()==Qt.Checked
		
		table=generateTable(
			self.constraints, self.ev, self.componentNames, isVector, 
			perfNameList, cornerNames, 
			reqFailed, self
		)
		
		self.layout.replaceWidget(self.table, table)
		self.table.close()
		self.table=table
		
