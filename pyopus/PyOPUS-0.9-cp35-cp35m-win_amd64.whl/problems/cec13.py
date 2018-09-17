# -*- coding: UTF-8 -*-
"""
.. inheritance-diagram:: pyopus.problems.cec13
    :parts: 1
	
**CEC13 test problems (PyOPUS subsystem name: CEC13)**

These are the test problems from the IEEE CEC 2013 real-parameter single 
objective optimization competition [cec13]_. 

Objects of this class are callable. Calling them evaluates the corresponding 
function. 

This module is independent of PyOPUS, meaning that it can be taken as is 
and used as a module in some other package. It depends only on the :mod:`cpi` 
and the :mod:`_cec13` modules. 

The code in the binary module shares variables. If multiple CEC13 functions 
are created the initialization will take place automatically whenever a 
different function from the previous one is evaluated. Evaluation takes time 
so make sure you don't switch functions frequently. 

.. [cec13] Liang J. J., Qu B. Y., Suganthan P. N., Hernández-Diaz A. G.: 
           Problem Definitions and Evaluation Criteria for the CEC 2013
           Special Session on Real-Parameter Optimization, 
           Technical Report 201212, Computational Intelligence Laboratory, 
           Zhengzhou University, Zhengzhou China, Technical Report, Nanyang 
           Technological University, Singapore, 2013. 
"""
from . import _cec13
import os
import numpy as np
from .cpi import CPI, MemberWrapper, TestFunctionError
try:
	from ..misc.debug import DbgMsg
except:
	def DbgMsg(x, y):
		return x+": "+y

__all__ = [ 'CEC13' ]

		
# Set path to data files folder
_cec13.initmod(os.path.dirname(_cec13.__file__))
		
class CEC13(CPI):
	"""
	CEC13 test problems. 
	
	* *name*   - problem name
	* *number* - problem number (0-27)
	* *n*      - problem dimension
	
	Attributes:
	
	* :attr:`name`    - problem name
	* :attr:`n`       - number of variables
	* :attr:`xl`      - vector of lower bounds on variables
	* :attr:`xh`      - vector of upper bounds on variables
	* :attr:`xmin`    - best known minimum position
	* :attr:`fmin`    - best known minimum value
	"""
	
	names=[
		# Unimodal
		"Sphere", 
		"RotatedElliptic", 
		"RotatedCigar", 
		"RotatedDiscus", 
		"DifferentPowers",
		# Basic multimodal
		"RotatedRosenbrock", 
		"RotatedSchafferF7", 
		"RotatedAckley", 
		"RotatedWeierstrass", 
		"RotatedGriewank", 
		"Rastrigin", 
		"RotatedRastrigin", 
		"DiscontinuousRotatedRastrigin", 
		"Schwefel", 
		"RotatedSchwefel", 
		"RotatedKatsuura", 
		"LunacekBiRastrigin", 
		"RotatedLunacekBiRastrigin", 
		"ExpandedGriewankRosenbrock", 
		"ExpandedSchafferF6", 
		# Composited functions
		"Composited1",
		"Composited2", 
		"Composited3", 
		"Composited4", 
		"Composited5", 
		"Composited6", 
		"Composited7", 
		"Composited8", 
	]
	"List of all function names"
	
	functionNumber=dict(zip(names, range(len(names))))
	
	def __init__(self, name=None, number=None, n=10):
		if number is None and name is None:
			raise TestFunctionError(DbgMsg("CEC13", "Must specify name or number."))
			
		if number is not None and name is not None:
			raise TestFunctionError(DbgMsg("CEC13", "Name and number cannot be specified at the same time."))
		
		if number is not None:
			self.number=number
			if number<0 or number>27:
				raise TestFunctionError(DbgMsg("CEC13", "Bad problem number."))
			self.name=self.names[number]
		
		if name is not None:
			if name not in self.functionNumber:
				raise TestFunctionError(DbgMsg("CEC13", "Function not found."))
			self.number=self.functionNumber[name]
			self.name=name
		
		self.n=n 
		self.xl=-np.ones(self.n)*100.0
		self.xh=np.ones(self.n)*100.0
		
		info=_cec13.cec13init(self.number, self.n)
		
		self.xmin=info['xmin']
		self.fmin=info['fmin']
		
		
	def __call__(self, x):
		"""
		Returns the value of the function at *x*. 
		
		If *x* is a 2D array multiple pointa are evaluated.
		First index is the point index and the second index is 
		the component index. 
		"""
		if len(x.shape)==1:
			return _cec13.cec13eval(self.number, x, x.shape[0], 1)
		elif len(x.shape)==2:
			return _cec13.cec13eval(self.number, x.ravel(), x.shape[1], x.shape[0])
		else:
			raise TestFunctionError(DbgMsg("CEC13", "Input vector must be a 1D or 2D array."))
			
	def cpi(self):
		"""
		Returns the common problem interface. 
		
		Gradient is not supported. 
		
		See the :class:`CPI` class for more information. 
		"""
		itf=self.prepareCPI(self.n, m=0)
		itf['name']=self.name
		itf['f']=self
		itf['xlo']=self.xl
		itf['xhi']=self.xh
		itf['fmin']=self.fmin
		itf['xmin']=self.xmin
		
		return self.fixBounds(itf)
	