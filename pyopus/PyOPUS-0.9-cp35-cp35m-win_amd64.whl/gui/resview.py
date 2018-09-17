from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .widgets import *
from ..design.sqlite import *
from .restree import *
from .tree import *
from .restext import *
from .style import styleWidget
from .fileview import *
from .treeitems import QPTreeItemPostprocRoot, QPTreeItemPostprocAspect, QPTreeItemPostprocAspects
from .fixproject import *
from . import values
import os, datetime, json

from .editnone import *
from .editselection import *

from .resbase import *
from .respostbase import *
from .respostmeas import *
from .respostplot import *

from .treeitems import itemEditorMap
from .treeitems import QPTreeItemPostprocMeasures, QPTreeItemMeasure
from .treeitems import QPTreeItemPostprocPlot, QPTreeItemPostprocAxes, QPTreeItemPostprocTrace

from .fixproject import *

from pprint import pprint

__all__ = [ "QPResultsViewer" ]


class QPPostprocTreeModel(QPTreeModel):
	def __init__(self, rootItem, parent=None, *args):
		QPTreeModel.__init__(self, rootItem, parent, *args)
		
	def setRecord(self, rec):
		rootItem=self.rootPath.item
		
		# Get aspects index
		aspectsIndex=self.index(0, 0, QModelIndex())
		
		# Old number of aspects
		n=self.rowCount(aspectsIndex)
		
		# Delete aspects
		self.beginRemoveRows(aspectsIndex, 0, n-1)
		# Setting record to None removes all aspects
		rootItem.setRecord(None)
		self.endRemoveRows()
		
		# New number of aspects
		n=len(rec.textAspects())
		
		# Set new aspects
		self.beginInsertRows(aspectsIndex, 0, n-1)
		# Setting a record will add new aspects
		rootItem.setRecord(rec)
		self.endInsertRows()
		
