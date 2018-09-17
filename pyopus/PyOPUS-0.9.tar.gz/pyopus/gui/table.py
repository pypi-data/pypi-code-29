''' 
Editable grid. 
'''
import operator
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from copy import deepcopy
from .. import PyOpusError

from .clipboard import isQPTableOnClipboard, tableFromClipboard, tableToClipboard


__all__ = [ 'QPTable', 'QPTableModel' ]


# TODO: if tab is pressed on bottom right cell a new row is added at the bottom
# TODO: sorting together with tree display
# TODO: cursor position after remove rows above/below last position 
# TODO: enable/disable actions in menu on selection change

# A QTableView with a size hint
# Horizontally and vertically we define a minimum size and a size hint
# Vertically we set a fixed size (minimum=maximum) 
class QSHTableView(QTableView):
	def __init__(self, parent=None, *args):
		QTableView.__init__(self, parent=parent, *args)
	
	sh=None
	
	def computeSizeHint(self):
		w = self.verticalHeader().width() + self.frameWidth()*2
		#   + self.horizontalHeader().width()
		h = self.horizontalHeader().height() + self.frameWidth()*2 
		#   + self.table_view.verticalHeader().length() 
		for i in range(self.model().rowCount(QModelIndex())):
			h += self.rowHeight(i)
		for i in range(self.model().columnCount(QModelIndex())):
			w += self.columnWidth(i)
		self.sh=(w,h)
		
	def minimumSizeHint(self):
		if self.sh is None:
			self.computeSizeHint()
			
		self.setMaximumHeight(self.sh[1])
		return QSize(self.sh[0], self.sh[1])
	
	def sizeHint(self):
		return self.minimumSizeHint()
	
	
