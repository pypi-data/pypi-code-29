"""
.. inheritance-diagram:: pyopus.evaluator.performance
    :parts: 1
	
**System performance evaluation module (PyOPUS subsystem name: PE)**

A **system description module** is a fragment of simulated system description. 
Usually it corresponds to a file or a section of a library file. 

**Performance measure ordering** is a list of performance measure names that 
defines the order of performance measures. 

The **heads** data structure provides the list of simulators with available 
system description modules. The **analyses** data structure specifies the 
analyses that will be performed by the listed simulators. The **corners** data 
structure specifies the corners across which the systems will be evaluated. 
The **measures** data structure describes the performance measures which are 
extracted from simulation results. 


The **heads** data structure is a dictionary with head name for key. The values 
are also dictionaries describing a simulator and the description of the system 
to be simulated with the following keys:

* ``simulator`` - the name of the simulator to use 
  (see the :func:`pyopus.simulator.simulatorClass` function`for details on 
  how this name is resolved to a simulator class) or a simulator class
* ``settings`` - a dictionary specifying the keyword arguments passed to the 
  simulator object's constructor 
* ``moddefs`` - definition of system description modules 
* ``options`` - simulator options valid for all analyses performed by this 
  simulator. This is a dictionary with option name for key. 
* ``params`` - system parameters valid for all analyses performed in this 
  simulator. This is a dictionary with parameter name for key. 
  
The definition of system description modules in the ``moddefs`` dictionary 
member are themselves dictionaries with system description module name for key. 
Values are dictionaries using the following keys for describing a system 
description module 

* ``file`` - file name in which the system description module is described
* ``section`` - file section name where the system description module 
  description can be bound

Specifying only the ``file`` member translates into an ``.include`` simulator 
input directive (or its equivalent). If additionally the ``section`` member is 
also specified the result is a ``.lib`` directive (or its equivalent). 


The **analyses** data structure is a dictionary with analysis name for key. 
The values are also dictionaries describing an analysis using the following 
dictionary keys:

* ``head`` - the name of the head describing the simulator that will be used 
  for this analysis
* ``modules`` - the list of system description module names that form the 
  system description for this analysis 
* ``options`` - simulator options that apply only to this analysis. This is a 
  dictionary with option name for key. 
* ``params`` - system parameters that apply only to this analysis. This is a 
  dictionary with parameter name for key. 
* ``saves`` - a list of strings which evaluate to save directives specifying 
  what simulated quantities should be included in simulator's output. See 
  individual simulator classes in the :mod:`pyopus.simulator` module for the 
  available save directive generator functions. 
* ``command`` - a string which evaluates to the analysis directive for the 
  simulator. See individual simulator classes in the :mod:`pyopus.simulator` 
  module for the available analysis directive generator functions. 
  
The environment in which the strings in the ``saves`` member and the string in 
the ``command`` member are evaluated is simulator-dependent. See individual 
simulator classes in the :mod:`pyopus.simulator` module for details. 

The environment in which the ``command`` string is evaluated has a member 
named ``param``. It is a dictionary containing all system parameters defined  
for the analysis. It also contains all variables that are passed at evaluator 
construction (passed via the *variables* argument). The variables are also 
available during save directive evaluation. If a variable name conflicts with 
a save directive generator function or is named ``param`` the variable is 
not available. 

The **measures** data structure is a dictionary with performance measure name 
for key. The values are also dictionaries describing individual performance 
measures using the following dictionary keys

* ``analysis`` - the name of the analysis that produces the results from which 
  the performance measure's value is extracted. Set it to ``None`` for 
  dependent measures (measures whose value is computed from the values of other 
  measures). 
* ``corners`` - the list of corner names across which the performance measure 
  is evaluated. Corner indices obtained from the 
  :meth:`~pyopus.evaluator.aggregate.MNbase.worstCornerIndex` method of 
  normalization objects (defined in the :mod:`pyopus.evaluator.aggregate` module) 
  can be converted to corner names by looking up the corresponding members of 
  this list. 
  If this list is omitted the measurement is evaluated across all 
  suitable corners. The list of such corners is generated in the constructor and 
  stored in the ``avaliableCornersForMeasure`` dictionary with measure name as 
  key. 
  Measures that are dependencies for other measures can be evaluated across a 
  broader set of corners than specified by ``corners`` (if required). 
* ``expression`` - a string specifying a Python expression that evaluates to the 
  performance measure's value or a Python script that stores the result in a 
  variable baring the same name as the performance measure. 
  An alternative is to store the result of a script in a variable named 
  ``__result``. 
* ``script`` - a string specifying a Python script that stores the performance 
  measure's value in a variable named ``__result``. The script is used only 
  when no ``expression`` is specified. This is obsolete. Use ``expression`` 
  instead. 
* ``vector`` - a boolean flag which specifies that a performance measure's 
  value may be a vector. If it is ``False`` and the obtained performance 
  measure value is not a scalar (or scalar-like) the evaluation is considered 
  as failed. Defaults to ``False``. 
* ``components`` - a string that evaluates to a list of names used for components 
  when the result of a measure is a vector. It is evaluated in an environment 
  where variables passed via the *variables* argument of the constructor are 
  available. If the resulting list is too short numeric indexes are used as 
  component names that are not defined by the list. 
* ``depends`` - an optional name list of measures required for evaluation of 
  this performance measure. Specified for dependent performance measures. 

If the ``analysis`` member is ``None`` the performance measure is a dependent 
performance measure and is evaluated after all other (independent) performance 
measure have been evaluated. Dependent performance measures can access the 
values of independent performance measures through the ``result`` data 
structure. 


``expression`` and ``script`` are evaluated in an environment with the 
following members: 

* Variables passed at construction via the *variables* argument. If a variable 
  conflicts with any of the remaining variables it is not visible. 
* ``m`` - a reference to the :mod:`pyopus.evaluator.measure` module providing 
  a set of functions for extracting common performance measures from simulated 
  response
* ``np`` - a reference to the NumPy module
* ``param`` - a dictionary with the values of system parameters that apply to 
  the particular analysis and corner used for obtaining the simulated response 
  from which the performance measure is being extracted. 
* Accessor functions provided by the results object. 
  These are not available for dependent measures. See classes derived 
  from the :class:`pyopus.simulator.base.SimulationResults` class. 
  The accessor functions are returned by the results object's 
  :meth:`driverTable` method. 
* ``result`` - a dictionary of dictionaries available to dependent performance 
  measures only. The first key is the performance measure name and the second 
  key is the corner name. The values represent performance measure values. 
  If a value is ``None`` the evaluation of the independent performance measure 
  failed in that corner. 
* ``cornerName`` - a string that reflects the name of the corner in which the 
  dependent performance measure is currently under evaluation. Not available 
  for independent performance measures. 

The **corners** data structure is a dictionary with corner name for key. The 
values are also dictionaries describing individual corners using the following 
dictionary keys: 

* ``heads`` - the list of head names to which this corner can be applied
* ``modules`` - the list of system description module names that form the system 
  description in this corner
* ``params`` - a dictionary with the system parameters that apply only to 
  this corner
  
This data structure can be omitted by passing ``None`` to the :class:`PerformanceEvaluator`
class. In that case a corner named 'default' with no modules and no parameters 
is created that applies to all defined heads. 
"""

from ..optimizer.base import Plugin, Annotator
from numpy import array, ndarray, iscomplex, dtype
from sys import exc_info
from traceback import format_exception, format_exception_only
from ..simulator import simulatorClass
from ..simulator.base import NoneSimulationResults
from ..misc.debug import DbgMsgOut, DbgMsg
from ..misc.identify import locationID
from ..parallel.cooperative import cOS
from .. import PyOpusError
import os, tempfile, shutil

