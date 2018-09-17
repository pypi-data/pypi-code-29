# -*- coding: UTF-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .widgets import *
from .style import styleWidget
from .logscan import QPLogIndex, QPLogIndexError
from .fileview import *

import datetime, os

__all__ = [ 'QPLogViewer' ]


class QPPlainTextEdit(QPlainTextEdit):
	def __init__(self, parent=None):
		QPlainTextEdit.__init__(self, parent)
		self.setFrameStyle(QFrame.NoFrame)
		
	def resizeEvent(self, e):
		# Size is the new size of the text area excluding scrollbars
		s=e.size()
		
		self.resized.emit(s.width(), s.height())
		QPlainTextEdit.resizeEvent(self, e)
	
	def visibleRows(self):
		topOffset=self.contentOffset().y()
		marg=self.contentsMargins()
		# print topOffset, marg.top(), marg.bottom()
		
		# Compute row-to-row spacing
		fm=self.fontMetrics()
		
		# Line height, method 1
		#h1=fm.lineSpacing()+1 # +1 pixel extra line spacing
		#print "h1:", h1
		
		# Line height, method 2
		h1=fm.height() 
		#print "h1:", h1
		
		# Line height, method 3
		#i1=fm.size(0, u"Atfgjpqy12345\nAtfgjpqy12345").height()
		#i2=fm.size(0, u"Atfgjpqy12345\nAtfgjpqy12345\nAtfgjpqy12345").height()
		#h1=i2-i1
		#print "h1:", i1, i2, h1
		
		#print self.height(), "-", topOffset, self.horizontalScrollBar().height(), marg.top(), marg.bottom()
		ht=self.height()-topOffset-self.horizontalScrollBar().height()-marg.top()-marg.bottom()
		# print("ht", ht, "h1", h1)
		
		return int(ht/h1)
		
	def wheelEvent(self, we):
		# 8 ticks / deg
		# Speed = 1 row / 5 deg
		chars=-we.angleDelta()/8/5
		
		self.scrollRequest.emit(chars)
	
	def keyPressEvent(self, ke):
		k=ke.key()
		m=ke.modifiers()
		
		if k==Qt.Key_PageUp and m==Qt.NoModifier:
			self.scrollRequest.emit(QPoint(0, -self.visibleRows()))
		elif k==Qt.Key_PageDown and m==Qt.NoModifier:
			self.scrollRequest.emit(QPoint(0, self.visibleRows()))
		elif k==Qt.Key_Home and (m&Qt.ControlModifier):
			self.topBottomRequest.emit(-1)
		elif k==Qt.Key_End and (m&Qt.ControlModifier):
			self.topBottomRequest.emit(1)
		elif k==Qt.Key_Home and m==Qt.NoModifier:
			self.leftRightRequest.emit(-1)
		elif k==Qt.Key_End and m==Qt.NoModifier:
			self.leftRightRequest.emit(1)
		else:
			QPlainTextEdit.keyPressEvent(self, ke)
		
	resized=pyqtSignal(int, int)
	
	scrollRequest=pyqtSignal(QPoint)
	topBottomRequest=pyqtSignal(int)
	leftRightRequest=pyqtSignal(int)


