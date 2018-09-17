from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .style import styleWidget
from .fstools import fileInfo, listDir
from .editbase import *

__all__ = [ 'QPEditFile' ]

# Model of the file structure excluding data in tables
class QPFileModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 2
	
	def rowCount(self, parent):
		return 1
	
	columnNames=['name']
	
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
				return self.data[0]
			if col==1:
				return self.data[1]['content']
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col==0 and self.data[0]!=value:
			self.data[0]=value
		elif col==1 and self.data[1]['content']!=value:
			self.data[1]['content']=value 
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		f=Qt.ItemIsEnabled | Qt.ItemIsSelectable
		
		col=index.column()
		
		if col==1 and not self.data[1]["external"]:
			f|=Qt.ItemIsEditable
		
		return f

class QPEditFile(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.nameBox=QLineEdit(self)
		self.editBox=QPlainTextEdit(self)
		styleWidget(self.editBox, ['monospace']);
		
		# Prevent editing of external files
		# Model flags should take care of this but they don't
		if self.data[1]['external']:
			self.editBox.setReadOnly(True)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPFileModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.nameBox, 0, b"text")
		if not self.data[1]['external']:
			self.dm.addMapping(self.editBox, 1, b"plainText")
		self.dm.toFirst()
		
		self.loadFile()
		
		layout.addWidget(QLabel("Name", self))
		layout.addWidget(self.nameBox)
		layout.addSpacing(2*layout.spacing())
		if self.data[1]['external']:
			wtxt="Content (external file, read-only)"
		else:
			wtxt="Content (editable)"
		layout.addWidget(QLabel(wtxt, self))
		layout.addWidget(self.editBox)
		
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		
		# Handle dataChanged() signal from the model to notify parent about name change 
		# and verify external file
		self.model.dataChanged.connect(self.onDataChanged)
	
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def onDataChanged(self, topLeft, bottomRight, roles):
		# Change in file name, notify parent (project window)
		if topLeft.column()<=0 and bottomRight.column()>=0:
			self.dataChanged.emit()
			if self.data[1]['external']:
				self.loadFile()
	
	def loadFile(self):
		if not self.data[1]['external']:
			return
		
		info=fileInfo(self.data[0])
		if info['type'] is None:
			# Does not exist
			self.editBox.setStyle
			styleWidget(self.editBox, ['error'])
			self.editBox.setPlainText("File not found.")
		elif info['type']=='dir':
			# Dir 
			try:
				dirs, files = listDir(self.data[0])
				if info['symlink']:
					txt='Link to folder '
				else:
					txt='Folder '
				txt+='with '+str(len(dirs))+' subfolder(s) and '+str(len(files))+' file(s)\n'
				for s in dirs:
					txt+='  '+s+'/\n'
				for s in files:
					txt+='  '+s+'\n'
				self.editBox.setPlainText(txt)
				styleWidget(self.editBox, ['monospace', 'folder'])
			except Exception:
				self.editBox.setStyle
				styleWidget(self.editBox, ['error'])
				self.editBox.setPlainText("Failed to read directory.")
		else:
			# File
			try:
				with open(self.data[0], 'r') as f:
					txt=f.read()
				self.editBox.setPlainText(txt)
				styleWidget(self.editBox, ['monospace'])
			except Exception:
				self.editBox.setStyle
				styleWidget(self.editBox, ['error'])
				self.editBox.setPlainText("Failed to read file.")
			
	def refreshView(self):
		# Call parent's method
		QPEditBase.refreshView(self)
		
		# Load file and display file information
		self.loadFile()
		
			
if __name__=='__main__':
	from pprint import pprint
	import sip 
	import sys
	import sampledata
	sip.setdestroyonexit(True)

	app = QApplication(sys.argv)
	
	# Create scroll area
	sa=QScrollArea()
	sa.setWindowTitle("File editor demo")
	sa.setWidgetResizable(True)
	
	# Add widget
	win=QPEditFile(sampledata.data['files'][0])
	sa.setWidget(win)
	
	# Show and run
	sa.show()
	app.exec_()
	
	# Print data
	pprint(sampledata.data)
	
	