# An editable QTableView with control buttons		
class QPTable(QWidget):
	def __init__(
		self, model, stretch=None, buttons=False, 
		 canDelete=True, canCreate=True, canMove=True, 
		 canCopy=True, canPaste=True, extendOnPaste=True, 
		 selectionBehavior=QAbstractItemView.SelectItems, 
		 parent=None, *args
	):
		QWidget.__init__(self, parent=parent, *args)
		
		self.canDelete=canDelete
		self.canCreate=canCreate
		self.canMove=canMove
		
		self.canCopy=canCopy
		self.canPaste=canPaste
		self.extendOnPaste=extendOnPaste
		
		self.buttons=buttons
		
		self.read_only=False
		
		# self.table_model = QPTableModel(self, data_list, header, dfl)
		self.table_view = QSHTableView(parent=self)
		self.table_view.setSelectionBehavior(selectionBehavior)
		self.setModel(model)
		self.storedEditTriggers=self.table_view.editTriggers()
		
		# Decrease row height
		self.table_view.verticalHeader().setDefaultSectionSize(
			self.table_view.verticalHeader().minimumSectionSize()+3
		)
		
		if stretch is not None:
			for ii in range(len(stretch)):
				if stretch[ii]:
					self.table_view.horizontalHeader().setSectionResizeMode(ii, QHeaderView.Stretch)
		
		self.table_view.horizontalHeader().sortIndicatorChanged.connect(
			self.handleSortIndicatorChanged
		)
		layout = QVBoxLayout(self)
		layout.setContentsMargins(0, 0, 0, 0)
		# layout.setSpacing(2)
		layout.addWidget(self.table_view)
		
		# Prepare actions
		self.cutAction=QAction("Cut", self)
		self.cutAction.setShortcut(QKeySequence.Cut)
		self.cutAction.setStatusTip("Move cells to clipboard")
		self.cutAction.triggered.connect(self.onCut)
		self.cutAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.copyAction=QAction("Copy", self)
		self.copyAction.setShortcut(QKeySequence.Copy)
		self.copyAction.setStatusTip("Copy cells to clipboard")
		self.copyAction.triggered.connect(self.onCopy)
		self.copyAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.pasteAction=QAction("Paste", self)
		self.pasteAction.setShortcut(QKeySequence.Paste)
		self.pasteAction.setStatusTip("Paste cells from clipboard")
		self.pasteAction.triggered.connect(self.onPaste)
		self.pasteAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.selectAllAction=QAction("Select all", self)
		self.selectAllAction.setShortcut(QKeySequence.SelectAll)
		self.selectAllAction.setStatusTip("Select all cells")
		self.selectAllAction.triggered.connect(self.onSelectAll)
		self.selectAllAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.invertSelectionAction=QAction("Invert selection", self)
		self.invertSelectionAction.setShortcut(QKeySequence("Ctrl+I"))
		self.invertSelectionAction.setStatusTip("Invert selection")
		self.invertSelectionAction.triggered.connect(self.onInvertSelection)
		self.invertSelectionAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.addBeforeAction=QAction("Add row before", self)
		self.addBeforeAction.setShortcuts([
			QKeySequence("Ctrl+Shift+Return"), 
			QKeySequence("Ctrl+Shift+Enter")
		])
		self.addBeforeAction.setStatusTip("Add row before")
		self.addBeforeAction.triggered.connect(self.onAddBefore)
		self.addBeforeAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.addAfterAction=QAction("Add row after", self)
		self.addAfterAction.setShortcuts([
			QKeySequence("Ctrl+Return"), 
			QKeySequence("Ctrl+Enter")
		])
		self.addAfterAction.setStatusTip("Add row after")
		self.addAfterAction.triggered.connect(self.onAddAfter)
		self.addAfterAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.clearAction=QAction("Clear cells", self)
		self.clearAction.setShortcut(QKeySequence.Delete)
		self.clearAction.setStatusTip("Clear cell contents")
		self.clearAction.triggered.connect(self.onClear)
		self.clearAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.removeRowsAction=QAction("Remove rows", self)
		self.removeRowsAction.setShortcut(QKeySequence("Ctrl+Delete"))
		self.removeRowsAction.setStatusTip("Remove rows")
		self.removeRowsAction.triggered.connect(self.onDeleteSelectedRows)
		self.removeRowsAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.moveUpAction=QAction("Move rows up", self)
		self.moveUpAction.setShortcut(QKeySequence("Ctrl+Shift+Up"))
		self.moveUpAction.setStatusTip("Move rows up")
		self.moveUpAction.triggered.connect(self.onMoveSelectedRowsUp)
		self.moveUpAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.moveDownAction=QAction("Move rows down", self)
		self.moveDownAction.setShortcut(QKeySequence("Ctrl+Shift+Down"))
		self.moveDownAction.setStatusTip("Move rows down")
		self.moveDownAction.triggered.connect(self.onMoveSelectedRowsDown)
		self.moveDownAction.setShortcutContext(Qt.WidgetWithChildrenShortcut)
		
		self.addAction(self.cutAction)
		self.addAction(self.copyAction)
		self.addAction(self.pasteAction)
		self.addAction(self.selectAllAction)
		self.addAction(self.invertSelectionAction)
		self.addAction(self.addBeforeAction)
		self.addAction(self.addAfterAction)
		self.addAction(self.clearAction)
		self.addAction(self.removeRowsAction)
		self.addAction(self.moveUpAction)
		self.addAction(self.moveDownAction)
		
		if self.buttons:
			hlayout = QHBoxLayout()
			
			self.buttonSelectAll=QPushButton("", self)
			self.buttonSelectAll.setText(self.selectAllAction.text())
			self.buttonSelectAll.clicked.connect(self.selectAllAction.trigger)
			self.buttonSelectAll.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
			hlayout.addWidget(self.buttonSelectAll)
			
			self.buttonInvertSelection=QPushButton("", self)
			self.buttonInvertSelection.setText(self.invertSelectionAction.text())
			self.buttonInvertSelection.clicked.connect(self.invertSelectionAction.trigger)
			self.buttonInvertSelection.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
			hlayout.addWidget(self.buttonInvertSelection)
			
			if self.canCreate:
				self.buttonAddBefore=QPushButton("", self)
				self.buttonAddBefore.setText(self.addBeforeAction.text())
				self.buttonAddBefore.clicked.connect(self.addBeforeAction.trigger)
				self.buttonAddBefore.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
				hlayout.addWidget(self.buttonAddBefore)
				
				self.buttonAddAfter=QPushButton("", self)
				self.buttonAddAfter.setText(self.addAfterAction.text())
				self.buttonAddAfter.clicked.connect(self.addAfterAction.trigger)
				self.buttonAddAfter.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
				hlayout.addWidget(self.buttonAddAfter)
			
			self.buttonClear=QPushButton("", self)
			self.buttonClear.setText(self.clearAction.text())
			self.buttonClear.clicked.connect(self.clearAction.trigger)
			self.buttonClear.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
			hlayout.addWidget(self.buttonClear)
			
			if self.canDelete:
				self.buttonRemoveRows=QPushButton("", self)
				self.buttonRemoveRows.setText(self.removeRowsAction.text())
				self.buttonRemoveRows.clicked.connect(self.removeRowsAction.trigger)
				self.buttonRemoveRows.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
				hlayout.addWidget(self.buttonRemoveRows)
			
			hlayout.addStretch(1)
			layout.addLayout(hlayout)
			
		self.setLayout(layout)
		
		# set column width to fit contents (set font first!)
		self.table_view.setVisible(False)
		self.table_view.resizeColumnsToContents()
		self.table_view.setVisible(True)
		
		# Set read_only mode (enable/disable actions and buttons)
		self.setReadOnly(self.read_only)
		
		self.table_view.selectionModel().selectionChanged.connect(self.handleSelectionChange)
	
	@pyqtSlot(QItemSelection, QItemSelection)
	def handleSelectionChange(self, selected, deselected):
		# selectionModel=self.selectionModel()
		# selection=selectionModel.selection()
		# indexes=selection.indexes()
		self.contextMenuEnableActions()
		
	def setIndexWidget(self, row, column, w):
		self.table_view.setIndexWidget(
			self.table_view.model().index(row, column, QModelIndex()), 
			w 
		)
		
	# Commit data that is being edited
	def submit(self):
		ndx=self.table_view.currentIndex()
		self.table_view.setCurrentIndex(QModelIndex())
		self.table_view.setCurrentIndex(ndx)
		
	# readOnly property
	def getReadOnly(self):
		return self.read_only
	
	def setReadOnly(self, value):
		self.read_only=value
		if value is True:
			self.storedEditTriggers=self.table_view.editTriggers()
			self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
		else:
			self.table_view.setEditTriggers(self.storedEditTriggers)
		
		self.contextMenuEnableActions()
		
		# Enable/disable buttons
		if self.buttons:
			if self.canCreate:
				self.buttonAddBefore.setEnabled(not self.read_only)
				self.buttonAddAfter.setEnabled(not self.read_only)
			self.buttonClear.setEnabled(not self.read_only)
			if self.canDelete:
				self.buttonRemoveRows.setEnabled(not self.read_only)
			
	readOnly=pyqtProperty(bool, getReadOnly, setReadOnly)
	
	
	# dataModel property
	def getDataModel(self):
		return self.table_model
	
	dataModel=pyqtProperty(QVariant, getDataModel)
	
	
	def horizontalHeader(self):
		return self.table_view.horizontalHeader()
	
	def verticalHeader(self):
		return self.table_view.verticalHeader()
	
	def reset(self):
		self.table_view.reset()
	
	def setItemDelegateForColumn(self, col, delegate):
		self.table_view.setItemDelegateForColumn(col, delegate)
		
	def setModel(self, model):
		self.table_model=model
		self.table_view.setModel(model)
		self.table_view.setSortingEnabled(self.table_model.sortable())
		
	def readSelectedIndexes(self):
		ix=self.table_view.selectionModel().selectedIndexes()
		return [(ndx.row(),ndx.column()) for ndx in ix]
	
	def readSelectedData(self, ndxs):
		data=[]
		m=self.table_model
		for row, col in ndxs:
			val=m.data(self.table_model.index(row, col), Qt.EditRole)
			if type(val)==QVariant:
				val=val.value()
			data.append(val)
		
		return data
	
	def selectionRange(self, ndxs):
		rmin=None
		rmax=None
		cmin=None
		cmax=None
		for row, col in ndxs:
			rmin=row if rmin is None or row<rmin else rmin
			rmax=row if rmax is None or row>rmax else rmax
			cmin=col if cmin is None or col<cmin else cmin
			cmax=col if cmax is None or col>cmax else cmax
		
		h=(rmax-rmin+1) if rmax is not None else 0
		w=(cmax-cmin+1) if cmax is not None else 0
		
		return rmin, cmin, h, w
	
	def normalizeSelection(self, ndxs, rmin, cmin):
		return [ [entry[0]-rmin, entry[1]-cmin ] for entry in ndxs ]
	
	def readCurrentIndex(self):
		ix=self.table_view.selectionModel().currentIndex()
		if ix.isValid():
			return ix.row(), ix.column()
		else: 
			return None
	
	def updateIndexesOnInsertRow(self, ndxs, pos):
		for ii in range(len(ndxs)):
			if ndxs[ii] is not None:
				row, col = ndxs[ii]
				if pos<=row:
					ndxs[ii]=(row+1,col)
	
	def updateIndexesOnDeleteRow(self, ndxs, pos):
		for ii in range(len(ndxs)):
			if ndxs[ii] is not None:
				row, col = ndxs[ii]
				if pos<row:
					ndxs[ii]=(row-1,col)
				elif pos==row:
					ndxs[ii]=None
	
	def updateIndexesOnMoveRows(self, ndxs, delta):
		for ii in range(len(ndxs)):
			ndxs[ii]=(ndxs[ii][0]+delta, ndxs[ii][1])
		
	def rowIndexes(self, indexes):
		ii=[ndx[0] for ndx in indexes]
		ii=list(set(ii))
		ii.sort()
		return ii
	
	def writeCurrentIndex(self, index):
		if index is not None:
			row, col = index
			self.table_view.selectionModel().setCurrentIndex(
				self.table_model.index(row, col) if index is not None else QModelIndex(), 
				QItemSelectionModel.NoUpdate
			)
	
	def writeSelection(self, indexes):
		sm=self.table_view.selectionModel()
		sm.clear()
		for index in indexes:
			if index is not None:
				row, col = index
				sm.select(self.table_model.index(row, col), QItemSelectionModel.Select)
	
	def contextMenuEnableActions(self):
		selection=self.readSelectedIndexes()
		current=self.readCurrentIndex()
		selectedRows=self.rowIndexes(selection)
		ppos=self.pastePosition()
		rowCount=self.table_model.rowCount(QModelIndex())
		
		canCopy=self.canCopy and len(selection)>0
		canCut=self.canCopy and not self.read_only and len(selection)>0
		canPaste=self.canPaste and not self.read_only and ppos is not None
		canClear=not self.read_only and len(selection)>0
		canDelete=not self.read_only and self.canDelete and len(selection)>0
		canMove=not self.read_only and self.canMove and len(selection)>0
		canCreate=not self.read_only and self.canCreate
		
		self.copyAction.setEnabled(canCopy)
		self.cutAction.setEnabled(canCut)
		self.pasteAction.setEnabled(canPaste)
		self.clearAction.setEnabled(canClear)
		self.removeRowsAction.setEnabled(canDelete)
		self.moveUpAction.setEnabled(canMove and min(selectedRows)>0)
		self.moveDownAction.setEnabled(canMove and max(selectedRows)<rowCount-1)
		self.addBeforeAction.setEnabled(canCreate)
		self.addAfterAction.setEnabled(canCreate)
		
	def contextMenuEvent(self, event):
		self.menu=QMenu(self)
		
		self.menu.addAction(self.cutAction)
		self.menu.addAction(self.copyAction)
		self.menu.addAction(self.pasteAction)
		
		self.menu.addAction(self.selectAllAction)
		self.menu.addAction(self.invertSelectionAction)
		
		self.menu.addAction(self.clearAction)
			
		self.menu.addAction(self.removeRowsAction)
			
		self.menu.addAction(self.moveUpAction)
		self.menu.addAction(self.moveDownAction)
		
		self.menu.addAction(self.addBeforeAction)
		self.menu.addAction(self.addAfterAction)
		
		self.contextMenuEnableActions()
		
		self.menu.popup(QCursor.pos())
	
	def refreshView(self):
		self.table_model.forceRefresh()
		
	# TODO: fix bool
	@pyqtSlot(int, Qt.SortOrder)
	def handleSortIndicatorChanged(self, index, order):
		if index not in self.table_model.sortingIndices:
			self.table_view.horizontalHeader().setSortIndicatorShown(False)
		else:
			self.table_view.horizontalHeader().setSortIndicatorShown(True)
	
	@pyqtSlot(bool)
	def onAddBefore(self, checked):
		if self.read_only:
			return
		
		selection=self.readSelectedIndexes()
		current=self.readCurrentIndex()
		ndxs=self.rowIndexes(selection)
		indexes=selection+[current]
		
		if len(ndxs)==0:
			self.table_model.addRow(0)
			self.updateIndexesOnInsertRow(indexes, 0)
		else:
			for ndx in reversed(sorted(ndxs)):
				self.table_model.addRow(ndx)
				self.updateIndexesOnInsertRow(indexes, ndx)
		
		self.writeSelection(indexes[:-1])
		self.writeCurrentIndex(indexes[-1])
		
		# Inform the layout the size hint of QTableView has changed
		self.table_view.computeSizeHint()
		self.table_view.updateGeometry()
		
	@pyqtSlot(bool)
	def onAddAfter(self, checked):
		if self.read_only:
			return
		
		selection=self.readSelectedIndexes()
		current=self.readCurrentIndex()
		ndxs=self.rowIndexes(selection)
		indexes=selection+[current]
		
		index=self.table_view.selectionModel().currentIndex()
		atRow=index.row()
		atCol=index.column()
		
		if len(ndxs)==0:
			self.table_model.addRow(-1)
		else:
			for ndx in reversed(sorted(ndxs)):
				self.table_model.addRow(ndx+1)
				self.updateIndexesOnInsertRow(indexes, ndx+1)
		
		self.writeSelection(indexes[:-1])
		self.writeCurrentIndex(indexes[-1])
		
		# Inform the layout the size hint of QTableView has changed
		self.table_view.computeSizeHint()
		self.table_view.updateGeometry()
		
	@pyqtSlot(bool)
	def onClear(self, checked):
		if self.read_only:
			return
		
		ndxs=self.readSelectedIndexes()
		
		if len(ndxs)>0:
			self.table_model.clearCells(ndxs)
		
		# Inform the layout the size hint of QTableView has changed
		self.table_view.computeSizeHint()
		self.table_view.updateGeometry()
		
	@pyqtSlot(bool)
	def onDeleteSelectedRows(self, checked):
		if self.read_only:
			return
		
		selection=self.readSelectedIndexes()
		current=self.readCurrentIndex()
		ndxs=self.rowIndexes(selection)
		indexes=selection+[current]
		
		for ndx in reversed(sorted(ndxs)):
			self.table_model.deleteRow(ndx)
			self.updateIndexesOnDeleteRow(indexes, ndx)
		
		self.writeSelection(indexes[:-1])
		self.writeCurrentIndex(indexes[-1])
		
		# Inform the layout the size hint of QTableView has changed
		self.table_view.computeSizeHint()
		self.table_view.updateGeometry()
	
	@pyqtSlot(bool)
	def onMoveSelectedRowsUp(self, checked):
		if self.read_only:
			return
		
		selection=self.readSelectedIndexes()
		current=self.readCurrentIndex()
		ndxs=self.rowIndexes(selection)
		indexes=selection+[current]
		
		ndxs=sorted(ndxs)
		if len(ndxs)<=0:
			return
		lowestNdx=ndxs[0]
		if lowestNdx<=0:
			return
		
		for ndx in ndxs:
			self.table_model.moveRow(ndx, ndx-1)
			
		self.updateIndexesOnMoveRows(indexes, -1)
		
		self.writeSelection(indexes[:-1])
		self.writeCurrentIndex(indexes[-1])
		
		# Inform the layout the size hint of QTableView has changed
		self.table_view.computeSizeHint()
		self.table_view.updateGeometry()
	
	@pyqtSlot(bool)
	def onMoveSelectedRowsDown(self, checked):
		if self.read_only:
			return
		
		selection=self.readSelectedIndexes()
		current=self.readCurrentIndex()
		ndxs=self.rowIndexes(selection)
		indexes=selection+[current]
		
		ndxs=sorted(ndxs)
		if len(ndxs)<=0:
			return
		highestNdx=ndxs[-1]
		ndxs=reversed(ndxs)
		if highestNdx>=self.table_model.rowCount(QModelIndex())-1:
			return
		
		for ndx in ndxs:
			self.table_model.moveRow(ndx, ndx+2)
			
		self.updateIndexesOnMoveRows(indexes, 1)
		
		self.writeSelection(indexes[:-1])
		self.writeCurrentIndex(indexes[-1])
		
		# Inform the layout the size hint of QTableView has changed
		self.table_view.computeSizeHint()
		self.table_view.updateGeometry()
	
	def copyEngine(self):
		ndxs=self.readSelectedIndexes()
		data=self.readSelectedData(ndxs)
		
		r,c,h,w = self.selectionRange(ndxs)
		if w>0 and h>0:
			nsel=self.normalizeSelection(ndxs, r, c)
			tableToClipboard([nsel,data])
			
			return ndxs, data
	
		return None, None
	
	@pyqtSlot(bool)
	def onCut(self, checked):
		ndxs, data = self.copyEngine()
		if ndxs is not None and len(ndxs)>0:
			self.table_model.clearCells(ndxs)
		
	@pyqtSlot(bool)
	def onCopy(self, checked):
		ndxs, data = self.copyEngine()
	
	def pastePosition(self):
		# Is a QPTable on clipboard
		if not isQPTableOnClipboard():
			return None
		
		# Get selection
		ndxs=self.readSelectedIndexes()
		r,c,h,w = self.selectionRange(ndxs)
		
		if r is not None and c is not None:
			return self.table_model.index(r, c, QModelIndex())
		else:
			return None
	
	@pyqtSlot(bool)
	def onPaste(self, checked):
		if not isQPTableOnClipboard():
			return
		
		# Get data from clipboard
		ndxs, data = tableFromClipboard()
		
		# Get paste position
		pos=self.pastePosition()
		if pos is None:
			return
		
		# Position (top, left)
		pr=pos.row()
		pc=pos.column()
		
		# Row and column count
		nr=self.table_model.rowCount()
		nc=self.table_model.columnCount()
		
		# Create additional rows at the end
		r,c,h,w = self.selectionRange(ndxs)
		if pr+h>nr and self.extendOnPaste:
			for ii in range(pr+h-nr):
				self.table_model.addRow(-1)
			
			# Inform the layout the size hint of QTableView has changed
			self.table_view.computeSizeHint()
			self.table_view.updateGeometry()
				
			# New row count
			nr=self.table_model.rowCount()
		
		# Paste
		endSel=[]
		for (r, c), d in zip(ndxs, data):
			rw=r+pr
			cw=c+pc
			# Skip if outside of table
			if rw>=nr or cw>=nc:
				continue
			self.table_model.setData(
				self.table_model.index(rw, cw, QModelIndex()), 
				d, Qt.DisplayRole
			)
			endSel.append((rw,cw))
			
		# Set selection
		self.writeSelection(endSel)
		
		# Set cursor position to paste position
		self.table_view.setCurrentIndex(pos)
	
	@pyqtSlot(bool)
	def onSelectAll(self, checked):
		sel=QItemSelection()
		sel.select(
			self.table_model.index(0,0), 
			self.table_model.index(self.table_model.rowCount(QModelIndex())-1, self.table_model.columnCount(QModelIndex())-1)
		)
		self.table_view.selectionModel().select(sel, QItemSelectionModel.Select)
		
	@pyqtSlot(bool)
	def onInvertSelection(self, checked):
		sel=QItemSelection()
		sel.select(
			self.table_model.index(0,0), 
			self.table_model.index(self.table_model.rowCount(QModelIndex())-1, self.table_model.columnCount(QModelIndex())-1)
		)
		self.table_view.selectionModel().select(sel, QItemSelectionModel.Toggle)
	
	def extendData(self, data):
		self.table_model.extendData(data)
		
		# Inform the layout the size hint of QTableView has changed
		self.table_view.computeSizeHint()
		self.table_view.updateGeometry()
	