class QPLogViewer(QPFileViewer):
	def __init__(self, fileName, loggerWidget=None, parent=None):
		QPFileViewer.__init__(self, fileName, loggerWidget, parent)
		
		self.statusTxt=""
		
		self.logIndex=QPLogIndex(self.realPath)
		
		hlvis = QHBoxLayout()
		hlvis.addWidget(QLabel("Show"))
		self.showTime=QCheckBox("Time", self)
		hlvis.addWidget(self.showTime)
		self.showHost=QCheckBox("Host", self)
		hlvis.addWidget(self.showHost)
		self.showProcess=QCheckBox("Process", self)
		hlvis.addWidget(self.showProcess)
		self.showTask=QCheckBox("Task", self)
		hlvis.addWidget(self.showTask)
		self.showSubsystem=QCheckBox("Subsystem", self)
		hlvis.addWidget(self.showSubsystem)
		self.showTail=QCheckBox("Tail", self)
		hlvis.addWidget(self.showTail)
		self.showTail.stateChanged.connect(self.tailClicked)
		hlvis.addStretch(1)
		
		self.vlayout.addLayout(hlvis)
		
		self.logText=QPPlainTextEdit(self)
		self.logText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.logText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.logText.setLineWrapMode(QPlainTextEdit.NoWrap)
		self.logText.setReadOnly(1); 
		self.topOffset=self.logText.contentOffset().y()
		self.logText.resized.connect(self.handleResize)
		self.logText.scrollRequest.connect(self.handleScrollRequest)
		self.logText.topBottomRequest.connect(self.handleTopBottomRequest)
		self.logText.leftRightRequest.connect(self.handleLeftRightRequest)
		self.logText.horizontalScrollBar().sliderMoved.connect(self.memorizeHPos)
		
		self.pos=0
		self.hpos=0
		self.vScroll=QScrollBar(Qt.Vertical, self)
		self.vScroll.valueChanged.connect(self.handleScrollValueChanged)
		self.vScroll.setSingleStep(1)
		
		self.frm=QFrame(self)
		self.vlayout.addWidget(self.frm)
		self.frm.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
		
		# Frame layout
		hl = QHBoxLayout(self.frm)
		hl.setContentsMargins(0,0,0,0)
		hl.setSpacing(0)
		hl.addWidget(self.logText)
		
		# Vertical scrollbar and bottom spacing
		vls=QVBoxLayout()
		vls.setSpacing(1)
		vls.addWidget(self.vScroll)
		# print self.vScroll.width()
		# vls.addSpacing(self.logText.horizontalScrollBar().height())
		hl.addLayout(vls)
		
		self.showTime.setCheckState(Qt.Checked)
		self.showTail.setCheckState(Qt.Checked)
		
		self.showTime.stateChanged.connect(self.reloadText)
		self.showHost.stateChanged.connect(self.reloadText)
		self.showProcess.stateChanged.connect(self.reloadText)
		self.showTask.stateChanged.connect(self.reloadText)
		self.showSubsystem.stateChanged.connect(self.reloadText)
		
		self.setViewerError(False)
		
	def statFile(self):
		try:
			nr, self.statusTxt = self.logIndex.scan()
		
			uuid=self.logIndex.uuid()
			t0=self.logIndex.startTime()
			
		except QPLogIndexError as e:
			nr=0
			
			self.statusTxt="Error occurred while indexing log file.\n"+str(e)
			
			# Let the parent class take care of this error
			raise
			
		return uuid, t0, nr>0
	
	def clearView(self):
		# Just clear the view, do nothing to the index
		self.logText.setPlainText("")
		
	def updateView(self):
		try:
			self.reloadTextEngine()
			self.scaleSlider()
		except:
			self.statusTxt="Failed to load text."
			raise
		
	def handleStatError(self):
		# Clear index, reset h and v pos, display status
		self.logIndex.blank()
		self.pos=0
		self.hpos=0
		self.logText.setPlainText(self.statusTxt)
		self.scaleSliderToText()
		self.logText.horizontalScrollBar().setValue(self.hpos)
		
	def handleUpdateError(self):
		# Display status, do not clear the index
		# Reset h pos
		self.hpos=0
		self.logText.setPlainText(self.statusTxt)
		self.scaleSliderToText()
		self.logText.horizontalScrollBar().setValue(self.hpos)
		
	def setViewerError(self, flag):
		if flag:
			styleWidget(self.logText, ["error"])
		else:
			styleWidget(self.logText, ["monospace"])
	
	# Called when show tail is checked
	@pyqtSlot(int)
	def tailClicked(self, state):
		if state==Qt.Checked:
			# Move to end 
			self.vScroll.setValue(self.vScroll.maximum())
	
	# Called when horizontal slider is moved by the user
	@pyqtSlot(int)
	def memorizeHPos(self, pos):
		self.hpos=pos
	
	# Handles scrollRequest signal emitted when the mouse whell is rotated
	@pyqtSlot(QPoint)
	def handleScrollRequest(self, chars):
		pos=self.pos+chars.y()
		
		if pos<0:
			pos=0
		pos=min(pos, self.logIndex.nRows()-1)
		
		self.vScroll.setValue(pos)
		
		# Text will be reloaded when the scrollbar emits the scrollValueChanged signal
	
	# Handles topBottomRequest signal emitted when CTRL+PAGEUP/PAGEDOWN is pressed
	@pyqtSlot(int)
	def handleTopBottomRequest(self, direction):
		if direction==1:
			self.vScroll.setValue(self.logIndex.nRows()-1)
		else:
			self.vScroll.setValue(0)
	
	# Handles leftRightRequest signal emitted when home/end is pressed
	@pyqtSlot(int)
	def handleLeftRightRequest(self, direction):
		hs=self.logText.horizontalScrollBar()
		if direction==1:
			hs.setValue(hs.maximum())
			self.hpos=hs.value()
		else:
			hs.setValue(0)
			self.hpos=0
	
	# Scales the vertical slider. Sets
	#   - max and min 
	#   - sets position to end if show tail is checked
	#     handleScrollValueChanged will be triggered by vertical scrollbar's 
	#     valueChanged signal. It will then call reloadText()
	def scaleSlider(self, handleTailing=True):
		nr=self.logIndex.nRows()
		if nr<0: 
			nr=1
		
		vr=self.logText.visibleRows()
		sMax=nr-vr
		if sMax<0:
			sMax=1
		self.vScroll.setMinimum(0)
		self.vScroll.setMaximum(sMax)
		
		if handleTailing and self.showTail.checkState() == Qt.Checked:
			# Move to tail
			vr=self.logText.visibleRows()
			moveTo=self.logIndex.nRows()-vr
			if moveTo<0:
				moveTo=0
			self.vScroll.setValue(moveTo)
	
	# Scale vertical scrollbar to displayed text
	def scaleSliderToText(self):
		self.vScroll.setMinimum(0)
		self.vScroll.setMaximum(self.logText.verticalScrollBar().maximum())
			
	# This is invoked whenever the verticall scrollbar's position is changed
	@pyqtSlot(int)
	def handleScrollValueChanged(self, value):
		self.pos=value
		self.reloadText()
	
	# This is triggered when the text viewer is resized
	@pyqtSlot(int, int)
	def handleResize(self, w, h):
		self.vScroll.setPageStep(self.logText.visibleRows())
		self.reloadText()
		self.scaleSlider()
		
	# Reload the visible part of text. Ignore exceptions. 
	@pyqtSlot(int)
	def reloadText(self, state=0):
		try:
			self.reloadTextEngine()
		except:
			pass
	
	# Reload the visible part of text
	def reloadTextEngine(self):
		nr=self.logText.visibleRows()
		
		try:
			rl=self.logIndex.rows(self.pos, self.pos+nr-1)
			
			w=self.logIndex.widths()
		
			showTime=self.showTime.checkState() == Qt.Checked
			showHost=self.showHost.checkState() == Qt.Checked
			showProcess=self.showProcess.checkState() == Qt.Checked
			showTask=self.showTask.checkState() == Qt.Checked
			showSubsystem=self.showSubsystem.checkState() == Qt.Checked
			
			flag=showTime or showHost or showProcess or showTask or showSubsystem
			
			ftl=[]
			for r in rl:
				rt=""
				
				flds=[]
				if showTime:
					flds.append("%*.1f" % (w[0]+2, r[0]))
				if showHost:
					flds.append("%-*s" % (w[1], r[1]))
				if showProcess:
					flds.append("0x%-*s" % (w[2], r[2]))
				if showTask:
					flds.append("0x%-*s" % (w[3], r[3]))
				if showSubsystem:
					flds.append("%-*s" % (w[4], r[4]))
				
				rt=" ".join(flds)
				
				if flag:
					rt+=": "
				
				rt+=r[-1]
				
				ftl.append(rt)
			
			txt="\n".join(ftl)
			
			# Show text and set horizontal scrollbar position
			self.logText.setPlainText(txt)
			self.logText.horizontalScrollBar().setValue(self.hpos)
			
		except QPLogIndexError as e:
			# print("Exception in reloadTextEngine")
			self.statusTxt="Error occurred while reading log file.\n"+str(e)
			raise
		
	
if __name__ == "__main__":
	from pprint import pprint
	import sip 
	import sys
	import sys
	
	sip.setdestroyonexit(True)

	app = QApplication(sys.argv)
	
	# Create viewer
	lv=QPLogViewer(sys.argv[1])
	lv.setWindowTitle("Log viewer demo")
	
	
	# Show and run
	lv.show()
	app.exec_()
	
