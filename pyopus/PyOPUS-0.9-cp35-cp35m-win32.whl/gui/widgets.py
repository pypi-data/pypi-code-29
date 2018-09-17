from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

__all__ = [ "QPAdaptiveLineEdit" ]


class QPAdaptiveLineEdit(QLineEdit):
	def __init__(self, parent=None):
		QLineEdit.__init__(self, parent)
		self.textChanged.connect(self.onTextChanged)
	
	@pyqtSlot(str)
	def onTextChanged(self, str): 
		self.updateGeometry()
		
	def sizeHint(self):
		s=QLineEdit.sizeHint(self)
		h=s.height()
		delta=self.width()-s.width()
		
		m=self.contentsMargins()
		tm=self.textMargins()
		fm=self.fontMetrics()
		br=fm.boundingRect(self.text())
		
		# Don't know where to get horizontalMargin and verticalMargin
		w=br.width()+m.left()+m.right()+tm.left()+tm.right()+2*5 # Missing 2*horizontalMargin
		h=br.height()+m.top()+m.bottom()+tm.top()+tm.bottom() # Missing 2*verticalMargin 
		
		st=self.style()
		sof=QStyleOptionFrame()
		self.initStyleOption(sof)
		
		s1=QSize(w, h)
		s2=st.sizeFromContents(QStyle.CT_LineEdit, sof, s1, self)
		
		return s2
