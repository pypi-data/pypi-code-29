"""
**Simulator support module**

Nothing from the submodules of this module is imported into the main 
:mod:`simulator` module. The :mod:`simulator` module provides only the 
:func:`simulatorClass` function for on-demand loading of simulator classes. 
"""
import sys, pkgutil, importlib

__all__=[ 'simulatorClass', 'simulatorModule' ]

def simulatorClass(className): 
	"""
	Returns the class object of the simulator named *className*. 
	Raises an exception if the simulator class object is not found. 
	
	This function provides on-demand loading of simulator classes. 
	
	To create a simulator object of the class SpiceOpus and put it in ``sim`` 
	use::
	
		from pyopus.simulator import simulatorClass
		SimClass=simulatorClass('SpiceOpus')
		sim=SimClass()
	
	For this function to work the simulator class must be in a module 
	whose name is the lowercase version of the simulator class name. 
	"""
	return getattr(importlib.import_module("pyopus.simulator."+className.lower()), className)

def simulatorModule(className):
	return importlib.import_module("pyopus.simulator."+className.lower())
	
def detectSimulators():
	"""
	Detects all available simulator classes. 
	
	Returns a list of tuples of the form 
	``(simulatorClassName, module, description)``. 
	"""
	result=[]
	for finder, name, ispkg in pkgutil.iter_modules(__path__):
		# Skip binary modules prefixed with underscore
		if name[0]=="_":
			continue
		# Try to import
		try:
			mod=importlib.import_module("pyopus.simulator."+name)
		except ImportError:
			mod=None
		
		if mod is None:
			continue
		
		if not hasattr(mod, "simulatorDescription"):
			continue
		
		className, desc = mod.simulatorDescription
		
		result.append((className, mod, desc))
	
	return result
	
