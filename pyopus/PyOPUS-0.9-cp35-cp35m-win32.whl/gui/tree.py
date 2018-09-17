from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .clipboard import *
from .. import PyOpusError

from pprint import pprint

__all__ = [ "QPTreeModel", "QPTreeView" ]


# Cached selector class
#   Path=() .. root
#   Path = None .. not valid
class QPTreePath(object):
	cache={}
	
	def __new__(cls, cacheBin, path=None):
		if (cacheBin, path) in QPTreePath.cache:
			return QPTreePath.cache[(cacheBin, path)]
		else:
			obj=object.__new__(cls)
			obj.path=path
			obj.cacheBin=cacheBin
			obj.item=None
			QPTreePath.cache[(cacheBin, path)]=obj
			return obj
	
	@classmethod
	def purgeCache(cls, cacheBin):
		ckeys=list(cls.cache.keys())
		for b, path in ckeys:
			 if b==cacheBin:
				 del cls.cache[(b, path)]
	
	@classmethod
	def dumpCache(cls):
		for b, path in cls.cache.keys():
			print(b, path)
		
	def __str__(self):
		return "QPTreePath<"+str(self.cacheBin)+":"+str(self.path)+",item="+str(self.item)+">"
	
	def isValid(self):
		return self.path is not None
	
	def name(self):
		return "unnamed" if self.item is None else self.item.name()
	
	# Every time the parent is accessed its item is updated with the latest data
	# Parent of invalid is invalid
	# Parent of root is invalid
	def parent(self):
		if self.path is None:
			# Invalid
			return QPTreePath(self.cacheBin, None)
		elif len(self.path)>0:
			# Valid, but not root
			p=QPTreePath(self.cacheBin, self.path[:-1])
			p.item=self.item.parent()
			return p
		else:
			# Root
			return QPTreePath(self.cacheBin, None)
	
	def countChildren(self):
		return 0 if self.path is None or self.item is None else self.item.countChildren()
		
	# Every time a child is accessed its item is updated with the latest data
	# Child of invalid is root
	def child(self, ndx):
		if self.path is None:
			# Child of invalid path is root
			# Root item, must be created manually somewhere else
			return QPTreePath(self.cacheBin, ())
		else:
			# Valid path
			p=QPTreePath(self.cacheBin, self.path+(ndx,))
			p.item=self.item.childItem(ndx)
			return p
	
	def rootData(self):
		return None if self.path is None or self.item is None else self.item.rootData
	
	def data(self):
		return None if self.path is None or self.item is None else self.item.data
	
	def getItem(self):
		return None if self.path is None else self.item
	
	# Return the index inside parent
	def index(self):
		return self.path[-1] if len(self.path)>0 else -1
		
	# Return the icon
	def icon(self):
		return None if self.item is None else self.item.icon()
	
	# Can we rename children
	def canRenameChildren(self):
		return False if self.item is None else self.item.canRenameChildren()
	
	# Can we move children around
	def canMoveChildren(self):
		return self.item.canMoveChildren()
	
	# Can we move children around
	def canDeleteChildren(self):
		return self.item.canDeleteChildren()
	
	# Can we create children
	def canCreateChildren(self):
		return self.item.canCreateChildren()
	
	# Can we copy children
	def canCopyChildren(self):
		return self.item.canCopyChildren()
	
	# Can we select multiple children 
	def canSelectMultipleChildren(self):
		return self.item.canSelectMultipleChildren()
	
	# Rename child
	def renameChild(self, ndx, name):
		return self.item.renameChild(ndx, name)
	
	# Delete child
	def deleteChild(self, ndx):
		return self.item.deleteChild(ndx)
	
	# Move child
	def moveChild(self, src, dest):
		return self.item.moveChild(src, dest)
	
	# Create child
	def createChild(self, ndx):
		return self.item.createChild(ndx)
	
	# Child template
	def childTemplate(self):
		return self.item.childTemplate()
	
	# Copy children
	def copyChildren(self, indices):
		return self.item.copyChildren(indices)
	
	# Does pasting overwrite items
	def pasteOverwrites(self):
		return self.item.pasteOverwrites()
	
	# Can we paste children here
	def canPasteChildren(self, lcItemClassName, position=-1):
		return self.item.canPasteChildren(lcItemClassName, position)
	
	# Paste children
	def pasteChildren(self, payload, position=-1):
		return self.item.pasteChildren(payload, position)
	
		
