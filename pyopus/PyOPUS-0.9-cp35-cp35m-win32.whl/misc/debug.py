"""
**Debug message generation module** 

Every PyOPUS module generates debug messages of the form 

``locationID subsystem: bodyText``. 

*locationID* uniquely identifies a Python process on a host. 
See :mod:`pyopus.misc.identify` for details. 

*subsystem* is a string identifying the PyOPUS subsystem that generated the 
message. 
"""
# Debug message output

from .identify import locationID
from .dbgprint import stdoutPrinter

import sys, time

__all__ = [ 'DbgSetup', 'DbgDefaultPrint', 'DbgSetDefaultPrinter', 'DbgMsg', 'DbgMsgOut' ]

prependTime=False
timePrecision=1
defaultPrinter=stdoutPrinter
prependPrefix=True

def DbgSetDefaultPrinter(p):
	"""
	Sets the default message printer. 
	
	If this function is not called the default printer 
	writes messages to stdout. 
	"""
	global defaultPrinter
	defaultPrinter=p 
	
def DbgSetup(pTime=False, tPrec=1, prefix=True):
	"""
	Configure debugging
	
	If *prependTime* is ``True`` a timestamp is prepended to every message. 
	
	*tPrec* is the precision of the timestamp. 
	"""
	global prependTime, timePrecision, prependPrefix
	prependTime=pTime
	timePrecision=tPrec
	prependPrefix=prefix

def DbgDefaultPrint(msg):
	"""
	Prints a message via the default printer. 
	"""
	defaultPrinter.write(msg)
	defaultPrinter.flush()
	
# Format a debug message. 
# Text can be a multiline text. Prefix every line with locationID and subsystem. 
def DbgMsg(subsystem, text):
	"""
	Generates a debug message with *text* in its body. The message originates 
	from the given PyOPUS *subsystem*.
	"""
	rows=text.split("\n");
	
	if not prependPrefix:
		return "\n".join(rows)
	
	if prependTime:
		t=time.time()
		prefix="%.*f %s %s: " % (timePrecision, t, locationID(), subsystem)
	else:
		prefix="%s %s: " % (locationID(), subsystem)

	out=[]
	for row in rows:
		out.append(prefix+row)
	return "\n".join(out)
	
# Format and print debug message. 
def DbgMsgOut(subsystem, text, printer=None):
	"""
	Generates and prints using the default message printer. 
	
	The message originates from the given PyOPUS *subsystem*.
	
	If *printer* is specified it is used for printing the message. 
	By default the message is printed with the default printer. 
	"""
	p=defaultPrinter if printer is None else printer
	
	rows=text.split("\n");
	
	if not prependPrefix:
		for row in rows:
			p.write(row+"\n")
	else:
		if prependTime:
			t=time.time()
			prefix="%.*f %s %s: " % (timePrecision, t, locationID(), subsystem)
		else:
			prefix="%s %s: " % (locationID(), subsystem)
		for row in rows:
			p.write(prefix+row+"\n")
	
	p.flush()
	