import pickle

from pprint import pprint

# Measurements and NumPy
from . import measure as m
import numpy as np

import sys

__all__ = [ 'PerformanceEvaluator', 'updateAnalysisCount', 'PerformanceAnnotator', 'PerformanceCollector' ] 

def updateAnalysisCount(count, delta, times=1):
	"""
	Updates the analysis counts in dictionary *count* by adding the 
	values from dictionary *delta*. If *count* is not given the 
	current count of every analysis is assumed to be zero. 
	
	Returns the updated dictionary *count*. 
	"""
	if count is None:
		count={}
	
	for name,value in delta.items():
		if name not in count:
			count[name]=0
		count[name]+=value*times
	
	return count	

class PerformanceEvaluator:
	"""
	Performance evaluator class. Objects of this class are callable. The 
	calling convention is ``object(paramDictionary)`` 
	where *paramDictionary* is a dictionary of input parameter values.
	The argument can also be a list of dictionaries containing parameter 
	values. The argument can be omitted (empty dictionary is passed). 
	
	*heads*, *analyses*, *measures*, and *corners* specify the heads, the 
	analyses, the corners, and the performance measures. If *corners* are 
	not specified, a default corner named ``default`` is created. 
	
	*activeMeasures* is a list of measure names that are evaluated by the 
	evaluator. If it is not specified all measures are active. Active measures 
	can be changed by calling the :meth:`setActiveMeasures` method. 
	
	*cornerOrder* - specified the order in which corners should be listed
	
	*fullEvaluation* - By default only those corner,analysis pairs are 
	evaluated where at least one independent measure must be computed. Result 
	files for evalauting dependent measures are generated only for corners 
	where at least one independent measure is evaluated. 
	When *fullEvaluation* is set to ``True`` all analyses across all 
	available corners (for the analysis' head) are performed. Result files 
	for dependent measure evaluation are generated for all available corners 
	across all heads. 
	
	*storeResults* - enables storing of simulation results in pickle files. 
	Results are stored locally on the machine where the corresponding 
	simulator job is run. The content of a results file is a pickled 
	object of class derived from :class:`SimulationResults`. 
	
	*resultsFolder* - specifies the folder where the results should be 
	stored. When set to ``None`` the results are stored in the system's 
	temporary folder. 
	
	*resultsPrefix* - specifies the prefix for the results file names.
	
	A pickle file is prefixed by *resultsPrefix* followed by an id 
	obtained from the :func:`misc.identify.locationID` function, job name,
	and an additional string that makes the file unique. 
	
	The complete list of pickle files across hosts is stored in the 
	``resFiles`` member which is a dictionary. The key to this dictionary 
	is a tuple comprising the host identifier (derived from the 
	:class:`pyopus.parallel.vm.HostID` class) and a tuple comprising 
	corner name and analysis name. Entries in this dictionary are full 
	paths to pickle files. If files are stored locally (on the host 
	where the host :class:`PerformanceEvaluator` was invoked) the host 
	identifier is ``None``. 
	
	Pickle files can be collected on the host that invoked the 
	:class:`PerformanceEvaluator` by calling the :meth:`collectResultFiles`
	method or deleted by calling the :meth:`deleteResultFiles` method. 
	
	*params* is a dictionary of parameters that have the same value 
	every time the object is called. They should not be passed in the 
	*paramDictionary* argument. This argument can also be a list of 
	dictionaries (dictionaries are joined to obtain one dictionary). 
	
	*variables* is a dictionary holding variables that are available 
	during every performance measure evaluation. 
	This can also be a list of dictionaries (dictionaries are joined). 
	
	If *debug* is set to a nonzero value debug messages are generated at the 
	standard output. Two debug levels are available (1 and 2). A higher *debug* 
	value results in greater verbosity of the debug messages. 
	
	Objects of this class construct a list of simulator objects based on the 
	*heads* data structure. Every simulator object performs the analyses which 
	list the corresponding head under ``head`` in the analysis description. 
	
	Every analysis is performed across the set of corners obtained as the union 
	of ``corners`` found in the descriptions of performance measures that list 
	the corresponding analysis as their ``analysis``. 
	
	The system description for an analysis in a corner is constructed from 
	system description modules specified in the corresponding entries in 
	*corners*, and *analyses* data structures. The definitions of the system 
	description modules are taken from the *heads* data structure entry 
	corresponding to the ``head`` specified in the description of the analysis 
	(*analysis* data structure). 
	
	System parameters for an analysis in a particular corner are obtained as 
	the union of

	* the input parameters dictionary specified when an object of the 
	  :class:`PerformanceEvaluator` class is called 
	* the ``params`` dictionary specified at evaluator construction. 
	* the ``params`` dictionary of the *heads* data structure entry 
	  corresponding to the analysis
	* the ``params`` dictionary of the *corners* data structure entry 
	  corresponding to the corner
	* the ``params`` dictionary of the *analyses* data structure entry 
	  corresponding to the analysis
	
	If a parameter appears across multiple dictionaries the entries in the 
	input parameter dictionary have the lowest priority and the entries in the 
	``params`` dictionary of the *analyses* have the highest priority. 
	
	A similar priority order is applied to simulator options specified in the 
	``options`` dictionaries (the values from *heads* have the lowest priority 
	and the values from *analyses* have the highest priority). The only 
	difference is that here we have no options separately specified at evaluator 
	construction because simulator options are always associated with a 
	particular simulator (i.e. head). 
	
	Independent performance measures (the ones with ``analysis`` not equal to 
	``None``) are evaluated before dependent performance measures (the ones 
	with ``analysis`` set to ``None``). 
	
	The evaluation results are stored in a dictionary of dictionaries with 
	performance measure name as the first key and corner name as the second 
	key. ``None`` indicates that the performance measure evaluation failed in 
	the corresponding corner. 
	
	Objects of this type store the number of analyses performed in the 
	*analysisCount* member. The couter is reset at every call to the 
	evaluator object. 
	
	A call to an object of this class returns a tuple holding the results 
	and the *analysisCount* dictionary. The results dictionary is a 
	dictionary of dictionaries where the first key represents the 
	performance measure name and the second key represents the corner name. 
	The dictionary holds the values of performance measure 
	values across corners. If some value is ``None`` the performance 
	measure evaluation failed for that corner. The return value is also stored 
	in the *results* member of the :class:`PermormanceEvaluator` object. 
	
	Lists of component names for measures that produce vectors are stored in 
	the *componentNames* member as a dictionary with measure name for key. 
	
	Simulator input and output files are deleted after a simulator job is 
	completed and its results are evaluated. If *cleanupAfterJob* is ``False`` 
	these files are not deleted. Consequently they accumulate on the harddrive. 
	Call the :meth:`finalize` method to remove them manually. Note this not 
	only cleans up all intermediate files, but also shuts down all simulators. 
	
	If *spawnerLevel* is not greater than 1, evaluations are distributed across 
	available computing nodes (that is unless task distribution takes place at 
	a higher level). Every computing node evaluates one job group. See 
	the :mod:`~pyopus.parallel.cooperative` module for details on parallel 
	processing. More information on job groups can be found in the 
	:mod:`~pyopus.simulator` module. 
	"""
	# Constructor
	def __init__(
		self, heads, analyses, measures, corners=None, params={}, variables={}, activeMeasures=None, 
		cornerOrder=None, fullEvaluation=False, 
		storeResults=False, resultsFolder=None, resultsPrefix="", 
		debug=0, cleanupAfterJob=True, 
		spawnerLevel=1
	):
		# Debug mode flag
		self.debug=debug
		
		# Store problem
		self.heads=heads
		self.analyses=analyses
		self.measures=measures
		
		if corners is not None:
			self.corners=corners
		else:
			# Construct default corner with no modules and no params
			self.corners={
				'default': {
					'heads': list(self.heads.keys()), 
					'modules': [], 
					'params': {}
				}
			}
		
		self.fullEvaluation=fullEvaluation
		
		self.storeResults=storeResults
		self.resultsFolder=resultsFolder
		self.resultsPrefix=resultsPrefix
		
		if cornerOrder is not None:
			self.cornerOrder=cornerOrder
		else:
			self.cornerOrder=list(self.corners.keys())
			
		self.spawnerLevel=spawnerLevel
		
		self.cleanupAfterJob=cleanupAfterJob
		
		# Set fixed parameters
		self.setParameters(params)
		
		# Set fixed variables
		self.skipCompile=True
		self.setVariables(variables)
		self.skipCompile=False
		
		# Set active measures and compile
		self.setActiveMeasures(activeMeasures)
		
		# Results of the performance evaluation
		self.results=None
		
		# Input parameters
		self.inputParams={}
		
		# Analysis count
		self.analysisCount={}
		
		self.resetCounters()
		
		# Evaluate measure component names
		self.componentNames={}
		for measureName, measure in self.measures.items():
			if 'vector' in measure and measure['vector'] and 'components' in measure:
				self.componentNames[measureName]=self.evaluateComponentNames(measureName, measure, self.fixedVariables)
				
	# Evaluate component names for a measure
	@classmethod
	def evaluateComponentNames(cls, measureName, measure, variables={}):
		compExpr=measure['components']
		
		tmpLocals={}
		tmpLocals.update(variables)
		try:
			names=eval(compExpr, globals(), tmpLocals)
		except Exception as e:
			raise PyOpusError(DbgMsg("PE", ("Failed to evaluate component names expression for measure '%s'.\n" % (measureName))+str(e)))
		
		if type(names) is not list:
			raise PyOpusError(DbgMsg("PE", "Component names expression for measure '%s' does not produce a list." % (measureName)))
		
		ii=0
		for name in names:
			if type(name) is not str:
					raise PyOpusError(DbgMsg("PE", "Component names list member %d for measure '%s' is not a string." % (ii, measureName)))
			ii+=1
		
		return names
	
	# Generate sets of possible corners for all measures
	def availableCornerListsForMeasures(self):
		# Build defined modules sets for heads
		definedModulesSets={}
		for headName, head in self.heads.items():
			definedModulesSets[headName]=set(head['moddefs'].keys())
			
		# Build corner sets for heads
		head2corners={}
		for cornerName, corner in self.corners.items():
			cornerModulesSet=set(corner['modules'])
			for headName in corner['heads']:
				if headName not in self.heads:
					raise PyOpusError(DbgMsg("PE", "Corner '%s' uses an undefined head '%s'." % (cornerName, headName)))
				
				head=self.heads[headName]
				
				# Check if modules are all defined in a head
				missingSet=cornerModulesSet.difference(definedModulesSets[headName])
				if len(missingSet)>0:
					raise PyOpusError(DbgMsg("PE", "Module '%s' used by corner '%s' is not defined in head '%s'." % (missingSet.pop(), cornerName, headName)))
				
				if len(cornerModulesSet)>len(corner['modules']):
					raise PyOpusError(DbgMsg("PE", "List of modules for corner '%s' contains duplicates." % (cornerName)))
				
				if headName not in head2corners:
					head2corners[headName]=set([])
				
				head2corners[headName].add(cornerName)
		
		# Go through independent measures, get heads, build corner lists
		measure2possibleCorners={}
		for measureName, measure in self.measures.items():
			if measure['analysis'] is None:
				continue
			analysisName=measure['analysis']
			
			if analysisName not in self.analyses:
				raise PyOpusError(DbgMsg("PE", "Measure '%s' is based on an undefined analysis '%s'." % (measureName, analysisName)))
			
			headName=self.analyses[analysisName]['head']
			
			if headName not in self.heads:
				raise PyOpusError(DbgMsg("PE", "Analysis '%s' uses an undefined head '%s'." % (analysisName, headName)))
			
			# Collect corners that are defined for that particular head
			measure2possibleCorners[measureName]=head2corners[headName]
			
			if len(head2corners[headName])<=0:
				raise PyOpusError(DbgMsg("PE", "Measure '%s' has no available corners." % (measureName)))
		
		# Go through dependent measures, collect measures they depend on, translate them to heads
		for measureName, measure in self.measures.items():
			if measure['analysis'] is not None:
				continue
			
			if 'depends' in measure and len(measure['depends'])>0:
				# The set of possible corners is the intersection across all measures corresponding to dependencies
				cornerSet=None
				for dependName in measure['depends']:
					if dependName not in self.measures:
						raise PyOpusError(DbgMsg("PE", "Dependent measure '%s' depends on an undefined measure '%s'." % (measureName, dependName)))
					
					if self.measures[dependName]['analysis'] is None:
						raise PyOpusError(DbgMsg("PE", "Dependent measure '%s' depends on another dependent measure '%s'." % (measureName, dependName)))
					
					if cornerSet is None:
						cornerSet=measure2possibleCorners[dependName]
					else:
						cornerSet=cornerSet.intersection(measure2possibleCorners[dependName])
			else:
				# Measure depends on no other measure, the corner set contains all corners
				cornerSet=set(self.corners.keys())
				
			if len(cornerSet)<=0:
				raise PyOpusError(DbgMsg("PE", "Dependent measure '%s' has no available corners." % (measureName)))
			
			measure2possibleCorners[measureName]=cornerSet
		
		# Build list of all corners where at least one measure is evaluated
		allCorners=set()
		for measure, cornerSet in measure2possibleCorners.items():
			allCorners.update(cornerSet)
		
		return measure2possibleCorners, allCorners, head2corners
	
	# Corner list/set dictionary
	# Convert sets to lists, sort in corner order
	def sortCornerListDict(self, cornerListDict):
		res={}
		for key, clist in cornerListDict.items():
			if self.cornerOrder is None:
				res[key]=list(clist)
			else:
				cs=set(clist)
				l=[]
				for c in self.cornerOrder:
					if c in cs:
						l.append(c)
				res[key]=l
			
		return res
			
	def _compile(self):
		"""
		Prepares internal structures for faster processing. 
		This function should never be called by the user. 
		"""
		# Sanity check
		for measureName in self.activeMeasures:
			if measureName not in self.measures:
				raise PyOpusError(DbgMsg("PE", "Measure '%s' is not defined." % measureName))
		
		# Generate sets of available corners for measures (m2c), 
		# all corners where at least one measure is evaluated (allc), and 
		# sets of corners defined for head (h2c)
		# Note that the 'default' corner is already there
		# This also does some heavy duty sanity checks
		m2c, allc, h2c = self.availableCornerListsForMeasures()
		
		# All defined corners across all heads
		allDefinedCorners=set()
		for headName, cset in h2c.items():
			allDefinedCorners.update(cset)
		
		
		# Construct list of computed measures
		computedMeasures=set(self.activeMeasures)
		
		# Check for duplicate corners
		for measureName in computedMeasures:
			if (
				'corners' in self.measures[measureName] and
				len(self.measures[measureName]['corners'])!=len(set(self.measures[measureName]['corners']))
			):
				raise PyOpusError(DbgMsg("PE", "Measure '%s' has duplicate corners listed." % (measureName)))
		
		# Build a list of measures that are actually going to be evaluated (include dependencies)
		# Repeat this until no more measures are added
		while True:
			# Go through all measures and add all dependancies
			candidates=[]
			for measureName in computedMeasures:
				if 'depends' in self.measures[measureName]:
					deps=self.measures[measureName]['depends']
					candidates.extend(deps)
			
			# Form union
			oldLen=len(computedMeasures)
			computedMeasures=computedMeasures.union(candidates)
			if len(computedMeasures)==oldLen:
				break
			
		# Store
		self.computedMeasures=computedMeasures
		
		# Check heads for simulator and moddefs
		for (name, head) in self.heads.items():
			if 'simulator' not in head:
				raise PyOpusError(DbgMsg("PE", "No simulator specified for head '%s'." % name))
			if 'moddefs' not in head or len(head['moddefs'])<1:
				raise PyOpusError(DbgMsg("PE", "No definitions specified for head '%s'." % name))
			
		# Build a dictionary with head name as key containing lists of analyses that use a particular head
		head2an={}
		for (name, an) in self.analyses.items():
			headName=an['head']
			# Sanity check
			if headName not in self.heads:
				raise PyOpusError(DbgMsg("PE", "Head '%s' used by analysis '%s' is not defined." % (headName, name)))
			
			if headName not in head2an:
				head2an[headName]=[name]
			else:
				head2an[headName].append(name)

		# Store head2an
		self.head2an=head2an
		
		# Dependent measures that are going to be computed
		computedDependentMeasures=[]
		
		# These lists take into account dependencies
		# List of corners to evaluate for every analysis (including None)
		an2corners={}
		# List of corners for all measures with analysis None
		measure2corners={}
		# List of measures evaluated for every (corner, analysis) pair
		key2measures={}
		
		# Go through measures that are going to be computed
		for measureName in self.computedMeasures:
			measure=self.measures[measureName]
			anName=measure['analysis']
			possibleCorners=m2c[measureName]
			
			# Check if all listed corners are possible for this measure
			if 'corners' in measure:
				listedCorners=set(measure['corners'])
				undefSet=listedCorners.difference(possibleCorners)
				if len(undefSet)>0:
					raise PyOpusError(DbgMsg("PE", "Corner '%s' listed in defintion of measure '%s' is not available for this measure." % (undefSet.pop(), measureName)))
			
			# Use listed corners if given, otherwise use availabe corners
			cornerNames=listedCorners if 'corners' in measure else m2c[measureName]
			
			# Handle analysis
			if anName is not None:
				# Named analysis
				# Add to list of corners for the analysis
				if anName not in an2corners:
					an2corners[anName]=set([])
				an2corners[anName].update(cornerNames)
				# Add  to list of corners for measure
				if measureName not in measure2corners:
					measure2corners[measureName]=set()
				measure2corners[measureName].update(set(cornerNames))
			else:
				# None analysis (dependent measure)
				measure2corners[measureName]=cornerNames
				computedDependentMeasures.append(measureName)
				
				# Add to list of corners for dependencies
				if 'depends' in measure:
					for depName in measure['depends']:
						depAnName=self.measures[depName]['analysis']
						
						# Add to list of corners for the analysis corresponding to the dependency
						if depAnName not in an2corners:
							an2corners[depAnName]=set([])
						an2corners[depAnName].update(cornerNames)
						
						# Add to list of list of corners for measures with named analyses
						if depName not in measure2corners:
							measure2corners[depName]=set()
						measure2corners[depName].update(set(cornerNames))
		
		# Full evaluation forced (all analyses in all corners)
		if self.fullEvaluation:
			# Independent analyses
			for anName, an in self.analyses.items():
				headName=an['head']
				if anName not in an2corners:
					an2corners[anName]=set()
				an2corners[anName].update(h2c[headName])
			
			# Add them None analyses for all of these corners
			an2corners[None]=allDefinedCorners
				
			# Put empty sets in key2measures for all corner, analysis pairs
			for anName, cset in an2corners.items():
				for cornerName in cset:
					key=(cornerName, anName)
					key2measures[key]=set()
			
		
		# Build key2measures
		# Compute a measure in every corner where its analysis is computed
		for measureName in self.computedMeasures:
			measure=self.measures[measureName]
			anName=measure['analysis']
			
			if anName is not None:
				# Named analyses
				
				# This adds all measures that belong to an analysis
				#for cornerName in an2corners[anName]:
				#	key=(cornerName,anName)
				#	if key not in key2measures:
				#		key2measures[key]=set([])
				#	key2measures[key].add(measureName)
				
				# Add only those measures that need to be evaluated
				for cornerName in measure2corners[measureName]:
					key=(cornerName,anName)
					if key not in key2measures:
						key2measures[key]=set([])
					key2measures[key].add(measureName)
			else:
				# None analysis
				for cornerName in measure2corners[measureName]:
					key=(cornerName,anName)
					if key not in key2measures:
						key2measures[key]=set([])
					key2measures[key].add(measureName)
		
		# Convert all an2corners entries to lists
		an2corners={ name: list(s) for (name, s) in an2corners.items() }
		
		# Convert sets to lists, sort in corner order
		m2c=self.sortCornerListDict(m2c)
		an2corners=self.sortCornerListDict(an2corners)
		measure2corners=self.sortCornerListDict(measure2corners)
		allCorners=sorted(list(allc))
		allDefinedCorners=sorted(list(allDefinedCorners))
		
		# Avaliable corners for measures
		self.availableCornersForMeasure=m2c
		
		# All corners where at least one measure is evaluated
		self.allCorners=allCorners
		
		# All defined corners
		self.allDefinedCorners=allDefinedCorners
		
		# Store an2corners, measure2corners, and key2measures. 
		self.an2corners=an2corners
		self.measure2corners=measure2corners
		self.key2measures=key2measures
		
		# Store names of dependent measures to compute
		self.computedDependentMeasures=computedDependentMeasures
		
		# Build joblists for all heads, remember key=(corner,analysis) for every job. 
		jobListForHead={}
		keyListForHead={}
		# Go through all heads
		for (headName, anList) in head2an.items(): 
			head=self.heads[headName]
			# For every head go through all analyses
			jobList=[]
			keyList=[]
			for anName in anList:
				analysis=self.analyses[anName]
				# For every analysis go through all corners
				if anName in an2corners:
					for cornerName in an2corners[anName]:
						corner=self.corners[cornerName]
						# Create job for analysis in corner
						job={}
						key=(cornerName, anName) 
						
						job['name']="C"+cornerName+"A"+anName
						job['command']=analysis['command']
						if 'saves' in analysis:
							job['saves']=analysis['saves']
						else:
							job['saves']=[]
											
						# Create a list of modules by joining analysis and corner lists. 
						modules=[]
						if 'modules' in corner:
							modules.extend(corner['modules'])
						if 'modules' in analysis:
							modules.extend(analysis['modules'])
						# Search for duplicates. 
						if len(modules)!=len(set(modules)):
							raise PyOpusError(DbgMsg("PE", "Duplicate modules in corner '%s', analysis '%s'." % (cornerName, anName)))

						# Translate to actual module definitions using information in the head. 
						job['definitions']=[]
						for module in modules: 
							# Sanity check
							if module not in head['moddefs']:
								raise PyOpusError(DbgMsg("PE", "Module '%s' used by '%s/%s' is not defined." % (module,anName, cornerName)))
								
							job['definitions'].append(head['moddefs'][module])
						
						# Merge params from head, corner, and analysis. 
						params={}
						if 'params' in head:
							params.update(head['params'])
							# print "head", head['params']
						if 'params' in corner:
							params.update(corner['params'])
							# print "corner", corner['params']
						if 'params' in analysis:
							params.update(analysis['params'])
							# print "analysis", analysis['params']
						job['params']=params
						
						# Build variables dictionary
						variables={}
						variables.update(self.fixedVariables)
						job['variables']=variables
						
						# Merge options from head, corner, and analysis. 
						options={}
						if 'options' in head:
							options.update(head['options'])
						if 'options' in corner:
							options.update(corner['options'])
						if 'options' in analysis:
							options.update(analysis['options'])
						job['options']=options
						# Append to job list for this head. 
						jobList.append(job)
						keyList.append(key)
						
						# print cornerName, corner
						# print "comp job -- ", job
			
			# Store in jobListforHead. 
			jobListForHead[headName]=jobList
			keyListForHead[headName]=keyList
		
		# Store jobListForHead and keyListForHead.  
		self.jobListForHead=jobListForHead
		self.keyListForHead=keyListForHead
		
		# Build simulator objects, one for every head. 
		# Build Local variable dictionaries for measurement evaluation. 
		self.simulatorForHead={}
		for (headName, head) in self.heads.items():
			# Get simulator class
			if type(head['simulator']) is str:
				try:
					SimulatorClass=simulatorClass(head['simulator'])
				except:
					raise PyOpusError(DbgMsg("PE", "Simulator '"+head['simulator']+"' not found."))
			else:
				SimulatorClass=head['simulator']
				
			# Create simulator
			simulator=SimulatorClass(**(head['settings'] if 'settings' in head else {}))
			simulator.setJobList(jobListForHead[headName]) 
			
			self.simulatorForHead[headName]=simulator
		
		# Compile measures
		self.compiledMeasures={}
		self.isScript={}
		for measureName, measure in self.measures.items():
			if "expression" not in measure:
				continue
			
			c, isScript = PerformanceEvaluator.compileMeasure(
				measureName, measure, self.debug
			)
			
			self.compiledMeasures[measureName]=c
			self.isScript[measureName]=isScript
			
		if self.debug:
			DbgMsgOut("PE", "  Simulator objects (%d): " % len(self.jobListForHead))
			for (headName, jobList) in self.jobListForHead.items(): 
				DbgMsgOut("PE", "    %s: %d analyses" % (headName, len(jobList)))
				if self.debug>1:
					for job in jobList:
						DbgMsgOut("PE", "      %s" % job['name'])
	
	@classmethod
	def compileMeasure(cls, measureName, measure, debug):
		# Return compiled measure and isScript flag
		
		# Strip leading and trailing whitespace
		s=measure["expression"].strip()
		
		# Zero length means an error
		if len(s)<=0:
			raise PyOpusError(DbgMsg("PE", "Measure expression/script '"+measureName+"' has zero length."))
		# Assume it is an expression
		try:
			c=compile(measure["expression"], measureName+" expression/script", "eval")
			isScript=False
		except:
			# Failed, try to compile it as a script
			try:
				c=compile(measure["expression"], measureName+" expression/script", "exec")
				isScript=True
			except:
				# Report error
				ei=exc_info()
				txt1="Failed to compile measure '"+measureName+"'.\n"
				for line in format_exception(ei[0], ei[1], ei[2]):
					txt1+=line
				DbgMsgOut("PE", txt1) 
				raise PyOpusError(DbgMsg("PE", "Failed to compile measure '"+measureName+"."))
		
		return c, isScript
	
	# For pickling
	def __getstate__(self):
		state=self.__dict__.copy()
		del state['head2an']    # lists of analyses for heads
		del state['an2corners'] # lists of corners for analyses (corner-analysis pairs to evaluate)
		del state['allCorners'] # all corners where at least one measure is evaluated
		del state['allDefinedCorners'] # all defined corners across all heads
		del state['measure2corners']   # corners where measures need to be evaluated
		del state['key2measures']      # measures for every corner,analysis pair
		del state['availableCornersForMeasure'] # corners in which a measure can be evaluated
		del state['computedDependentMeasures']  # list of dependent measures that are going to be computed
		del state['jobListForHead']
		del state['keyListForHead']
		del state['simulatorForHead']
		del state['compiledMeasures']
		del state['isScript']
		
		return state
	
	# For unpickling
	def __setstate__(self, state):
		self.__dict__.update(state)
		
		self._compile()
	
	# Reconfigure fixed parameters
	def setParameters(self, params):
		"""
		Sets the parameters dictionary. 
		Can handle a list of dictionaries. 
		"""
		if type(params) is list:
			inputList=params
		else:
			inputList=[params]
		self.fixedParameters={}
		for inputDict in inputList:
			self.fixedParameters.update(inputDict)
	
	# Reset analysis counters
	def resetCounters(self):
		"""
		Resets analysis counters to 0. 
		"""
		self.analysisCount={}
		for name in self.analyses.keys():
			self.analysisCount[name]=0
		
	# Set the variables dictionary. 
	def setVariables(self, variables):
		"""
		Sets the variables dictionary. 
		Can handle a list of dictionaries. 
		"""
		if type(variables) is list:
			inputList=variables
		else:
			inputList=[variables]
		self.fixedVariables={}
		for inputDict in inputList:
			self.fixedVariables.update(inputDict)
		# Need to recompile because the jobs have changed
		if not self.skipCompile:
			self._compile()
	
	# Reconfigure measures
	def setActiveMeasures(self, activeMeasures=None):
		"""
		Sets the list of measures that are going to be evaluated. 
		Specifying ``None`` as *activeMeasures* activates all 
		measures. 
		"""
		# Evaluate all measures by default
		if activeMeasures is not None:
			self.activeMeasures=activeMeasures
		else:
			self.activeMeasures=list(self.measures.keys())
		
		# Compile
		if self.debug:
			DbgMsgOut("PE", "Compiling.")
			
		self._compile()
		
	# Get active measures
	def getActiveMeasures(self):
		"""
		Returns the names of the active measures. 
		"""
		return self.activeMeasures
	
	def getComputedMeasures(self):
		"""
		Returns the names of all measures that are computed 
		by the evaluator. 
		"""
		return self.computedMeasures
	
	def getParameters(self):
		"""
		Returns the parameters dictionary. 
		"""
		return self.fixedParameters
	
	def getVariables(self):
		"""
		Returns the variables dictionary. 
		"""
		return self.fixedVariables
	
	# Return simulators dictionary. 
	def simulators(self):
		"""
		Returns the dictionary with head name for key holding the corresponding 
		simulator objects. 
		"""
		return self.simulatorForHead
	
	# Cleanup simulator intermediate files and stop interactive simulators. 
	def finalize(self):
		"""
		Removes all intermediate simulator files and stops all interactive 
		simulators. 
		"""
		for (headName, simulator) in self.simulatorForHead.items():
			simulator.cleanup()
			simulator.stopSimulator()
	
	def generateJobs(self, inputParams):
		# Go through all simulators
		for (headName, simulator) in self.simulatorForHead.items():
			if self.debug: 
				DbgMsgOut("PE", "  Simulator/head %s" % headName)
			
			# Get head.
			head=self.heads[headName]
			
			# Get job list. 
			jobList=self.jobListForHead[headName]
			
			# Get key list. 
			keyList=self.keyListForHead[headName]
			
			# Set input parameters. 
			simulator.setInputParameters(inputParams)
			
			# Count job groups. 
			ngroups=simulator.jobGroupCount()
			
			# Go through all job groups, prepare job
			for i in range(ngroups):
				yield (
					self.processJob, [
						headName, simulator, jobList, keyList, i, 
						inputParams, self.isScript, self.key2measures, self.measures, 
						self.storeResults, self.resultsFolder, self.resultsPrefix, 
						self.cleanupAfterJob, 
						self.debug
					]
				)
	
	@classmethod
	def evaluateMeasure(cls, evalEnvironment, measureName, measure, isScript, debug):
		# Returns measure value
		# TODO: maybe run it in a function so it has its own namespace
		# Evaluate measure, catch exception that occurs during evaluation. 
		try: 
			# Prepare evaluation environment, copy template
			tmpLocals={}
			tmpLocals.update(evalEnvironment)
			if measureName in isScript:
				if isScript[measureName]:
					# Handle as script
					# Do not use compiled version because no debug information is produced on errors
					exec(measure['expression'], globals(), tmpLocals)
					# Collect result
					if "__result" in tmpLocals:
						measureValue=tmpLocals['__result']
					elif measureName in tmpLocals:
						measureValue=tmpLocals[measureName]
					else:
						measureValue=None
				else:
					# Handle as expression 
					# Do not use compiled version because no debug information is produced on errors
					measureValue=eval(measure['expression'], globals(), tmpLocals)	
			elif 'script' in measure:
				# Legacy 'script'
				exec(measure['script'], globals(), tmpLocals)
				measureValue=tmpLocals['__result']
			else:
				raise PyOpusError(DbgMsg("PE", "No expression or script."))
			if debug>1:
				DbgMsgOut("PE", "      %s : %s" % (measureName, str(measureValue)))
			elif debug>0: 
				DbgMsgOut("PE", "      %s OK" % (measureName))
		except KeyboardInterrupt:
			DbgMsgOut("PE", "Keyboard interrupt.")
			raise
		except:
			measureValue=None
			if debug:
				DbgMsgOut("PE", "      %s FAILED" % measureName)
				ei=exc_info()
				if debug>1:
					for line in format_exception(ei[0], ei[1], ei[2]):
						DbgMsgOut("PE", "        "+line) 
				else:
					for line in format_exception_only(ei[0], ei[1]):
						DbgMsgOut("PE", "        "+line)
		
		return measureValue
	
	@classmethod
	def _postprocessMeasure(cls, measureValue, isVector, debug):
		"""
		Postprocesses *measureValue* obtained by evaluating the ``script`` or
		the ``expression`` string describing the measurement. 
		
		1. Converts the result to an array. 
		2. Signals an error if the array type is complex. 
		3. Converts the array of values to a double floating point array. 
		4. If the array is empty (size==0) signals an error. 
		5. Signals an error if *isVector* is ``False`` and the array has size>1. 
		6. Scalarizes array (makes it a 0D array) if *isVector* is ``False``. 
		"""
		# None indicates a failure, nothing further to do. 
		if measureValue is not None:
			# Pack it in an array
			if type(measureValue) is not ndarray: 
				# This will convert lists and tuples to arrays
				try:
					measureValue=array(measureValue)
				except KeyboardInterrupt:
					DbgMsgOut("PE", "keyboard interrupt")
					raise
				except:
					if debug:
						DbgMsgOut("PE", "        Result can't be converted to an array.")
					measureValue=None
			
			# Was conversion successfull? 
			if measureValue is not None: 
				# It is an array
				# Check if it is complex
				if iscomplex(measureValue).any():
					# Bad. Complex value not allowed.
					if debug:
						DbgMsgOut("PE", "        Measurement produced a complex array.")
					measureValue=None
				elif measureValue.dtype is not dtype('float64'):
					# Not complex. Convert it to float64. 
					# On conversion failure we get an exception and a failed measurement. 
					try:
						measureValue=measureValue.astype(dtype('float64'))
					except KeyboardInterrupt:
						DbgMsgOut("PE", "keyboard interrupt")
						raise
					except:
						if debug:
							DbgMsgOut("PE", "        Failed to convert result into a real array.")
						measureValue=None
				
				# Check if it is empty
				if measureValue is not None and measureValue.size==0: # TODO fix crash
					# It is empty, this is bad
					if debug:
						DbgMsgOut("PE", "        Measurement produced an empty array.")
					measureValue=None
				
				# Scalarize if measurement is scalar
				if (measureValue is not None) and (not isVector):
					# We are expecting a scalar.
					if measureValue.size==1:
						# Scalarize it
						measureValue=measureValue.ravel()[0]
					else:
						# But we have a vector, bad
						if debug:
							DbgMsgOut("PE", "        Scalar measurement produced a vector.")
						measureValue=None
		
		return measureValue
	
	@classmethod
	def processJob(cls, headName, simulator, jobList, keyList, i, inputParams, isScript, key2measures, measures, storeResults, resultsFolder, resultsPrefix, cleanupAfterJob, debug):
		# Run jobs in job group and collect results. 
		(jobIndices, status)=simulator.runJobGroup(i)
		
		results={}
		analysisCount={}
		
		# Go through all job indices in i-th job group. 
		resFiles={}
		for j in jobIndices: 
			# Get (corner, analysis) key for j-th job. 
			key=keyList[j]
			(cornerName, anName)=key
			job=jobList[j]
			
			# Load results (one job at a time to save memory). 
			res=simulator.readResults(j, status)
			
			# Do we have a result? 
			if res is None: 
				# No. 
				# Assume all measurements that depend on this analysis have failed
				if debug: 
					DbgMsgOut("PE", "    Corner: %s, analysis %s ... FAILED" % (cornerName, anName))
					
				# Set corresponding measurements to None
				for measureName in key2measures[key] if key in key2measures else []:
					# Store result
					if measureName not in results:
						results[measureName]={}
					results[measureName][cornerName]=None
					
					if debug: 
						DbgMsgOut("PE", "      %s : FAILED" % measureName)
			else:
				# Yes, we have a result. 
				if debug: 
					DbgMsgOut("PE", "    Corner: %s, analysis: %s ... OK" % (cornerName, anName))
				
				# Prepare evaluation environment template
				evalEnvironment=res.evalEnvironment()
				
				# Update analysis counter
				if key[1] not in analysisCount:
					analysisCount[key[1]]=1
				else:
					analysisCount[key[1]]+=1
				
				# Go through all measurements for this key. 
				for measureName in key2measures[key] if key in key2measures else []:
					# Get measure. 
					measure=measures[measureName]
					
					# Evaluate it
					measureValue=cls.evaluateMeasure(
						evalEnvironment, measureName, measure, isScript, debug
					)
					
					# Prepare measure storage (first evaluation corner)
					if measureName not in results:
						results[measureName]={}
					
					# Are we expecting a vector?
					isVector=bool(measure['vector']) if 'vector' in measure else False
					
					# Postprocess and store
					results[measureName][cornerName]=cls._postprocessMeasure(measureValue, isVector, debug)
			
			# Store simulator results in a temporary pickle file
			# If an analysis failed None is stored in the results file
			if storeResults:
				namePrefix=resultsPrefix+locationID()+'_'+job['name']+"_"
				tmpfh, filePath = tempfile.mkstemp(prefix=namePrefix, dir=resultsFolder)
				fd=os.fdopen(tmpfh, "wb")
				pickle.dump(res, fd)
				fd.close()
				#os.fsync(tmpfh)
				#os.close(tmpfh)
				resFiles[key]=filePath
			
		# Clean up - if simulators writing to the same folder have same ID this causes a bug
		# where one simulator deletes files of an other simulator
		if cleanupAfterJob:
			simulator.cleanup()
		
		return results, analysisCount, resFiles
	
	def collectResults(self, analysisCount, results):
		while True:
			index, job, (res1, anCount, resFiles), hostID = (yield)
			
			for key, resFile in resFiles.items():
				self.resFiles[(hostID, key)]=resFile
			
			updateAnalysisCount(analysisCount, anCount)
			for measName, cornerResults in res1.items():
				if measName not in results:
					results[measName]={}
				for cornerName, value in cornerResults.items():
					results[measName][cornerName]=value
	
	@classmethod
	def collectResultFilesWorker(cls, xferList, move):
		collected={}
		for localPath, abstractPath, (key, destinationFile) in xferList:
			destinationPath=cOS.toActualPath(abstractPath)
			try:
				if move:
					shutil.move(localPath, destinationPath)
				else:
					shutil.copy2(localPath, destinationPath)
				collected[key]=destinationFile
			except:
				pass
		
		return collected 
	
	@classmethod
	def deleteResultFilesWorker(cls, localFilesList):
		status=[]
		for localPath in localFilesList:
			try:
				os.remove(localPath)
				status.append(True)
			except:
				status.append(False)
			
	def collectResultFiles(self, destination, prefix="", move=True):
		"""
		Result files are always stored locally on the host where the 
		corresponding simulator job was run. This function copies or 
		moves them to the host where the :class:`PerformanceEvaluator`
		object was called to evaluate the circuit's performance. 
		
		The files are stored in a folder specified by *destination*. 
		*destination* must be mounted on all workers and must be in 
		the path specified by the ``PARALLEL_MIRRORED_STORAGE`` 
		environmental variable if parallel processing across multiple 
		computers is used. 
		
		If *move* is set to ``True`` the original files are removed. 
		
		The file name consists of *prefix*, corner name, analysis name, 
		and ``.pck``. 
		
		Returns a dictionary with (cornerName, analysisName) for key 
		holding the corresponding result file names. 
		"""
		# Prepare files dictionary
		files={}
		
		# Group keys by hosts
		toCollect={}
		for (host, key), localPath in self.resFiles.items():
			if host not in toCollect:
				toCollect[host]=[]
			toCollect[host].append((key, localPath))
		
		# Handle local files first
		if None in toCollect:
			for key, localPath in toCollect[None]:
				cornerName, analysisName = key
				if analysisName is None:
					destinationFile=prefix+cornerName+'.pck'
				else:
					destinationFile=prefix+cornerName+'_'+analysisName+'.pck'
					
				destinationPath=os.path.join(
					destination, 
					destinationFile
				)
				try:
					if move:
						shutil.move(localPath, destinationPath)
					else:
						shutil.copy2(localPath, destinationPath)
					files[key]=destinationFile
				except:
					pass
			
			# Remove local file entries from dictionary
			del toCollect[None]
			
		# Now handle remote files by spawning collect jobs
		tidList=set()
		for host, fileList in toCollect.items():
			xferList=[]
			for key, localPath in fileList:
				cornerName, analysisName = key
				if analysisName is None:
					destinationFile=prefix+cornerName+'.pck'
				else:
					destinationFile=prefix+cornerName+'_'+analysisName+'.pck'
					
				destinationPath=os.path.join(
					destination, 
					destinationFile
				)
				abstractPath=cOS.toAbstractPath(destinationPath)
				xferList.append(
					(localPath, abstractPath, (key, destinationFile))
				)
				
			tid=cOS.Spawn(
				self.collectResultFilesWorker, 
				(xferList, move), 
				remote=True, block=False, enqueue=True
			)
			tidList.add(tid)
		
		# Join collect jobs
		while len(tidList)>0:
			jr=cOS.Join(block=True)
			for tid, retval in jr.items():
				tidList.discard(tid)
				files.update(retval)
			
		return files
	
	def deleteResultFiles(self):
		"""
		Removes the result files from all hosts where simulation jobs 
		were run. 
		"""
		# Group keys by hosts
		toCollect={}
		for (host, key), localPath in self.resFiles.items():
			if host not in toCollect:
				toCollect[host]=[]
			toCollect[host].append((key, localPath))
		
		# Handle local files first
		if None in toCollect:
			for key, localPath in toCollect[None]:
				try:
					os.remove(localPath)
				except:
					pass
			
			del toCollect[None]
			
		# Now handle remote files by spawning delete jobs
		tidList=set()
		for host, fileList in toCollect.items():
			delList=[]
			for key, localPath in fileList:
				delList.append(localPath)
			
			tid=cOS.Spawn(
				self.deleteResultFilesWorker, 
				(delList, ), 
				remote=True, block=False, enqueue=True
			)
			tidList.add(tid)
			
		# Join remove tasks
		while len(tidList)>0:
			jr=cOS.Join(block=True)
			for tid, retval in jr.items():
				tidList.discard(tid)
		
	def __call__(self, parameters={}):
		if self.debug: 
			DbgMsgOut("PE", "Evaluation started.") 
		
		# Reset counters
		self.resetCounters()
		
		# Clear results.
		self.results={}
		
		# Collect parameters when they are given as a list of dictionaries
		if type(parameters) is tuple or type(parameters) is list:
			srcList=parameters
		else:
			srcList=[parameters]
		
		inputParams1={}
		for subList in srcList:
			# Update parameter dictionary
			inputParams1.update(subList)
		
		# Merge with fixed parameters
		inputParams={}
		inputParams.update(self.fixedParameters)
		inputParams.update(inputParams1)
		
		# Check for conflicts
		if len(inputParams)<len(inputParams1)+len(self.fixedParameters):
			# Find conflicts
			conflict=set(inputParams1.keys()).intersection(self.fixedParameters)
			raise PyOpusError(DbgMsg("PE", "Input parameters "+str(list(conflict))+" conflict with parameters specified at construction."))
		
		# Store parameters
		self.inputParams=inputParams
		
		# Reset temporary results storage
		results={}
		analysisCount={}
		self.resFiles={}
		
		# Dispatch tasks
		cOS.dispatch(
			jobList=self.generateJobs(inputParams), 
			collector=self.collectResults(analysisCount, results), 
			collectHostIDs=True, remote=self.spawnerLevel<=1
		)
		
		# Store results
		self.results=results
		self.analysisCount=analysisCount
		
		# Build result files for None analysis
		# across all corners where at least one measure is defined
		# or across all defined corners (if full evaluation is requested)
		noneRes={}
		for cornerName in self.allDefinedCorners if self.fullEvaluation else self.allCorners:
			corner=self.corners[cornerName]
			
			params={}
			params.update(inputParams)
			if 'params' in corner:
				params.update(corner['params'])
			
			res=NoneSimulationResults(params, self.fixedVariables, self.results)
			noneRes[cornerName]=res
			
			# Store in a file
			if self.storeResults:
				namePrefix=self.resultsPrefix+locationID()+"C"+cornerName+"_"
				tmpfh, filePath = tempfile.mkstemp(prefix=namePrefix, dir=self.resultsFolder)
				fd=os.fdopen(tmpfh, "wb")
				pickle.dump(res, fd)
				fd.close()
				# os.fsync(tmpfh)
				# os.close(tmpfh)
				# None host (local), None corner, None analysis
				self.resFiles[None,(cornerName,None)]=filePath
		
		# Go through all dependent measures
		for measureName in self.computedDependentMeasures:
			cornerNames=self.measure2corners[measureName]
			
			# Go through all corners
			for cornerName in cornerNames:
				corner=self.corners[cornerName]
				
				if self.debug: 
					DbgMsgOut("PE", "    Corner: %s, analysis: None" % cornerName)
				
				# Get measure. 
				measure=self.measures[measureName]
				
				# Get results object
				res=noneRes[cornerName]
				
				# Prepare dictionary of local variables for measurement evaluation
				evalEnvironment=res.evalEnvironment()
				evalEnvironment['cornerName']=cornerName
				
				measureValue=PerformanceEvaluator.evaluateMeasure(
					evalEnvironment, measureName, measure, self.isScript, self.debug
				)
				
				# Prepare measure storage (first evaluation corner)
				if measureName not in self.results:
					self.results[measureName]={}
				
				# Are we expecting a vector?
				isVector=bool(measure['vector']) if 'vector' in measure else False
				
				# Postprocess and store
				self.results[measureName][cornerName]=self._postprocessMeasure(measureValue, isVector, self.debug)
				
		return self.results, self.analysisCount
		
	def formatResults(self, outputOrder=None, nMeasureName=10, nCornerName=6, nResult=12, nPrec=3):
		"""
		Formats a string representing the results obtained with the last call 
		to this object. Generates one line for every performance measure 
		evaluation in a corner. 
		
		*outputOrder* (if given) specifies the order in which the performance 
		measures are listed. 
		
		*nMeasureName* specifies the formatting width for the performance 
		measure name. 
		
		*nCornerName* specifies the formatting width for the corner name. 
		
		*nResult* and *nPrec* specify the formatting width and the number of 
		significant digits for the performance measure value. 
		"""
		# List of measurement names
		if outputOrder is None:
			# Default is sorted by name
			nameList=[]
			# for (measureName, measure) in self.measures.items():
			for measureName in self.computedMeasures:
				measure=self.measures[measureName]
				nameList.append(measureName)
			nameList.sort()
		else:
			nameList=outputOrder

		# Format output
		outStr=""
		for measureName in nameList: 
			if measureName not in self.measures:
				raise PyOpusError(DbgMsg("PE", "Measure '%s' is not defined." % measureName))
			measure=self.measures[measureName]
			# Format measurement values
			first=True
			cornerNames=self.availableCornersForMeasure[measureName]
			for cornerName in cornerNames: 
				# Do we have a result entry
				if measureName not in self.results:
					continue
				if cornerName not in self.results[measureName]:
					continue
				
				# First header
				if first:
					header="%*s | " % (nMeasureName, measureName)
				
				# Result in one corner
				if self.results[measureName][cornerName] is None:
					textVal='%*s: %-*s' % (nCornerName, cornerName, nResult, 'FAILED')
				else:
					if self.results[measureName][cornerName].size==1:
						textVal="%*s: %*.*e" % (nCornerName, cornerName, nResult, nPrec, self.results[measureName][cornerName])
					else:
						textVal="%*s: " % (nCornerName, cornerName) + str(self.results[measureName][cornerName])
				
				# Append
				outStr+=header+textVal+"\n"

				# Remaining headers
				if first:
					first=False
					header="%*s | " % (nMeasureName, '')
				
		return outStr
		
	# Return annotator plugin. 
	def getAnnotator(self):
		"""
		Returns an object of the :class:`PerformanceAnnotator` class which can 
		be used as a plugin for iterative algorithms. The plugin takes care of 
		cost function details (:attr:`results` member) propagation from the 
		machine where the evaluation of the cost function takes place to the 
		machine where the evaluation was requested (usually the master). 
		"""
		return PerformanceAnnotator(self)
	
	# Return collector plugin. 
	def getCollector(self):
		"""
		Returns an object of the :class:`PerformanceCollector` class which can 
		be used as a plugin for iterative algorithms. The plugin gathers 
		performance information from the :attr:`results` member of the 
		:class:`PerformanceEvaluator` object across iterations of the algorithm. 
		"""
		return PerformanceCollector(self)
		
	
