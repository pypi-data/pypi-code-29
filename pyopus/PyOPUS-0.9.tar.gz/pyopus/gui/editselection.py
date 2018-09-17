from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .editbase import *

__all__ = [ 'QPEditSelection' ]

class QPEditSelection(QPEditBase):
	def __init__(self, treePathList, logger=None, parent=None, *args):
		parentPath=treePathList[0].parent()
		QPEditBase.__init__(self, parentPath, logger, parent=parent, *args)
		
		# Prepare path to selection
		selectionPath=[]
		path=parentPath
		while path.isValid():
			selectionPath.insert(0, path.name())
			path=path.parent()
		
		# Prepare list of item names
		itemNames=[]
		for path in treePathList:
			itemNames.append(path.name())
		
		layout = QVBoxLayout(self)
		layout.setSpacing(4)
		# Layout should set the minimum and maximum size of the widget
		layout.setSizeConstraint(QLayout.SetMinAndMaxSize);
		
		self.listing=QTextEdit("", self)
		self.listing.setReadOnly(True)
		layout.addWidget(self.listing)
		
		self.setLayout(layout)
	
		txt=( 
			""+
			" :: " . join(selectionPath) + "\n    " +
			"\n    " . join(itemNames)
		)
		self.listing.setText(txt)
	
