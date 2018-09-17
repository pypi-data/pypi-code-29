from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .table import *
from . import guiglobals

__all__ = [ "QPHostsEditor" ]


class QPHostsTableModel(QPTableModel):
	def __init__(self, data, parent=None, *args):
		QPTableModel.__init__(
			self, data, 
			header=[ "Host", "CPUs", "Running design task(s) with process counts" ], 
			editable=[ True, True, False ], 
			dfl=["", "1"], 
			sortingIndices=[], 
			parent=None, *args
		)
		self.tasksOnHost={}
		self.usedSlots=0
	
	def rowCount(self, parent=QModelIndex()):
		return len(self.mylist)
	
	def columnCount(self, parent=QModelIndex()):
		return len(self.header)
	
	def data(self, index, role):
		if not index.isValid():
			return None
		
		row=index.row()
		col=index.column()
			
		if role == Qt.DisplayRole or role == Qt.EditRole:
			if col>=0 and col<=1:
				return QVariant(self.mylist[row][col])
			if col==2:
				txt=""
				hl=guiglobals.tasksMonitor.hostLayout(self.mylist[row][0])
				for taskName, ncpu in hl.items():
					txt+="%s (%d) " % (taskName, ncpu)
				return QVariant(txt)
			else:
				return None
		else:
			return None
	
	def setData(self, index, value, role):
		row=index.row()
		col=index.column()
		if col==0 and self.mylist[row][0]!=value:
			self.mylist[row][0]=value 
		elif col==1 and self.mylist[row][col]!=value:
			try:
				ncpu=int(value)
				if ncpu<1:
					return False
				self.mylist[row][col]=value 
			except:
				return False
		else:
			return False
		
		# Refresh whole row if columns 0 or 1 are changed
		self.dataChanged.emit(self.index(row, col, QModelIndex()), self.index(row, self.columnCount()-1, QModelIndex()))
		
		return True
	
	def refreshTasks(self):
		self.dataChanged.emit(
			self.index(0, 2, QModelIndex()), 
			self.index(self.rowCount()-1, 2, QModelIndex())
		)
		
class QPHostsEditor(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		
		vl=QVBoxLayout(self)
		
		self.sLabel=QLabel("", self)
		
		self.hModel=QPHostsTableModel(guiglobals.hosts, parent)
		self.hTable=QPTable(
			self.hModel, 
			canDelete=True, canCreate=True, canMove=True, 
			stretch=[False, False, True], 
			buttons=False,
			parent=self
		)
		
		vl.addWidget(self.sLabel)
		vl.addWidget(self.hTable)
		
		vl.addStretch(1)
		self.setLayout(vl)
		
		self.hModel.dataChanged.connect(self.handleDataChanged)
		self.hModel.rowsInserted.connect(self.handleRowsInserted)
		self.hModel.rowsRemoved.connect(self.handleRowsRemoved)
		
		guiglobals.tasksMonitor.tasksOnHostChanged.connect(self.handleTasksOnHostChanged)
		
		self.handleTasksOnHostChanged()
		
	def destroy(self):
		guiglobals.tasksMonitor.tasksOnHostChanged.disconnect(self.handleTasksOnHostChanged)
	
	def forceCommit(self):
		pass
	
	@pyqtSlot()
	def handleTasksOnHostChanged(self):
		self.hModel.refreshTasks()
		self.refreshCPUs()
		
	@pyqtSlot(QModelIndex, QModelIndex)
	def handleDataChanged(self, i1, i2):
		self.refreshCPUs()
	
	@pyqtSlot(QModelIndex, int, int)
	def handleRowsInserted(self, index, r1, r2):
		self.refreshCPUs()
	
	@pyqtSlot(QModelIndex, int, int)
	def handleRowsRemoved(self, index, r1, r2):
		self.refreshCPUs()
	
	def refreshCPUs(self):
		slots=guiglobals.availableCPUcount()
		# Used slots are by default computed across hosts listed in hosts table
		usedSlots=guiglobals.tasksMonitor.usedCPUCount()
		
		self.sLabel.setText(
			"%d process slot(s) available, %d used, %d free%s." % 
			(
				slots, usedSlots, slots-usedSlots, 
				" (Possible error!)" if slots-usedSlots<0 else ""
			)
		)
			
		guiglobals.tasksMonitor.emitHostsListChanged()
	
if __name__ == "__main__":
	from pprint import pprint
	import sip 
	import sampledata
	import sys
	
	sip.setdestroyonexit(True)

	app = QApplication(sys.argv)
	
	# Create viewer
	he=QPHostsEditor()
	he.setWindowTitle("Hosts editor demo")
	
	
	# Show and run
	he.show()
	app.exec_()
	
	print(guiglobals.hosts)
