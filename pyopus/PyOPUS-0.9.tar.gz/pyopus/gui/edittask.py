from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .delegates import QPComboBox
from .table import *
from .editbase import *
from .fstools import *
from .tasksmonitor import *
from .dumptools import dumpProject, getVariables, writeFiles, QPDumpError
from .tasks import taskTitle, taskDumper
from .mpidump import *
from . import guiglobals 

import shutil, os, os.path, datetime, subprocess, sys, json, platform, time

__all__ = [ 'QPEditTask' ]

from pprint import pprint

# Model of the head structure excluding data in tables
class QPTaskModel(QAbstractTableModel):
	def __init__(self, data, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.data=data
	
	def columnCount(self, parent):
		return 2
	
	def rowCount(self, parent):
		return 1
	
	columnNames=[
		'name', 'description'
	]
	
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
			elif col==1:
				return self.data[1]['description']
		return None
	
	def setData(self, index, value, role):
		col=index.column()
		if col==0 and self.data[0]!=value:
			self.data[0]=value
		elif col==1 and self.data[1]['description']!=value:
			self.data[1]['description']=value
		else:
			return False
		
		self.dataChanged.emit(index, index)
		return True
		
	def flags(self, index):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


class QPEditTask(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None, *args):
		QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
		
		self.nameBox=QLineEdit(self)
		self.descriptionBox=QPlainTextEdit(self)
		
		# Map data to widgets
		self.dm=QDataWidgetMapper(self)
		self.model=QPTaskModel(self.data, parent=self)
		self.dm.setModel(self.model)
		self.dm.addMapping(self.nameBox, 0, b"text")
		self.dm.addMapping(self.descriptionBox, 1, b"plainText")
		self.dm.toFirst()
		
		self.runStatus=QLabel("")
		
		self.checkProject()
		
		self.timer=QTimer(self)
		self.timer.timeout.connect(self.checkProject)
		self.timer.start(500)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		layout.addWidget(QLabel(taskTitle[self.data[1]['type']], self))
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Task name", self))
		layout.addWidget(self.nameBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Description", self))
		layout.addWidget(self.descriptionBox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(self.runStatus)
		layout.addSpacing(2*layout.spacing())
		
		# Add a stretch at the bottom so that when member widgets shrink they are ordered at the top
		# layout.addStretch(1)
		self.setLayout(layout)
		
		# Register model/view pairs
		self.registerModelView(self.model, self.dm)
		
		# Handle dataChanged() signal from the model to notify parent about name change 
		self.model.dataChanged.connect(self.onDataChanged)
		
		# Connect to tasks monitor 
		guiglobals.tasksMonitor.taskStatusChanged.connect(self.handleTaskStatusChanged)
		
	# Cleanup 
	def destroy(self):
		self.timer.stop()
		guiglobals.tasksMonitor.taskStatusChanged.disconnect(self.handleTaskStatusChanged)
	
	@pyqtSlot(str)
	def handleTaskStatusChanged(self, t):
		name=self.data[0].strip()
		if t==name:
			# Update task status display 
			self.checkProject()
			
	# @pyqtSlot(QModelIndex, QModelIndex, list) # Requires QVector instead of list. Just do not specify types. 
	def onDataChanged(self, topLeft, bottomRight, roles):
		# Change in task name
		if topLeft.column()<=0 and bottomRight.column()>=0:
			self.dataChanged.emit()
		
	@pyqtSlot()
	def checkProject(self):
		name=self.data[0].strip()
		
		# Status text
		state=guiglobals.tasksMonitor.state(name)
		if state is None:
			self.runStatus.setText("Design task is not running.\n")
		elif state=='running':
			runningSince=guiglobals.tasksMonitor.runningSince(name)
			ncpu=guiglobals.tasksMonitor.taskCPUCount(name)
			if ncpu>1:
				txt="Design task running with %d parallel processes\n" % ncpu
			else:
				txt="Design task running with one process\n"
			self.runStatus.setText(
				txt+"since "+
				datetime.datetime.fromtimestamp(runningSince).strftime('%Y-%m-%d %H:%M:%S')+
				", runtime "+formatPassedTime(runningSince)+".")
		elif state=='stopping':
			self.runStatus.setText("Design task is being stopped.\n")
		elif state=='starting':
			self.runStatus.setText("Design task is starting.\n")
		elif state=='finished':
			if guiglobals.tasksMonitor.exitStatus(name)==0:
				self.runStatus.setText("Design task finished.\n")
			else:
				self.runStatus.setText("Design task was interrupted.\n")
		elif state=='ready':
			self.runStatus.setText("Task ready for startup.\n")
		else:
			self.runStatus.setText(
				"Error reading task status.\n"+
				"Kill task manually and delete "+os.path.join(name, "lock.*")+" files.")
			
	
