# Under windows 7, copy /Python27/Lib/site-packages/PyQt5/libEGL.dll to /Windows/System32
# Without this the gui won't start

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .values import version
from .logview import *
from .resview import *
from .logger import *
from .hostseditor import *
from .treeedit import *
from .values import blankProject
from .fstools import *
from .tasksmonitor import *
from . import guiglobals
from ..misc.identify import revision
from .fixproject import *

from .dumptools import dumpProject, getVariables, writeFiles, QPDumpError
from .tasks import taskTitle, taskDumper
from .mpidump import *

from .treeitems import QPTreeItemProjectRoot, QPTreeItemTasksRoot, taskItemTypes

from copy import deepcopy
import json, shutil, os, os.path, datetime, subprocess, signal, sys, json, platform, time
from pprint import pprint


class QPTabWidget(QTabWidget):
	def __init__(self, parent=None):
		QTabWidget.__init__(self, parent)
	
	
class QPMainWindow(QMainWindow):
	def __init__(self, parent=None, *args):
		QMainWindow.__init__(self, parent, *args)
		# Project file name (without path, assume it is in the working directory)
		self.projectFileName=None
		
		# Project data
		self.data=None
		
		# Modified widgets
		self.changedWidgets=set()
		
		# Widget to tab title mapper
		self.tabTitle={}
		
		# Create task monitor
		guiglobals.tasksMonitor=QPTasksMonitor()
		guiglobals.tasksMonitor.setCheckPeriod(2000)
		
		# Create splitter 
		self.splitter=QSplitter(Qt.Vertical, parent=self)
		
		# Create logger 
		self.loggerWidget=QPLogger(self)
			
		# Create tab widget
		self.tabWidget=QTabWidget()
		self.tabWidget.setMovable(True)
		self.tabWidget.setTabsClosable(True)
		
		self.tabWidget.tabCloseRequested.connect(self.handleTabCloseRequest)
		self.tabWidget.tabBarClicked.connect(self.onTabBarClicked)
		
		# Create project widget 
		self.projectWidget=QPTreeEdit(self.loggerWidget, parent=self)
		self.projectWidget.projectChanged.connect(self.handleWidgetChanged)
		
		self.projectWidget.requestAction.connect(self.handleRequestAction)
		
		# Create tasks widget
		self.tasksWidget=QPTreeEdit(self.loggerWidget, parent=self)
		self.tasksWidget.projectChanged.connect(self.handleWidgetChanged)
		
		self.tasksWidget.requestAction.connect(self.handleRequestAction)
		
		# Clear project changed flas
		self.markProjectUnmodified()
		
		# Populate tabs
		projI=self.addTab(self.projectWidget, QIcon(":resources/project.png"), "Project")
		taskI=self.addTab(self.tasksWidget, QIcon(":resources/design.png"), "Design Tasks")
		
		# TODO: load window layout from ini file
		
		#  No close button for project and tasks tabs
		self.tabWidget.tabBar().setTabButton(projI, QTabBar.RightSide, None)
		self.tabWidget.tabBar().setTabButton(taskI, QTabBar.RightSide, None)
							  
		# Populate splitter
		self.splitter.addWidget(self.tabWidget)
		self.splitter.addWidget(self.loggerWidget)
		
		# Set central widget
		self.setCentralWidget(self.splitter)
		
		# Create status bar 
		sb=self.statusBar()
		
		self.activeTaskStatusWidget=QLabel("")
		self.totalNcpuWidget=QLabel("")
		
		sb.addPermanentWidget(self.activeTaskStatusWidget)
		w=QWidget()
		w.setFixedWidth(10)
		sb.addPermanentWidget(w, 0)
		sb.addPermanentWidget(self.totalNcpuWidget)
		
		self.cursorPositionWidget=QLabel("")
		sb.addWidget(self.cursorPositionWidget)
		
		# Enable cursor position monitoring
		self.projectWidget.cursorPosition.connect(self.displayCursorPosition)
		self.tasksWidget.cursorPosition.connect(self.displayCursorPosition)
		
		# Enable active task detection
		self.tasksWidget.selectedItemsChanged.connect(self.handleTaskSelectionChanged)
		
		# Create actions
		self.createActions()
		
		# Load GUI config
		self.readGUIConfig()
		
		self.activeTaskName=None
		
		guiglobals.tasksMonitor.taskStatusChanged.connect(self.handleTaskStatusChanged)
		guiglobals.tasksMonitor.hostsListChanged.connect(self.handleHostsListChanged)
		
		# self.viewHosts()
	
	def addTab(self, widget, icon, title):
		self.tabTitle[widget]=title
		return self.tabWidget.addTab(widget, icon, title)
		
	def removeTab(self, ndx):
		# Get widget
		widget=self.tabWidget.widget(ndx)
		
		# TODO: handle tab save on close
		
		if widget is not None:
			# Valid widget
			if type(widget) is QPResultsViewer:
				# Results widget
				# Disconnect cursor position notifications
				widget.cursorPosition.disconnect(self.displayCursorPosition)
				# Disconnect crosshair position notifications
				widget.crosshairPosition.disconnect(self.displayCrosshairPosition)
				# Disconnect change notifications
				widget.projectChanged.disconnect(self.handleWidgetChanged)
			
			# Mark widget unmodified 
			self.markWidgetUnmodified(widget)
			
			# Remove from widget to title mapper
			if widget in self.tabTitle:
				del self.tabTitle[widget]
			
			# Widget cleanup
			widget.destroy()
		
		# Remove tab
		self.tabWidget.removeTab(ndx)
			
	def createActions(self):
		self.fileMenu=self.menuBar().addMenu("&File")
		
		newAction=QAction("&New", self)
		newAction.setShortcuts(QKeySequence.New)
		newAction.setStatusTip("Create a new project")
		newAction.triggered.connect(self.newProject)
		self.fileMenu.addAction(newAction)
		
		openAction=QAction("&Open", self)
		openAction.setShortcuts(QKeySequence.Open)
		openAction.setStatusTip("Open an existing project")
		openAction.triggered.connect(self.openFile)
		self.fileMenu.addAction(openAction)
		
		self.saveAction=QAction("&Save", self)
		self.saveAction.setShortcuts(QKeySequence.Save)
		self.saveAction.setStatusTip("Save project/postprocessing")
		self.saveAction.triggered.connect(self.save)
		self.fileMenu.addAction(self.saveAction)
		
		saveasAction=QAction("Save Project &As...", self)
		saveasAction.setStatusTip("Save project under a new name")
		saveasAction.triggered.connect(self.saveAs)
		self.fileMenu.addAction(saveasAction)
		
		self.saveAllAction=QAction("Save A&ll", self)
		self.saveAllAction.setShortcuts(QKeySequence("CTRL+L"))
		self.saveAllAction.setStatusTip("Save all files")
		self.saveAllAction.triggered.connect(self.saveAll)
		self.fileMenu.addAction(self.saveAllAction)
		
		self.fileMenu.addSeparator()
		
		exitAction=QAction("E&xit", self)
		exitAction.triggered.connect(self.close)
		self.fileMenu.addAction(exitAction)
		
		
		self.viewMenu=self.menuBar().addMenu("&View")
		
		viewProjectAction=QAction("Project", self)
		viewProjectAction.setShortcuts(QKeySequence("F3"))
		viewProjectAction.setStatusTip("View project")
		viewProjectAction.triggered.connect(self.viewProject)
		self.viewMenu.addAction(viewProjectAction)
		
		viewTasksAction=QAction("Design tasks", self)
		viewTasksAction.setShortcuts(QKeySequence("F4"))
		viewTasksAction.setStatusTip("View design tasks")
		viewTasksAction.triggered.connect(self.viewTasks)
		self.viewMenu.addAction(viewTasksAction)
		
		viewHostsAction=QAction("MPI hosts", self)
		viewHostsAction.setShortcuts(QKeySequence("F8"))
		viewHostsAction.setStatusTip("View MPI hosts")
		viewHostsAction.triggered.connect(self.viewHosts)
		self.viewMenu.addAction(viewHostsAction)
		
		self.viewMenu.addSeparator()
		
		clearLogAction=QAction("Clear GUI messages", self)
		clearLogAction.setStatusTip("Clear GUI messages")
		clearLogAction.triggered.connect(self.clearLog)
		self.viewMenu.addAction(clearLogAction)
		
		
		self.taskMenu=self.menuBar().addMenu("&Task")
		
		self.startTaskAction=QAction("Start locally", self)
		self.startTaskAction.setShortcuts(QKeySequence("F5"))
		self.startTaskAction.setStatusTip("Start task locally")
		self.startTaskAction.triggered.connect(self.startActiveTask)
		self.taskMenu.addAction(self.startTaskAction)
		
		self.startTaskMPIAction=QAction("Start on cluster", self)
		self.startTaskMPIAction.setShortcuts(QKeySequence("Shift+F5"))
		self.startTaskMPIAction.setStatusTip("Start task on cluster")
		self.startTaskMPIAction.triggered.connect(self.startActiveTaskMPI)
		self.taskMenu.addAction(self.startTaskMPIAction)
		
		self.stopTaskAction=QAction("Stop", self)
		self.stopTaskAction.setShortcuts(QKeySequence("Shift+F9"))
		self.stopTaskAction.setStatusTip("Stop task")
		self.stopTaskAction.triggered.connect(self.stopActiveTask)
		self.taskMenu.addAction(self.stopTaskAction)
		
		self.taskLogAction=QAction("View log", self)
		self.taskLogAction.setShortcuts(QKeySequence("F6"))
		self.taskLogAction.setStatusTip("View task log")
		self.taskLogAction.triggered.connect(self.viewActiveTaskLog)
		self.taskMenu.addAction(self.taskLogAction)
		
		self.taskResultsAction=QAction("View results", self)
		self.taskResultsAction.setShortcuts(QKeySequence("F7"))
		self.taskResultsAction.setStatusTip("View task results")
		self.taskResultsAction.triggered.connect(self.viewActiveTaskResults)
		self.taskMenu.addAction(self.taskResultsAction)
		
		self.unlockTaskAction=QAction("Unlock", self)
		self.unlockTaskAction.setStatusTip("Unlock task")
		self.unlockTaskAction.triggered.connect(self.unlockActiveTask)
		self.taskMenu.addAction(self.unlockTaskAction)
		
		
		self.menuBar().addSeparator()
		self.helpMenu=self.menuBar().addMenu("&Help")
		
		aboutAction=QAction("About PyOPUS GUI", self)
		aboutAction.setStatusTip("Show the application's About box")
		aboutAction.triggered.connect(self.about)
		self.helpMenu.addAction(aboutAction)
	
	def enableTaskActions(self):
		if self.activeTaskName is None:
			status=None
		else:
			status=guiglobals.tasksMonitor.state(self.activeTaskName)
		if status in ["error", "starting", "stopping"]:
			self.startTaskAction.setEnabled(False)
			self.startTaskMPIAction.setEnabled(False)
			self.stopTaskAction.setEnabled(False)
		elif status in ["running"]:
			self.startTaskAction.setEnabled(False)
			self.startTaskMPIAction.setEnabled(False)
			self.stopTaskAction.setEnabled(True)
		elif status in ["finished", "initial"]:
			self.startTaskAction.setEnabled(True)
			self.startTaskMPIAction.setEnabled(True)
			self.stopTaskAction.setEnabled(False)
		else:
			self.startTaskAction.setEnabled(True)
			self.startTaskMPIAction.setEnabled(True)
			self.stopTaskAction.setEnabled(False)
			
		if self.activeTaskName is not None:
			self.taskLogAction.setEnabled(True)
			self.taskResultsAction.setEnabled(True)
		else:
			self.taskLogAction.setEnabled(False)
			self.taskResultsAction.setEnabled(False)
			
		if self.activeTaskName is not None:
			self.unlockTaskAction.setEnabled(True)
		else:
			self.unlockTaskAction.setEnabled(False)
	
	def findTaskByName(self, name):
		
		for ii in range(len(self.data["tasks"])):
			if self.data["tasks"][ii][0] == name:
				return ii
		
		return None
		
	def startTask(self, mpi=False):
		name=self.activeTaskName
		
		# Find task entry
		ndx=self.findTaskByName(name)
		if ndx is None:
			return
		taskData=self.data['tasks'][ndx]
		
		dumpOK=False
		
		try:
			# Check if subfolder exists
			info=fileInfo(name)
			
			if info['type'] is not None:
				# Exists
				confirmed=False
				if info['type']=='dir':
					# Folder
					if (
						QMessageBox.question(
							None, 
							"Folder exists, confirm delete", 
							"Folder '"+name+"' exists. By proceeding you will delete it along with all the results it contains. \nAre you sure?", 
							QMessageBox.Yes|QMessageBox.No
						) == QMessageBox.Yes
					):
						confirmed=True
				else:
					# File
					if (
						QMessageBox.question(
							None, 
							"File exists, confirm delete", 
							"File '"+name+"' exists. By proceeding you will delete it. \nAre you sure?", 
							QMessageBox.Yes|QMessageBox.No
						) == QMessageBox.Yes
					):
						confirmed=True
				
				if not confirmed:
					self.startTaskAction.setEnabled(True)
					self.startTaskMPIAction.setEnabled(guiglobals.mpiSupported)
					return
				
				self.log("\nPreparing folder and files for running task '"+name+"'.")
				
				# Remove it
				try:
					self.log("Removing folder/file '"+name+"'.")
			
					if info['type']=='dir':
						shutil.rmtree(name)
					else:
						os.remove(name)
				except Exception:
					raise QPDumpError("Failed to remove file/folder '"+name+"'.")
			
			self.log("Dumping data.")
			
			# Create folder 
			try:
				os.makedirs(name)
			except Exception:
				raise QPDumpError("Failed to create folder '"+name+"'.")
				
			# Copy files
			try:
				writeFiles(self.data, name)
			except QPDumpError as e:
				raise QPDumpError("Error copying files/folders.\n"+str(e))
			
			# Dump common part
			try:
				dictCommon, varDict = dumpProject(self.data)
			except QPDumpError as e:
				raise QPDumpError("Error dumping problem description (common part).\n"+str(e))
				
			# Dump task part
			try:
				dumper=taskDumper[taskData[1]['type']]
				dictTask = dumper(self.data, taskData, varDict)
			except QPDumpError as e:
				raise QPDumpError("Error dumping problem description (task part).\n"+str(e))
			
			# Prepare MPI part
			if mpi:
				# MPI settings from task
				try:
					dictMPI = dumpMPI(self.data, taskData, varDict)
				except QPDumpError as e:
					raise QPDumpError("Error dumping MPI setup (task part).\n"+str(e))
			
				# Prepare VM layout
				try:
					vmLayout=generateVMLayout(taskData)
				except QPDumpError as e:
					raise QPDumpError("Error generating tasks layout.\n"+str(e))
				
				# Prepare hosts file
				try:
					hostsFileTxt=dumpHostsFile(vmLayout)
				except QPDumpError as e:
					raise QPDumpError("Failed to generate hosts file.\n"+str(e))
				
			# Write to files
			if mpi:
				try:
					with open(os.path.join(name, "vmlayout"), "w") as f:
						f.write(json.dumps(vmLayout))
				except Exception:
					raise QPDumpError("Failed to write vmlayout file for task '"+name+"'.")
				
				try:
					with open(os.path.join(name, "hosts"), "w") as f:
						f.write(hostsFileTxt)
				except Exception:
					raise QPDumpError("Failed to write hosts file for task '"+name+"'.")
			
			try:
				with open(os.path.join(name, "runme.py"), "w") as f:
					# Encoding
					f.write("# -*- coding: UTF-8 -*-\n")
					f.write("import os, sys, traceback, json\n")
					f.write("from pyopus.misc.debug import DbgSetup, DbgMsgOut\n")
					f.write("DbgSetup(True, 1)\n")
					f.write("\n")
					
					# MPI disabled for now
					if not mpi:
						f.write("useMPI=False\n")
					else:
						f.write("useMPI=True\n")
						f.write("mpiData="); pprint(dictMPI, stream=f)
						f.write("\n")
						
					f.write("\n")
					f.write("projData="); pprint(dictCommon, stream=f)
					f.write("\n")
					f.write("taskData="); pprint(dictTask, stream=f)
					f.write("\n")
					f.write("if __name__=='__main__':\n")
					
					# Random seed 0 for default random generator
					f.write("  import numpy as np\n")
					f.write("  np.random.seed(0)\n")
					f.write("\n")
					
					# MPI preamble
					f.write("  if useMPI:\n")
					f.write("    from pyopus.parallel.mpi import MPI\n")
					f.write("    from pyopus.parallel.cooperative import cOS\n")
					f.write("\n")
					f.write("    cOS.setDebug(mpiData['cosdebug'])\n")
					f.write("    if mpiData['mirror']:\n")
					f.write("      vm=MPI(mirrorMap=projData['mirrormap'], persistentStorage=mpiData['persistent'], debug=mpiData['vmdebug'])\n")
					f.write("    else:\n")
					f.write("      vm=MPI(debug=mpiData['vmdebug'])\n")
					f.write("    cOS.setVM(vm)\n")
					f.write("\n")
					f.write("    hosts=MPI.vmStatus['hosts']\n")
					f.write("    slots=MPI.vmStatus['slots']\n")
					f.write("    DbgMsgOut('VM', 'Process list (total %d):' % (len(slots)))\n")
					f.write("    for host in hosts.keys():\n")
					f.write("      DbgMsgOut('VM', '  Host %s with %d process(es)' % (host, len(hosts[host]['slots'])))\n")
					f.write("      for slot in hosts[host]['slots']:\n")
					f.write("        DbgMsgOut('VM', '    slot %d: pid=0x%x (%d)' % (slot, slots[slot]['pid'], slots[slot]['pid']))\n")
					f.write("\n")
					
					# SQLite database
					f.write("  from pyopus.design.sqlite import SQLiteDatabase\n")
					# f.write("  sqld=SQLiteDatabase(taskData['name']+'.sqlite')\n")
					f.write("  sqld=SQLiteDatabase(os.path.join('..', taskData['name']+'.sqlite'))\n")
					f.write("\n")
					
					# Start task
					f.write("  from pyopus.gui.tasks import taskRunner\n\n")
					f.write("  try:\n")
					f.write("    runner=taskRunner[taskData['type']]\n")
					f.write("    runner(projData, taskData, sqld)\n")
					f.write("  except Exception as e:\n")
					f.write("    DbgMsgOut('TASK', 'Task terminated due to exception.')\n")
					f.write("    DbgMsgOut('TASK', traceback.format_exc())\n")
					f.write("    sys.exit(1)\n")
					f.write("\n")
					
					# MPI finalize
					f.write("  if useMPI:\n")
					f.write("    cOS.finalize()\n")
					
					f.close()
				
				dumpOK=True
				
			except Exception:
				raise QPDumpError("Failed to write startup script for task '"+name+"'.")
			
		except QPDumpError as e:
			# Enable start button again (we failed)
			self.startTaskAction.setEnabled(True)
			self.startTaskMPIAction.setEnabled(guiglobals.mpiSupported)
			self.log(str(e), isError=True)
			shutil.rmtree(name)
			self.log("Removing folder '"+name+"'.")
		
		# Spawn, wait for process or failure to start
		if dumpOK:
			# Dump OK, write to lock.request to indicate start of launch process
			with open(os.path.join(name, "lock.request"), "w") as fl:
				fl.write("%.1f starting\n" % (time.time()))
			
			guiglobals.tasksMonitor.poll([name])
			
			# Start pyopus.gui.launcher module with task name and optional "mpi"
			argList=[sys.executable, '-m', 'pyopus.gui.launcher', name]
			if mpi:
				nprocStr=str(taskData[1]['mpi']['processors']).strip()
				argList+=["mpi"]
				self.log("Task '"+name+"' starting in MPI mode.")
			else:
				self.log("Task '"+name+"' starting in single process mode.")
		
			daemonLaunch(argList)
		
		# Stop button will be enabled automatically when the run starts
	
	def stopTask(self, name):
		# Disable stop action
		if name==self.activeTaskName:
			self.stopTaskAction.setEnabled(False)
		
		# Write to lock.request to indicate that task is being stopped
		with open(os.path.join(name, "lock.request"), "a") as fl:
			fl.write("%.1f stopping\n" % (time.time()))
		
		self.log("Stopping task '"+name+"'.")
		
		guiglobals.tasksMonitor.poll([name])
		
		try:
			guiglobals.tasksMonitor.killTask(name)
		except QPTasksMonitorError as e:
			self.stopTaskAction.setEnabled(True)
			self.log("Failed to terminate task '"+name+"'. Terminate and delete lock.* files manually.", isError=True)
	
	@pyqtSlot()
	def startActiveTask(self):
		if self.activeTaskName is not None:
			self.startTask(mpi=False)
	
	@pyqtSlot()
	def startActiveTaskMPI(self):
		if self.activeTaskName is not None:
			self.startTask(mpi=True)
	
	@pyqtSlot()
	def stopActiveTask(self):
		if self.activeTaskName is not None:
			self.stopTask(self.activeTaskName)
	
	@pyqtSlot()
	def unlockActiveTask(self):
		if (
			QMessageBox.warning(
				None, 
				"Warning. Unlocking a task.", 
				"A task is unlocked by deleting its lock files and hosts list. \n"+
				"Task results can become corrupted if you restart the task before \n"+
				"all processes writing to its folder are finished. \n\n"+
				"Do you want to unlock task '"+self.activeTaskName+"'?", 
				QMessageBox.Yes|QMessageBox.No
			) == QMessageBox.Yes
		):
			name=self.activeTaskName
			try:
				os.remove(os.path.join(name, "lock.request"))
				os.remove(os.path.join(name, "lock.response"))
				os.remove(os.path.join(name, "vmlayout"))
				os.remove(os.path.join(name, "hosts"))
			except:
				pass
	@pyqtSlot()
	def viewActiveTaskLog(self):
		if self.activeTaskName is not None:
			self.logTab(
				os.path.realpath(os.path.join(self.activeTaskName, self.activeTaskName+".log"))
			)
	
	@pyqtSlot()
	def viewActiveTaskResults(self):
		if self.activeTaskName is not None:
			self.resultsTab(
				# os.path.realpath(os.path.join(self.activeTaskName, self.activeTaskName+".sqlite"))
				self.activeTaskName+".sqlite"
			)
	
	@pyqtSlot(str)
	def handleTaskStatusChanged(self, name):
		if name==self.activeTaskName:
			self.updateTaskStatus()
			self.updateCPUstatus()
			self.enableTaskActions()
		
		# Get status
		status=guiglobals.tasksMonitor.state(name)
		# Write to log window
		if status=="running":
			self.log("Task '"+name+"' started.")
		elif status=="finished":
			if guiglobals.tasksMonitor.exitStatus(name)==0:
				self.log("Task '"+name+"' finished.")
			else:
				self.log("Task '"+name+"' was interrupted.")
		
		
	@pyqtSlot()
	def handleHostsListChanged(self):
		self.updateCPUstatus()
	
	def findTaskItemParent(self, item):
		while True:
			pItem=item.parent()
			if pItem is None:
				break
			if type(pItem) in taskItemTypes:
				return pItem
			item=pItem
		
		return None
	
	def updateTaskStatus(self):
		# Check if task name is unique
		if self.activeTaskName is not None:
			names=[t[0] for t in self.data["tasks"]]
			if names.count(self.activeTaskName)>1:
				# Name not unique
				self.activeTaskName=None
			
		if self.activeTaskName is not None:
			ncpu=guiglobals.tasksMonitor.taskCPUCount(self.activeTaskName)
			ncpu=0 if ncpu is None else ncpu
			status=guiglobals.tasksMonitor.state(self.activeTaskName)
			if status=="finished" and guiglobals.tasksMonitor.exitStatus(self.activeTaskName)!=0:
				status="was interrupted"
			if status is None:
				statusTxt="Active task '%s'" % (self.activeTaskName)
					
			elif status=="ready":
				statusTxt="Active task '%s' ready to be started" % (self.activeTaskName)
			else:
				statusTxt="Active task '%s' %s" % (
					self.activeTaskName, 
					status, 
				)
			if ncpu>0:
				statusTxt+=", using %d CPU(s)" % (ncpu)
			statusTxt+=""
		else:
			statusTxt="No active task"
		
		self.activeTaskStatusWidget.setText(statusTxt)
	
	def updateCPUstatus(self):
		cpuAvail=guiglobals.availableCPUcount()
		cpuFree=cpuAvail-guiglobals.tasksMonitor.usedCPUCount()
		if cpuFree<0:
			cpuFree=0
		self.totalNcpuWidget.setText(
			"%d/%d CPU(s) free" % (cpuFree, cpuAvail)
		)
		
	@pyqtSlot(list)
	def handleTaskSelectionChanged(self, items): 
		# One item which is a task
		if len(items)==1:
			item=items[0]
			if type(item) in taskItemTypes:
				taskItem=item
			else:
				taskItem=self.findTaskItemParent(item)
		elif len(items)>1:
			# Multiple items, look for common parent task
			taskItem=self.findTaskItemParent(items[0])
		else:
			taskItem=None
		
		# Task name
		self.activeTaskName=taskItem.name().strip() if taskItem is not None else None
		
		self.updateTaskStatus()
		self.updateCPUstatus()
		self.enableTaskActions()
		
	@pyqtSlot(int, int)
	def displayCursorPosition(self, l, c):
		if l<0 or c<0:
			self.cursorPositionWidget.setText("")
		else:
			self.cursorPositionWidget.setText(
				"Row %d, Column %d" % (l+1, c+1)
			)
	@pyqtSlot(str, object, object)
	def displayCrosshairPosition(self, name, x, y):
		if x is None or y is None:
			self.cursorPositionWidget.setText("")
		else:
			self.cursorPositionWidget.setText(
				"%s @ x=%e y=%e" % (name, x, y)
			)
		
	@pyqtSlot(int)
	def onTabBarClicked(self, ndx):
		# Force commit of current tab before a tab is switched or closed
		atNdx=self.tabWidget.currentIndex()
		if atNdx>=0:
			self.tabWidget.widget(atNdx).forceCommit()
		
	def markProjectUnmodified(self):
		# Remove project widget and tasks widget from changedWidgets
		self.markWidgetUnmodified(self.projectWidget)
		self.markWidgetUnmodified(self.tasksWidget)
		
	@pyqtSlot(str, object)
	def handleRequestAction(self, action, args):
		if action=="open log":
			self.logTab(args[0])
		if action=="open results":
			self.resultsTab(args[0])
	
	def logTab(self, realPath):
		# Extract file name
		base, fileName = os.path.split(realPath)
		
		# Find tab
		tabI=self.findLogTab(realPath)
		
		if tabI<0:
			lv=QPLogViewer(realPath, self.loggerWidget, parent=self)
			tabI=self.addTab(
				lv, QIcon(":resources/log.png"), fileName
			)
			self.log("Opened log file '"+realPath+"'.")
		
		# Activate tab
		self.tabWidget.setCurrentIndex(tabI)
	
	def resultsTab(self, realPath):
		# Find corresponding task
		realPath=os.path.realpath(realPath)
		
		# Extract file name
		base, fileName = os.path.split(realPath)
		
		# Find tab
		tabI=self.findResultsTab(realPath)
		
		if tabI<0:
			rv=QPResultsViewer(realPath, self.loggerWidget, parent=self)
			
			# Receive notifications of changes in widget
			rv.projectChanged.connect(self.handleWidgetChanged)
		
			tabI=self.addTab(
				rv, QIcon(":resources/results.png"), fileName
			)
			rv.cursorPosition.connect(self.displayCursorPosition)
			rv.crosshairPosition.connect(self.displayCrosshairPosition)
			
			self.log("Opened results file '"+realPath+"'.")
		
		# Activate tab
		self.tabWidget.setCurrentIndex(tabI)
		
	def findLogTab(self, realPath):
		# Scan all tabs
		for ii in range(self.tabWidget.count()):
			w=self.tabWidget.widget(ii)
			if type(w) is QPLogViewer and w.realPath==realPath:
				return ii
		
		return -1
	
	def findResultsTab(self, realPath):
		# Scan all tabs
		for ii in range(self.tabWidget.count()):
			w=self.tabWidget.widget(ii)
			if type(w) is QPResultsViewer and w.realPath==realPath:
				return ii
		
		return -1
	
	# Close all tabs except project and tasks
	def closeAllTabs(self):
		for ii in range(self.tabWidget.count()-1,-1,-1):
			w=self.tabWidget.widget(ii)
			if w is not self.projectWidget and w is not self.tasksWidget:
				self.handleTabCloseRequest(ii)
	
	# Close all logs and results, initial tab ordering
	def resetTabs(self):
		self.closeAllTabs()
		
		ndx=self.tabWidget.indexOf(self.projectWidget)
		if ndx!=0:
			self.tabWidget.tabBar().moveTab(ndx, 0)
		
		ndx=self.tabWidget.indexOf(self.tasksWidget)
		if ndx!=1:
			self.tabWidget.tabBar().moveTab(ndx, 1)
		
		self.tabWidget.setCurrentIndex(0)
		
	@pyqtSlot(int)
	def handleTabCloseRequest(self, ndx):
		w=self.tabWidget.widget(ndx)
		if type(w) is QPResultsViewer:
			if w in self.changedWidgets:
				if self.maybeSavePostprocessing(w):
					# Remove from changed widgets
					self.markWidgetUnmodified(w)
					
					self.removeTab(ndx)
			else:
				self.removeTab(ndx)
		else:
			# Remove tab immediately
			self.removeTab(ndx)
		
	# TODO: log close all
	
	# Save GUI config to local folder as pyopusGUI.config
	def writeGUIConfig(self):
		try:
			guidata = {
				'version': version, 
				'hosts': guiglobals.hosts, 
			}
			p=os.path.realpath("pyopusgui.config")
			dtxt=json.dumps(guidata, indent=2)
			with open(p, "w") as f:
				guidata={
					'version': version, 
					'hosts': guiglobals.hosts
				}
				f.write(dtxt)
		except:
			self.log("Failed to save GUI config to %s." % p, isError=True)
	
	def readGUIConfig(self):
		try:
			p=os.path.realpath("pyopusgui.config")
			with open(p, "r") as f:
				txt=f.read()
				guidata=json.loads(txt)
				if guidata['version']!=version:
					self.log("Version mismatch in '%s'. Using defaults." % p, isError=True)
				else:
					guiglobals.hosts=guidata['hosts']
					guiglobals.tasksMonitor.poll()
					self.updateTaskStatus()
					self.updateCPUstatus()
					self.enableTaskActions()
		
					self.log("GUI configuration loaded from '%s'." % p)
		except:
			self.log("Failed to load '%s'. Using defaults." % p)
	
	def markWidgetModified(self, w):
		self.changedWidgets.add(w)
		
		# Find tab
		ndx=self.tabWidget.indexOf(w)
		if ndx>=0:
			# Add * to title
			self.tabWidget.setTabText(ndx, self.tabTitle[w]+" *")
				
		if len(self.changedWidgets)>0:
			self.setWindowModified(True)
		else:
			self.setWindowModified(False)
			
	def markWidgetUnmodified(self, w):
		self.changedWidgets.discard(w)
		
		# Find tab
		ndx=self.tabWidget.indexOf(w)
		if ndx>=0:
			# Remove * from title
			self.tabWidget.setTabText(ndx, self.tabTitle[w])
		
		if len(self.changedWidgets)>0:
			self.setWindowModified(True)
		else:
			self.setWindowModified(False)
	
	def markAllWidgetsUnmodified(self):
		self.changedWidgets=set()
		self.setWindowModified(False)
		
	@pyqtSlot()
	def handleWidgetChanged(self):
		# Mark widget modified
		self.markWidgetModified(self.sender())
		
	def findWidget(self, widget):
		for ii in range(self.tabWidget.count()):
			w=self.tabWidget.widget(ii)
			if w is widget:
				return ii
		return None
	
	def findWidgetByType(self, widgetType):
		for ii in range(self.tabWidget.count()):
			w=self.tabWidget.widget(ii)
			if type(w) is widgetType:
				return ii
		return None
	
	@pyqtSlot()
	def viewProject(self):
		# This one cannot be closed
		ii=self.findWidget(self.projectWidget)
		self.tabWidget.setCurrentIndex(ii)
				
	@pyqtSlot()
	def viewTasks(self):
		# This one cannot be closed
		ii=self.findWidget(self.tasksWidget)
		self.tabWidget.setCurrentIndex(ii)
		
	@pyqtSlot()
	def viewHosts(self):
		ii=self.findWidgetByType(QPHostsEditor)
		if ii is None:
			ii=self.addTab(
				QPHostsEditor(self),
				QIcon(":resources/hosts.png"), "MPI hosts"
			)
		self.tabWidget.setCurrentIndex(ii)
	
	# Assume data is OK, overwrite current project, close all tabs
	def setProject(self, data, fileName):
		self.resetTabs()
		
		self.data=data
		self.projectFileName=fileName
		
		guiglobals.tasksMonitor.setProject(data)
		
		self.projectWidget.setRootItem(QPTreeItemProjectRoot("Project", data, data))
		self.tasksWidget.setRootItem(QPTreeItemTasksRoot(data['tasks'], data))
		
		self.updateTitle()
		
		# Project is no longer modified
		self.markProjectUnmodified()
			
		# Force poll in tasks monitor
		guiglobals.tasksMonitor.poll(sendStatusChanged=False)
		self.updateTaskStatus()
		self.updateCPUstatus()
		self.enableTaskActions()
		
	@pyqtSlot()
	def clearLog(self):
		self.loggerWidget.clear()
	
	@pyqtSlot()
	def newProject(self):
		if self.maybeSaveAll():
			# Mark all widgets unmodified so we don't get another dialog
			self.markAllWidgetsUnmodified()
			
			self.data=deepcopy(blankProject)
			self.setProject(self.data, None)
				
			self.log("Started a new blank project.")
			self.logCwd()
	
	def newNamedProject(self, fileName):
		if self.maybeSaveAll():
			# Mark all widgets unmodified so we don't get another dialog
			self.markAllWidgetsUnmodified()
			
			# Get real path
			rpath=os.path.realpath(fileName)
			
			# Split to folder and filenane
			folderName, fileName = os.path.split(rpath)
			
			# Test if folder exists
			if os.path.isdir(folderName):
				# Exists, start a new named project in that folder
				self.data=deepcopy(blankProject)
				self.setProject(self.data, fileName)
				
				self.log("Started a new blank project named '"+fileName+'.')
				
				# Are we already in that folder?
				if folderName!=os.getcwd():
					# Go to folder
					os.chdir(folderName)
					
				# Log folder name
				self.logCwd()
			else:
				# Does not exist, start a new blank project in current folder
				self.log("Folder '"+folderName+"' does not exist.")
				self.newProject()
	
	def logCwd(self):
		self.log("Current folder is '"+os.getcwd()+"'.")
		
	@pyqtSlot()
	def save(self):
		# If active tab is postprocessing
		ndx=self.tabWidget.currentIndex()
		w=self.tabWidget.widget(ndx)
		if type(w) is QPResultsViewer:
			# Save postprocessing
			self.savePostprocessingFile(w)
		else:
			# Save project
			self.saveProject()
	
	@pyqtSlot()
	def saveAll(self):
		# Go through all tabs, save project and postprocessing tabs
		st=self.saveProject()
		# Go through all tabs, save postprocessing files
		for ndx in range(self.tabWidget.count()):
			w=self.tabWidget.widget(ndx)
			if type(w) is QPResultsViewer:
				# Save it
				st=st and self.savePostprocessingFile(w)
		
		return st
	
	@pyqtSlot()
	def saveAs(self):
		# Save As always saves the project
		return self.saveProjectAs()
	
	# Save the project, open file dialog if the project is unnamed
	def saveProject(self):
		if (self.projectFileName is None): 
			return self.saveProjectAs()
		else:
			return self.saveProjectFile(self.projectFileName)
	
	# Save postprocessing widget to file
	def savePostprocessingFile(self, ppWidget):
		if ppWidget.savePostprocessingFile():
			# Mark widget unmodified
			self.markWidgetUnmodified(ppWidget)
			return True
		else:
			return False
		
	# Open a file name dialog, then save project
	def saveProjectAs(self):
		dialog=QFileDialog(self)
		dialog.setWindowModality(Qt.WindowModal);
		dialog.setAcceptMode(QFileDialog.AcceptSave);
		dialog.setDirectory(os.getcwd())
		dialog.setNameFilters([
			"Project files (*.pog)", 
			"All files (*)"
		])
		if (dialog.exec_() != QDialog.Accepted):
			return False
		
		txt=dialog.selectedFiles()[0]
		
		# Force extension *.pog
		l=txt.split(".")
		if len(l)<2 or l[-1]!="pog":
			txt+=".pog"
		
		return self.saveProjectFile(txt);
		
	# Save data in file 'name' regardless of the state of the project 
	def saveProjectFile(self, name):
		# Force commit the data in the project
		self.projectWidget.forceCommit()
		self.tasksWidget.forceCommit()
		
		try:
			p=os.path.expanduser(name)
			p=os.path.abspath(p)
			fpath, fname = os.path.split(p)
			
			dtxt=json.dumps(self.data, indent=2)
			with open(p, "w+") as f:
				f.write(dtxt)
			
			self.projectFileName=fname
			self.updateTitle()
			
			self.log("Saved project file '"+fname+"'.")
			
			# Set working folder
			if fpath!=os.getcwd():
				os.chdir(fpath)			
				# Display current folder message only if current folder is changed
				self.logCwd()
			
			# Project is no longer modified
			self.markProjectUnmodified()
			
			# Force poll in tasks monitor
			guiglobals.tasksMonitor.poll()
			self.updateTaskStatus()
			self.updateCPUstatus()
			self.enableTaskActions()
		
			return True
		except:
			self.log("Failed to save file '"+name+"'.", isError=True)
			return False
	
	def countUnsaved(self):
		count=0
		projectChanged=False
		for w in self.changedWidgets:
			if type(w) is QPResultsViewer:
				count+=1
			else:
				projectChanged=True
		
		return projectChanged, count
	
	def maybeSavePostprocessing(self, ppWidget):
		if ppWidget not in self.changedWidgets:
			return True
		
		title=self.tabTitle[ppWidget]
		
		ret=QMessageBox.warning(
			self, "Save changes?", 
			"The postprocessing settings have been modified.\n"+
			"Do you want to save postprocessing settings for '"+title+"'?", 
			QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel
		)
		if ret==QMessageBox.Save:
			return self.savePostprocessingFile(ppWidget)
		elif ret==QMessageBox.Cancel:
			return False
		else:
			return True
	
	def maybeSaveAll(self):
		# If nothing is modified, we're done
		if not self.isWindowModified():
			return True
		
		# Count unsaved items
		projectChanged, unsavedPostprocCount = self.countUnsaved()
		
		msg="The following items were modified but not saved:\n"
		if projectChanged:
			msg+="  project\n"
		if unsavedPostprocCount>0:
			msg+="  postprocessing setup for "+str(unsavedPostprocCount)+" result file(s)\n" 
		msg+="Do you want to save them?"
		ret=QMessageBox.warning(
			self, "Save changes?", msg, 
			QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel
		)
		if ret==QMessageBox.Save:
			return self.saveAll()
		elif ret==QMessageBox.Cancel:
			return False
		else:
			return True
	
		
	def updateTitle(self):
		displayName="Untitled" if self.projectFileName is None else self.projectFileName
		self.setWindowTitle(displayName+"[*] \u2014 PyOPUS GUI")
	
	@pyqtSlot()
	def openFile(self):
		dialog=QFileDialog(self)
		dialog.setWindowModality(Qt.WindowModal);
		dialog.setAcceptMode(QFileDialog.AcceptOpen);
		dialog.setDirectory(os.getcwd())
		dialog.setNameFilters([
			"All PyOPUS GUI files (*.pog *.log *.sqlite)", 
			"Project files (*.pog)", 
			"Log files (*.log)", 
			"Result files (*.sqlite)", 
			"All files (*)"
		])
		if (dialog.exec_() != QDialog.Accepted):
			return
		
		name=dialog.selectedFiles()[0]
		if len(name)>0:
			if name[-4:]==".pog":
				if self.maybeSaveAll():
					# Mark all widgets unmodified so we don't get another dialog
					self.markAllWidgetsUnmodified()
			
					self.loadFile(name)
			elif name[-4:]==".log":
				rp=os.path.realpath(name)
				self.logTab(rp)
			elif name[-7:]==".sqlite":
				rp=os.path.realpath(name)
				self.resultsTab(rp)
			else:
				fn=os.path.split(name)[-1]
				QMessageBox.information(self, "Cannot open file", "Don't know how to open '"+fn+"'.")
		
	# Load data from file 'name' regardless of the state of the project
	def loadFile(self, name, forceLogCWD=False):
		try:
			p=os.path.expanduser(name)
			p=os.path.abspath(p)
			fpath, fname = os.path.split(p)
			with open(p, "r") as f:
				jtxt=f.read()
			data=json.loads(jtxt)
		except:
			self.log("Failed to open file '"+name+"'.", isError=True)
			return False
		
		try:
			fv=data['info']['version']
		except:
			self.log("Bad file format. Keeping old project.", isError=True)
			return False
		
		# Add missing fields
		projectFixer(data)
		
		# In future versions importing of old project files must be implemented here
		if fv!="1.0":
			self.log("Don't know how to read file format "+fv+".", isError=True)
			self.log("Newer version of the GUI is required for opening '"+fname+"'.", isError=True)
			return False
		
		# Set working folder
		if fpath!=os.getcwd() or forceLogCWD:
			os.chdir(fpath)
			
		self.setProject(data, fname)
		
		self.log("Opened file '"+fname+"'.")
		
		# Display current folder always after open
		self.logCwd()
		
		return True
		
	def closeEvent(self, e):
		# Save GUI config to current folder
		self.writeGUIConfig()
		
		if self.maybeSaveAll():
			# Mark all widgets unmodified so we don't get another dialog
			self.markAllWidgetsUnmodified()
			# Cleanup
			self.closeAllTabs()
			self.projectWidget.destroy()
			self.tasksWidget.destroy()
			e.accept()
		else:
			e.ignore()
		
	@pyqtSlot()
	def about(self):
		QMessageBox.information(
			self, "About PyOPUS GUI",
			"<p>This is <b>PyOPUS GUI</b></p>"
			"<p>Version 0.9, revision "+str(revision)+"</p>"+
			"<p>(c)2017 EDA Lab FE Uni-LJ</p>"
		);
	
	def log(self, txt, isError=False, asHtml=True):
		self.loggerWidget.log(txt, isError, asHtml)

