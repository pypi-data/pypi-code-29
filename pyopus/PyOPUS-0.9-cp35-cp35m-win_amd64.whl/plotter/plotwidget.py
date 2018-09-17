"""
.. inheritance-diagram:: pyopus.plotter.plotwidget
    :parts: 1
	
**PyQt canvas for displaying Matplotlib plots**

This module provides a PyQt canvas for Matplotlib to render its plots on. 
The canvas supports zooming and displays cursor position in axes coordinates 
as the cursor moves across the canvas. 

A plot window is an object of the :class:`QWidget` class. The canvas itself 
is an object of the :class:`PlotPanel` class. 

The module also provides saving of the plots to raster (e.g. PNG) or vector 
files (e.g. Postscript). 
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import os.path
import weakref

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import rcParams
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

__version__ = '1.0'

__all__ = [ 'QPPlotWindow', 'QPFigureCanvas', 'QPOverlay' ]

class AxesLimits(object):
	"""
	Stores the zoom history for Matplotlib :class:`Axes` objects. The history 
	is stored in a :class:`WeakKeyDictionary` with :class:`Axes` objects for 
	keys. 
	
	History is a list of tuples of the form (*xlim*, *ylim*) where *xlim* and 
	*ylim* are the return values of the :meth:`get_xlim` and :meth:`get_ylim` 
	methods of the corresponding :class:`Axes` object. 
	
	
	Alters the X and Y limits of C{Axes} objects while maintaining a history of
	the changes.
	"""
	def __init__(self):
		self.history = weakref.WeakKeyDictionary()

	def _get_history(self, axes):
		"""
		Returns the history list of X and Y limits associated with the *axes*
		object. 
		"""
		# Return history for axes, set history to [] if not in the dictionary
		return self.history.setdefault(axes, [])
	
	def zoomed(self, axes):
		"""
		Returns a boolean indicating whether *axes* has had its limits
		altered.
		"""
		# Return True if there is anything in the history for axes
		return not (not self._get_history(axes))

	def setNew(self, axes, xr, yr):
		"""
		Changes the X and Y limits of *axes* to *xrange* and *yrange*
		respectively by calling the :meth:`set_xlim` and :meth:`set_ylim` 
		methods of the *axes* object. The old state of axes is stored in the 
		history list. A boolean indicating whether or not the axes should be 
		redrawn is returned, because polar axes cannot have their limits 
		changed sensibly.
		"""
		# Can handle only rectilinear exes
		if axes.name!='rectilinear':
			return False

		# Retrieve history
		history = self._get_history(axes)
		
		# Get current axes range as old range
		# Must copy because the returned value is always the same array with different contents
		# Need to do this because older versions of matplotlib return xlim and ylim as numpy array
		# while newer versions return a tuple
		try:
			oldRange = axes.get_xlim().copy(), axes.get_ylim().copy()
		except:
			oldRange = axes.get_xlim(), axes.get_ylim()
		
		# Store old axes range in history
		history.append(oldRange)
		
		# Set new limits
		axes.set_xlim(xr)
		axes.set_ylim(yr)
		
		return True

	def restore(self, axes):
		"""
		Changes the X and Y limits of C{axes} to their previous values 
		obtained from teh corresponding history list. A boolean indicating 
		whether or not the axes should be redrawn is returned, because polar 
		axes cannot have their limits changed sensibly.
		"""
		# Get history for axes
		hist = self._get_history(axes)

		if not hist:
			# Nothing in history
			return False
		else:
			# Pop history
			xr, yr = hist.pop()
			
			# Is entry a range
			if xr is None and yr is None:
				# Autoscale if both are None
				axes.autoscale_view()
				return True
			elif xr is not None and yr is not None:
				# Set limits if both are not None
				axes.set_xlim(*xr)
				axes.set_ylim(*yr)
				return True
			else:
				# One is None and the other isn't, nothing to do
				return False


class QPOverlay(QWidget):
	"""
	A transparent Qt widget that overlays crosshair and rubberband. 
	"""
	def __init__(self, parent=None, enableCrosshair=True, enableRubberband=True):
		QWidget.__init__(self, parent)
		
		self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		
		# self.setFocusPolicy(Qt.NoFocus)
		
		self.crosshair=None
		self.pos0=None
		self.pos=None
		
		self.crosshairEnabled=enableCrosshair
		self.rubberbandEnabled=enableRubberband
		
	def showCrosshair(self, state):
		"""
		Enable/disable crosshair. 
		"""
		self.crosshairEnabled=state
	
	def showRubberband(self, state):
		"""
		Enable/disable rubberband. 
		"""
		self.rubberbandEnabled=state
	
	def setCrosshair(self, pos):
		"""
		Set crosshair position *pos* (a tuple holding x,y coordinates). 
		It is assumed y coordinate is inverted (increasing from bottom 
		to top of the widget). 
		
		Ip *pos* is set to ``None`` crosshair is not displayed. 
		
		Calling this function schedules an update of the overlay. 
		"""
		self.crosshair=pos
		self.update()
	
	def setRubberband(self, pos0=None, pos=None):
		"""
		Set rubberband to be a rectangle between *pos0* and *pos*. 
		Both positions are tuples holding x,y coordinates. 
		It is assumed y coordinate is inverted (increasing from bottom 
		to top of the widget). 
		
		Ip *pos0* or *pos* is set to ``None`` rubberband is not displayed. 
		
		Calling this function schedules an update of the overlay. 
		"""
		self.pos0=pos0
		self.pos=pos
		self.update()
		
	def paintEvent(self, event):
		"""
		Repaints the overlay. 
		"""
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.Antialiasing, False)
		
		if self.rubberbandEnabled and self.pos0 is not None and self.pos is not None:
			p=painter.pen()
			p.setWidth(0)
			painter.setPen(p)
			x0, y0 = self.pos0
			x, y = self.pos
			
			y0 = self.height()-1-y0
			y = self.height()-1-y
			
			xo=min(x0, x)
			yo=min(y0, y)
			
			w=abs(x-x0)
			h=abs(y-y0)
			
			painter.fillRect(xo, yo, w, h, QColor(0, 0, 128, 32))
		
		if self.crosshairEnabled and self.crosshair is not None:
			p=painter.pen()
			p.setWidth(0)
			painter.setPen(p)
			x, y = self.crosshair
			y = self.height()-1-y
			painter.drawLine(0, y, self.width(), y)
			painter.drawLine(x, 0, x, self.height())
		
		painter.setPen(QPen(Qt.NoPen))   
		
	def keyPressEvent(self, event):
		"""
		Key press event handler. Ignores the events so they get sent to
		the parent widget (the one that is under the overlay). 
		"""
		event.ignore()
		

#
# Matplotlib canvas in a PyQt window
#

class QPFigureCanvas(FigureCanvas):
	"""
	A Matplotlib canvas suitable for embedding in PyQt5 applications. 
	
	For *parent* see PyQt documentation. 
	
	*lock* is a :class:`threading.Lock` object for preventing other threads 
	from accessing gui data while the gui thread uses them. 
	
	Setting *showCrosshair* and *showRubberband* to ``True`` enables 
	the corresponding facilities of the canvas. 
	
	By setting *point* and *selection* to ``True`` the canvas emits 
	:class:`PointEvent` (:class:`SelectionEvent`) events whenever 
	crosshair position (rubberband) is changed. 
	
	Setting *zooming* to ``True`` enables zooming. 
	
	*figsize* is a tuple specifying the figure width and height in inches. 
	Together with *dpi* they define the size of the figure in pixels. 
	
	*figpx* is a tuple with the horizontal and vertical size of the figure 
	in pixels. If it is given it overrides the *figsize* setting. *dpi* is 
	used for obtaining the figure size in inches. 
	
	If neither *figsize* nor *figpx* are given the settings from matplotlibrc 
	are used. The same holds for *dpi*. 
	
	Holding down the left button and moving the mouse selects the area to be 
	zoomed. The zooming is performed when the button is released. 
	
	Right-clicking zooms out to the previous view. 
	
	Pressing the ``I`` key identifies the nearest curve and shows a tooltip. 
	"""
	def __init__(
		self, parent=None, lock=None, 
		showCrosshair=True, showRubberband=True, 
		pointEvents=True, selectionEvents=True, 
		zooming=True, 
		figpx=None, figsize=None, dpi=None
	):
		self.guiLock=lock
		self.lockedInEventHandler=0
		
		# If no figsize is given, use figure.figsize from matplotlibrc
		if figsize is None:
			figsize=rcParams['figure.figsize']
		
		# If no dpi is given, use figure.dpi from matplotlibrc
		if dpi is None:
			dpi=rcParams['figure.dpi']
		
		# When given, figpx overrides figsize. 
		# figsize is calculated from figpx and dpi. 
		if figpx is not None:
			figsize=(figpx[0]*1.0/dpi, figpx[1]*1.0/dpi)
			pxsize=figpx
		else:
			pxsize=figsize[0]*dpi,figsize[1]*dpi
		
		self.userpxsize=pxsize
		
		self.figureObject=Figure(figsize=figsize, dpi=dpi)
		self.figureObject.set_figheight(figsize[1])
		self.figureObject.set_figwidth(figsize[0])
		
		FigureCanvas.__init__(self, self.figureObject)
		self.setParent(parent)
		
		self.overlay=QPOverlay(self, enableCrosshair=showCrosshair, enableRubberband=showRubberband)
		
		FigureCanvas.setSizePolicy(
			self,
			QSizePolicy.Expanding,
			QSizePolicy.Expanding
		)
		
		FigureCanvas.updateGeometry(self)
		
		self.pointEvents = pointEvents
		self.selectionEvents = selectionEvents
		self.zooming = zooming

		self.figureObject.set_edgecolor('black')
		self.figureObject.set_facecolor('white')
		
		# Turn on repaint
		self.repaintEnabled=True
		
		# Zoom corner 1, data and Qt coordinates
		self.axes1 = None
		self.zoom1 = None
		self.point1 = None
		
		# Axes history
		self.limits=AxesLimits()
		
		# Connect matplotlib event handlers
		self.figureObject.canvas.mpl_connect('motion_notify_event', self.on_motion_notify_event)
		self.figureObject.canvas.mpl_connect('button_press_event', self.on_button_press_event)
		self.figureObject.canvas.mpl_connect('button_release_event', self.on_button_release_event)
		self.figureObject.canvas.mpl_connect('pick_event', self.on_pick_event)
		self.figureObject.canvas.mpl_connect('key_press_event', self.on_key_press_event)
		
	def sizeHint(self):
		return QSize(self.userpxsize[0], self.userpxsize[1])
			
	# Override main event handler so that we can lock the gui before events are handled
	def event(self, e):
		# print("Enter event", e, type(e))
		if self.guiLock is not None:
			# Events are invoked recursively. We may lock only when we start to handle first event. 
			if self.lockedInEventHandler==0:
				self.guiLock.acquire()
			self.lockedInEventHandler+=1
		retval=super(QPFigureCanvas, self).event(e)
		if self.guiLock is not None:
			# Events are invoked recursively. We may unlock only when we finish handling first event. 
			if self.lockedInEventHandler==1:
				self.guiLock.release()
			self.lockedInEventHandler-=1
		# print("Leave event", e)
		return retval
			
	def resizeEvent(self, e):
		self.overlay.resize(e.size())
		super(QPFigureCanvas, self).resizeEvent(e)
		
	"""
	Signal that gets emitted every time crosshair moves. 
	"""
	newCoordinates=pyqtSignal(list)
	
	"""
	Signal that gets emitted every time rubberband is changed 
	"""
	newSelection=pyqtSignal(list)
	
	def _to_data_coords(self, axes, x, y):
		"""
		Takes Qt coordinates and converts them to 
		axes coordinates. Returns a tuple of two values or
		``None, None`` if conversion fails. 
		
		Coordinates outside axes are also converted which makes 
		it possible to handle rubberbands outside axes and zoom 
		to extents with one corner outside axes. 
		"""
		# No axes, nothing to do
		if axes is None:
			return (None, None)
			
		# Convert to coordinates on axes
		try:
			xdata, ydata = axes.transData.inverted().transform_point((x, y))
		except ValueError:
			return (None, None)
		else:
			return (xdata, ydata)

	#
	# Matplotlib event handling 
	#
	
	def emitCoordinates(self, event):
		"""
		Extracts coordinate information and emits a ``newCoordinates``
		signal. 
		"""
		axes=event.inaxes
		x = event.x
		y = event.y
		xdata = event.xdata
		ydata = event.ydata
		if axes is not None:
			# Get history
			zoomHistory=self.limits._get_history(axes)
			if len(zoomHistory)>0:
				zoomStr=" zoom level %d" % len(zoomHistory)
			else:
				zoomStr=""
			
			# Post coordinates events with data
			self.newCoordinates.emit([
				axes.name, xdata, ydata, axes.format_coord(xdata, ydata)+zoomStr
			])
		else:
			# Outside axes
			# Post coordinates event
			self.newCoordinates.emit([
				"No axes", None, None, "unknown"
			])
	
	def on_motion_notify_event(self, event):
		"""
		A handler for matplotlib ``motion_notify_event`` events. 
		Invoked every time mouse moves across the canvas or when  
		a mouse button is released.  
		"""
		self.overlay.setFocus()
		axes=event.inaxes
		x = event.x
		y = event.y
		xdata = event.xdata
		ydata = event.ydata
		
		# If we are in selection mode we must draw a rubberband
		if self.axes1 is not None:
			# Yes, draw rubberband
			x0, y0 = self.point1
			self.overlay.setRubberband((x0, y0), (x, y))
			
		# If we are inside axes 
		if axes is not None:
			# Set a cross cursor and draw crosshairs
			self.setCursor(Qt.BlankCursor)
			self.overlay.setCrosshair((x, y))
		else:
			# Outside axes
			# If there is any rubberband, it remains where it was
			
			# Normal cursor, no crosshairs
			self.setCursor(Qt.ArrowCursor)
			self.overlay.setCrosshair(None)
		
		# Update coordinates display
		if self.pointEvents:
			self.emitCoordinates(event)
		
		# Remove tooltip 
		## self.SetToolTip(None)
		
	def on_button_press_event(self, event):
		"""
		A handler for matplotlib ``button_press_event`` events. 
		Invoked every time a mouse button is pressed. 
		"""
		axes=event.inaxes
		x = event.x
		y = event.y
		xdata = event.xdata
		ydata = event.ydata
		
		if event.button==1:
			# Left button pressed
			
			# Are we inside axes
			if axes is not None:
				# Are the axes rectilinear
				if axes.name=='rectilinear':
					# OK, we have zoom point 1
					self.axes1 = axes
					self.zoom1 = xdata, ydata
					self.point1 = x, y
		elif event.button==3:
			# Right button pressed and zooming enabled
			if axes is not None:
				if self.zooming and self.limits.restore(axes):
					# We have axes and zoom out requires a redraw
					self.draw()
					
					# Update coordinates display
					if self.pointEvents:
						self.emitCoordinates(event)
	
	def on_button_release_event(self, event):
		"""
		A handler for matplotlib ``button_release_event`` events. 
		Invoked every time a mouse button is released. 
		"""
		axes=event.inaxes
		x = event.x
		y = event.y
		xdata = event.xdata
		ydata = event.ydata
		
		if event.button==1:
			# Left button released
			
			# If we are in selection mode, clear rubberband
			if self.axes1 is not None:
				self.overlay.setRubberband()
			
			# Calculate second point coordinates from x,y based on self.axes1
			# This way we get to zoom beyond axes. 
			actualxdata, actualydata = self._to_data_coords(self.axes1, x, y)
			
			# Are we in selection mode and do we have a second point
			if self.zooming and self.axes1 is not None and actualxdata is not None and actualydata is not None:
				# Prepare ranges
				xr=self.zoom1[0], actualxdata
				yr=self.zoom1[1], actualydata
					
				# Fix ranges
				if xr[0]>xr[1]:
					xr=xr[-1::-1]
				if yr[0]>yr[1]:
					yr=yr[-1::-1]
					
				# Is the range nonzero?
				if xr[1]-xr[0]>0 and yr[1]-yr[0]>0:
					# Yes, it is
					# Emit a selection event if selection events are enabled
					if self.selectionEvents: 
						self.newSelection.emit([self.axes1, xr[0], yr[0], xr[1], yr[1]])
						
					# Are coordinates rectilinear and is zoom allowed. 
					if self.axes1.name=='rectilinear' and self.zooming:
						# Yes, zoom ... 
						if self.limits.setNew(self.axes1, xr, yr):
							# ... and redraw if needed
							self.draw()
							
							# Update coordinates display
							if self.pointEvents:
								self.emitCoordinates(event)
				else:
					# We have no range, just a point
					# Emit a point event if point events are enabled
					
					if self.pointEvents:
						self.emitCoordinates(event)
					
			# Reset zoom point 1, leave selection mode
			self.axes1 = None
			self.zoom1 = None
			self.point1 = None
			
		# Normal cursor if no axes
		if axes is None:
			self.setCursor(Qt.ArrowCursor)
		else:
			# No cursor if we have axes
			self.setCursor(Qt.BlankCursor)
	
	def enablePicking(self, axes, width=8):
		"""
		Enables picking for all artists under given axes. 
		"""
		for artist in axes.get_children():
			artist.set_picker(width)
		
	def on_key_press_event(self, event):
		"""
		A handler for matplotlib ``key_press_event`` events. 
		Invoked every time a key is pressed. 
		
		If ``I`` is pressed pickign is enabled for all artists and 
		a pick event is generated at cursor position. 
		"""
		if event.key=='i':
			# Identification
			# Hide tooltip
			cp=QCursor.pos()
			QToolTip.showText(cp, "", self)
			if event.inaxes is not None:
				# Set picker width to 8 for all children
				self.enablePicking(event.inaxes, 8)
				
				# Tell artists to fire pick events
				event.inaxes.pick(event)
				
	def on_pick_event(self, event):
		"""
		A handler for matplotlib ``pick_event`` events. 
		Invoked every time user picks a location close to some object. 
		"""
		label=event.artist.get_label()
		
		# Ignore artists without labels
		if type(label)==str and len(label)>0:
			cp=QCursor.pos()
			QToolTip.showText(cp, label, self, QRect(), 1500)
			
	#
	# Getters and setters
	#
	
	def getFigure(self):
		"""
		Returns the MatPlotLib :class:`Figure` associated with 
		this canvas.
		"""
		return self.figureObject
		
	def showCrosshair(self, state):
		"""
		Enable or disable drawing crosshair when mouse cursor moves 
		inside a matplotlib axes.
		"""
		self.crosshair=overlay.showCrosshair(state)
	
	def showRubberband(self, state):
		"""
		Enable or disable rubberband drawing. 
		"""
		self.rubberband=self.overlay.showRubberband(state)

	def enableCoordinatesEvents(self, state):
		"""
		Enable or disable emitting ``newCoordinates`` signal. 
		"""
		self.pointEvents = state
		
	def enableSelectionEvents(self, state):
		"""
		Enable or disable ``newSelection`` signal. 
		"""
		self.selectionEvents = state

	def enableZooming(self, state):
		"""
		Enable or disable zooming in/out when the user makes an area selection 
		or right-clicks the axes. 
		"""
		self.zooming=state
	
	def set_repaint(self, state):
		"""
		Enable or disable repainting. 
		"""
		self.repaintEnabled=state

		
#
# Matplotlib canvas in a top-level PyQt window
#

class QPPlotWindow(QMainWindow):
	"""
	A matplotlib canvas embedded in a PyQt window.
	
	For *parent* see PyQt documentation. 
	
	*title* is the title of the window. See PyQt documentation for *parent* 
	and *id*. 
	
	*lock* is a :class:`threading.Lock` object that prevents other threads 
	from accessing Matplotlib objects while PyQt events are handled. It is 
	passed to the :class:`QPFigureCanvas` object. 
	
	All remaining arguments are passed to the :class:`QPFigureCanvas` 
	constructor. 
	"""
	def __init__(self, parent=None, title="Plot window", lock=None, **kwargs):
		QMainWindow.__init__(self, parent)
		
		self.canvasWidget = QPFigureCanvas(parent, lock=lock, **kwargs)

		self.setWindowTitle(title)
		
		self.createStatusBar()
		
		self.setCentralWidget(self.canvasWidget)
		
		self.canvasWidget.newCoordinates.connect(self.updateCoordinates)
		
		self.createActions()
		
		# Limited to 2/3 of screen
		# self.adjustSize()
		
		# Not limited
		rect=self.childrenRect()
		self.resize(rect.width(), rect.height())
		
	"""
	This signal is emitted whenever the window is about to close. 
	"""
	windowClosing=pyqtSignal(QWidget)
	
	"""
	This signal is emitted when the user requests closing 
	of all plot windows. 
	"""
	closeAllRequest=pyqtSignal()
	
	def createStatusBar(self):
		"""
		Creates a statu sbar at the bottom of the window. 
		"""
		return self.statusBar()
	
	@pyqtSlot(list)
	def updateCoordinates(self, data):
		"""
		Updates the coordinates display in status bar. 
		"""
		axtxt, x, y, txt = data
		self.statusBar().showMessage("%s: %s" % (axtxt, txt))
	
	def createActions(self):
		"""
		Creates menu actions. 
		"""
		self.fileMenu=self.menuBar().addMenu("&File")
		
		newAction=QAction("&Save as...", self)
		newAction.setShortcuts(QKeySequence("CTRL+S"))
		newAction.setStatusTip("Save plot to a file")
		newAction.triggered.connect(self.onFileSave)
		self.fileMenu.addAction(newAction)
		
		self.fileMenu.addSeparator()
		
		closeAction=QAction("&Close window", self)
		closeAction.setShortcuts(QKeySequence("CTRL+W"))
		closeAction.setStatusTip("Close window")
		closeAction.triggered.connect(self.onClose)
		self.fileMenu.addAction(closeAction)
		
		closeAllAction=QAction("&Close all windows", self)
		closeAllAction.setStatusTip("Close all windows")
		closeAllAction.triggered.connect(self.onCloseAll)
		self.fileMenu.addAction(closeAllAction)
		
		
		self.helpMenu=self.menuBar().addMenu("&Help")
		
		aboutAction=QAction("About", self)
		aboutAction.setStatusTip("About this window")
		aboutAction.triggered.connect(self.onAbout)
		self.helpMenu.addAction(aboutAction)
		
	@pyqtSlot()
	def onAbout(self):
		"""
		Handles the Help/About option. 
		"""
		QMessageBox.information(
			self, 'About PyOPUS plot window',
			'<p>This is <b>PyOPUS plot window</b></p>'
			'Copyright 2017 Arpad Buermen</p>'
			'<p>'
			'Zoom in: left mouse button and drag.<br />'
			'Zoom out: right mouse button.<br />'
			'Press I for object identification.'
			'</p>'
		)
	
	@pyqtSlot()
	def onClose(self):
		"""
		Handles the File/Close option. 
		"""
		self.close()
	
	@pyqtSlot()
	def onCloseAll(self):
		"""
		Handles the File/Close all windows option. 
		"""
		self.closeAllRequest.emit()
	
	def closeEvent(self, e):
		"""
		Just before the window is closed this handler is invoked. 
		It emits a ``windowClosing`` signal. 
		"""
		self.windowClosing.emit(self)
		e.accept()
		
	@pyqtSlot()
	def onFileSave(self):
		"""
		Handles File/Save option. 
		"""
		# Build list of supported formats
		filters=[
			description+' (*.'+extension+')'
			for extension, description in FigureCanvas.filetypes.items()
		]
		
		dialog=QFileDialog(self)
		dialog.setWindowModality(Qt.WindowModal);
		dialog.setAcceptMode(QFileDialog.AcceptSave);
		dialog.setDirectory(os.getcwd())
		dialog.setNameFilters(filters)
		
		if (dialog.exec_() != QDialog.Accepted):
			return
		
		fileName=dialog.selectedFiles()[0]
		
		# figpx (figsize*dpi) is used for raster images
		# figsize and dpi are used for postscript and pdf
		try:
			self.getCanvas().print_figure(fileName)
		except IOError as e:
			QMessageBox.critical(
				self, "Error", 
				"Failed to save plot as '"+fileName+"'.\n"+str(e)
			)

	def getFigure(self):
		"""
		Returns the MatPlotLib :class:`Figure` associated with this 
		canvas.
		"""
		return self.canvasWidget.getFigure()
	
	def getCanvas(self):
		"""
		Returns the :class:`QPFigureCanvas` object associated with 
		this window. 
		"""
		return self.canvasWidget

	def draw(self):
		"""
		Draw the associated :class:`Figure` onto the screen. 
		Shortcut to the :meth:`QPFigureCanvas.draw` method. 
		"""
		self.canvasWidget.draw()


if __name__ == '__main__':
	import sip 
	import sys
	
	sip.setdestroyonexit(False)
	
	app = QApplication(sys.argv)
	
	#w=QPPlotWindow(figsize=(6,4), dpi=72)
	w=QPPlotWindow(figpx=(800,600))
	f=w.getFigure()
	a=f.add_subplot(111)
	a.plot([0,1,2,3], [4,3,2,5], 'r')
		
	w.show()
	app.exec_()
	
