import os
import sys
import logging

from macros import *

logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

def funcCheckFile(fname):
	
	f=str(fname[0])
	if os.path.isfile(f)==True:
		return f
	else:
		logging.error("File does not exist: "+f)
		raise ValueError("File does not exist: "+f)

def funcCheckPath(pname):

	if os.path.exists(pname)==True:
		return os.path.abspath(pname)
	else:
		logging.error("Path does not exist: "+pname)
		raise ValueError("Path does not exist: "+pname)