# Default annotator for performance evaluator
class PerformanceAnnotator(Annotator):
	"""
	A subclass of the :class:`~pyopus.optimizer.base.Annotator` iterative 
	algorithm plugin class. This is a callable object whose job is to
	
	* produce an annotation (details of the evaluated performance) stored in the 
	  *performanceEvaluator* object 
	* update the *performanceEvaluator* object with the given annotation 
	
	Annotation is a copy of the :attr:`results` member of 
	*performanceEvaluator*. 
	
	Annotators are used for propagating the details of the cost function from 
	the machine where the evaluation takes place to the machine where the 
	evaluation was requested (usually the master). 
	"""
	def __init__(self, performanceEvaluator):
		self.pe=performanceEvaluator
	
	def produce(self):
		return self.pe.results.copy(), self.pe.inputParams.copy(), self.pe.analysisCount.copy(), self.pe.resFiles.copy()
	
	def consume(self, annotation):
		self.pe.results=annotation[0]
		self.pe.inputParams=annotation[1]
		self.pe.analysisCount=annotation[2]
		self.pe.resFiles=annotation[3]

					
# Performance record collector
class PerformanceCollector(Plugin, PerformanceAnnotator):
	"""
	A subclass of the :class:`~pyopus.optimizer.base.Plugin` iterative 
	algorithm plugin class. This is a callable object invoked at every 
	iteration of the algorithm. It collects the summary of the evaluated 
	performance measures from the :attr:`results` member of the 
	*performanceEvaluator* object (member of the :class:`PerformanceEvaluator` 
	class). 
	
	This class is also an annotator that collects the results at remote 
	evaluation and copies them to the host where the remote evaluation was 
	requested. 
	
	Let niter denote the number of stored iterations. The *results* structures 
	are stored in a list where the index of an entry represents the iteration 
	number. The list can be obtained from the :attr:`performance` member of the 
	:class:`PerformanceCollector` object. 
	
	Some iterative algorithms do not evaluate iterations sequentially. Such 
	algorithms denote the iteration number with the :attr:`index` member. If 
	the :attr:`index` is not present in the iterative algorithm object the 
	internal iteration counter of the :class:`PerformanceCollector` is used. 
	
	If iterations are not performed sequentially the *performance* list may 
	contain gaps where no valid *results* structure is found. Such gaps are 
	denoted by ``None``.
	"""
	
	def __init__(self, performanceEvaluator):
		Plugin.__init__(self)
		PerformanceAnnotator.__init__(self, performanceEvaluator)
		
		# Performance evaluator object
		self.performanceEvaluator=performanceEvaluator
		
		# Colletion of performance records
		self.performance=[]
		
		# Local index - used when opt does not impose iteration ordering with an index member
		self.localIndex=0
				
	def __call__(self, x, ft, opt):
		if 'index' in opt.__dict__:
			# Iteration ordering imposed by opt
			index = opt.index 
		else:
			# No iteration ordering
			index = self.localIndex
			self.localIndex += 1
							
		# Check if the index is inside the already allocated space -> if not allocate new space in memory
		while index >= len(self.performance): 
			newelems=len(self.performance)-index+1
			self.performance.extend([None]*newelems)
				
		# write data
		self.performance[index]=self.performanceEvaluator.results
		
	def reset(self):
		"""
		Clears the :attr:`performance` member. 
		"""
		
		self.performance=[]
		
