from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

__all__ = [ 'QPEditBase' ]


class QPEditBase(QWidget):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QWidget.__init__(self, parent=parent, *args)
		# Tree path and data
		self.treePath=treePath
		self.data=treePath.data() if treePath is not None else None
		self.rootData=treePath.rootData() if treePath is not None else None
		
		# Logger
		self.logger=logger
		
		# List fo view widgets
		self.modelView=[]
	
	# Cleanup function
	def destroy(self):
		pass
	
	def rootTreePath(self):
		# Find root tree path
		p=self.treePath
		while True:
			np=p.parent()
			if not np.isValid():
				break
			p=np
		
		return p
		
	def registerModelView(self, model, view):
		self.modelView.append([model, view])
		
		# Connect model's signals to emit a contentChanged signal
		model.dataChanged.connect(self.generateContentChangedOnDataChanged)
		model.rowsInserted.connect(self.generateContentChangedOnRowsInserted)
		model.rowsRemoved.connect(self.generateContentChangedOnRowsRemoved)
		model.rowsMoved.connect(self.generateContentChangedOnRowsMoved)
		
		# Connect all QPlainTextEdit widgets
		if type(view) is QDataWidgetMapper:
			for ii in range(model.columnCount(QModelIndex())):
				w=view.mappedWidgetAt(ii)
				if type(w) is not QPlainTextEdit:
					continue
				w.cursorPositionChanged.connect(self.emitCursorPosition)
				w.installEventFilter(self)
				
	def eventFilter(self, source, event):
		if (
			event.type() is QEvent.FocusOut
			and type(source) is QPlainTextEdit
		):
			self.cursorPosition.emit(-1, -1)
			
		return super(QPEditBase, self).eventFilter(source, event)
	
	cursorPosition=pyqtSignal(int, int)
	
	@pyqtSlot()
	def emitCursorPosition(self):
		sender=self.sender()
		if type(sender) is QPlainTextEdit and sender==qApp.focusWidget():
			cur=sender.textCursor()
			self.cursorPosition.emit(cur.blockNumber(), cur.positionInBlock())
		else:
			self.cursorPosition.emit(-1, -1)
			
	def refreshView(self):
		for m, v in self.modelView:
			if type(v) is QDataWidgetMapper:
				# QDataWidgetMapper must be set to first (and only) entry
				v.toFirst()
			else:
				# Other widgets must have a refreshView() method which is invoked here
				v.refreshView()
	
	def forceCommit(self):
		# Forces commit of all values in editors of view widgets
		for m, v in self.modelView:
			# All views must implement the submit() method
			v.submit()
	
	# Editor -> tree signals
	
	# Emit to request an action in main window (name, argument list)
	requestAction=pyqtSignal(str, object)
	
	# Emit when data that affects the active tree item is changed (usually the label)
	dataChanged=pyqtSignal()
	
	# Emit when data that affects the active tree item's children is changed (usually the label)
	childrenChanged=pyqtSignal(int, int)
	
	# Emit when data that affects the tree structure is about to be changed
	structureAboutToBeChanged=pyqtSignal()
	
	# Emit when data that affects the tree structure has been changed
	structureChanged=pyqtSignal()
	
	# Emit when the contents of the editor are changed
	contentChanged=pyqtSignal()
	
	# Slot receiving dataChanged signal from models and generating contentChanged signal
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def generateContentChangedOnDataChanged(self, topLeft, bottomRight, roles=[]):
		self.contentChanged.emit()
	
	# Slot receiving rowsInserted signal from models and generating contentChanged signal
	@pyqtSlot(QModelIndex, int, int)
	def generateContentChangedOnRowsInserted(self, ndx, i1, i2):
		self.contentChanged.emit()
	
	# Slot receiving rowsRemoved signal from models and generating contentChanged signal
	@pyqtSlot(QModelIndex, int, int)
	def generateContentChangedOnRowsRemoved(self, ndx, i1, i2):
		self.contentChanged.emit()
	
	# Slot receiving rowsInserted signal from models and generating contentChanged signal
	@pyqtSlot(QModelIndex, int, int, QModelIndex, int)
	def generateContentChangedOnRowsMoved(self, ndx1, s1, s2, ndx2, d):
		self.contentChanged.emit()
	
	def log(self, txt, isError=False, asHtml=True):
		if self.logger is not None:
			self.logger.log(txt, isError, asHtml)
			