class QPTreeModel(QAbstractItemModel): 
	instanceCounter=0
	
	def __init__(self, rootItem, parent=None, *args):
		QAbstractItemModel.__init__(self, parent=parent, *args)
		self.instanceIndex=self.instanceCounter
		self.rootPath=QPTreePath(self.instanceCounter, ())
		self.rootPath.item=rootItem
		QPTreeModel.instanceCounter+=1
	
	# Purges cache entries because this model is no longer needed
	def destroy(self):
		#print "before"
		#QPTreePath.dumpCache()
		QPTreePath.purgeCache(self.instanceIndex)
		#print "after"
		#QPTreePath.dumpCache()
	
	# index.internalPointer() is the corresponding QPTreeItem object
	# row is the index of the object within its parent
	def rowCount(self, parent = QModelIndex()):
		# Receiving an invalid parent means to count the children of root node
		if parent.column() > 0:
			return 0
		
		if not parent.isValid():
			# Count children of root
			return self.rootPath.countChildren()
		else:
			# Count children of given parent
			return parent.internalPointer().countChildren()
		
	def columnCount(self, parentIndex = QModelIndex()):
		return 1
	
	def data(self, index, role):
		if not index.isValid():
			return QVariant()
		path = self.treePath(index)
		if role == Qt.DisplayRole or role == Qt.UserRole or role == Qt.EditRole:
			return path.name()
		elif role == Qt.DecorationRole:
			return QVariant(path.icon())
		else:
			return QVariant()
	
	def headerData(self, column, orientation, role):
		if (orientation == Qt.Horizontal and role == Qt.DisplayRole):
			return QVariant(self.rootPath.name())
	
		return QVariant()
	
	def flags(self, index):
		f=Qt.ItemIsEnabled | Qt.ItemIsSelectable
		
		# Get QPTreePath of item
		itemPath=self.treePath(index)
		
		# If item is root, stop here
		if itemPath == self.rootPath:
			return f
		
		# Get parent QPTreePath, check if we can rename its children
		if itemPath.parent().canRenameChildren():
			f |= Qt.ItemIsEditable
		return f
	
	def setData(self, index, value, role):
		path=self.treePath(index)
		parentPath=path.parent()
		if parentPath.canRenameChildren():
			parentPath.renameChild(index.row(), value)
			self.dataChanged.emit(index, index)
			return True
		else:
			return False
	
	# Index is defined by row, column, and parentPath object of type QPTreePath
	# which refers to the QPTreePath of the item
	# Construct index of a child positioned in row, column under parent
	def index(self, row, column, parent):
		# Check if an element with given row, column, and parent exists
		if not self.hasIndex(row, column, parent):
			return QModelIndex()
		
		# For invalid parent use the QPTreePath object of root element
		if not parent.isValid():
			parentPath=self.rootPath
		else:
			parentPath=parent.internalPointer()
		
		# Get QPTreePath of child
		childPath=parentPath.child(row)
		
		# Create index of child
		return self.createIndex(row, column, childPath)
	
	# Find first child by item type
	def firstChildByItemType(self, index, itemType):
		tp=self.treePath(index)
		nc=tp.countChildren()
		for ii in range(nc):
			ctp=tp.child(ii)
			ci=ctp.getItem()
			if type(ci) is itemType:
				return self.index(ii, 0, index)
		
		# Not found
		return QModelIndex()
		
	# Construct index of a parent
	def parent(self, index):
		# This function should never return in index corresponding to the root item
		# i.e. internalPointer() with QPTreePath pointing to root item
		# Invalid index should be returned insted
		
		# When invalid index is passed, return an invalid index
		if not index.isValid():
			return QModelIndex()
		
		# Get QPTreePath corresponding to index
		childPath=index.internalPointer()
		# Get QPTreePath of parent
		parentPath=childPath.parent()
		
		# If parent is root, return an invalid index
		if parentPath==self.rootPath:
			return QModelIndex()
		
		# Otherwise return the index corresponding to parent
		return self.createIndex(parentPath.index(), 0, parentPath)
		
	# Return QPTreePath object for index
	def treePath(self, index):
		# Get QPTreePath stored in the index
		path=index.internalPointer()
		
		# If path is None or index is not valid, return root QPTreePath
		if not index.isValid() or path is None:
			return self.rootPath
		else:
			return path
		
	# Layout change notification from outside, somebody else changed the layout of our data
	def beginLayoutChange(self, parentIndex):
		self.layoutAboutToBeChanged.emit([QPersistentModelIndex(parentIndex)])
		
	def endLayoutChange(self, parentIndex):
		self.layoutChanged.emit([QPersistentModelIndex(parentIndex)])
	
	# Removing children from the tree
	def removeChildren(self, parentIndex, first, last):
		parentItem=self.treePath(parentIndex)
		if not parentItem.canDeleteChildren():
			return
		
		self.beginRemoveRows(parentIndex, first, last)
		for ndx in range(last, first-1, -1):
			parentItem.deleteChild(ndx)
		self.endRemoveRows()
		
	# Move a child
	def moveChild(self, parentIndex, src, dest):
		parentItem=self.treePath(parentIndex)
		if not parentItem.canMoveChildren():
			return
		
		nChildren=parentItem.countChildren()
		
		if src<0:
			src=nChildren+src
		if src<0 or src>nChildren:
			raise PyOpusError("Bad index in moveChild()")
		if dest<0:
			dest=nChildren+dest
		if dest<0 or dest>nChildren:
			raise PyOpusError("Bad index in moveChild()")
		
		self.beginMoveRows(parentIndex, src, src, parentIndex, dest)
		parentItem.moveChild(src, dest)
		self.endMoveRows()
	
	# Create a child
	def createChild(self, parentIndex, position=-1):
		parentPath=self.treePath(parentIndex)
		if not parentPath.canCreateChildren():
			return
		
		nChildren=parentPath.countChildren()
		
		if position<0:
			position=nChildren+position+1
		if position<0 or position>nChildren:
			raise PyOpusError("Bad index in createChild()")
		
		self.beginInsertRows(parentIndex, position, position)
		parentPath.createChild(position)
		self.endInsertRows()
		
	# Paste children
	def pasteChildren(self, payload, parentIndex, pos=-1):
		if pos<0:
			pos+=self.rowCount(parentIndex)+1
			
		nItems=len(payload[1])
		
		# Paste
		parentPath=self.treePath(parentIndex)
		overwrite=parentPath.pasteOverwrites()
		if overwrite:
			self.beginLayoutChange(parentIndex)
		else:
			self.beginInsertRows(parentIndex, pos, pos+nItems-1)
		ndxs=parentPath.pasteChildren(payload, pos)
		if overwrite:
			self.endLayoutChange(parentIndex)
		else:
			self.endInsertRows()
		
		return ndxs
	