class QPResultsViewer(QPFileViewer):
	def __init__(self, fileName, loggerWidget=None, parent=None):
		QPFileViewer.__init__(self, fileName, loggerWidget, parent)
		
		# Get postprocessing file name 
		base, sqliteFileName = os.path.split(fileName)
		ndx=sqliteFileName.rfind(".")
		if ndx>=0:
			# Have ending, replace it with .post.json
			self.baseName=sqliteFileName[:ndx]
			postFileName=sqliteFileName[:ndx]+".post.json"
		else:
			# No ending, add .post.json
			self.baseName=sqliteFileName
			postFileName=sqliteFileName+".post.json"
		self.postFileName=os.path.join(base, postFileName)
		
		# Open postprocessing file
		try:
			with open(self.postFileName, 'r') as f:
				txt=f.read()
				postprocessing=json.loads(txt)
				postprocessingFixer(postprocessing)
				if postprocessing['version']!=values.version:
					self.log("Version mismatch in '%s'. Creating blank postprocessing setup." % self.postFileName, isError=True)
					postprocessing=deepcopy(values.blankPostprocessing)
				else:
					self.log("Loaded postprocessing file '"+self.postFileName+"'.")
		except:
			self.log("Failed to load '%s'. Creating blank postprocessing setup." % self.postFileName)
			postprocessing=deepcopy(values.blankPostprocessing)
		
		postprocessingFixer(postprocessing)
		
		# Add entries for record and aspects
		postprocessing['record']=None
		
		self.postprocessing=postprocessing
		
		# Create results tree
		self.tree=QPResultsTree(self.realPath, self)
		
		# Create postprocessing tree
		self.postprocTree=QPTreeView(self)
		self.postprocTree.setSelectionMode(QAbstractItemView.ExtendedSelection)
		
		# Create postprocessing model
		self.postprocTreeModel=QPPostprocTreeModel(
			QPTreeItemPostprocRoot(self.postprocessing), 
			parent=self.postprocTree
		)
		self.postprocTree.setModel(self.postprocTreeModel)
		
		self.postprocTree.resizeColumnToContents(0)

		# Expand postprocessing tree up to and including items in level 0
		self.postprocTree.expandToDepth(1)
		
		# Connect signals from postprocessing tree model
		self.postprocTreeModel.dataChanged.connect(self.onTreeDataChanged)
		self.postprocTreeModel.rowsAboutToBeRemoved.connect(self.onTreeRowsAboutToBeRemoved)
		self.postprocTreeModel.rowsRemoved.connect(self.onTreeRowsRemoved)
		self.postprocTreeModel.rowsAboutToBeMoved.connect(self.onTreeRowsAboutToBeMoved)
		self.postprocTreeModel.rowsMoved.connect(self.onTreeRowsMoved)
		self.postprocTreeModel.rowsAboutToBeInserted.connect(self.onTreeRowsAboutToBeInserted)
		self.postprocTreeModel.rowsInserted.connect(self.onTreeRowsInserted)
		self.postprocTreeModel.layoutAboutToBeChanged.connect(self.onLayoutAboutToBeChanged)
		self.postprocTreeModel.layoutChanged.connect(self.onLayoutChanged)
		
		# Results display frame
		self.resFrame=QFrame(self)
		self.resFrame.setFrameStyle(QFrame.Plain | QFrame.Box)
		
		self.fvlayout=QVBoxLayout(self.resFrame)
		self.resFrame.setLayout(self.fvlayout)
		
		# Horizontal layout for record header data
		fhlayout1=QHBoxLayout()
		self.fvlayout.addLayout(fhlayout1)
		
		self.idWidget=QPAdaptiveLineEdit(self)
		self.typeWidget=QPAdaptiveLineEdit(self)
		self.entryTimeWidget=QLineEdit(self)
		
		self.idWidget.setReadOnly(True)
		self.typeWidget.setReadOnly(True)
		self.entryTimeWidget.setReadOnly(True)
		
		self.idWidget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
		self.typeWidget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
		self.entryTimeWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		
		fhlayout1.addWidget(QLabel("Id"))
		fhlayout1.addWidget(self.idWidget)
		fhlayout1.addWidget(QLabel("Type"))
		fhlayout1.addWidget(self.typeWidget)
		fhlayout1.addWidget(QLabel("Time"))
		fhlayout1.addWidget(self.entryTimeWidget)
		
		self.textMode=QCheckBox(self)
		self.textMode.setCheckState(Qt.Unchecked)
		self.textMode.setText("Text mode")
		self.textMode.setLayoutDirection(Qt.RightToLeft)
		
		fhlayout1.addWidget(self.textMode)
		
		# Scroller for unsplit mode
		self.viewScroller=QScrollArea(parent=self)
		self.viewScroller.setWidgetResizable(True)
		self.viewScroller.hide()
		
		# Splitter for split mode 
		self.viewSplitter=QSplitter(Qt.Vertical, parent=self.resFrame)
		self.postprocPlaceholder=QWidget(self.viewSplitter)
		self.postprocPlaceholderLayout=QVBoxLayout(self.postprocPlaceholder)
		self.postprocPlaceholderLayout.setContentsMargins(0, 0, 0, 0) # l t r b
		
		self.editorScroller=QScrollArea(parent=self.viewSplitter)
		self.editorScroller.setWidgetResizable(True)
		self.viewSplitter.addWidget(self.postprocPlaceholder)
		self.viewSplitter.addWidget(self.editorScroller)
		self.viewSplitter.hide()
		self.postprocWidget=None
		
		# Main splitter holding two trees and editor pane
		self.splitter=QSplitter(Qt.Horizontal, parent=self)
		self.splitter.addWidget(self.tree)
		self.splitter.addWidget(self.postprocTree)
		self.splitter.addWidget(self.resFrame)
		
		self.splitter.setCollapsible(0, False)
		self.splitter.setCollapsible(1, False)
		self.splitter.setCollapsible(2, False)
		self.splitter.setStretchFactor(0, 0)
		self.splitter.setStretchFactor(1, 0)
		self.splitter.setStretchFactor(2, 1)
		
		# Add main splitter to inherited vertical layout 
		self.vlayout.addWidget(self.splitter)
		
		# Signals handling record selection and postprocessing item selection
		self.tree.newDisplay.connect(self.switchRecord)
		self.postprocTree.treeSelectionChanged.connect(self.postprocSelectionChanged)
		
		# Signal for handling text view checkbox 
		self.textMode.stateChanged.connect(self.handleTextModeChanged)
		
		# Defaukt aspect for record type
		# Key is record typename
		self.defaultAspect={}
		
		# Result viewer configuration for record type and aspect
		# Key is (typename, aspect)
		self.resultsViewerConfig={}
		
		# Set at record switch
		self.activeRec=None
		
		# Set at postproc item switch
		self.activePath=None
		
		# Active postproc item index
		self.activeIndex=None
		
		# Active postproc editor widget
		self.activeEditor=None
		
		# Set at editor switch
		self.splitMode=None
		
		# Start unsplit mode
		self.switchViewerMode(splitMode=False)
		
		# Disables change notification
		self.blockChangeNotification=False
		
		# Initial configuration of main splitter
		sizes=self.splitter.sizes()
		w=self.sizeHint().width()
		tw=min(self.tree.sizeHint().width(), w*0.45*0.55)
		ppw=min(self.postprocTree.sizeHint().width(), w*0.45*0.45)
		self.splitter.setSizes([tw, ppw, w-tw-ppw])
		
	def savePostprocessingFile(self):
		try:
			pp={}
			pp.update(self.postprocessing)
			del pp['record']
			
			txt=json.dumps(pp, indent=2)
			
			with open(self.postFileName, "w") as f:
				f.write(txt)
			
			self.log("Saved postprocessing file '"+self.postFileName+"'.")
			
			return True
		except:
			self.log("Failed to save '%s'." % self.postFileName, isError=True)
			return False
			
	# Signal for reporting changes
	projectChanged=pyqtSignal()
	
	# Request an action from main window
	requestAction=pyqtSignal(str, object)
	
	# Send cursor position
	cursorPosition=pyqtSignal(int, int)
	
	# Send crosshair position
	crosshairPosition=pyqtSignal(str, object, object)
	
	# Forward crosshair position signal
	@pyqtSlot(str, object, object)
	def forwardCrosshairPosition(self, name, x, y):
		self.crosshairPosition.emit(name, x, y)
	
	# Handle cursor position change in editor widget
	@pyqtSlot(int, int)
	def cursorPositionChanged(self, l, c):
		self.cursorPosition.emit(l, c)
	
	# Force commit of uncommited changes
	def forceCommit(self):
		if self.activeEditor is not None:
			self.activeEditor.forceCommit()
		
		self.postprocTree.forceCommit()
	
	@pyqtSlot(int)
	def handleTextModeChanged(self, state):
		if self.activeRec is not None:
			self.switchRecord(self.activeRec.recordId)
		
	@pyqtSlot(int)
	def switchRecord(self, resId):
		# print("Switch record", resId)
		if resId>0:
			# Set active record
			db=SQLiteDatabase(self.realPath)
			rec=db.get(resId)
			rec.getAuxiliaryData()
			self.activeRec=rec
			
			# Are we at an aspect?
			atIndex=self.postprocTree.readCurrentIndex()
			if atIndex is not None:
				# Item selected. If it is an aspect, move to a new aspect. 
				atItem=self.postprocTreeModel.treePath(atIndex).getItem()
				atAspect=issubclass(type(atItem), QPTreeItemPostprocAspect)
			else:
				# No item selected yet, select an aspect. 
				atAspect=True
			
			# Update postprocessing tree
			# Replace aspects with new ones
			# The actual change in the tree may take place later!
			# Disable change notification
			self.blockChangeNotification=True
			# Switch record
			self.postprocTreeModel.setRecord(rec)
			# Enable change notification
			self.blockChangeNotification=False
			
			# If we were looking at an aspect
			if atAspect:
				# Restore active aspect for this type of record
				# Get default aspect
				aspects=rec.textAspects()
				if rec.typename in self.defaultAspect:
					aspect=self.defaultAspect[rec.typename]
				else:
					if len(aspects)>0:
						aspect=aspects[0]
					else:
						aspect=None
				
				try:
					# Get index of aspect in aspects list
					ndx=aspects.index(aspect)
					
					# Find under root the aspects index
					aspectsIndex=self.postprocTreeModel.firstChildByItemType(
						QModelIndex(), QPTreeItemPostprocAspects
					)
					
					# Print all aspects and record
					#tp=self.postprocTreeModel.treePath(aspectsIndex)
					#nn=tp.countChildren()
					#print("New number of aspects", nn)
					#print("Tree record", tp.rootData()['record'])
					#for ii in range(nn):
					#	print("  aspect", tp.child(ii).data())
					
					aspectIndex=self.postprocTreeModel.index(ndx, 0, aspectsIndex)
					self.postprocTree.writeCurrentIndex(aspectIndex)
					self.postprocTree.writeSelection([aspectIndex])
				except ValueError:
					raise
					self.postprocTree.writeCurrentIndex(None)
					self.postprocTree.writeSelection([])
				
		else:
			# No active record
			self.activeRec=None
		
		# Switch editor
		selectedIndexes=self.postprocTree.readSelectedIndexes()
		self.switchEditor(selectedIndexes)
	
	@pyqtSlot(list)
	def postprocSelectionChanged(self, selectedIndexes):
		# Is one aspect item selected? 
		if len(selectedIndexes)==1:
			self.activeIndex=selectedIndexes[0]
			self.activePath=self.postprocTreeModel.treePath(self.activeIndex)
			item=self.activePath.getItem()
			if issubclass(type(item), QPTreeItemPostprocAspect):
				# Remember default aspect for this result type
				typename=self.activePath.rootData()['record'].typename
				aspect=self.activePath.data()
				self.defaultAspect[typename]=aspect
		else:
			self.activeIndex=None
			self.activePath=None
			
		# Set viewer
		self.switchEditor(selectedIndexes)
	
	# TODO: remember main horizontal splitter position for split mode
	def switchViewerMode(self, splitMode=False):
		if self.splitMode!=splitMode:
			# Split mode change
			if splitMode:
				# Entering split mode (postprocessing)
				# No need to restore splitter position because it was hidden
				self.textMode.hide()
				self.viewScroller.hide()
				self.fvlayout.removeWidget(self.viewScroller)
				self.fvlayout.addWidget(self.viewSplitter)
				self.viewSplitter.show()
			else:
				# Leaving split mode, entering results aspect mode
				# No need to remember splitter position because it will be hidden
				self.viewSplitter.hide()
				self.fvlayout.removeWidget(self.viewSplitter)
				self.fvlayout.addWidget(self.viewScroller)
				self.textMode.show()
				self.viewScroller.show()
				
			self.splitMode=splitMode
	
	def connectSelectionViewer(self, indices):
		# Prepare list of tree paths
		treePathList=[ self.postprocTreeModel.treePath(index) for index in indices ]
		
		# Prepare selection editor 
		w=QPEditSelection(treePathList, logger=self.loggerWidget, parent=self)
		
		self.viewScroller.setWidget(w)
		
		# No active editor (signals are disconnected)
		
	def connectTreeEditor(self):
		# Assume blank viewer
		Cls=QPEditNone
		
		if self.activePath is not None:
			# Have active path, get item
			item=self.activePath.getItem()
			# Is it a result aspect
			if (issubclass(type(item), QPTreeItemPostprocAspect)):
				# Result aspect
				if (
					type(item) not in itemEditorMap or
					self.textMode.checkState()==Qt.Checked
				):
					# No viewer in itemEditorMap or forcing text mode
					Cls=QPTextResults
				else:
					# Graphic viewer
					Cls=itemEditorMap[type(item)]
			else:
				# Not a result aspect
				if type(item) in itemEditorMap:
					# Viewer in itemEditorMap
					Cls=itemEditorMap[type(item)]
		
		w=Cls(
			treePath=self.activePath, 
			logger=self.loggerWidget, 
			parent=self.viewScroller if not self.splitMode else self.editorScroller
		)
		
		# Is the viewer derived from QPResultsWidget
		if issubclass(Cls, QPResultsWidget) and w.rec is not None:
			# Retrieve config
			key=(w.rec.typename, w.aspect)
			if key in self.resultsViewerConfig:
				w.setViewerConfig(self.resultsViewerConfig[key])
			else:
				w.setViewerConfig({})
			
		if self.splitMode:
			self.editorScroller.setWidget(w)
			
			# Find out if we are looking at a measure or a plot
			if self.activePath is None:
				# Nothing, blank widget
				pw=QPPostBase(self.activePath, 
					os.path.join(self.baseName, "waveforms.pck"), 
					logger=self.loggerWidget, parent=self
				)
			elif type(self.activePath.getItem()) in [ QPTreeItemPostprocMeasures, QPTreeItemMeasure ]:
				# Measures or measure
				pw=QPPostMeasures(
					self.activePath, 
					os.path.join(self.baseName, "waveforms.pck"), 
					logger=self.loggerWidget, parent=self
				)
			elif type(self.activePath.getItem()) in [ QPTreeItemPostprocPlot, QPTreeItemPostprocAxes, QPTreeItemPostprocTrace ]:
				# Plot, axes, or trace
				pw=QPPostPlots(
					self.activePath, 
					os.path.join(self.baseName, "waveforms.pck"), 
					logger=self.loggerWidget, parent=self
				)
			else:
				# Everything else (plots), blank widget
				pw=QPPostBase(self.activePath, 
					os.path.join(self.baseName, "waveforms.pck"), 
					logger=self.loggerWidget, parent=self
				)
			
			# Forward cursor position signal
			pw.crosshairPosition.connect(self.forwardCrosshairPosition)
			
			# Retrieve config for postprocessing widgets
			if issubclass(type(pw), QPPostBase):
				key=(type(pw), None)
				if key in self.resultsViewerConfig:
					pw.setViewerConfig(self.resultsViewerConfig[key])
				else:
					pw.setViewerConfig({})
			
			self.postprocPlaceholderLayout.addWidget(pw)
			self.postprocWidget=pw
			pw.refresh()
		else:
			self.viewScroller.setWidget(w)
		
		self.activeEditor=w
		
		# Connect signals
		# Enable editor notifications for the tree
		self.activeEditor.dataChanged.connect(self.onDataChanged)
		self.activeEditor.childrenChanged.connect(self.onChildrenChanged)
		self.activeEditor.structureAboutToBeChanged.connect(self.onStructureAboutToBeChanged)
		self.activeEditor.structureChanged.connect(self.onStructureChanged)
		self.activeEditor.requestAction.connect(self.onRequestAction)
		
		# Enable content change monitoring
		self.activeEditor.contentChanged.connect(self.onContentChanged)
		
		# Enable cursor position reporting
		self.activeEditor.cursorPosition.connect(self.cursorPositionChanged)
		
	def disconnectTreeEditor(self):
		# Are we is split mode
		if self.splitMode:
			# Take old editor widget
			oldWidget=self.editorScroller.takeWidget()
			# Take old postprocessing widget
			if self.postprocWidget is not None:
				self.postprocPlaceholderLayout.removeWidget(self.postprocWidget)
				oldPostprocWidget=self.postprocWidget
		else:
			# Take old viewer widget
			oldWidget=self.viewScroller.takeWidget()
			oldPostprocWidget=None
		
		# Results viewer widget showing an aspect?
		if issubclass(type(oldWidget), QPResultsWidget) and oldWidget.rec is not None:
			# Store old config
			cfg=oldWidget.viewerConfig()
			key=(oldWidget.rec.typename, oldWidget.aspect)
			self.resultsViewerConfig[key]=cfg
		
		# Postproc widget showing postprocessing results
		if oldPostprocWidget is not None and issubclass(type(oldPostprocWidget), QPPostBase):
			# Store old postproc widget config
			cfg=oldPostprocWidget.viewerConfig()
			key=(type(oldPostprocWidget), None)
			self.resultsViewerConfig[key]=cfg
			oldPostprocWidget.crosshairPosition.disconnect(self.forwardCrosshairPosition)
		
		if self.activeEditor is not None:
			# Disable tree updating from old editor
			self.activeEditor.dataChanged.disconnect(self.onDataChanged)
			self.activeEditor.childrenChanged.disconnect(self.onChildrenChanged)
			self.activeEditor.structureAboutToBeChanged.disconnect(self.onStructureAboutToBeChanged)
			self.activeEditor.structureChanged.disconnect(self.onStructureChanged)
			self.activeEditor.requestAction.disconnect(self.onRequestAction)
			
			# Disable content change monitoring
			self.activeEditor.contentChanged.disconnect(self.onContentChanged)
			
			# Disable cursor position reporting
			self.activeEditor.cursorPosition.disconnect(self.cursorPositionChanged)
		
		if oldWidget is not None:
			oldWidget.close()
		
		if oldPostprocWidget is not None:
			oldPostprocWidget.close()
			
		# Clear cursor position display
		self.cursorPosition.emit(-1, -1)
		
		self.activeEditor=None
	
	# Switches the right part of the results window
	def switchEditor(self, selectedIndexes):
		# print("switch editor, active record", self.activeRec)
		#if self.activePath is not None:
		#	print("item record", self.activePath.rootData()['record'])
		
		# Display record ID, type, and time
		if self.activeRec is not None:
			self.idWidget.setText("%d" % self.activeRec.recordId)
			self.typeWidget.setText(self.activeRec.typename[7:])
			self.entryTimeWidget.setText(
				#datetime.datetime.fromtimestamp(
				#	self.activeRec.timestamp
				#).strftime("%Y-%m-%d %H:%M:%S")
				#+ ( " (T0+%.1f)" % (self.activeRec.timestamp-self.t0))
				( "%.1f" % (self.activeRec.timestamp-self.t0))
			)
		
		# Disconnect old editor/viewer
		self.disconnectTreeEditor()
		
		# print("selected item count", len(selectedIndexes))
		# Set split mode, connect new editor
		if len(selectedIndexes)>1:
			# Multiple items selected, selection viewer, no split mode
			self.switchViewerMode(splitMode=False)
			self.connectSelectionViewer(selectedIndexes)
		elif len(selectedIndexes)==0:
			# Nothing selected, activePath is None, blank viewer, no split mode
			self.switchViewerMode(splitMode=False)
			self.connectTreeEditor()
		else:
			# One item selected, check it out
			item=self.activePath.getItem()
			# print("item type", type(item))
			
			if ( 
				issubclass(type(item), QPTreeItemPostprocAspect) or 
				type(item) is QPTreeItemPostprocAspects
			):
				# Aspect node or aspects root node
				# Simple (non-split mode)
				# print("switch to unsplit")
				self.switchViewerMode(splitMode=False)
			else:
				# Measure or plot node
				# Split mode with postprocessor and editor
				# print("switch to split")
				self.switchViewerMode(splitMode=True)
			
			# Connect new editor
			self.connectTreeEditor()
		
	def save(self):
		pass
	
	def statFile(self):
		db=SQLiteDatabase(self.realPath)
		rec=db.get(0)
	
		uuid=rec.payload.uuid
		t0=rec.timestamp
		
		return uuid, t0, True
	
	def clearView(self):
		self.tree.clearTree()
		
	def updateView(self):
		self.tree.update()
		
	def setViewerError(self, flag):
		if flag:
			styleWidget(self.tree, ["error"])
		else:
			styleWidget(self.tree, [])
	
	# On action request from editor
	@pyqtSlot(str, object)
	def onRequestAction(self, action, args):
		self.requestAction.emit(action, args)
		
	# Notifications of changes in the editor that affect the tree
	# Data edited by current editor has changed (usually the name of the item)
	# No structural changes
	@pyqtSlot()
	def onDataChanged(self):
		# Refresh tree view
		if self.activeIndex is not None:
			self.postprocTree.update(self.activeIndex)
	
	# Children of the item edited by current editor have changed (usually the names of the items)
	# No structural change
	@pyqtSlot(int, int)
	def onChildrenChanged(self, first, last):
		if self.activeIndex is not None:
			for ndx in range(first,last+1):
				self.postprocTree.update(self.postprocTreeModel.index(ndx, 0, self.activeIndex))
	
	# Notifications that changes in the editor are about to affect the tree structure
	@pyqtSlot()
	def onStructureAboutToBeChanged(self):
		if self.activeIndex is not None:
			self.postprocTreeModel.beginLayoutChange(self.activeIndex)
		
	# Notifications that changes in the editor took place affecting the tree structure
	@pyqtSlot()
	def onStructureChanged(self):
		if self.activeIndex is not None:
			self.postprocTreeModel.endLayoutChange(self.activeIndex)
		
	# Notifications of changes in the tree that affect the editor and data structure
	# Usually this is due to renaming of a node in the tree that has to be reflected by the editor
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def onTreeDataChanged(self, topLeftIndex, bottomRightIndex, roles=[]):
		indexes=[]
		for row in range(topLeftIndex.row(), bottomRightIndex.row()+1):
			path=self.postprocTreeModel.treePath(topLeftIndex)
			if path is self.activePath and self.activeEditor is not None:
				# Update editor
				self.activeEditor.refreshView()
		
		# Project changed
		self.onContentChanged()
	
	# Notification that rows are about to be deleted from the tree
	@pyqtSlot(QModelIndex, int, int)
	def onTreeRowsAboutToBeRemoved(self, ndx, i1, i2):
		# Get active item's parent index
		if self.activeIndex is not None:
			parentIndex=self.activeIndex.parent()
			row=ndx.row()
			if ndx==parentIndex and row>=i2 and row<=i2:
				# Deleting active item
				self.postprocTree.selectionModel().setCurrentIndex(QModelIndex(), QItemSelectionModel.NoUpdate)
	
	# Notification that rows were deleted from the tree
	@pyqtSlot(QModelIndex, int, int)
	def onTreeRowsRemoved(self, ndx, i1, i2):
		# Parent index is ndx
		parentPath=self.postprocTreeModel.treePath(ndx)
		if parentPath is self.activePath and self.activeEditor is not None: 
			# Update editor if it is showing the parent
			self.activeEditor.refreshView()
		
		# Project changed
		self.onContentChanged()
	
	# Notification that rows are about to be moved in the tree
	@pyqtSlot(QModelIndex, int, int, QModelIndex, int)
	def onTreeRowsAboutToBeMoved(self, ndx, i1, i2, ndxDest, idest):
		pass
	
	# Notification that rows were moved in the tree
	@pyqtSlot(QModelIndex, int, int, QModelIndex, int)
	def onTreeRowsMoved(self, ndx, i1, i2, ndxDest, idest):
		# Parent index ndx or ndxDest
		srcPath=self.postprocTreeModel.treePath(ndx)
		dstPath=self.postprocTreeModel.treePath(ndxDest)
		if (
			(srcPath is self.activePath or dstPath is self.activePath) and 
			self.activeEditor is not None
		): 
			# Update editor if it is showing the parent where the change took place
			self.activeEditor.refreshView()
		
		# Project changed
		self.onContentChanged()
	
	
	# Notification that rows are about to be inserted in the tree
	@pyqtSlot(QModelIndex, int, int)
	def onTreeRowsAboutToBeInserted(self, ndx, i1, i2):
		pass
	
	# Notification that rows were inbserted in the tree
	@pyqtSlot(QModelIndex, int, int)
	def onTreeRowsInserted(self, ndx, i1, i2):
		# Parent index is ndx
		parentPath=self.postprocTreeModel.treePath(ndx)
		if parentPath is self.activePath and self.activeEditor is not None: 
			# Update editor if it is showing the parent
			self.activeEditor.refreshView()
		
		# Project changed
		self.onContentChanged()
	
	# Notification that layout is about to change
	# @pyqtSlot(list, QAbstractItemModel.LayoutChangeHint) # Requires QList instead of list. Just do not specify types. 
	def onLayoutAboutToBeChanged(self, parentList, hint):
		pass
	
	# Notification that layout changed
	# @pyqtSlot(list, int) # Requires QList instead of list. Just do not specify types. 
	def onLayoutChanged(self, parentList, hint):
		self.onContentChanged()
	
	# Handle content change in tree and editor
	@pyqtSlot()
	def onContentChanged(self):
		if not self.blockChangeNotification:
			self.projectChanged.emit()
			
			if self.splitMode and self.postprocWidget is not None:
				self.postprocWidget.requestRefresh()
	
	
if __name__=="__main__":
	from pprint import pprint
	import sip 
	import sys
	
	sip.setdestroyonexit(True)
	
	app = QApplication(sys.argv)
	
	w=QPResultsViewer(sys.argv[1])
	
	w.resize(QSize(800, 600))
	w.show()
	app.exec_()
	
	
