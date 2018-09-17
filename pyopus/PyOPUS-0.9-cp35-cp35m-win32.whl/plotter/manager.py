"""
.. inheritance-diagram:: pyopus.plotter.manager
    :parts: 1
	
**Manager for Matplotlib plot windows**

The graphical part (PyQt + MatPlotLib) is running in a thread and the 
part that issues the plotting commands (defined in the 
:mod:`~pyopus.plotter.interface` module) runs in the main thread (or process). 

The main thread uses a :class:`QPController` object for sending and receiving 
messages from the graphical thread. The messages are sent to the GUI by 
emitting a ``messagePoster`` signal from a :class:`QPController`. 
A :class:`queue.Queue` object is used for sending the response back to the 
main thread. On the graphical thread's side a :class:`QPControlWindow` widget 
is handling the received commands. 

The ``processMessage`` slot in :class:`QPControlWindow` calls the 
:meth:`QPControlWindow.interpretCommand` method that dispatches the received 
message to the corresponding command handler. 
"""

import threading
import queue
import pickle
import traceback
import time
import os

from matplotlib import rcParams
from matplotlib.lines import Line2D
try:
	from mpl_toolkits.mplot3d import Axes3D
except:
	print("Failed to import Axes3D. 3D plotting is not available.")

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ..gui.style import styleWidget
from .. import PyOpusError

from .plotwidget import *

__all__ = [ 'QPController' ]

#
# QPControlWindow providing a main window for messages
#

