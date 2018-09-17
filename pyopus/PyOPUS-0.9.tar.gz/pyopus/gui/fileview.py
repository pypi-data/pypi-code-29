from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .widgets import *
from ..design.sqlite import *
from .restree import *
from .restext import *
from .style import styleWidget
from .logger import *

from copy import deepcopy
import os, platform, datetime
#import pdb
#from PyQt5.QtCore import pyqtRemoveInputHook


class QPFileViewer(QWidget):
	def __init__(self, fileName, loggerWidget=None, parent=None):
		QWidget.__init__(self, parent)
		
		if loggerWidget is None:
			self.loggerWidget=QPDummyLogger()
		else:
			self.loggerWidget=loggerWidget
			
		self.fileName=fileName
		self.realPath=os.path.realpath(fileName)
		self.uuid=None
		self.t0=None
		
		if platform.platform().startswith('Windows'):
			# Under Windows use polling because QFileSystemWatcher does not work
			self.pollWatcher=True
		else:
			self.pollWatcher=False
		
		# Uncomment this to disable file change notification and use polling exclusively
		# self.pollWatcher=True
		
		self.timer=QTimer(self)
		self.timer.timeout.connect(self.checkFileTimeout)
		
		self.fw=QFileSystemWatcher(self)
		self.fw.fileChanged.connect(self.checkFile)
		
		self.fileWidget=QLineEdit(self)
		self.fileWidget.setReadOnly(True)
		self.fileWidget.setText(self.realPath)
		
		self.timeWidget=QPAdaptiveLineEdit(self)
		self.timeWidget.setReadOnly(True)
		self.timeWidget.setText("-")
		
		self.fileWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		self.timeWidget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
		
		h=QHBoxLayout()
		h.addWidget(QLabel("File", self))
		h.addWidget(self.fileWidget)
		h.addWidget(self.timeWidget)
		
		self.vlayout=QVBoxLayout(self)
		self.vlayout.addLayout(h)
		
		self.setLayout(self.vlayout)
		
		# Single shot for the first time, after that waitingModeEnable() will set it to periodic
		self.waitingMode=False
		self.timer.setSingleShot(True)
		self.timer.start(10)
		
	def log(self, txt, isError=False, asHtml=True):
		self.loggerWidget.log(txt, isError, asHtml)

	# Override in child class, returns uuid, t0, and flag if the display needs updating
	def statFile(self):
		return None, None, False
	
	# Override in child, clears the view when a new file is detected
	def clearView(self):
		pass
	
	# Override in child, updates the view to reflect the changes
	def updateView(self):
		pass
	
	# Override in child, handles a stat error
	def handleStatError(self):
		pass
	
	# Override in child, handles an update error
	def handleUpdateError(self):
		pass
	
	# Override in child, sets the viewer to reflect an error
	def setViewerError(self, flag):
		pass
			
	# Cleanup (happens after the tab with this widget is closed)
	def destroy(self):
		if self.waitingMode:
			self.timer.stop()
		else:
			self.fw.removePath(self.realPath)
			
	# Force commit (need not do anything, used in editors)
	def forceCommit(self):
		pass
		
	def waitingModeEnable(self, flag, timeout=1000):
		if flag:
			#print("req enable wm")
			#print("enable wm")
			if len(self.fw.files())>0:
				st=self.fw.removePath(self.realPath)
			self.timer.setSingleShot(False)
			self.timer.start(timeout)
			self.waitingMode=True
		else:
			#print("req disable wm")
			#print("disable wm")
			self.timer.stop()
			if len(self.fw.files())==0:
				st=self.fw.addPath(self.realPath)
			self.waitingMode=False
			
	@pyqtSlot()
	def checkFileTimeout(self):
		self.checkFile()
	
	@pyqtSlot(str)
	def checkFile(self, dummyPath=None):
		# Stat file
		#print("chk")
		statFailed=False
		try:
			uuid, self.t0, needUpdate = self.statFile()
			#print("uuid", uuid, "t0", self.t0, "Need update", needUpdate)
		except:
			# Failed to stat file (error)
			# print("stat failed")
			# raise
			statFailed=True
			uuid=None
			self.t0=None
			needUpdate=False
		
		# Update time display
		if self.t0 is not None:
			self.timeWidget.setText(
				datetime.datetime.fromtimestamp(
					self.t0
				).strftime("%Y-%m-%d %H:%M:%S")
			)
		else:
			self.timeWidget.setText("-")
		
		if statFailed:
			# Handle error
			self.handleStatError()
			self.setViewerError(True)
			
			# Go to polling mode
			self.waitingModeEnable(True)
			
		if uuid!=self.uuid:
			# Handle new file
			#print("new uuid", uuid)
			self.uuid=uuid
			self.clearView()
		
		# Try updating the view
		if needUpdate:
			try:
				# Leave waiting mode if applicable
				if self.pollWatcher:
					# In poll watcher mode we are using only polling
					self.waitingModeEnable(True)
				else:
					# If not in poll watcher mode, turn off polling
					self.waitingModeEnable(False)
				
				# Clear error first so that the style of the widget is set to normal mode
				self.setViewerError(False)
				
				# Update view
				self.updateView()
				
			except:
				# Go to waiting mode
				self.waitingModeEnable(True)
				
				# Failed, set error
				self.setViewerError(True)
				
