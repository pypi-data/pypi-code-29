from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .widgets import *
from ..design.sqlite import *
from . import resources
from .style import styleWidget
from .resbase import *
import datetime

from .delegates import QPComboBox

from .. import PyOpusError
from .dumptools import QPDumpError
from .postdump import *

from .respostbase import *

from ..evaluator.posteval import *
from ..misc.debug import DbgSetDefaultPrinter, DbgSetup
from ..misc.dbgprint import MemoryMessagePrinter

from .treeitems import QPTreeItemMeasure

from .rescbdperf import generateTable

from .style import *

import numpy as np

from sys import exc_info
from traceback import format_exception, format_exception_only

from pprint import pprint

__all__ = [ "QPPostMeasures" ]


class QPPostMeasures(QPPostBase):
	def __init__(self, treePath, resultsFolder, logger=None, parent=None):
		QPPostBase.__init__(self, treePath, resultsFolder, logger, parent)
		
		# Scroller for results
		self.resScroller=QScrollArea(self)
		self.resScroller.setFrameStyle(QFrame.Plain | QFrame.Box)
		# self.resFrame.setFrameStyle(QFrame.NoFrame)
		self.resScroller.setWidgetResizable(True)
		
		# Blank widget holding all others, put it into scroller
		self.resWidget=QWidget(self)
		self.resScroller.setWidget(self.resWidget)
		
		# Insert scroller into vertical splitter as first widget
		self.splitter.insertWidget(0, self.resScroller)
		
		# Initial splitter postion at 50%
		self.splitter.setSizes([0.5*self.sizeHint().width(), 0.5*self.sizeHint().width()])
		
		# Vertical layout for the scroller
		self.fvlayout=QVBoxLayout(self.resWidget)
		# self.fvlayout.setContentsMargins(0,0,0,0)
		self.resWidget.setLayout(self.fvlayout)
		
		# Horizontal layout for controls on top of the frame
		fhlayout=QHBoxLayout()
		self.fvlayout.addLayout(fhlayout)
		
		# Controls
		self.perfList=QPComboBox(self.resWidget)
		self.cornerList=QPComboBox(self.resWidget)
		
		self.failedOnly=QCheckBox(self.resWidget)
		self.failedOnly.setCheckState(Qt.Unchecked)
		self.failedOnly.setText("Failures only")
		self.failedOnly.setLayoutDirection(Qt.RightToLeft)
		
		fhlayout.addWidget(self.perfList)
		fhlayout.addWidget(self.cornerList)
		fhlayout.addWidget(self.failedOnly)
		
		# Blank widget for table
		self.table=QWidget(self.resWidget)
		self.fvlayout.addWidget(self.table)
		
		self.fvlayout.addStretch(1)
		
		self.ppStruct=None
		self.results=None
		self.componentNames=None
		
		self.perfList.currentIndexChanged.connect(self.handlePerfChange)
		self.cornerList.currentIndexChanged.connect(self.handleCornerChange)
		self.failedOnly.stateChanged.connect(self.handleFailedOnlyChange)
		
		self.preferredMeasure=None
		self.preferredCorner=None
		
	def viewerConfig(self):
		cfg=QPPostBase.viewerConfig(self)
		cfg['measure']=self.preferredMeasure
		cfg['corner']=self.preferredCorner
		cfg['failedOnly']=(self.failedOnly.checkState()==Qt.Checked)
		return cfg
	
	def setViewerConfig(self, cfg):
		QPPostBase.setViewerConfig(self, cfg)
		if 'measure' in cfg:
			self.preferredMeasure=cfg['measure']
		if 'corner' in cfg:
			self.preferredCorner=cfg['corner']
		if 'failedOnly' in cfg:
			if cfg['failedOnly']:
				self.failedOnly.setCheckState(Qt.Checked)
			else:
				self.failedOnly.setCheckState(Qt.Unchecked)
	
	@pyqtSlot(int)
	def handlePerfChange(self, state):
		ndxp=self.perfList.currentIndex()
		self.preferredMeasure=self.perfList.itemText(ndxp) if ndxp>0 else None
		
		self.table.hide()
		self.buildTable()
	
	@pyqtSlot(int)
	def handleCornerChange(self, state):
		ndxc=self.cornerList.currentIndex()
		self.preferredCorner=self.cornerList.itemText(ndxc) if ndxc>0 else None
			
		self.table.hide()
		self.buildTable()
	
	@pyqtSlot(int)
	def handleFailedOnlyChange(self, state):
		self.table.hide()
		self.buildTable()
	
	def recompute(self):
		self.ppStruct=None
		self.results=None
		
		self.table.hide()
		
		self.statusText.setText("Evaluating measures.")
		try:
			# Get postprocessig data
			rootData=self.treePath.rootData()
			item=self.treePath.getItem()
			
			# Is it a measure 
			if type(item) is QPTreeItemMeasure:
				# One measure, get name
				activeMeasures=[item.name()]
			else:
				# All measures
				activeMeasures=None
				
			# Verify and dump
			self.ppStruct=dumpPostprocessingMeasures(rootData)
			self.errMsg="Measures setup OK."
			self.statusText.setText("Measures configuration dumped.")
			styleWidget(self.statusText, [])
			
			# Get record
			rec=rootData['record']
			
			# No record
			if rec is None:
				return
			
			# Measure evaluation
			files=rec.waveforms
			
			DbgSetup(prefix=False)
			mmp=MemoryMessagePrinter()
			DbgSetDefaultPrinter(mmp)
			
			pe=PostEvaluator(
				resultsFolder=self.resultsFolder, files=files,
				measures=self.ppStruct['measures']
			)
			pe.evaluateMeasures(activeMeasures)
			self.statusText.setText("Measures evaluated.")
			styleWidget(self.statusText, [])
			
			self.results=pe.results
			self.componentNames=pe.componentNames
			self.errMsg=mmp.messages()
		
		except QPDumpError as e:
			self.errMsg=str(e)
			self.results=None
			self.statusText.setText("Failed to dump measures configuration.")
			styleWidget(self.statusText, ["error"])
		
		except PyOpusError as e:
			self.errMsg=str(e)
			self.results=None
			self.statusText.setText("Failed to evaluate measures.")
			styleWidget(self.statusText, ["error"])
				
		except Exception as e:
			ei=exc_info()
			self.errMsg="\n".join(format_exception(ei[0], ei[1], ei[2]))
			self.results=None
			self.statusText.setText("Internal error in measure evaluation.")
			styleWidget(self.statusText, ["error"])
		
		# Build requirements
		if self.ppStruct is not None and self.results is not None:
			# Measure names
			self.nameList=list(self.ppStruct['measureNames'])	
			
			# Corner names
			if 'task' in self.rec.auxData and 'cornerNames' in self.rec.auxData['task']:
				# Get corner names (optiter record)
				self.cornerNames=self.rec.auxData['task']['cornerNames']
			else:
				# Build list of corner names
				cNames=set()
				for mName, vals in self.results.items():
					cNames.update(list(vals.keys()))
				self.cornerNames=sorted(list(cNames))
			
			# Extract contraints and norm, set default norm in the same manner as cbd does
			self.constraints={}
			for name in self.nameList:
				self.constraints[name]={
					'lo': None, 
					'hi': None, 
				}
				dflNormList=[]
				if name in self.ppStruct['measureLower']:
					self.constraints[name]['lo']=self.ppStruct['measureLower'][name]
					dflNormList.append(np.abs(self.constraints[name]['lo']))
				if name in self.ppStruct['measureUpper']:
					self.constraints[name]['hi']=self.ppStruct['measureUpper'][name]
					dflNormList.append(np.abs(self.constraints[name]['hi']))
				
				if name in self.ppStruct['measureNorm']:
					self.constraints[name]['norm']=self.ppStruct['measureNorm'][name]
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
			
			# Disconnect controls
			self.perfList.currentIndexChanged.disconnect(self.handlePerfChange)
			self.cornerList.currentIndexChanged.disconnect(self.handleCornerChange)
			self.failedOnly.stateChanged.disconnect(self.handleFailedOnlyChange)
			
			# Update performance combo box
			self.perfList.clear()
			self.perfList.addItem("All measures", None)
			self.perfList.setCurrentIndex(0)
			ndx=1
			for name in self.nameList:
				self.perfList.addItem(name, name)
				if name==self.preferredMeasure:
					self.perfList.setCurrentIndex(ndx)
				ndx+=1
			
			# Update corner combo box
			self.cornerList.clear()
			self.cornerList.addItem("All corners", None)
			self.cornerList.setCurrentIndex(0)
			ndx=1
			for name in self.cornerNames:
				self.cornerList.addItem(name, name)
				if name==self.preferredCorner:
					self.perfList.setCurrentIndex(ndx)
				ndx+=1
			
			# Connect controls
			self.perfList.currentIndexChanged.connect(self.handlePerfChange)
			self.cornerList.currentIndexChanged.connect(self.handleCornerChange)
			self.failedOnly.stateChanged.connect(self.handleFailedOnlyChange)
			
			self.buildTable()
	
	def buildTable(self):
		if self.ppStruct is not None and self.results is not None:
			# Is vector flag
			isVector={ 
				mName:self.ppStruct['measures'][mName]['vector'] for mName in self.nameList 
			}
			
			# List of performances to display
			ndxp=self.perfList.currentIndex()
			perfNameList=self.nameList if ndxp<=0 else [self.nameList[ndxp-1]]
			
			# List of corners to display
			ndxc=self.cornerList.currentIndex()
			cornerNames=self.cornerNames if ndxc<=0 else [self.cornerNames[ndxc-1]]
			
			# Show only failed requirements
			reqFailed=self.failedOnly.checkState()==Qt.Checked
			
			# Create table
			table=generateTable(
				self.constraints, self.results, self.componentNames, isVector, 
				perfNameList, cornerNames, 
				reqFailed, self.resWidget
			)
			
			# Put it in layout
			self.fvlayout.replaceWidget(self.table, table)
			self.table.close()
			self.table=table
			
			
		
