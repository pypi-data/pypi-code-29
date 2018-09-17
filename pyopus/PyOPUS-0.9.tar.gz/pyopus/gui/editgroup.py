from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .editbase import *
from .table import *
from .clipboard import *

__all__ = [ 'QPGroupTableModel', 'QPGroupTable', 'QPEditGroup' ]


class QPGroupTableModel(QPTableModel):
	def __init__(self, treePath, *args, **kwargs):
		QPTableModel.__init__(self, treePath.data(), *args, **kwargs)
		self.treePath=treePath
	
	def pasteChildren(self, payload, pos=-1):
		if pos<0:
			pos+=self.rowCount()+1
			
		nItems=len(payload[1])
		
		# Paste
		self.beginInsertRows(QModelIndex(), pos, pos+nItems-1)
		ndxs=self.treePath.pasteChildren(payload, pos)
		self.endInsertRows()
		
		return ndxs
	
class QPGroupTable(QPTable):
	def __init__(self, *args, **kwargs):
		QPTable.__init__(self, selectionBehavior=QAbstractItemView.SelectRows, *args, **kwargs)
	
	def writeRowSelection(self, rowIndexes):
		sm=self.table_view.selectionModel()
		sm.clear()
		for rowIndex in rowIndexes:
			sm.select(
				self.table_model.index(rowIndex, 0), 
				QItemSelectionModel.Select|QItemSelectionModel.Rows
			)
	
	def contextMenuEnableActions(self):
		selection=self.readSelectedIndexes()
		current=self.readCurrentIndex()
		selectedRows=self.rowIndexes(selection)
		ppos=self.pastePosition()
		rowCount=self.table_model.rowCount(QModelIndex())
		ptp=self.table_model.treePath
		pos=self.pastePosition()
		
		canCopy=self.canCopy and len(selection)>0 and ptp.canCopyChildren()
		canCut=self.canCopy and not self.read_only and len(selection)>0
		canPaste=self.canPaste and not self.read_only and ppos is not None
		canClear=not self.read_only and len(selection)>0 and False
		canDelete=not self.read_only and self.canDelete and len(selection)>0 and ptp.canDeleteChildren()
		canMove=not self.read_only and self.canMove and len(selection)>0 and ptp.canMoveChildren()
		canCreate=not self.read_only and self.canCreate and ptp.canCreateChildren()
		
		self.copyAction.setEnabled(canCopy)
		self.cutAction.setEnabled(canCopy and canDelete)
		self.pasteAction.setEnabled(canPaste)
		self.clearAction.setEnabled(canClear)
		self.removeRowsAction.setEnabled(canDelete)
		self.moveUpAction.setEnabled(canMove and min(selectedRows)>0)
		self.moveDownAction.setEnabled(canMove and max(selectedRows)<rowCount-1)
		self.addBeforeAction.setEnabled(canCreate)
		self.addAfterAction.setEnabled(canCreate)
		
	@pyqtSlot(bool)
	def onCopy(self, checked):
		parentPath=self.table_model.treePath
		
		# Get selected row indices
		selection=self.readSelectedIndexes()
		
		# No selection
		if len(selection)<=0:
			return
		
		childNdxs=self.rowIndexes(selection)
		
		# Copy to clipboard
		payload=parentPath.copyChildren(childNdxs)
		treeToClipboard(payload)
	
	@pyqtSlot(bool)
	def onCut(self, checked):
		self.onCopy(checked)
		self.onDeleteSelectedRows(checked)
	
	# Calculate paste position based on mime type (without unpacking data)
	# Returns position
	# Returns None when the clipboard content cannot be pasted
	def pastePosition(self):
		lcItemClassName=lcTreeItemClassNameOnClipboard()
		if lcItemClassName is None:
			return None
		
		# Get current item row, column position or None if no current item
		current = self.readCurrentIndex()
		
		# Get row, column
		currentRow, currentCol = current if current is not None else (None, None)
		
		selection=self.readSelectedIndexes()
		selectedRows=self.rowIndexes(selection)
		
		# Paste position
		# Try with selection first, then current index, finally default to beginning
		if len(selectedRows)==1:
			# Paste after selected item
			pasteAt=selectedRows[0]+1
		elif len(selectedRows)>1:
			# More than one item selected, paste after last item
			pasteAt=max(selectedRows)+1
		elif currentRow is not None:
			# No selection, paste after active item
			pasteAt=currentRow+1
		else: 
			# Give up
			return None
			
		# Check subtree compatibility
		if not self.table_model.treePath.canPasteChildren(lcItemClassName, pasteAt):
			return None
		
		return pasteAt
		
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
		pos=self.pastePosition()
		if pos is None:
			return
		
		# Paste
		ndxs=self.table_model.pasteChildren(payload, pos)
		
		# Update table display
		self.table_view.computeSizeHint()
		self.table_view.updateGeometry()
		
		# Set selection
		self.writeRowSelection(ndxs)
		self.writeCurrentIndex((min(ndxs),0))
		
		
class QPEditGroup(QPEditBase):
	def __init__(self, ModelClass, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		self.treePath=treePath
		
		self.model=ModelClass(treePath, parent=self)
		
		# Connect signals from table model and emit own signals for notifying the outside world
		self.model.dataChanged.connect(self.handleDataChanged)
		self.model.rowsAboutToBeRemoved.connect(self.handleRowsAboutToBeRemoved)
		self.model.rowsAboutToBeInserted.connect(self.handleRowsAboutToBeInserted)
		self.model.rowsAboutToBeMoved.connect(self.handleRowsAboutToBeMoved)
		
		self.model.rowsRemoved.connect(self.handleRowsRemoved)
		self.model.rowsInserted.connect(self.handleRowsInserted)
		self.model.rowsMoved.connect(self.handleRowsMoved)
	
	# Refresh editor request from outside, somebody else changed our data
	def refreshView(self):
		for m, v in self.modelView:
			if type(v) is QDataWidgetMapper:
				# QDataWidgetMapper must be set to first (and only) entry
				v.toFirst()
			else:
				# The structure can change with tree manipulations, a rebuild is required
				# Widgets must implement reset() method which is invoked here
				v.reset()
	
	# Notifications for outside world that we changed their data
	
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def handleDataChanged(self, topLeftIndex, bottomRightIndex, roles=[]):
		self.childrenChanged.emit(topLeftIndex.row(), bottomRightIndex.row())
	
	
	@pyqtSlot(QModelIndex, int, int)
	def handleRowsAboutToBeRemoved(self, parentIndex, first, last):
		self.structureAboutToBeChanged.emit()
	
	@pyqtSlot(QModelIndex, int, int)
	def handleRowsAboutToBeInserted(self, parentIndex, first, last):
		self.structureAboutToBeChanged.emit()
	
	@pyqtSlot(QModelIndex, int, int, QModelIndex, int)
	def handleRowsAboutToBeMoved(self, sourceIndex, first, last, destinationIndex, position):
		self.structureAboutToBeChanged.emit()
	
	
	@pyqtSlot(QModelIndex, int, int)
	def handleRowsRemoved(self, parentIndex, first, last):
		self.structureChanged.emit()
	
	@pyqtSlot(QModelIndex, int, int)
	def handleRowsInserted(self, parentIndex, first, last):
		self.structureChanged.emit()
	
	@pyqtSlot(QModelIndex, int, int, QModelIndex, int)
	def handleRowsMoved(self, sourceIndex, first, last, destinationIndex, position):
		self.structureChanged.emit()
	
