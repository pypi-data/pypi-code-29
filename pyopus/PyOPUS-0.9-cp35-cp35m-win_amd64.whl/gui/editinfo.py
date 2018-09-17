from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .editbase import *

__all__ = [ 'QPEditInfo' ]

# Model of the info structure excluding data in tables
class QPInfoModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 1
	
	def rowCount(self, parent):
		return 1
	
	columnNames=['description']
	
	def headerData(self, ii, orientation, role):
		if orientation == Qt.Horizontal and role == Qt.DisplayRole:
			return self.columnNames[ii]
		elif orientation == Qt.Vertical and role == Qt.DisplayRole:
			return ii+1
		return None
	
	def data(self, index, role):
		if not index.isValid():
			return None
		elif role == Qt.DisplayRole or role == Qt.EditRole:
			col=index.column()
			if col==0:
				return self.data["description"]
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col==0 and self.data["description"]!=value:
			self.data["description"]=value
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

class QPEditInfo(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent, *args)
		
		self.editBox=QPlainTextEdit(self)
		
		self.dm=QDataWidgetMapper(self)
		self.model=QPInfoModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.editBox, 0, b"plainText")
		self.dm.toFirst()
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		layout.addWidget(QLabel("Project description", self))
		layout.addWidget(self.editBox)
		
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		
		
if __name__=='__main__':
	from pprint import pprint
	import sip 
	import sys
	import sampledata
	sip.setdestroyonexit(True)

	app = QApplication(sys.argv)
	
	# Create scroll area
	sa=QScrollArea()
	sa.setWindowTitle("Info editor demo")
	sa.setWidgetResizable(True)
	
	# Add widget
	win=QPEditInfo(sampledata.data['info'])
	sa.setWidget(win)
	
	# Show and run
	sa.show()
	app.exec_()
	
	# Print data
	pprint(sampledata.data)
	
	

