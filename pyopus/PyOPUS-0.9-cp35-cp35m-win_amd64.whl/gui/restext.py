from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .widgets import *
from ..design.sqlite import *
from . import resources
from .style import styleWidget
from .resbase import *
import datetime

__all__ = [ "QPTextResults" ]


class QPTextResults(QPResultsWidget):
	def __init__(self, treePath, logger=None, parent=None):
		QPResultsWidget.__init__(self, treePath, logger, parent)
		
		self.contentWidget=QPlainTextEdit(self)
		self.contentWidget.setReadOnly(True)
		self.contentWidget.setLineWrapMode(QPlainTextEdit.NoWrap)
		
		styleWidget(self.contentWidget, ["monospace"])
		
		l=QVBoxLayout(self)
		l.setSpacing(4)
		l.addWidget(self.contentWidget)
		# l.setContentsMargins(0, 0, 0, 0)
		
		self.setLayout(l)
		
		if self.aspect is not None and self.aspect is not "":
			txt=self.rec.formatStr(self.aspect)
		else:
			txt=""
		
		self.contentWidget.setPlainText(txt)
		
if __name__ == "__main__":
	from pprint import pprint
	import sip 
	import sys
	
	sip.setdestroyonexit(True)
	
	app = QApplication(sys.argv)
	
	w=QPTextResults(sys.argv[1], recId=int(sys.argv[2]), aspect=sys.argv[3])
	
	w.show()
	
	app.exec_()
	
	
