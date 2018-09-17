from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

__all__ = [ 'QPLogger', 'QPDummyLogger' ]


class QPDummyLogger(object):
	def __init__(self):
		pass
	
	def log(self, txt, isError=False, asHtml=True):
		pass
	
	
class QPLogger(QPlainTextEdit):
	def __init__(self, parent=None):
		QPlainTextEdit.__init__(self, parent)
		self.setReadOnly(True)
		
	def log(self, txt, isError=False, asHtml=True):
		if asHtml:
			txt=txt.rstrip()
			for row in txt.split('\n'):
				if isError:
					row="<b><font color='#ff0000'>"+row+"</font></b>"
				self.appendHtml(row)
		else:
			self.appendPlainText(txt.rstrip())
		self.verticalScrollBar().setValue(
			self.verticalScrollBar().maximum()
		)
		
	def clear(self):
		self.setPlainText("")
	
	def sizeHint(self):
		return QSize(0, 50)
	