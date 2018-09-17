from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .widgets import *
from ..design.sqlite import *
from . import resources
from .style import styleWidget
from .resbase import *

from .. import PyOpusError
from .dumptools import QPDumpError
from .postdump import *

from .respostbase import *

from ..evaluator.posteval import *
from ..misc.debug import DbgSetDefaultPrinter, DbgSetup
from ..misc.dbgprint import MemoryMessagePrinter

from .treeitems import QPTreeItemPostprocPlot, QPTreeItemPostprocAxes, QPTreeItemPostprocTrace

from .style import *

from ..plotter.plotwidget import QPOverlay

import pyqtgraph as pg

from sys import exc_info
from traceback import format_exception, format_exception_only

from pprint import pprint

import time

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

__all__ = [ "QPPostPlots" ]


class QPPostPlots(QPPostBase):
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
		
		# Blank plot widget
		self.plotw=QWidget(self.resWidget)
		self.fvlayout.addWidget(self.plotw)
		
		self.ppStruct=None
		self.trcVecs=None
		self.sclVecs=None
		
		self.preferredMeasure=None
		self.preferredCorner=None
		
		self.plotWidgetList=[]
		self.crosshair=None
		
	def viewerConfig(self):
		cfg=QPPostBase.viewerConfig(self)
		return cfg
	
	def setViewerConfig(self, cfg):
		QPPostBase.setViewerConfig(self, cfg)
		
	def recompute(self):
		self.ppStruct=None
		self.trcVecs=None
		self.sclVecs=None
		
		self.plotw.hide()
		
		self.statusText.setText("Evaluating traces.")
		try:
			# Start timing
			t0=time.time()
			
			# Get postprocessig data
			rootData=self.treePath.rootData()
			item=self.treePath.getItem()
			
			# Verify and dump
			self.ppStruct=dumpPostprocessingPlots(rootData)
			self.errMsg="Plot setup OK."
			self.statusText.setText("Plot configuration dumped.")
			styleWidget(self.statusText, [])
			
			# Get record
			rec=rootData['record']
			
			# No record
			if rec is None:
				return
			
			# What kind of item are we looking at, build trace dict
			traceDict={}
			if type(item) is QPTreeItemPostprocPlot:
				# A plot, get its name
				plotName=item.name()
				plotData=self.ppStruct['plots'][plotName]
				limitToAxes=None
				
				# Generate traces
				for axesName, axesData in plotData['axes'].items():
					for traceName, traceData in axesData['traces'].items():
						traceKey=(plotName, axesName, traceName)
						traceDict[traceKey]=traceData
			elif type(item) is QPTreeItemPostprocAxes:
				# Axes, get plot and axes name
				axesName=item.name()
				plotName=item.parent().name()
				plotData=self.ppStruct['plots'][plotName]
				axesData=plotData['axes'][axesName]
				limitToAxes=axesName
				
				# Generate traces
				for traceName, traceData in axesData['traces'].items():
					traceKey=(plotName, axesName, traceName)
					traceDict[traceKey]=traceData
			else:
				# Trace
				traceName=item.name()
				axesName=item.parent().name()
				plotName=item.parent().parent().name()
				plotData=self.ppStruct['plots'][plotName]
				axesData=plotData['axes'][axesName]
				traceData=axesData['traces'][traceName]
				limitToAxes=axesName
				
				# Generate traces
				traceKey=(plotName, axesName, traceName)
				traceDict[traceKey]=traceData
			
			self.plotName=plotName
			self.plotData=plotData
			self.axesName=axesName
			self.axesData=axesData
			self.limitToAxes=limitToAxes
			self.traceDict=traceDict
			
			# Trace evaluation
			files=rec.waveforms
			
			DbgSetup(prefix=False)
			mmp=MemoryMessagePrinter()
			DbgSetDefaultPrinter(mmp)
			
			pe=PostEvaluator(
				resultsFolder=self.resultsFolder, files=files,
				traces=traceDict
			)
			pe.evaluateTraces()
			self.statusText.setText("Traces evaluated.")
			styleWidget(self.statusText, [])
			
			self.trcVecs=pe.trcVecs
			self.sclVecs=pe.sclVecs
			
			self.errMsg=mmp.messages()
		
		except QPDumpError as e:
			self.errMsg=str(e)
			self.trcVecs=None
			self.sclVecs=None
			self.statusText.setText("Failed to dump plot configuration.")
			styleWidget(self.statusText, ["error"])
		
		except PyOpusError as e:
			self.errMsg=str(e)
			self.trcVecs=None
			self.sclVec=None
			self.statusText.setText("Failed to evaluate traces.")
			styleWidget(self.statusText, ["error"])
				
		except Exception as e:
			ei=exc_info()
			self.errMsg="\n".join(format_exception(ei[0], ei[1], ei[2]))
			self.trcVecs=None
			self.sclVecs=None
			self.statusText.setText("Internal error in trace evaluation.")
			styleWidget(self.statusText, ["error"])
		
		#print("Evaluation time", time.time()-t0)
		
		t0=time.time()
		self.buildPlot()
		#print("Plotting time", time.time()-t0)
	
	@pyqtSlot()
	def traceClicked(self):
		QToolTip.showText(QCursor.pos(), self.sender().name(), self)
	
	# Do not add pyqtSlot decorator because it causes a crash
	def mouseMoved(self, evt):
		# pos=evt[0]
		pos=evt
		
		scene=self.sender()
		
		for axw in self.plotWidgetList:
			brect=axw.sceneBoundingRect()
			if brect.contains(pos):
				# This may crash if transformation is singular
				try:
					mousePoint = axw.getViewBox().mapSceneToView(pos)
				except:
					return
				
				xm=mousePoint.x()
				ym=mousePoint.y()
					
				# Handle log scale
				plotName, axesName = self.axw2desc[axw]
				axesData=self.ppStruct['plots'][plotName]['axes'][axesName]
				x=10.0**xm if axesData['type'] in ['xlog', 'log'] else xm
				y=10.0**ym if axesData['type'] in ['ylog', 'log'] else ym
				
				name="%s:%s" % (plotName, axesName)
				self.crosshairPosition.emit(name, x, y)
				
				self.positionLabel.setText("%s\nx=%e y=%e" % (name, x, y))
				self.positionLabel.move(brect.topLeft().x(), brect.topLeft().y())
				self.positionLabel.adjustSize()
				self.positionLabel.show()
				
				self.crosshair.setCrosshair((pos.x(), self.crosshair.height()-1-pos.y()))
				
				return
	
	def eventFilter(self, obj, ev):
		if ev.type()==QEvent.Leave:
			self.crosshairPosition.emit("", None, None)
			self.positionLabel.hide()
			if self.crosshair is not None:
				self.crosshair.setCrosshair(None)
			self.setCursor(Qt.ArrowCursor)
		if ev.type()==QEvent.Enter:
			self.setCursor(Qt.BlankCursor)
		elif ev.type()==QEvent.Resize:
			if self.crosshair is not None:
				self.crosshair.resize(ev.size())
			
		return QObject.eventFilter(self, obj, ev)
	
	def buildPlot(self):
		self.plotWidgetList=[]
		self.axw2desc={}
		
		if self.ppStruct is not None and self.trcVecs is not None:
			plotw=pg.GraphicsLayoutWidget(self.resWidget)
			
			# Build axes
			axesDict={}
			if self.limitToAxes is not None:
				axw=plotw.addPlot(
					row=0, col=0, rowspan=1, colspan=1, 
					title=self.axesData['title']
				)
				axesDict[self.axesName]=axw
				self.axw2desc[axw]=(self.plotName, self.axesName)
			else:
				for axesName, axesData in self.plotData['axes'].items():
					axw=plotw.addPlot(
						row=axesData['ypos'], col=axesData['xpos'], 
						rowspan=axesData['yspan'], colspan=axesData['xspan'], 
						title=axesData['title']
					)
					axesDict[axesName]=axw
					self.axw2desc[axw]=(self.plotName, axesName)
				
			# Traverse all axes
			axw=None
			for axesName, axw in axesDict.items():
				# Axes data
				axesData=self.plotData['axes'][axesName]
				axw=axesDict[axesName]
				
				# Traverse all traces
				for traceName, traceData in axesData['traces'].items():
					# Get trace and scale
					traceKey=(self.plotName, axesName, traceName)
					
					if traceKey not in self.trcVecs:
						continue
					if traceKey not in self.sclVecs:
						continue
					
					trcVecs=self.trcVecs[traceKey]
					sclVecs=self.sclVecs[traceKey]
					
					# Traverse all corners
					for cornerName, vec in trcVecs.items():
						# Get scale
						if cornerName not in sclVecs:
							continue
						
						scl=sclVecs[cornerName]
						
						# Plot
						trc=axw.plot(
							scl, vec, 
							name="%s:%s" % (traceName, cornerName), 
							pen=pg.mkPen(pg.mkColor(0, 0, 0)), 
							clickable=True, 
							antialias=True
						)
						trc.curve.setClickable(True)
						trc.sigClicked.connect(self.traceClicked)
						
				# Log axis mode
				if axesData['type']=='xlog':
					axw.setLogMode(x=True)
				elif axesData['type']=='ylog':
					axw.setLogMode(y=True)
				elif axesData['type']=='log':
					axw.setLogMode(x=True, y=True)
					
				# Labels
				ax=axw.getAxis('bottom')
				ax.setLabel(text=axesData['xlabel'])
				ax=axw.getAxis('left')
				ax.setLabel(text=axesData['ylabel'])
				
				# View box
				vb=axw.getViewBox()
				
				# Aspect ratio
				if axesData['type']=='lin' and axesData['aspect']:
					vb.setAspectLocked(ratio=1.0)
				
				# Range
				manualx=axesData['xlo'] is not None and axesData['xhi'] is not None
				manualy=axesData['ylo'] is not None and axesData['yhi'] is not None
				if manualx and manualy:
					vb.disableAutoRange(axis=pg.ViewBox.XYAxes)
				elif manualx:
					vb.disableAutoRange(axis=pg.ViewBox.XAxis)
				elif manualy:
					vb.disableAutoRange(axis=pg.ViewBox.YAxis)
				if manualx:
					vb.setXRange(axesData['xlo'], axesData['xhi'], padding=0.01)
				if manualy:
					vb.setYRange(axesData['ylo'], axesData['yhi'], padding=0.01)
				
				# Grid
				axw.showGrid(x=axesData['xgrid'], y=axesData['ygrid'], alpha=0.3)
				
				# Store plot list
				self.plotWidgetList.append(axw)
			
			# Scene is common to all displayed axes
			if axw is not None:
				scene=axw.scene()
				scene.sigMouseMoved.connect(self.mouseMoved)
			
			# Crosshair overlay
			self.crosshair=QPOverlay(plotw, enableRubberband=False)
			
			# Overlay cursor position widget
			self.positionLabel=QLabel(plotw)
			self.positionLabel.setAutoFillBackground(True)
			self.positionLabel.setAttribute(Qt.WA_TransparentForMouseEvents, True)
			pal=self.positionLabel.palette()
			pal.setColor(self.plotw.backgroundRole(), QColor(240, 240, 255))
			self.positionLabel.setPalette(pal)
			self.positionLabel.move(0, 0)
			self.positionLabel.hide()
			
			# Remove event filter from old plot
			self.plotw.removeEventFilter(self)
			
			# Install event filter to new plot
			plotw.installEventFilter(self)
			
			# Put it in layout
			self.fvlayout.replaceWidget(self.plotw, plotw)
			self.plotw.close()
			self.plotw=plotw
			
			
			
		
