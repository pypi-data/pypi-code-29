from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .logger import *
from .tree import *
from .treeitems import *

__all__ = [ 'QPTreeEdit' ]

# TODO: sorting of table with list of children shows up in tree

from .editselection import *


class QPTreeEdit(QWidget):
	def __init__(self, loggerWidget=None, parent=None, *args):
		QWidget.__init__(self, parent=parent, *args)
		
		self.treeModel=None
		self.activeIndex=None
		self.activePath=None
		self.activeEditor=None
		self.loggerWidget=loggerWidget if loggerWidget is not None else QPDummyLogger()
		
		self.tree=QPTreeView(parent=self)
		self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
				
		self.editorScroller=QScrollArea(parent=self)
		self.editorScroller.setWidgetResizable(True)
		
		self.splitter=QSplitter(Qt.Horizontal, parent=self)
		self.splitter.addWidget(self.tree)
		self.splitter.addWidget(self.editorScroller)
		
		self.splitter.setCollapsible(0, False)
		self.splitter.setCollapsible(1, False)
		self.splitter.setStretchFactor(0, 0)
		self.splitter.setStretchFactor(1, 1)
		
		hb=QHBoxLayout(self)
		hb.addWidget(self.splitter)
		
		self.setLayout(hb)
		
		self.setMinimumSize(QSize(640, 400))
		
		# Handle tree selection change
		self.tree.treeSelectionChanged.connect(self.onSelectionChanged)
		
	# Signal for reporting changes
	projectChanged=pyqtSignal()
	
	# Request an action from main window
	requestAction=pyqtSignal(str, object)
	
	# Send cursor position
	cursorPosition=pyqtSignal(int, int)
	
	# Handle cursor position change in editor widget
	@pyqtSlot(int, int)
	def cursorPositionChanged(self, l, c):
		self.cursorPosition.emit(l, c)
		
	# Cleanup function
	def destroy(self):
		if self.activeEditor is not None:
			self.disconnectEditor()
			self.activeEditor=None
		
		if self.treeModel is not None:
			self.treeModel.destroy()
		
	# Set new data structure to display
	def setRootItem(self, rootItem):
		# Disconnect signals from old model
		if self.treeModel is not None:
			self.treeModel.dataChanged.disconnect(self.onTreeDataChanged)
			self.treeModel.rowsAboutToBeRemoved.disconnect(self.onTreeRowsAboutToBeRemoved)
			self.treeModel.rowsRemoved.disconnect(self.onTreeRowsRemoved)
			self.treeModel.rowsAboutToBeMoved.disconnect(self.onTreeRowsAboutToBeMoved)
			self.treeModel.rowsMoved.disconnect(self.onTreeRowsMoved)
			self.treeModel.rowsAboutToBeInserted.disconnect(self.onTreeRowsAboutToBeInserted)
			self.treeModel.rowsInserted.disconnect(self.onTreeRowsInserted)
			self.treeModel.layoutAboutToBeChanged.disconnect(self.onLayoutAboutToBeChanged)
			self.treeModel.layoutChanged.disconnect(self.onLayoutChanged)
		
		self.disconnectEditor()
		self.activeIndex=None
		self.activePath=None
		self.activeEditor=None
		
		# Save ol model
		oldtm=self.treeModel
		
		# Create model
		self.treeModel=QPTreeModel(rootItem, parent=self.tree)
		self.tree.setModel(self.treeModel)
		
		self.tree.resizeColumnToContents(0)
		
		# Activate default item
		self.tree.activateItem()
		
		# Expand up to and including items in level 0
		self.tree.expandToDepth(0)
		
		# Connect signals from new model
		self.treeModel.dataChanged.connect(self.onTreeDataChanged)
		self.treeModel.rowsAboutToBeRemoved.connect(self.onTreeRowsAboutToBeRemoved)
		self.treeModel.rowsRemoved.connect(self.onTreeRowsRemoved)
		self.treeModel.rowsAboutToBeMoved.connect(self.onTreeRowsAboutToBeMoved)
		self.treeModel.rowsMoved.connect(self.onTreeRowsMoved)
		self.treeModel.rowsAboutToBeInserted.connect(self.onTreeRowsAboutToBeInserted)
		self.treeModel.rowsInserted.connect(self.onTreeRowsInserted)
		self.treeModel.layoutAboutToBeChanged.connect(self.onLayoutAboutToBeChanged)
		self.treeModel.layoutChanged.connect(self.onLayoutChanged)
		
		# Release old model (purge path cache entries)
		# Do not do this because we never know when Qt might use a cached TreePath 
		# that belongs to a destroyed treeModel. If that happens we get a crash. 
		#if oldtm is not None:
		#	oldtm.destroy()
		
		# if oldtm is not None:
		# 	oldtm.rootPath=None
		# 	import gc
		# 	gc.collect()
		# 	print "refs", gc.get_referrers(oldtm)
	
	# Force commit of uncommited changes
	def forceCommit(self):
		if self.activeEditor is not None:
			self.activeEditor.forceCommit()
		
		self.tree.forceCommit()
	
	selectedItemsChanged=pyqtSignal(list)
	
	def emitSelectedItems(self, selectedIndexes):
		items=[]
		for ndx in selectedIndexes:
			tp=self.treeModel.treePath(ndx)
			if tp is None:
				continue
			it=tp.getItem()
			if it is None:
				continue
			items.append(it)
		
		self.selectedItemsChanged.emit(items)
	
	# Handle selection change signal from tree
	@pyqtSlot(list)
	def onSelectionChanged(self, selected):
		if len(selected)>1:
			# Multiple items selected, show selection editor
			self.setSelectionEditor(selected)
		elif len(selected)==1:
			# Single item selected, show editor
			self.setEditor(selected[0])
		else:
			# Nothing selected, show blank editor
			self.setBlankEditor()
		
		self.emitSelectedItems(selected)
			
	def disconnectEditor(self):
		if self.activeEditor is not None:
			# Call destroy method of editor
			self.activeEditor.destroy()
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
			
			# Remove old editor from view
			self.editorScroller.takeWidget()
			
			# Clear cursor position display
			self.cursorPosition.emit(-1, -1)
			
	
	def connectEditor(self):
		# Put on display
		self.editorScroller.setWidget(self.activeEditor)
		
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
		
	# Display blank editor
	def setBlankEditor(self):
		self.disconnectEditor()
		self.activeIndex=None
		self.activePath=None
		self.activeEditor=DefaultEditorClass(None, parent=self)
		self.connectEditor()
		
	# Display item editor 
	def setEditor(self, index):
		if index is not None and index.isValid():
			self.disconnectEditor()
			self.activeEditor=None
		
			# Get new item
			self.activeIndex=index
			self.activePath=self.treeModel.treePath(index)
			
			# Prepare new editor
			EditorClass=itemEditorMap[type(self.activePath.item)] if type(self.activePath.item) in itemEditorMap else DefaultEditorClass
			self.activeEditor=EditorClass(
				treePath=self.activePath, 
				logger=self.loggerWidget, 
				parent=self
			)
			self.connectEditor()
	
	# Display selection editor
	def setSelectionEditor(self, indices):
		# Prepare list of tree paths
		treePathList=[ self.treeModel.treePath(index) for index in indices ]
		
		# Prepare selection editor 
		if type(self.activeEditor) != QPEditSelection:
			self.disconnectEditor()
			self.activeIndex=None
			self.activePath=None
			self.activeEditor=QPEditSelection(
				treePathList, 
				logger=self.loggerWidget, 
				parent=self
			)
			self.connectEditor()
		
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
			self.tree.update(self.activeIndex)
	
	# Children of the item edited by current editor have changed (usually the names of the items)
	# No structural change
	@pyqtSlot(int, int)
	def onChildrenChanged(self, first, last):
		if self.activeIndex is not None:
			for ndx in range(first,last+1):
				self.tree.update(self.treeModel.index(ndx, 0, self.activeIndex))
	
	# Notifications that changes in the editor are about to affect the tree structure
	@pyqtSlot()
	def onStructureAboutToBeChanged(self):
		if self.activeIndex is not None:
			self.treeModel.beginLayoutChange(self.activeIndex)
		
	# Notifications that changes in the editor took place affecting the tree structure
	@pyqtSlot()
	def onStructureChanged(self):
		if self.activeIndex is not None:
			self.treeModel.endLayoutChange(self.activeIndex)
		
	# Notifications of changes in the tree that affect the editor and data structure
	# Usually this is due to renaming of a node in the tree that has to be reflected by the editor
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def onTreeDataChanged(self, topLeftIndex, bottomRightIndex, roles=[]):
		indexes=[]
		for row in range(topLeftIndex.row(), bottomRightIndex.row()+1):
			path=self.treeModel.treePath(topLeftIndex)
			if path is self.activePath and self.activeEditor is not None:
				# Update editor
				self.activeEditor.refreshView()
		
		# Need to do this so that active task is refreshed after a rename
		self.emitSelectedItems(self.tree.readSelectedIndexes())
			
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
				self.tree.selectionModel().setCurrentIndex(QModelIndex(), QItemSelectionModel.NoUpdate)
	
	# Notification that rows were deleted from the tree
	@pyqtSlot(QModelIndex, int, int)
	def onTreeRowsRemoved(self, ndx, i1, i2):
		# Parent index is ndx
		parentPath=self.treeModel.treePath(ndx)
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
		srcPath=self.treeModel.treePath(ndx)
		dstPath=self.treeModel.treePath(ndxDest)
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
		parentPath=self.treeModel.treePath(ndx)
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
		self.projectChanged.emit()
	
	
	
if __name__=='__main__':
	from pprint import pprint
	import sip 
	import sys
	import sampledata
	import resources
	
	sip.setdestroyonexit(True)
	
	app = QApplication(sys.argv)
	
	p=QPTreeEdit()
	p.setRootItem(QPTreeItemProjectRoot("Project", sampledata.data, sampledata.data))
	p.setWindowTitle("Project viewer demo")
	p.show()
	p.resize(QSize(800, 600))
	app.exec_()
	
	pprint(sampledata.data)
	