def diagnoseSimulators():
	from ..simulator import simulatorClass
	from .values import simulators

	txt=""
	found=False
	for name, key in simulators:
		cls=simulatorClass(key)
		simPath=cls.findSimulator()
		if simPath is not None:
			txt+="Found local simulator "+name+": "+simPath+"\n"
			found=True
	if not found:
		txt+="No local simulator found.\n"
	
	return txt

def diagnoseVM():
	from ..parallel import base
	from . import guiglobals
	
	if not guiglobals.mpiSupported:
		txt="MPI is not supported on this computer.\n"
	else:
		txt="Found MPI launcher: "+guiglobals.mpiLauncher+"\n"
	
		txt+="Local machine's VM mirrored storage:\n"
		ii=1
		for name in base.ParallelMirroredStorage:
			txt+="-- %d: %s\n" % (ii, name)
			ii+=1
		txt+="Local machine's VM local storage: "+base.ParallelLocalStorage+"\n"
	
	return txt

def main():
	import sip 
	import sys
	import platform
	from . import resources
	
	sip.setdestroyonexit(False)
	
	appName="pyog"
	
	if platform.platform().startswith('Windows'):
		import ctypes
		myappid = 'feunilj.pyopus.gui.1' # arbitrary string
		ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
	
	app = QApplication(sys.argv)
	
	w=QPMainWindow()
	icon=QIcon()
	icon.addFile(":resources/gui.png")
	icon.addFile(":resources/gui24.png")
	icon.addFile(":resources/gui32.png")
	icon.addFile(":resources/gui48.png")
	icon.addFile(":resources/gui256.png")
	w.setWindowIcon(icon)
	
	w.log("Running on host '%s' with %d CPU(s)." % (guiglobals.hostname, guiglobals.localCPUcount))
	w.log(diagnoseSimulators())
	w.log(diagnoseVM())
	w.log("Using PyOPUS GUI file format version 1.0.")
	
	if len(sys.argv)>1:
		projectName=None
		windows=[]
		ndx=1
		while ndx<len(sys.argv):
			arg=sys.argv[ndx]
			if arg=="-h" or arg=="--help":
				print("PyOPUS GUI usage:")
				print("")
				print("  Open files")
				print("    "+appName+" [project_file.pog|log_file.log|results_file.sqlite]")
				print("")
				print("  Help")
				print("    "+appName+" [-h|--help]")
				print("")
				sys.exit(1)
			else:
				# Determine file type
				if arg.rfind(".pog")>=0:
					if projectName is not None:
						sys.stderr.write("Multiple project (.pog) files specified.\n")
						sys.stderr.flush()
						sys.exit(1)
					projectName=os.path.realpath(arg)
				elif arg.rfind(".log")>=0:
					windows.append(
						[ "log", os.path.realpath(arg) ]
					)
				elif arg.rfind(".sqlite")>=0:
					windows.append(
						[ "results", os.path.realpath(arg) ]
					)
				else:
					sys.stderr.write("Unknown file type, file '"+arg+"'.\n")
					sys.stderr.flush()
					sys.exit(1)
			ndx+=1
			
		# Try to load project
		if projectName is not None:
			if not w.loadFile(sys.argv[1], True):
				# On failure try to start a new blank project with given name
				w.newNamedProject(sys.argv[1])
		
		# Load log and results files
		for ft, fn in windows:
			if ft=="log":
				w.logTab(fn)
			elif ft=="results":
				w.resultsTab(fn)
	else:
		# Start unnamed blank project in current folder
		w.newProject()
	
	w.log("Welcome to PyOPUS GUI.")
	
	w.show()
	# w.resize(QSize(1050, 768))
	app.exec_()
	
	return 0

if __name__=='__main__':
	main()
	
