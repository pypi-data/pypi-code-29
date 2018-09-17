from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .widgets import *
from ..design.sqlite import *
from . import resources
from .style import styleWidget
from .resbase import *
import datetime

from .dumptools import QPDumpError
from .postdump import *

from .style import *

# import traceback

__all__ = [ "QPPostBase" ]


class QPPostBase(QPResultsWidget):
	def __init__(self, treePath, resultsFolder, logger=None, parent=None):
		QPResultsWidget.__init__(self, treePath, logger, parent)
		
		self.resultsFolder=resultsFolder
		
		self.splitter=QSplitter(Qt.Horizontal, parent=self)
		
		vl=QVBoxLayout(self)
		vl.setContentsMargins(0,0,0,0)
		
		hl=QHBoxLayout()
		vl.addLayout(hl)
		
		vl.addWidget(self.splitter)
		
		self.statusText=QLineEdit(self)
		self.refreshButton=QPushButton("Refresh", self)
		self.stopButton=QPushButton("Stop", self)
		self.autorefresh=QCheckBox("Autorefresh", self)
		
		hl.addWidget(self.statusText)
		hl.addWidget(self.stopButton)
		hl.addWidget(self.refreshButton)
		hl.addWidget(self.autorefresh)
		
		self.text=QPlainTextEdit(self.splitter)
		self.splitter.addWidget(self.text)
		styleWidget(self.text, ["monospace"])
		
		self.setLayout(vl)
		
		self.statusText.setReadOnly(True)
		self.text.setReadOnly(True)
		self.text.setLineWrapMode(QPlainTextEdit.NoWrap)
		
		self.statusText.setText("Idle")
		self.autorefresh.setCheckState(Qt.Checked)
		self.stopButton.setEnabled(False)
		
		self.autorefresh.stateChanged.connect(self.handleAutorefreshChanged)
		self.refreshButton.clicked.connect(self.handleRefresh)
		
		self.errMsg=""
	
	crosshairPosition=pyqtSignal(str, object, object)
	
	def closeEvent(self, e):
		# This is weird. If I don't close the children here, they will linger on 
		# after this widget (parent) is closed
		for w in [
			self.statusText, self.refreshButton, self.stopButton, self.autorefresh, 
			self.splitter
		]: 
			w.close()
		e.accept()
		
	def viewerConfig(self):
		return {
			'autorefresh': self.autorefresh.checkState()==Qt.Checked, 
			'splitterPos': self.splitter.sizes(), 
		}
	
	def setViewerConfig(self, cfg):
		if 'autorefresh' in cfg:
			if cfg['autorefresh']:
				self.autorefresh.setCheckState(Qt.Checked)
			else:
				self.autorefresh.setCheckState(Qt.Unchecked)
		if 'splitterPos' in cfg:
			self.splitter.setSizes(cfg['splitterPos'])
			
	@pyqtSlot(int)
	def handleAutorefreshChanged(self, state):
		if self.autorefresh.checkState()==Qt.Checked:
			# Autorefresh enabled, refresh now if needed
			if self.refreshButton.isEnabled():
				self.refresh()
		
	@pyqtSlot(bool)
	def handleRefresh(self, b):
		self.refresh()
		
	def requestRefresh(self):
		if self.autorefresh.checkState()==Qt.Checked:
			self.refresh()
		else:
			self.refreshButton.setEnabled(True)
		
	def recompute(self):
		pass
		
	def refresh(self):
		# Compute locally
		self.recompute()
		
		# Display
		self.text.setPlainText(self.errMsg)
		self.refreshButton.setEnabled(False)
		
