from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .fstools import *
from . import guiglobals
from .. import PyOpusError

import os, os.path, time, math, json, signal

__all__ = [ 
	'QPTasksMonitorError', 'QPTasksMonitor' 
]

# lock.request
# at beginning of dump
#   timestamp starting
# at stop request
#   timestamp stopping
#   
# lock.response
# at start
#   timestamp started pid
# at end
#   timestamp finished status

# States:
#  None      = no tags / can start
#  starting  = starting !started !finished 
#  running   = starting started  !stopping !finished / can stop
#  stopping  = starting started stopping !finished 
#  finished  = starting started ?stopping finished / can start
#  error     = undefined (error reading state)
# message: started @ transition starting -> running or initial -> running
#          stopped @ transition running -> finished or stopping -> finished

class QPTasksMonitorError(PyOpusError):
	def __init__(self, message, *args):
		super(QPTasksMonitorError, self).__init__(message, *args)

class QPTasksMonitor(QObject):
	def __init__(self, data=None, fullCheck=True, parent=None):
		QObject.__init__(self, parent)
		self.fullCheck=True
		
		# Dictionary of dictionaries, first indes is task name, second index in aspect
		# Holds all aspects of a task's status
		self.status={}
		
		# Available task status aspects
		#   state (None starting started stopping finished)
		#   startTime (timestamp)
		#   pid (int)
		#   vmLayout (dictionary, host name for key, CPU count for value)
		#   exitStatus (int)
		
		self.timerId=None
		self.setProject(data)
		
		# Dictionary of dictionaries, first index is host name, second index is task name
		# Holds number of assigned CPUs on a host for a task
		self.tasksOnHost={}
		
		self.starting=set()
		self.stopping=set()
		self.lastRunningTasks=set()
		
		# Initially we don't want to send out status changed signals
		# which trigger messages in the log window
		self.poll(sendStatusChanged=False)
		
	tasksOnHostChanged=pyqtSignal()
	taskStatusChanged=pyqtSignal(str)
	
	hostsListChanged=pyqtSignal()
	
	def emitHostsListChanged(self):
		self.hostsListChanged.emit()
		
	# Cleanup
	def destroy(self):
		setCheckPeriod(-1)
		
	def setProject(self, data):
		self.data=data
		self.status={}
	
	def setFullCheck(self, b):
		self.fullCheck=fullCheck
	
	def removeFromTasksOnHost(self, taskName):
		if taskName in self.status:
			vmLayout=self.status[taskName]['vmLayout']
			changedVm=False
			if vmLayout is not None:
				for host, cpus in vmLayout.items():
					if host not in self.tasksOnHost:
						h={}
						self.tasksOnHost[host]=h
					else:
						h=self.tasksOnHost[host]
					
					if taskName in h:
						del h[taskName]
						changedVm=True
			
			if changedVm:
				self.tasksOnHostChanged.emit()
	
	def readVmLayout(self, taskName):
		p=os.path.join(taskName, "vmlayout")
		try:
			with open(p, "r") as f:
				txt=f.read()
				vmLayout=json.loads(txt)
		except Exception:
			# No vmlayout - default to one process on localhost
			vmLayout={ guiglobals.hostname: 1 }
		
		return vmLayout
	
	def mergeWithTasksOnHost(self, taskName, vmLayout):
		if vmLayout is None:
			return
		
		changedVm=False
		for host, ncpu in vmLayout.items():
			if host not in self.tasksOnHost:
				self.tasksOnHost[host]={}
			hostDict=self.tasksOnHost[host]
			
			if taskName not in hostDict:
				# Task name not in host dictionary (task just appeared)
				# Add it to host dictionary
				hostDict[taskName]=ncpu
				changedVm=True
			elif ncpu!=hostDict[taskName]:
				# Task is in host dict, but the number of CPUs has changed
				# Record change
				hostDict[taskName]=ncpu
				changedVm=True
	
		if changedVm:
			self.tasksOnHostChanged.emit()
	
	def removeTask(self, taskName):
		if taskName in self.status:
			self.removeFromTasksOnHost(taskName)
			del self.status[taskName]
		
		self.taskStatusChanged.emit(taskName)
			
	def readTaskStatus(self, taskName):
		# Defaults
		state=None
		startTime=None
		pid=None
		vmLayout=None
		exitStatus=None
		
		# Tag set 
		tags=set([])
		
		# Open lock.request
		p=os.path.join(taskName, "lock.request")
		try:
			with open(p, "r") as f:
				# Read lines
				while True:
					s=f.readline()
					
					if len(s)==0:
						# EOF
						break
					
					# Split at spaces
					parts=s.split(" ")
					
					# Ignore anything without at least two parts
					if len(parts)<2:
						continue
					
					# Extract
					timestamp=float(parts[0])
					tags.add(parts[1].strip())
		except Exception:
			pass
		
		# Open lock.response
		p=os.path.join(taskName, "lock.response")
		try:
			with open(p, "r") as f:
				# Read lines
				while True:
					s=f.readline()
					
					if len(s)==0:
						# EOF
						break
					
					# Split at spaces
					parts=s.split(" ")
					
					# Ignore anything without at least two parts
					if len(parts)<2:
						continue
					
					# Extract
					timestamp=float(parts[0])
					tag=parts[1].strip()
					if tag=="started" and len(parts)>=4:
						pid=int(parts[2].strip())
						tags.add(tag)
						startTime=timestamp
					elif tag=="finished" and len(parts)>=3:
						exitStatus=int(parts[2].strip())
						tags.add(tag)
		except Exception:
			pass
		
		# Get state
		if (
			"starting" in tags and 
			"started" not in tags and 
			"stopping" not in tags and
			"finished" not in tags
		): 
			state="starting"
		elif (
			"starting" in tags and 
			"started" in tags and 
			"stopping" not in tags and
			"finished" not in tags
		): 
			state="running"
		elif (
			"starting" in tags and 
			"started" in tags and 
			"stopping" in tags and
			"finished" not in tags
		): 
			state="stopping"
		elif (
			"starting" in tags and 
			"started" in tags and 
			"finished" in tags
		): 
			state="finished"
		elif (
			"starting" not in tags and 
			"started" not in tags and 
			"stopping" not in tags and
			"finished" not in tags
		):
			state="ready"
		else:
			state="error"
		
		return state, startTime, pid, exitStatus
	
	def blankTask(self):
		return {
			'state': "inital", 
			'startTime': None, 
			'pid': None, 
			'vmLayout': None, 
			'exitStatus': None
		}
		
	def poll(self, taskNames=None, sendStatusChanged=True):
		# If no tasks are explicitly given
		if taskNames is None:
			# Tasks in project
			taskNames=[t[0] for t in self.data['tasks']] if self.data is not None else []
			
			# Construct a list of all task folders
			if self.fullCheck:
				# Make a list of subfolders
				dirs, files = listDir(".")
				taskNames.extend(dirs)
			
		# Go through all candidates
		for taskName in taskNames:
			# Does subfolder exists
			info=fileInfo(taskName)
			if info['type'] is None:
				# Does not exist, remove
				self.removeTask(taskName)
				
				# Signal we can start it
				self.taskStatusChanged.emit(taskName)
				
				continue
			
			# New task folder detected
			if taskName not in self.status:
				self.status[taskName]=self.blankTask()
			
			# Read status
			state, startTime, pid, exitStatus = self.readTaskStatus(taskName)
			
			# Detect status change
			oldStatus=self.status[taskName]
			if oldStatus['state']!=state:
				st=self.status[taskName]
				
				# Write status information
				if state=="error":
					st['startTime']=None
					st['pid']=None
					st['vmLayout']=None
					st['exitStatus']=None
				elif state=="starting":
					# Task is starting
					st['startTime']=None
					st['pid']=None
					st['vmLayout']=None
					st['exitStatus']=None
				elif state=="running":
					# Task just started
					# Read vmLayout file
					vmLayout=self.readVmLayout(taskName)
					st['vmLayout']=vmLayout
					# Merge it with tasksOnHost
					self.mergeWithTasksOnHost(taskName, vmLayout)
					st['startTime']=startTime
					st['pid']=pid
					st['exitStatus']=None
				elif state=="stopping":
					# Task is about to be stopped
					st['startTime']=startTime
					st['pid']=pid
					st['exitStatus']=None
				elif state=="finished":
					# Task just finished
					# Remove task from tasksOnHost
					self.removeFromTasksOnHost(taskName)
					st['startTime']=None
					st['pid']=None
					st['vmLayout']=None
					st['exitStatus']=exitStatus
				elif state is "ready":
					# Task in initial state
					self.removeFromTasksOnHost(taskName)
					st['startTime']=None
					st['pid']=None
					st['vmLayout']=None
					st['exitStatus']=None
					
				# Record new state
				st['state']=state
				
				# print("task", taskName, "new status", state)
				if sendStatusChanged:
					self.taskStatusChanged.emit(taskName)
				
	def setCheckPeriod(self, ms):
		if ms<0 and self.timerId is not None:
			self.killTimer(self.timerId)
		elif ms>0:
			self.timerId=self.startTimer(ms, Qt.VeryCoarseTimer)
	
	def timerEvent(self, te):
		self.poll()
	
	def usedCPUCount(self, hosts=None):
		if hosts is None:
			# hosts are not validated, must remove duplicates
			hosts=list(set([h[0].strip() for h in guiglobals.hosts]))
			
		usedSlots=0
		for host in hosts:
			# hostLayout() returns {} if no such host is found
			for taskName, ncpu in guiglobals.tasksMonitor.hostLayout(host).items():
				usedSlots+=ncpu
		return usedSlots
	
	def state(self, taskName):
		return self.status[taskName]['state'] if taskName in self.status else None
	
	def exitStatus(self, taskName):
		# Assumes task is in finished state
		return self.status[taskName]['exitStatus']
	
	def isRunning(self, taskName):
		return True if taskName in self.status and self.status[taskName]['state']=="running" else False
	
	def runningSince(self, taskName):
		# Assumes task is in started state so that startTime is availabke
		return self.status[taskName]['startTime']
	
	def killTask(self, taskName):
		if taskName in self.status:
			pid=self.status[taskName]['pid']
			if pid is not None:
				try:
					os.kill(pid, signal.SIGTERM)
				except:
					raise QPTasksMonitorError("Failed to kill task.")
	
	def vmLayout(self, taskName):
		if taskName in self.status:
			return self.status[taskName]['vmLayout']
		else:
			return {}
	
	def taskCPUCount(self, taskName):
		if taskName in self.status and self.status[taskName]['vmLayout'] is not None:
			vl=self.status[taskName]['vmLayout']
			return sum([ncpu for hname, ncpu in vl.items()]+[0])
	
	def allocatedHostNames(self):
		return list(self.tasksOnHost.keys())
	
	def hostLayout(self, hostName):
		if hostName in self.tasksOnHost:
			return self.tasksOnHost[hostName]
		else:
			return {}
	