class QPControlWindow(QMainWindow):
	"""
	This is the main GUI ControlWindow and command dispatcher. 
	
	*parent* is the parent window. *title* is the window title. 
	
	*queue* is a :class:`queue.Queue` object for sending responses back to 
	the main thread. 
	
	*lock* is a :class:`threading.Lock` object that prevents other threads 
	from messing up MatPlotLib objects while Qt events are processed. 
	"""
	def __init__(self, parent=None, title="Plot manager", queue=None, lock=None):
		QMainWindow.__init__(self, parent)
		
		self.setWindowTitle(title)
		
		# Store the lock and queue
		self.lock=lock
		self.queue=queue
		
		# And a menu 
		self.createActions()
		
		# Create staus bar
		self.statusBar()
		
		# Create display for messages
		self.messages=QPlainTextEdit(self)
		self.messages.setReadOnly(True)
		styleWidget(self.messages, ["monospace"])
		
		self.setCentralWidget(self.messages)
		
		# Create message frame
		self.outputMessage("Control window ready.\n")

		# Plot window storage
		self.plotWindows={}
		self.plotTagIndex={}
		
		# Initialize interpreter
		self.plot_cmdtab={}
		self.InitInterpreter()
		
		self.resize(400,200)
		
	def createActions(self):
		"""
		Create menu actions. 
		"""
		self.fileMenu=self.menuBar().addMenu("&File")
		
		newAction=QAction("&New plot", self)
		newAction.setShortcuts(QKeySequence("CTRL+N"))
		newAction.setStatusTip("Open new plot window")
		newAction.triggered.connect(self.onNewPlot)
		self.fileMenu.addAction(newAction)
		
		closeAction=QAction("&Close all plots", self)
		closeAction.setStatusTip("Close all plot windows")
		closeAction.triggered.connect(self.onCloseAll)
		self.fileMenu.addAction(closeAction)
		
		exitAction=QAction("E&xit", self)
		exitAction.setStatusTip("Exit")
		exitAction.triggered.connect(self.onExit)
		self.fileMenu.addAction(exitAction)
		
	def outputMessage(self, msg, colour=(0,0,0)):
		"""
		Displays a message given by *msg* in the control window. 
		The message colour is specified by *colour*. 
		"""
		prefix="<font color='#%02x%02x%02x'>" % (colour)
		suffix="</font>"
		self.messages.appendHtml(prefix+msg.replace("\n","<br />")+suffix)
		
	def InitInterpreter(self):
		"""
		Initializes the interpreter command tables. 
		
		Every command is a list with the command string, the positional 
		arguments, and the keyword arguments. 
		
		Every command is passed an *args* tuple of positional arguments and a 
		*kwargs* dictionary of keyword arguments. 
		
		Every plot window is actually a 
		:class:`~pyopus.plotter.plotwidget.QPPlotWindow` object displaying a 
		Matplotlib :class:`Figure`. Every plot window is associated with a 
		hashable tag at its creation (currently the corresponding 
		:class:`Figure` object is used as tag). 
		
		The ``plot`` command group has the following commands:
		
		* ``exit`` - exits the interpreter
		* ``updatercparams`` - update the rc parameters with the given 
		  dictionary
		* ``new`` - create a new plot window and return its tag
		* ``close`` - close a plot window
		* ``closeall`` - close all plot windows
		* ``setwindowtitle`` - sets the title of a plot window
		* ``show`` - show or hide aplot window
		* ``raise`` - raise a plot window
		* ``savefigure`` - saves the contents of a figure to a file
		
		"""
		self.plot_cmdtab={
			'exit':				self.exitInterpreter, 
			'updatercparams':	self.updateRCParams, 
			'new':				self.newPlotWindow, 
			'close':			self.closePlotWindow, 
			'closeall':			self.closeAllPlotWindows, 
			'setwindowtitle':	self.setPlotWindowTitle, 
			'show':				self.showPlotWindow,
			'raise':			self.raisePlotWindow, 
			'savefigure':		self.saveFigure, 
		}
		
	def exitInterpreter(self):
		"""
		Handles the ``exit`` command.
		
		Exits the interpreter (thread or process).
		"""
		self.close()
	
	def updateRCParams(self, dict):
		"""
		Handles the ``updatercparams`` command.
		
		Update the rcParams structure of Matplotlib with the given dictionary.
		Returns ``True`` on success. 
		"""
		try:
			rcParams.update(dict);
			retval=True
		except:
			retval=False
		
		return retval
		
	def newPlotWindow(self, windowTitle="Untitled", show=True, inFront=True, **kwargs):
		"""
		Handles the ``'new`` command.
		
		*windowTitle* is the title string for the plot window. 
		
		If *show* is ``True`` the window becomes visible immediately after it 
		is created. 
		
		If *inFront* is ``True`` the window is created atop of all other 
		windows. 
		
		All remaining arguments are passed on to the constructor of the 
		:class:`~pyopus.plotter.plotwidget.QPFigureCanvas` object. 
		
		Returns the plot window's :class:`Figure` object or ``None`` on failure.
		"""
		# Pass the lock to the QPPlotWindow (plot window). 
		window=QPPlotWindow(None, title=windowTitle, lock=self.lock, **kwargs)
		tag=window.getFigure()
		
		self.plotTagIndex[window]=tag
		self.plotWindows[tag]={}
		self.plotWindows[tag]['obj']=window
		
		# Connection must be queued because just before the window is closed a signal
		# is emitted that triggers the deletion of the window from manager's structures. 
		# Then the garbage collector deletes the window object. Unfortunately if 
		# DirectConnection is used we return from the slot that did the deletion to the 
		# place where the signal was emitted. Now Qt tries to do the final steps of 
		# closing a window but the window is gone already which results in a crash. 
		# This does not happen with a QueuedConnection because deletion is performed after 
		# Qt does its window closing stuff. 
		window.windowClosing.connect(self.onChildClosed, Qt.QueuedConnection)
		window.closeAllRequest.connect(self.onCloseAll, Qt.QueuedConnection)
		
		if show:
			window.show()
		
		if inFront:
			window.raise_()
		
		return tag
		
	def closePlotWindow(self, tag=None):
		"""
		Handles the ``close`` command.
		
		Closes a plot window with given *tag*. 
		
		Returns ``True`` on success.
		"""
		if tag in self.plotWindows:
			self.plotWindows[tag]['obj'].close()
			return True
		else:
			return False
			
	def closeAllPlotWindows(self):
		"""
		Handles the ``closeall`` command.
		
		Closes all plot windows.
		"""
		tags=list(self.plotWindows.keys())
		for tag in tags:
			self.plotWindows[tag]['obj'].close()
		
		return True
	
	def setPlotWindowTitle(self, tag, title):
		"""
		Handles the ``setwindowtitle`` command.
		
		Sets the window title of the active plot window. 
		
		Returns ``True`` on success. 
		"""
		if tag in self.plotWindows:
			window=self.plotWindows[tag]['obj']
		else:
			return False
		
		window.setWindowTitle(title)
		
		return True
	
	def showPlotWindow(self, tag, on=True):
		"""
		Handles the ``show`` command.
		
		Shows (*on* set to ``True``) or hides a plot window. 
		
		Returns ``True`` on success. 
		"""
		if tag in self.plotWindows:
			window=self.plotWindows[tag]['obj']
		else:
			return False
		
		if on:
			window.show()
		else:
			window.hide()
		
		return True
	
	def raisePlotWindow(self, tag):
		"""
		Handles the ``raise`` command.
		
		Raises a plot window with given *tag*. 
		
		Returns ``True`` on success. 
		"""
		if tag in self.plotWindows:
			window=self.plotWindows[tag]['obj']
		else:
			return False
		
		window.raise_()
		
		return True
		
	def saveFigure(self, tag, fileName):
		"""
		Handles the ``savefigure`` command.
		
		Saves the contents of a plot window with given *tag* to a file with a 
		name given by *fileName*. File type is determined from the extension 
		in the *fileName*. 
		
		See the :meth:`FigureCanvas.print_figure` method. The available 
		file types are listed in the :attr:`FigureCanvas.filetypes` 
		dictionary. 
		
		Returns ``True`` on success. 
		"""
		# Get window (PlotFrame)
		if tag in self.plotWindows:
			window=self.plotWindows[tag]['obj']
		else:
			return False
		
		# Get canvas
		fig=window.getCanvas()
		
		# Save to file
		fig.print_figure(fileName)
		
		return True
		
	def FigureAlive(self, tag):
		"""
		Returns ``True`` if figure *tag* is alive (i.e. window is not closed). 
		"""
		if tag in self.plotWindows and self.plotWindows[tag]['obj']:
			return True
		else:
			return False
		
	def figureDraw(self, tag):
		"""
		Redraws the figure *tag* immediately. 
		
		If *tag* is not alive doesn't do anything. 
		"""
		if tag in self.plotWindows:
			window=self.plotWindows[tag]['obj']
		
			if window:
				window.draw()
		
	def _RemovePlotWindow(self, window):
		"""
		Removes a plot window given by object *window* from the list of plot 
		windows. 
		
		Returns ``True`` on success.
		
		This should not be called directly. Call closePlotWindow() instead.
		"""
		if window in self.plotTagIndex:
			tag=self.plotTagIndex[window]
		else:
			return False
		
		if tag is not None:
			del self.plotWindows[tag]
			del self.plotTagIndex[window]
			
			return True
		else:
			return False
				
	def interpretCommand(self, command, args=[], kwargs={}):
		"""
		Interprets the command given by the *command* list of strings. The 
		first string is the command family and the second string is the 
		command. Currently only one command family is available (``plot``). 
		
		The arguments to the command are given by *args* and *kwargs*. 
		
		The command handlers are given in handler dictionaries with command 
		name for key. The handler dictionary for the ``plot`` command family 
		is is the :attr:`plot_cmdtab` member. 
		
		Every command is handled in a ``try-except`` block If an error occurs 
		during command execution the error is displayed in the command window. 
		
		The return value of the command handler is returned. 
		
		This method is invoked by the :class:`QPControlWindow` on every 
		message received from a :class:`QPController` object. The contents of 
		the message specify the command and the arguments (args and kwargs). 
		"""
		response=None
		
		if command[0]=='plot':
			# Plot commands
			# In future this will be a part of the plot controller object
			# Figure commands
			if command[1] in self.plot_cmdtab:
				try:
					# self.outputMessage("Command: '"+str(command)+" "+str(args)+str(kwargs)+"'\n")
					response=self.plot_cmdtab[command[1]](*args, **kwargs)
					# self.outputMessage("Response: '"+str(response)+"'\n")
				except:
					self.outputMessage('Exception in '+str(command)+'\n', colour=(0,0,0))
					self.outputMessage(traceback.format_exc(), colour=(180,0,0))
					response=None
			else:
				self.outputMessage("Unknown command [1]: '"+str(command)+"'\n")
		else:
			self.outputMessage("Unknown command [0]: '"+str(command)+"'\n")
		
		return response
	
	@pyqtSlot()
	def onNewPlot(self):
		"""
		Handles the File/New plot option. 
		"""
		self.newPlotWindow()
	
	@pyqtSlot()
	def onCloseAll(self):
		"""
		Handles the File/Close all plots option. 
		"""
		keys=self.closeAllPlotWindows()
	
	@pyqtSlot(QWidget)
	def onChildClosed(self, w):
		"""
		Called when a child (plot window) is about to close. 
		"""
		# Remove it from the list
		self._RemovePlotWindow(w)
		
	@pyqtSlot()
	def onExit(self):
		"""
		Handles the File/Exit option. 
		"""
		self.close()
	
	@pyqtSlot(object)
	def processMessage(self, message):
		"""
		Handles incoming messages (signals conencted to this slot). 
		
		A message is a list containing the command, args, and kwargs. 
		"""
		response=self.interpretCommand(message['cmd'], message['args'], message['kwargs'])
		self.queue.put(response)
		
	def closeEvent(self, e):
		self.onCloseAll()
		e.accept()
	
