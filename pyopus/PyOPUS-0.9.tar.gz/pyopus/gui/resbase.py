from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .editbase import *

__all__ = [ "QPResultsWidget" ]


class QPResultsWidget(QPEditBase):
	def __init__(self, treePath=None, logger=None, parent=None):
		QPEditBase.__init__(self, treePath, logger, parent)
		item=treePath.getItem() if treePath is not None else None
		if item is None:
			self.rec=None
			self.aspect=None
		else:
			self.rec=treePath.rootData()['record']
			self.aspect=treePath.data()
			
	def viewerConfig(self):
		return {}
	
	def setViewerConfig(self, cfg):
		pass
	
