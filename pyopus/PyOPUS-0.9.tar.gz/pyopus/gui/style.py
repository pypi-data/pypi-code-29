from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import platform

__all__ = [ 'styleWidget', 'enableWidget' ]

styles = {
	'monospace': "font-family: Monospace;", 
	'folder': "background-color: rgb(200,255,200); color: black;", 
	'error': "background-color: rgb(255,200,200); color: black;", 
	'disabled': "color: gray; background: lightgray;",
}

# Courier is ugly and Monospace is not recognized under Windows
# Set Lucida Console as fixed width font
if platform.platform().startswith('Windows'):
	styles['monospace']="font-family: Lucida Console;"

def styleWidget(w, nameList):
	w.setStyleSheet(" ".join([ styles[s] for s in nameList ]))

def enableWidget(w, flag=True, baselineStyle=[]):
	# w.setReadOnly(not flag)
	w.setEnabled(flag)
	styleWidget(w, baselineStyle if flag else baselineStyle+['disabled'])
	
	