#
# This are the GUIcontrol classes.  
#

def GUIentry(args, queue, lock):
	"""
	Entry point of the GUI thread. 
	
	This function creates a :class:`QPControlWindow` object and starts the 
	GUI application's main loop. *queue* is the queue that is used for 
	returning values from the GUI. Commands are sent to the GUI by emitting
	signals from a :class:`QPController` object whose ``messagePoster`` 
	signal is connected to the ``processMessage`` slot of the 
	:class:`QPControlWindow` object. 
	
	*lock* is a :class:`threading.Lock` object for preventing the main thread 
	from messing with gui data while gui events are handled. 
	"""
	app=QApplication(args)
		
	w=QPControlWindow(None, queue=queue, lock=lock)
	w.show()
	w.raise_()
	
	# Send the QPControlWindow object to the main thread
	# so that we can connect to its slots
	queue.put(w, True)
	
	# Enter GUI main loop. 
	#while True:
	#	app.processEvents()
	app.exec_()
	
	# This is reached after main loop finishes
	
	

#
# ControlApp running in a separate thread with its own event loop that handles the plot windows
#

class QPController(QObject):
	"""
	This is the controller responsible for sending commands to the GUI 
	and collection responses. 
	
	*args* are passed to the :func:`GUIentry` function which forwards 
	them as command line arguments to the :class:`QApplication` object. 
	"""
	messagePoster=pyqtSignal(object)
	
	def __init__(self, args=[]):
		QObject.__init__(self)
		
		self.controlWindow=None
		self.responseQueue=queue.Queue(-1)
		self.lock=threading.Lock()
		self.locked=False
		self.guiThread=None
		self.controlWindow=None

	def startGUI(self):
		"""
		Starts the GUI thread. 
		"""
		_, fn = os.path.split(__file__)
		if not self.checkIfAlive():
			self.guiThread=threading.Thread(
				target=GUIentry, args=[[fn], self.responseQueue, self.lock]
			)
			# self.guiThread.daemon=True
			self.guiThread.start()
			# Get the control app from the GUI (wait for thread to start)
			self.controlWindow=self.responseQueue.get(True)
			self.messagePoster.connect(self.controlWindow.processMessage, Qt.QueuedConnection)

	def checkIfAlive(self):
		"""
		Returns ``True`` if the GUI thread is running. 
		"""
		if self.guiThread is not None: 
			if self.guiThread.isAlive():
				return True
			else: 
				self.guiThread=None
				self.messagePoster.disconnect()
				return False
		else:
			return False

	def stopGUI(self):
		"""
		Stops the GUI thread by sending it the ``exit`` command. 
		"""
		self.postMessage({
				'cmd':['plot', 'exit'], 
				'args': [], 
				'kwargs': {}
			}
		)
	
	def join(self):
		"""
		Waits for the GUI thread to finish. 
		
		:obj:`KeyboardInterrupt` and :obj:`SystemExit` are caught and the GUI 
		is stopped upon which the exception is re-raised. 
		"""
		try:
			while self.guiThread.is_alive():
				self.guiThread.join(timeout=0.1)
		except (KeyboardInterrupt, SystemExit):
			self.stopGUI()
			raise
	
	def postMessage(self, message): 
		"""
		This is the function that is invoked for every command that is sent 
		to the GUI. It emits a ``messagePoster`` signal. 
		"""
		if self.checkIfAlive():
			self.messagePoster.emit(message)
			response=self.responseQueue.get()
			return response
		else:
			return None
		
	def figureAlive(self, tag):
		"""
		Checks if the window of the given :class:`Figure` is still open. 
		"""
		try:
			retval=self.controlWindow.FigureAlive(tag)
		except (KeyboardInterrupt, SystemExit):
			# Re-reaise these two exceptions
			raise
		except:
			# Everything else is an error
			raise PyOpusError("Matplotlib GUI thread is not running.")
	
		return retval
		
	def figureDraw(self, tag):
		"""
		Forces redrawing of the given :class:`Figure`. 
		"""
		try:
			self.controlWindow.figureDraw(tag)
		except (KeyboardInterrupt, SystemExit):
			# Re-reaise these two exceptions
			raise
		except:
			# Everything else is an error
			raise
			raise PyOpusError("Matplotlib GUI thread is not running.")
	
	def lockGUI(self):
		"""
		Marks the beginning of a section of code where Matplotlib API calls are 
		made. Locking prevents these calls from interfering with the PyQt
		event loop and crashing the application. 
		"""
		# Lock if not already locked
		if not self.locked:
			# print("Locking GUI")
			self.locked=True
			self.lock.acquire(True)
	
	def unlockGUI(self):
		"""
		Marks the end of a section of code where Matplotlib API calls are made. 
		It reenables the PyQt event loop.  
		"""
		if self.locked:
			# print("Unlocking GUI")
			self.lock.release()
			self.locked=False
			

if __name__=='__main__':
	import sip 
	import sys
	
	sip.setdestroyonexit(False)
	
	if 0:
		app = QApplication(sys.argv)
		
		w=QPControlWindow()
		
		w.show()
		app.exec_()
		
	c=QPController()
	c.startGUI()
	
	ret=c.postMessage({
			'cmd':['plot', 'new'], 
			'args': [], 
			'kwargs': {}
		})
	print(ret)
	
	c.join()
	
