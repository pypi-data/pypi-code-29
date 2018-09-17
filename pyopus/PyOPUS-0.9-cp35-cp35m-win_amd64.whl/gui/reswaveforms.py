from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .table import *
from .widgets import *
from ..design.sqlite import *
from . import resources
from .style import styleWidget
from .resbase import *

import datetime

from .indicators import *
from .editbase import *

__all__ = [ "QPResultsWaveforms" ]

class QPResultsWaveforms(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None):
		QPEditBase.__init__(self, treePath, logger, parent)
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.listing=QTextEdit("", self)
		self.listing.setReadOnly(True)
		layout.addWidget(self.listing)
		
		self.setLayout(layout)
		
		txt="No waveforms available."
		
		rootData=self.treePath.rootData()
		if rootData is not None:
			rec=rootData['record']
			if rec is not None:
				files=rec.waveforms 
				
				anList={}
				for cor, an in files.keys():
					if an not in anList:
						anList[an]=[]
					anList[an].append(cor)
				
				txt="Number of available waveform files: %d\n" % (len(files))
				for an in anList.keys():
					corners=anList[an]
					if an is None:
						continue
					txt+=an+":\n"
					for cor in corners:
						txt+="  "+cor+": "+files[(cor, an)]+"\n"
				for an in anList.keys():
					corners=anList[an]
					if an is not None:
						continue
					txt+="No analysis (summary of measures):\n"
					for cor in corners:
						txt+="  "+cor+": "+files[(cor, an)]+"\n"
				
		self.listing.setText(txt)
		

