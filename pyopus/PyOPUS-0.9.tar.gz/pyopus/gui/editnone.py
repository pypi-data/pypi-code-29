from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .editbase import *

__all__ = [ 'QPEditNone' ]

class QPEditNone(QPEditBase):
		def __init__(self, treePath=None, logger=None, parent=None, *args):
			QPEditBase.__init__(self, treePath, logger, parent=parent, *args)
			
			
if __name__=='__main__':
	from pprint import pprint
	import sip 
	import sys
	import sampledata
	sip.setdestroyonexit(True)

	app = QApplication(sys.argv)
	
	# Create scroll area
	sa=QScrollArea()
	sa.setWindowTitle("Blank editor demo")
	sa.setWidgetResizable(True)
	
	# Add widget
	win=QPEditNone()
	sa.setWidget(win)
	
	# Show and run
	sa.show()
	app.exec_()
	
	# Print data
	pprint(sampledata.data)
	
	

