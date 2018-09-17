from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ..design.sqlite import *
from . import resources

__all__ = [ "QPResultsTree" ]


# TODO: add selection, expand, collapse

class QPResultsTree(QWidget):
	def __init__(self, fileName, parent=None):
		QWidget.__init__(self, parent)
		
		self.fileName=fileName
		
		
		self.tree=QTreeWidget(self)
		self.tree.setHeaderHidden(False)
		self.tree.setHeaderLabels(["Results database"])
		self.tree.currentItemChanged.connect(self.onTreeItemChanged)
		
		layout=QVBoxLayout(self)
		layout.setContentsMargins(QMargins(0,0,0,0))
		layout.setSpacing(0)
		layout.addWidget(self.tree)
		self.setLayout(layout)
		
		root=self.tree.invisibleRootItem()
		root.setData(1, Qt.EditRole, QVariant(0))
		
		self.id2item={ 0: root }
		
		self.lastId=None
		
		self.defaultAspect={}
	
	newDisplay=pyqtSignal(int)
	
	def getTaskIcon(self, db, iid):
		try:
			rec=db.get(iid)
		except PyOpusSqliteError:
			return QIcon(":resources/file.png")
		
		ttype=rec.payload.task['type']
		if ttype=="cbd":
			return QIcon(":resources/cbd.png")
		else:
			return QIcon(":resources/file.png")

	def getIcon(self, db, iid, typeName):
		if typeName=="SQLDataTask":
			return self.getTaskIcon(db, iid)
		elif typeName=="SQLDataTaskCBD":
			return QIcon(":resources/scales.png")
		elif typeName=="SQLDataCorners":
			return QIcon(":resources/corners.png")
		elif typeName=="SQLDataOptIter":
			return QIcon(":resources/performance.png")
		elif typeName=="SQLDataConclusion":
			return QIcon(":resources/sum.png")
		else:
			return QIcon(":resources/file.png")
	
	def getAspectIcon(self, aspect):
		if aspect=="parameters":
			return QIcon(":resources/designpar.png")
		if aspect=="performance":
			return QIcon(":resources/measure.png")
		if aspect=="cost":
			return QIcon(":resources/scales.png")
		if aspect=="corners":
			return QIcon(":resources/corners.png")
		if aspect=="summary":
			return QIcon(":resources/sum.png")
		else:
			return QIcon(":resources/file.png")
	
	def clearTree(self):
		self.tree.clear()
		self.lastId=None
		self.newDisplay.emit(-1)
	
	def update(self):
		db=SQLiteDatabase(self.fileName)
		
		ids, parents, names, types = db.getNewNodes(
			self.lastId+1 if self.lastId is not None else 0
		)
		
		if len(ids)>0:
			self.lastId=max(ids)
		
		for ii in range(len(ids)):
			iid=ids[ii]
			parentId=parents[ii]
			name=names[ii]
			typeName=types[ii]
			
			if parentId>=0:
				# Add to existing parent
				parentItem=self.id2item[parentId]
				item=QTreeWidgetItem(parentItem, [name])
				item.setData(1, Qt.EditRole, QVariant(iid))
				item.setData(2, Qt.EditRole, QVariant(typeName))
				icon=self.getIcon(db, iid, typeName)
				item.setIcon(0, icon)
				
				self.id2item[iid]=item
				
				# Expand parent item when a child is added
				self.tree.expandItem(parentItem)
			else:
				# This is root node, do nothing
				pass
			
	def expandToDepth(self, depth):
		self.tree.expandToDepth(depth)
	
	@pyqtSlot(QTreeWidgetItem, QTreeWidgetItem)
	def onTreeItemChanged(self, current, previous):
		if current is not None:
			recId=int(current.data(1, Qt.EditRole))
			db=SQLiteDatabase(self.fileName)
			
			self.newDisplay.emit(recId)
			
if __name__ == "__main__":
	from pprint import pprint
	import sip 
	import sys
	
	@pyqtSlot(int, str)
	def slot(i, n):
		print(i, n)
		
	sip.setdestroyonexit(True)
	
	app = QApplication(sys.argv)
	
	w=QPResultsTree(fileName="corner.sqlite")
	w.newDisplay.connect(slot)
	
	w.update()
	w.expandToDepth(1)
	
	w.show()
	app.exec_()
	
	
