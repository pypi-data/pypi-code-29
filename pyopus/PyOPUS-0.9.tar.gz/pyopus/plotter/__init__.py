"""
**Threaded plotting support based on Matplotlib and PyQt5**

This module uses PyQt5. 

It provides the basic plot window managemet that is performed in a separate 
thread so that MATLAB style plotting is possible in Python. The rendering is 
performed by Matplotlib on a PyQt canvas. 

Because this module depends on Matplotlib and PyQt5 its members are not 
imported into the main PyOPUS module. 

All members of the :mod:`~pyopus.plotter.interface` module are imported 
into the :mod:`~pyopus.plotter` module. This way you can import the plotting 
interface as::

	from pyopus import plotter as pyopl
	
instead of more complicated::
	
	from pyopus.plotter import interface as pyopl
"""
from .interface import *