class QPTreeView(QTreeView):
	def __init__(self, parent):
		QTreeView.__init__(self, parent)
		
		# Create before CTRL+SHIFT+ENTER
		# 1) can create child -> new first child
		# 2) can create sibling -> new sibling before
		# 3) can create child or sibling -> ask
		
		# Create after CTRL+ENTER
		# 1) can create child -> new last child
		# 2) can create sibling -> new sibling after
		# 3) can create child or sibling -> ask
		
		# Define actions
		self.selectAllAction=QAction("Select all siblings", self)
		self.selectAllAction.setShortcut(QKeySequence.SelectAll)
		self.selectAllAction.setStatusTip("Select all siblings")
		self.selectAllAction.triggered.connect(self.onSelectAll)
		self.selectAllAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.invertSelectionAction=QAction("Invert selection", self)
		self.invertSelectionAction.setShortcut(QKeySequence("Ctrl+I"))
		self.invertSelectionAction.setStatusTip("Invert selection")
		self.invertSelectionAction.triggered.connect(self.onInvertSelection)
		self.invertSelectionAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.deleteAction=QAction("Delete", self)
		self.deleteAction.setShortcut(QKeySequence("Ctrl+Delete"))
		self.deleteAction.setStatusTip("Delete selected items")
		self.deleteAction.triggered.connect(self.onDeleteNodes)
		self.deleteAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.expandAction=QAction("Expand", self)
		self.expandAction.setShortcut(QKeySequence("Right"))
		self.expandAction.setStatusTip("Expand selected items")
		self.expandAction.triggered.connect(self.onExpandNodes)
		self.expandAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.collapseAction=QAction("Collapse", self)
		self.collapseAction.setShortcut(QKeySequence("Left"))
		self.collapseAction.setStatusTip("Collapse selected items")
		self.collapseAction.triggered.connect(self.onCollapseNodes)
		self.collapseAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.renameAction=QAction("Rename", self)
		self.renameAction.setShortcut(QKeySequence("F2"))
		self.renameAction.setStatusTip("Rename item")
		self.renameAction.triggered.connect(self.onRenameNode)
		self.renameAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.moveUpAction=QAction("Move up", self)
		self.moveUpAction.setShortcut(QKeySequence("Ctrl+Shift+Up"))
		self.moveUpAction.setStatusTip("Move selected items up")
		self.moveUpAction.triggered.connect(self.onMoveUp)
		self.moveUpAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.moveDownAction=QAction("Move down", self)
		self.moveDownAction.setShortcut(QKeySequence("Ctrl+Shift+Down"))
		self.moveDownAction.setStatusTip("Move selected items down")
		self.moveDownAction.triggered.connect(self.onMoveDown)
		self.moveDownAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.addBeforeAction=QAction("Add item before", self)
		self.addBeforeAction.setShortcuts([
			QKeySequence("Ctrl+Shift+Return"), 
			QKeySequence("Ctrl+Shift+Enter")
		])
		self.addBeforeAction.setStatusTip("Add item before")
		self.addBeforeAction.triggered.connect(self.onAddBefore)
		self.addBeforeAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.addAfterAction=QAction("Add item after", self)
		self.addAfterAction.setShortcuts([
			QKeySequence("Ctrl+Return"), 
			QKeySequence("Ctrl+Enter")
		])
		self.addAfterAction.setStatusTip("Add item after")
		self.addAfterAction.triggered.connect(self.onAddAfter)
		self.addAfterAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.cutAction=QAction("Cut", self)
		self.cutAction.setShortcut(QKeySequence.Cut)
		self.cutAction.setStatusTip("Move items to clipboard")
		self.cutAction.triggered.connect(self.onCut)
		self.cutAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.copyAction=QAction("Copy", self)
		self.copyAction.setShortcut(QKeySequence.Copy)
		self.copyAction.setStatusTip("Copy items to clipboard")
		self.copyAction.triggered.connect(self.onCopy)
		self.copyAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.pasteAction=QAction("Paste", self)
		self.pasteAction.setShortcut(QKeySequence.Paste)
		self.pasteAction.setStatusTip("Paste items from clipboard")
		self.pasteAction.triggered.connect(self.onPaste)
		self.pasteAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		# Add actions to widget
		self.addAction(self.cutAction)
		self.addAction(self.copyAction)
		self.addAction(self.pasteAction)
		self.addAction(self.selectAllAction)
		self.addAction(self.invertSelectionAction)
		self.addAction(self.deleteAction)
		self.addAction(self.expandAction)
		self.addAction(self.collapseAction)
		self.addAction(self.renameAction)
		self.addAction(self.moveUpAction)
		self.addAction(self.moveDownAction)
		self.addAction(self.addBeforeAction)
		self.addAction(self.addAfterAction)
		
	def setModel(self, model):
		# Disconnect signals from previous model
		if self.selectionModel() is not None:
			self.selectionModel().selectionChanged.disconnect(self.handleSelectionChange)
			self.selectionModel().currentChanged.disconnect(self.handleCurrentChange)
		
		QTreeView.setModel(self, model)
		
		# Connect signals from new model
		# Handle selection change
		self.selectionModel().selectionChanged.connect(self.handleSelectionChange)
		# Handle current item change
		self.selectionModel().currentChanged.connect(self.handleCurrentChange)
	
	# Force commit of uncommited changes
	def forceCommit(self):
		ndx=self.currentIndex();
		if ndx.isValid():
			self.currentChanged(ndx, ndx)
	
	def contextMenuEnableActions(self):
		indexes=self.readSelectedIndexes()
		rows=[ndx.row() for ndx in indexes]
		nSelectedRows=len(rows)
		parentIndex, pos = self.pastePosition()
		
		# For move actions
		if nSelectedRows>0:
			rmin=min(rows)
			rmax=max(rows)
			firstParent=indexes[0].parent()
			nRowsFirstParent=self.model().rowCount(firstParent)
		else:
			rmin=None
			rmax=None
			nRowsFirstParent=None
		
		# Do we have selection
		if nSelectedRows==0:
			# No, parent for operation must be root
			selectionParentIndex=QModelIndex()
		else:
			# Yes, get parent of selected items
			selectionParentIndex=indexes[0].parent()
		
		# Selection parent tree path
		sptp=self.model().treePath(selectionParentIndex)
		
		# Paste parent tree path
		pptp=self.model().treePath(parentIndex) if parentIndex is not None else None
		
		# Can delete
		canDelete=nSelectedRows>0 and sptp is not None and sptp.canDeleteChildren()
		
		# Can move
		canMove=nSelectedRows>0 and sptp is not None and sptp.canMoveChildren()
		
		# Can rename
		canRename=nSelectedRows==1 and sptp is not None and sptp.canRenameChildren()
		
		# Can expand, collapse
		canExpand=False
		canCollapse=False
		if nSelectedRows>0:
			for index in indexes:
				tp=self.model().treePath(index)
				if tp is not None and tp.countChildren()>0:
					if self.isExpanded(index):
						canCollapse=True
					else:
						canExpand=True
		
		# Can copy
		canCopy=nSelectedRows>0 and sptp is not None and sptp.canCopyChildren()
		
		# Can paste
		canPaste=parentIndex is not None
		
		# Can select all 
		canSelectAll=sptp is not None and sptp.canSelectMultipleChildren()
		
		# Can invert selection
		canInvertSelection=nSelectedRows>0 and canSelectAll
		
		# For create actions
		enableCreateAction = nSelectedRows==0 and self.model().rootPath.canCreateChildren()
		if nSelectedRows==1:
			path=self.model().treePath(indexes[0])
			parentPath=path.parent()
			enableCreateAction = enableCreateAction or path.canCreateChildren()
			if parentPath.isValid():
				enableCreateAction = enableCreateAction or parentPath.canCreateChildren()
		
		self.copyAction.setEnabled(canCopy)
		self.cutAction.setEnabled(canCopy and canDelete)
		self.pasteAction.setEnabled(canPaste)
		
		self.selectAllAction.setEnabled(canSelectAll)
		self.invertSelectionAction.setEnabled(canInvertSelection)
		self.deleteAction.setEnabled(canDelete)
		self.expandAction.setEnabled(canExpand)
		self.collapseAction.setEnabled(canCollapse)
		
		self.renameAction.setEnabled(canRename)
		
		self.moveUpAction.setEnabled(
			canMove and rmin is not None and rmin>0
		)
		self.moveDownAction.setEnabled(
			canMove and rmax is not None and rmax<nRowsFirstParent-1
		)
		self.addBeforeAction.setEnabled(enableCreateAction)
		self.addAfterAction.setEnabled(enableCreateAction)
		
	# Context menu
	def contextMenuEvent(self, event):
		self.menu=QMenu(self)
		
		self.menu.addAction(self.cutAction)
		self.menu.addAction(self.copyAction)
		self.menu.addAction(self.pasteAction)
		
		self.menu.addAction(self.selectAllAction)
		self.menu.addAction(self.invertSelectionAction)
		self.menu.addAction(self.deleteAction)
		self.menu.addAction(self.expandAction)
		self.menu.addAction(self.collapseAction)
		
		self.menu.addAction(self.renameAction)
		
		self.menu.addAction(self.moveUpAction)
		self.menu.addAction(self.moveDownAction)
		
		self.menu.addAction(self.addBeforeAction)
		self.menu.addAction(self.addAfterAction)
		
		self.contextMenuEnableActions()
		
		self.menu.popup(QCursor.pos())
	
	def readSelectedIndexes(self):
		return [ndx for ndx in self.selectionModel().selectedIndexes()]
	
	def readCurrentIndex(self):
		ix=self.selectionModel().currentIndex()
		if ix.isValid():
			return ix
		else: 
			return None
	
	def updateIndexesOnDelete(self, ndxs, pos):
		for ii in range(len(ndxs)):
			if ndxs[ii] is not None:
				ndx=ndxs[ii]
				row = ndx.row()
				if pos<row:
					ndxs[ii]=self.model().index(row-1, 0, ndx.parent())
				elif pos==row:
					ndxs[ii]=None
	
	def updateIndexesOnMove(self, ndxs, delta):
		for ii in range(len(ndxs)):
			ndx=ndxs[ii]
			if ndx is not None:
				ndxs[ii]=self.model().index(ndx.row()+delta, 0, ndx.parent())
	
	def updateIndexesOnInsert(self, ndxs, pos):
		for ii in range(len(ndxs)):
			if ndxs[ii] is not None:
				ndx=ndxs[ii]
				row = ndx.row()
				if pos<=row:
					ndxs[ii]=self.model().index(row+1, 0, ndx.parent())
	
	def writeCurrentIndex(self, index):
		self.selectionModel().setCurrentIndex(
			self.model().index(index.row(), 0, index.parent()) if index is not None else QModelIndex(), 
			QItemSelectionModel.NoUpdate
		)
	
	def writeSelection(self, indexes):
		sel=QItemSelection()
		for ndx in indexes:
			if ndx is not None:
				sel.select(ndx, ndx)
		self.selectionModel().select(
			sel, 
			QItemSelectionModel.ClearAndSelect
		)
	
	# Copy action handler
	@pyqtSlot(bool)
	def onCopy(self, checked):
		# Get selection
		indexes=self.readSelectedIndexes()
		# Assume all selected items have the same parent, get the first item
		if len(indexes)>0:
			parentPath=self.model().treePath(indexes[0].parent())
			childNdxs=[index.row() for index in indexes]
			payload=parentPath.copyChildren(childNdxs)
			treeToClipboard(payload)
	
	# Cut action handler
	@pyqtSlot(bool)
	def onCut(self, checked):
		self.onCopy(checked)
		self.onDeleteNodes(checked)
	
	# Calculate paste position based on mime type (without unpacking data)
	# Returns parentIndex, position
	# Returns None, None when the clipboard content cannot be pasted
	def pastePosition(self):
		lcItemClassName=lcTreeItemClassNameOnClipboard()
		if lcItemClassName is None:
			return None, None
		
		# Get selection
		indexes=self.readSelectedIndexes()
		
		if len(indexes)==0:
			# No selection, paste under root (at last entry if root is a list)
			parentIndex=self.model().parent(QModelIndex())
			parentPath=self.model().treePath(parentIndex)
			pasteAt=-1
			if not parentPath.canPasteChildren(lcItemClassName, pasteAt):
				# No, cannot paste under root
				return None, None
			else:
				return parentIndex, pasteAt
		else:
			# Assume all selected indexes have the same parent, get first index
			index=indexes[0]
			
			# Get immediate parent
			immediateParent=index.parent()
			immediateParentPath=self.model().treePath(immediateParent)
			
			# Assume we want to paste as sibling after last selected item
			pasteAt=max([index.row() for index in indexes])+1
			
			# Can we paste under immediate parent (as sibling)
			# Assume pasting at end during check
			if immediateParentPath.canPasteChildren(lcItemClassName, pasteAt):
				# Paste as sibling, compute insertion point after last selected item
				# Find selection member with highest row index, paste after that member
				return immediateParent, pasteAt
			else:
				# Cannot paste as sibling
				if len(indexes)>1:
					# More than one selected item, cannot paste as child because parent is not unique
					return None, None
				
				# Look for suitable parent up the tree, start at selected item
				parentIndex=index
				# Paste at beginning when pasting as child
				pasteAt=0
				while True:
					# Get current parent's tree path
					parentPath=self.model().treePath(parentIndex)
					
					# Can we paste here?
					if not parentPath.canPasteChildren(lcItemClassName, pasteAt):
						# No
						if not parentIndex.isValid():
							# We just checked root index as parent, stop now and give up
							return None, None
						# Go to next parent
						parentIndex=parentIndex.parent()
					else:
						# Yes, stop searching
						return parentIndex, pasteAt
				
				# This should never be reached, but just in case 
				return None, None
			
	# Paste action handler
	@pyqtSlot(bool)
	def onPaste(self, checked):
		lcItemClassName=lcTreeItemClassNameOnClipboard()
		if lcItemClassName is None:
			return
		
		payload=treeFromClipboard(lcItemClassName)
		
		# If payload is empty, stop
		if len(payload[1])<=0:
			return
		
		# Compute paste position
		parentIndex, pos = self.pastePosition()
		
		if parentIndex is None:
			return
		
		# Paste
		self.writeSelection([])
		ndxs=self.model().pasteChildren(payload, parentIndex, pos)
		
		# Select freshly pasted data
		sel = [ self.model().index(ii, 0, parentIndex) for ii in ndxs ]
		# First move current index to first new item, then select all new items so 
		# handleSelectionChange() won't mess up the selection
		self.writeCurrentIndex(sel[0])
		self.writeSelection(sel)
			
	# Select all action handler
	@pyqtSlot(bool)
	def onSelectAll(self, checked):
		# Get selection
		indexes=self.readSelectedIndexes()
		# Assume all selected items have the same parent, get the first item
		if len(indexes)>0:
			parentIndex=indexes[0].parent()
			sel=[]
			for ii in range(self.model().rowCount(parentIndex)):
				ndx=self.model().index(ii, 0, parentIndex)
				sel.append(ndx)
			self.writeSelection(sel)
	
	# Invert selection action handler
	@pyqtSlot(bool)
	def onInvertSelection(self, checked):
		# Get selection
		indexes=self.readSelectedIndexes()
		# Assume all selected items have the same parent, get the first item
		if len(indexes)>0:
			rows=set([ndx.row() for ndx in indexes])
			parentIndex=indexes[0].parent()
			sel=[]
			for ii in range(self.model().rowCount(parentIndex)):
				if ii in rows:
					continue
				ndx=self.model().index(ii, 0, parentIndex)
				sel.append(ndx)
			self.writeSelection(sel)
	
	# Delete nodes action handler
	@pyqtSlot(bool)
	def onDeleteNodes(self, checked):
		# Get selection
		indexes=self.readSelectedIndexes()
		current=self.readCurrentIndex()
		ndxlist=indexes+[current]
		
		parentIndex=indexes[0].parent()
		parentPath=self.model().treePath(parentIndex)
		if not parentPath.canDeleteChildren():
			return
		
		# List row numbers for deletion
		rows=[index.row() for index in indexes]
		rows=sorted(rows)
		
		# Delete
		for row in reversed(rows):
			path=parentPath.child(row)
			
			# Remove items from tree, do it via tree model
			self.model().removeChildren(parentIndex, row, row)
			
			# Update index list
			self.updateIndexesOnDelete(ndxlist, row)
		
		self.writeSelection(ndxlist[:-1])
		self.writeCurrentIndex(ndxlist[-1])
	
	# Expand nodes action handler
	@pyqtSlot(bool)
	def onExpandNodes(self, checked):
		# Get selection
		indexes=self.readSelectedIndexes()
		for index in indexes:
			if not self.isExpanded(index):
				self.setExpanded(index, True)
	
	# Collapse nodes action handler
	@pyqtSlot(bool)
	def onCollapseNodes(self, checked):
		# Get selection
		indexes=self.readSelectedIndexes()
		for index in indexes:
			if self.isExpanded(index):
				self.setExpanded(index, False)
		
	# Rename node action handler
	@pyqtSlot(bool)
	def onRenameNode(self, checked):
		# Get selection
		indexes=self.readSelectedIndexes()
		if len(indexes)==1:
			parentPath=self.model().treePath(indexes[0]).parent()
			if parentPath.canRenameChildren():
				self.edit(indexes[0])
				
	# Move up action handler
	@pyqtSlot(bool)
	def onMoveUp(self, checked):
		indexes=self.readSelectedIndexes()
		current=self.currentIndex()
		ndxlist=indexes+[current]
		
		# List row numbers for moving
		rows=[ndx.row() for ndx in indexes]
		rows=sorted(rows)
		
		# Check feasibility
		parent=indexes[0].parent()
		parentPath=self.model().treePath(parent)
		if not parentPath.canMoveChildren():
			return
		
		if len(rows)<=0:
			return
		lowestRow=rows[0]
		if lowestRow<=0:
			return
		
		# Move
		for row in rows:
			self.model().moveChild(parent, row, row-1)
		
		self.updateIndexesOnMove(ndxlist, -1)
		
		self.writeSelection(ndxlist[:-1])
		self.writeCurrentIndex(ndxlist[-1])
	
	# Move down action handler
	@pyqtSlot(bool)
	def onMoveDown(self, checked):
		indexes=self.readSelectedIndexes()
		current=self.currentIndex()
		ndxlist=indexes+[current]
		
		# List row numbers for moving
		rows=[ndx.row() for ndx in indexes]
		rows=sorted(rows)
		
		# Check feasibility
		parent=indexes[0].parent()
		parentPath=self.model().treePath(parent)
		if not parentPath.canMoveChildren():
			return
		
		if len(rows)<=0:
			return
		highestRow=rows[-1]
		if highestRow>=self.model().rowCount(parent)-1:
			return
		
		# Move
		for row in reversed(rows):
			self.model().moveChild(parent, row, row+2)
		
		self.updateIndexesOnMove(ndxlist, 1)
		
		self.writeSelection(ndxlist[:-1])
		self.writeCurrentIndex(ndxlist[-1])
	
	def siblingOrChild(self):
		# Return value is a tuple
		#   createChild (bool)
		#   index of the parent where the new item is to be created
		#   QPTreePath of the parent where the new item is to be created
		#   row within its parent for the selected item
		#   number of children of the selected item 
		indexes=self.readSelectedIndexes()
		
		# Check feasibility (exactly zero or one selected item is required)
		if len(indexes)>1:
			return None, None, None, None, None
		
		# If nothing is selected we are adding children to the root item
		if len(indexes)==0:
			# Create a child of the root item
			index=self.model().parent(QModelIndex())
			itemPath=self.model().treePath(index)
			return True, index, itemPath, 0, itemPath.countChildren()
		
		# We have exactly one selected item	
		index=indexes[0]
		itemPath=self.model().treePath(index)
		
		pIndex=index.parent()
		pItemPath=self.model().treePath(pIndex)
		
		createSibling=pItemPath.canCreateChildren()
		createChild=itemPath.canCreateChildren()
		
		if not (createSibling or createChild):
			# Nothing to do
			return None, None, None, None, None
		elif createSibling and createChild:
			# Resolve dilemma
			mb=QMessageBox(self)
			mb.setWindowTitle("Create child or sibling?")
			mb.setText("Do you want to create a child or a sibling of the selected node?")
			chb=QPushButton("Child", self)
			mb.addButton(chb, QMessageBox.AcceptRole)
			mb.addButton("Sibling", QMessageBox.RejectRole)
			mb.setDefaultButton(chb)
			if mb.exec_()==QMessageBox.AcceptRole:
				createSibling=False
			else:
				createChild=False
		
		if createChild:
			return True, index, itemPath, index.row(), itemPath.countChildren()
		else:
			return False, pIndex, pItemPath, index.row(), itemPath.countChildren()
		
	# Add node before action handler
	@pyqtSlot(bool)
	def onAddBefore(self, checked):
		createChild, parentIndex, parentItemPath, itemRow, nItems = self.siblingOrChild()
		
		# siblingOrChild() did not allow it
		if createChild is None:
			return
		
		# siblingOrChild() allowed it, but the parent cannot create children
		if not parentItemPath.canCreateChildren():
			return
		
		# Deselect everything
		self.writeSelection([])
		
		ndx = 0 if createChild else itemRow
		self.model().createChild(parentIndex, ndx)
		newItemIndex=self.model().index(ndx, 0, parentIndex)
		
		if createChild:
			# Expand parent
			self.setExpanded(parentIndex, True)
		
		# Activate 
		self.writeCurrentIndex(newItemIndex)
		self.writeSelection([newItemIndex])
		
		# Edit
		self.edit(newItemIndex)
		
	# Add node after action handler
	@pyqtSlot(bool)
	def onAddAfter(self, checked):
		createChild, parentIndex, parentItemPath, itemRow, nItems = self.siblingOrChild()
		
		# siblingOrChild() did not allow it
		if createChild is None:
			return
		
		# siblingOrChild() allowed it, but the parent cannot create children
		if not parentItemPath.canCreateChildren():
			return
		
		# Deselect everything
		self.writeSelection([])
		
		ndx = nItems if createChild else itemRow+1
		self.model().createChild(parentIndex, ndx)
		newItemIndex=self.model().index(ndx, 0, parentIndex)
		
		if createChild:
			# Expand parent
			self.setExpanded(parentIndex, True)
		
		# Activate 
		self.writeCurrentIndex(newItemIndex)
		self.writeSelection([newItemIndex])
		
		# Edit
		self.edit(newItemIndex)
		
	
	# Set current item. By default set it to first item. 
	def activateItem(self, index=None):
		if index is None:
			index=self.model().index(0, 0, QModelIndex())
		self.selectionModel().setCurrentIndex(index, QItemSelectionModel.Select)
		
	# Emit when selection changes, list contains the indices of selected items
	treeSelectionChanged=pyqtSignal(list)
	
	# Emit when current item changes
	treeCurrentItemChanged=pyqtSignal(QModelIndex, QModelIndex)
	
	# Deselect previously selected children of different parent
	# Emit selectionChanged signal
	@pyqtSlot(QItemSelection, QItemSelection)
	def handleSelectionChange(self, selected, deselected):
		# Get selection
		selectionModel=self.selectionModel()
		selection=selectionModel.selection()
		current=self.currentIndex()
		parent=current.parent()
		
		# New empty selection
		bad=QItemSelection()
		
		# Are we allowed to select multiple children?
		tp=self.model().treePath(parent)
		if tp is not None and not tp.canSelectMultipleChildren():
			# Can select only one, add all but current index to bad selection
			for index in selection.indexes():
				if index != current:
					bad.select(index, index)
		else:
			# Add all items that don't have the same parent as current index to bad selection
			for index in selection.indexes():
				if index.parent() != parent:
					bad.select(index, index)
		
		# Deselect all items in bad selection
		selectionModel.select(bad, QItemSelectionModel.Deselect)
		
		# Get indexes of all selected items
		indexes=selectionModel.selection().indexes()
		
		# Emit selectionChanged signal
		self.treeSelectionChanged.emit(indexes)
		
		# Adjust availability of actions
		self.contextMenuEnableActions()
		
	@pyqtSlot(QModelIndex, QModelIndex)
	def handleCurrentChange(self, index, previousIndex):
		self.treeCurrentItemChanged.emit(index, previousIndex)
	
	
if __name__=='__main__':
	from pprint import pprint
	import sip 
	import sys
	import sampledata
	from .treeitems import QPTreeItemProjectRoot

	sip.setdestroyonexit(True)
	
	app = QApplication(sys.argv)
	
	w=QWidget()
	vl=QVBoxLayout(w)
	
	tv=QTreeView()
	m=QPTreeModel(QPTreeItemProjectRoot("Project", sampledata.data, sampledata.data), parent=tv)
	tv.setModel(m)
	
	@pyqtSlot(bool)
	def action(checked):
		pprint(sampledata.data)
		m.beginLayoutChange(QModelIndex())
		f1=sampledata.data["files"][0]
		f2=sampledata.data["files"][1]
		print(f1, f2)
		sampledata.data["files"][0]=f2
		sampledata.data["files"][1]=f1
		m.endLayoutChange(QModelIndex())
		pprint(sampledata.data)
	
	vl.addWidget(tv)
	
	b=QPushButton("click", parent=w)
	b.clicked.connect(action)
	
	vl.addWidget(b)
	
	w.show()
	app.exec_()
	
	pprint(sampledata.data)
	
