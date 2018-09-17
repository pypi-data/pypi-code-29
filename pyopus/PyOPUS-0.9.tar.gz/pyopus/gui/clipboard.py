from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from copy import deepcopy
import json

from .values import version

__all__ = [ 
	'lcTreeItemClassNameOnClipboard', 
	'treeToClipboard', 
	'treeFromClipboard', 
	'isQPTableOnClipboard',
	'tableToClipboard', 
	'tableFromClipboard' 
]

# Subtree payload (mime type pyopus-gui-subtree-<version>/className) is a tuple
#  - parent item type name
#  - list of children data
#
# Children data is 
#  - a list of data for parents that store their children in a list
#  - a list of tuples for parents that store their children in a dictionary
#    - dictionary key
#    - data

# Table cells payload is
#   - list with two members
#     - list of pairs (row, col) (lowest row/col number in list is 0)
#     - list of corresponding data values

# Data version on clipoard must match the version of the application reading the clipboard
# If it does not the data on the clipboard is ignored. 
# Version in an integral part of mime type name. 

# Mime types are lowercase
# This function returns the parent item class name in lowercase without unpacking the data. 
# Returns None if clipboard does not contain a subtree
def lcTreeItemClassNameOnClipboard():
	cb=QGuiApplication.clipboard()
	md=cb.mimeData(QClipboard.Clipboard)
	types=set(md.formats())
	
	prefix='x-pyopus-gui-subtree-'+version.lower()+'/'
	for t in types:
		if t.lower().find(prefix)==0:
			lcname=t.split("/")[1].lower()
			
			return lcname
			
	# Not a subtree
	return None

def treeToClipboard(payload):
	mimeType='x-pyopus-gui-subtree-'+version.lower()+'/'+payload[0].lower()
	mimeData=QMimeData()
	mimeData.setData(mimeType, QByteArray(json.dumps(payload).encode("utf-8")))
	
	cb=QGuiApplication.clipboard()
	cb.setMimeData(mimeData, QClipboard.Clipboard)

# Assume data is of correct version and available on the clipboard
def treeFromClipboard(lcItemClassName):
	cb=QGuiApplication.clipboard()
	md=cb.mimeData(QClipboard.Clipboard)
	byteArray=md.data('x-pyopus-gui-subtree-'+version.lower()+'/'+lcItemClassName)
	jsonData=byteArray.data().decode("utf-8")
	payload=json.loads(jsonData)
	return payload
	
	
def isQPTableOnClipboard():
	return lcTreeItemClassNameOnClipboard()=="qptable"
	
def tableToClipboard(tableData):
	treeToClipboard(("QPTable", tableData))

# Assume data is of correct version and available on the clipboard	
def tableFromClipboard():
	typeName, tableData = treeFromClipboard("qptable")
	return tableData
	