class QPTableModel(QAbstractTableModel):
	def __init__(self, mylist, header, editable=None, dfl=None, sortingIndices=[], parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.mylist = mylist
		self.header = header
		self.editable = editable
		if type(dfl) in [list, tuple] and len(dfl)==0:
			dfl=['']*len(header)
		self.dfl=dfl
		self.sortingIndices=sortingIndices
		
		self.read_only=False
	
	def dataTable(self):
		return self.mylist
	
	def extendData(self, data):
		i1=len(self.mylist)
		n=len(data)
		self.beginInsertRows(QModelIndex(), i1, i1+n-1)
		self.mylist.extend(data)
		self.endInsertRows()
		
	# readOnly property
	def getReadOnly(self):
		return self.read_only
	
	def setReadOnly(self, flag=True):
		self.read_only=flag
	
	readOnly=pyqtProperty(bool, getReadOnly, setReadOnly)
	
	def formatForDisplay(self, data):
		if type(data) is QVariant:
			data=data.value()
		
		if type(data) is int:
			return data
		elif type(data) is float:
			return ("%g"%data)
		else:
			return data
		# Under Python 2 this handled unicode -> str
		# No longer needed because str is unicode now
		#else:
		#	return data.encode("utf-8")
		
	def rowCount(self, parent=QModelIndex()):
		return len(self.mylist)
	
	def columnCount(self, parent=QModelIndex()):
		return len(self.header)
	
	def data(self, index, role):
		if not index.isValid():
			return None
		elif role == Qt.DisplayRole or role == Qt.EditRole:
			return QVariant(self.formatForDisplay(self.mylist[index.row()][index.column()]))
		else:
			return None
	
	def headerData(self, ii, orientation, role):
		if orientation == Qt.Horizontal and role == Qt.DisplayRole:
			return self.header[ii]
		elif orientation == Qt.Vertical and role == Qt.DisplayRole:
			return ii+1
		return None
	
	def sortable(self):
		return len(self.sortingIndices)>0
	
	def sort(self, col, order):
		"""sort table by given column number col"""
		if self.read_only:
			return
		
		if col not in self.sortingIndices:
			return
		
		# Build a move program
		moves=[]
		items=[x[col] for x in self.mylist]
		itemToMove=None
		for jj in range(len(self.mylist)-1):
			for ii in range(jj, len(self.mylist)):
				# Find smallest/largest element
				if (
					itemToMove is None or 
					(order==Qt.AscendingOrder and items[ii]<items[itemToMove]) or
					(order==Qt.DescendingOrder and items[ii]>items[itemToMove])
				):
					itemToMove=ii
			moves.append((itemToMove, jj))
		
		# Run move program
		for move in moves:
			self.moveRow(move[0], move[1])
		
	def addRow(self, position=-1):
		if self.read_only:
			return
		
		if self.dfl is None:
			return
		
		if position<0:
			position=len(self.mylist)+position+1
		if position<0 or position>len(self.mylist):
			raise PyOpusError("Bad index in addRow()")
		self.beginInsertRows(QModelIndex(), position, position)
		self.mylist.insert(position, deepcopy(self.dfl))
		self.endInsertRows()
			
	def clearCells(self, positions):
		if self.read_only:
			return
		
		for position in positions:
			row, col = position
			if self.editable is not None and not self.editable[col]:
				return
			
		for position in positions:
			row, col = position
			if row<0:
				row=len(self.mylist)+row
			if row<0 or row>=len(self.mylist):
				raise PyOpusError("Bad index in clearCells()")
			if col<0:
				col=len(self.header)+col
			if col<0 or col>=len(self.header):
				raise PyOpusError("Bad index in clearCells()")
			self.setData(self.index(row, col), "", Qt.DisplayRole)
		
	def deleteRow(self, position):
		if self.read_only:
			return
		
		if position<0:
			position=len(self.mylist)+position
		if position<0 or position>=len(self.mylist):
			raise PyOpusError("Bad index in deleteRow()")
		self.beginRemoveRows(QModelIndex(), position, position)
		del self.mylist[position]
		self.endRemoveRows()
		
	def moveRow(self, sourceNdx, destinationNdx):
		if self.read_only:
			return
		
		if sourceNdx<0:
			sourceNdx=len(self.mylist)+sourceNdx
		if sourceNdx<0 or sourceNdx>len(self.mylist):
			raise PyOpusError("Bad index in moveRow()")
		if destinationNdx<0:
			destinationNdx=len(self.mylist)+destinationNdx
		if destinationNdx<0 or destinationNdx>len(self.mylist):
			raise PyOpusError("Bad index in moveRow()")
		self.beginMoveRows(QModelIndex(), sourceNdx, sourceNdx, QModelIndex(), destinationNdx)
		el=self.mylist[sourceNdx]
		self.mylist.insert(destinationNdx, el)
		if sourceNdx<=destinationNdx:
			self.mylist.pop(sourceNdx)
		else:
			self.mylist.pop(sourceNdx+1)
		self.endMoveRows()
		
	def forceRefresh(self):
		self.dataChanged.emit(
			self.index(0, 0, QModelIndex()), 
			self.index(self.rowCount(QModelIndex())-1,self.columnCount(QModelIndex())-1, QModelIndex())
		)
		
	def setData(self, index, value, role):
		if self.read_only:
			return False
		if self.editable is not None and not self.editable[index.column()]:
			return False
		
		# Write and emit signals only when data is really changed
		if self.mylist[index.row()][index.column()]!=value:
			self.mylist[index.row()][index.column()]=value 
			self.dataChanged.emit(index, index)
			
		return True
		
	def flags(self, index):
		f = Qt.ItemIsEnabled | Qt.ItemIsSelectable 
		if not self.read_only:
			if self.editable is not None:
				if type(self.editable) is list:
					if self.editable[index.column()]:
						f = f | Qt.ItemIsEditable
				elif self.editable:
					f = f | Qt.ItemIsEditable
			else:
				f = f | Qt.ItemIsEditable
		return f

if __name__=='__main__':
	from pprint import pprint
	import sip 
	import sys
	sip.setdestroyonexit(True)

	# the solvent data ...
	header = ['Solvent Name', ' BP (deg C)', ' MP (deg C)', ' Density (g/ml)']

	# use numbers for numeric data to sort properly
	data_list1 = [
		['ACETIC ACID', 117.9, 16.7, 1.049],
		['ACETIC ANHYDRIDE', 140.1, -73.1, 1.087],
		['ACETONE', 56.3, -94.7, 0.791],
		['ACETONITRILE', 81.6, -43.8, 0.786],
	]

	# use numbers for numeric data to sort properly
	data_list2 = [
		['ACETIC ACID', 117.9, 16.7, 1.049],
		['ACETIC ANHYDRIDE', 140.1, -73.1, 1.087],
		['ACETONE', 56.3, -94.7, 0.791],
		['ACETONITRILE', 81.6, -43.8, 0.786],
	]
	
	class MW(QWidget):
		def __init__(self, parent=None, *args):
			QWidget.__init__(self, parent=parent, *args)
			
			self.w1=QPTable(
				QPTableModel(data_list1, header, sortingIndices=[], parent=self), 
				buttons=True, parent=self
			)
			self.w2=QPTable(
				QPTableModel(data_list2, header, sortingIndices=[0], parent=self), 
				buttons=True, parent=self
			)
			
			layout = QVBoxLayout(self)
			# Layout should set the minimum and maximum size of the widget
			layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
			layout.addWidget(self.w1)
			layout.addWidget(self.w2)
			# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
			layout.addStretch(1)
			self.setLayout(layout)
			
			

	app = QApplication(sys.argv)
	
	# Create scroll area
	sa=QScrollArea()
	sa.setWindowTitle("Table view demo")
	sa.setWidgetResizable(True)
	
	# Add widget
	win=MW()
	sa.setWidget(win)
	
	# Show and run
	sa.show()
	app.exec_()
	
	# Print data
	pprint(data_list1)
	pprint(data_list2)
	
