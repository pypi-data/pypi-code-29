# -*- coding: UTF-8 -*-
"""
Netlister modules for EDA tools. 

Currently supports Spice Opus netlist output for KiCad. 
"""

__all__ = [ 'PyNetlisterError' ]

class PyNetlisterError(Exception):
	def __init__(self, message, *args):
		super(PyNetlisterError, self).__init__(message, *args)
