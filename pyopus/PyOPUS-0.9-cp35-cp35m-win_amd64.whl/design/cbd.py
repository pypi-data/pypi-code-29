"""
.. inheritance-diagram:: pyopus.design.cbd
    :parts: 1

**Corners-based design (PyOPUS subsystem name: CBD)**

Finds the circuit parameters for which the performances satisfy the 
requirements across all specified corners. 
""" 

from ..optimizer import optimizerClass
from ..optimizer.base import Reporter, Annotator
from ..misc.debug import DbgMsgOut, DbgMsg
from ..evaluator.performance import PerformanceEvaluator, updateAnalysisCount
from ..evaluator.aggregate import *
from ..evaluator.auxfunc import listParamDesc, paramDict, paramList, dictParamDesc
from .sqlite import *

import sys
import time
import numpy as np
import itertools
from copy import deepcopy

__all__ = [ 'generateCorners', 'CornerBasedDesign' ] 

class AnCountAnnotator(Annotator):
	"""
	Transfers analysis counts from remote tasks to local tasks. 
	"""
	def __init__(self, pe):
		self.pe=pe
	
	def produce(self):
		return self.pe.analysisCount
	
	def consume(self, annotation):
		self.pe.analysisCount=annotation
		
def generateCorners(specs, heads, prefix='c', enumStart=1):
	"""
	Generates corners reflecting all combinations of parameter ranges 
	given by *paramSpec* and device models given by *modelSpec*. 
	
	Returns a tuple (*corners*, *cornerNames*) where *corners* is a 
	dictionary holding corners with corner name for key and 
	*cornerNames* is a list of corner names in the order in which 
	the corners were generated. 
	
	*specs* is a list of model/parameter specifications. Every specifications 
	is a tuple/list holding 3 or 4 elements. The elements are 
	
	  * 'model' or 'param' specifying if this entry is a list of modules 
	    describing a model or a list of parameter values. 
	    
	  * A name of a model or parameter.
	
	  * A list of module names or parameter values. 
	
	  * A list of aliases used for constructing the corner names. 
	    ``None`` indicates the module name/parameter value has no alias. 
	    If this list is omitted no aliases are defined for this specification. 
	
	*heads* is a list of head names to which the generated corners apply. 
	
	*prefix* is the strin prefix for the names of the generated corners. 
	
	*enumStart* is the number of the first generated corner. If this value 
	is set to ``None`` the corners are not enumerated. Note that this 
	results in duplicate corner names if some parameter value/module lacks 
	an alias. Duplicate corner names must be detected by the user by inspecting 
	the *cornerNames* list. 
	
	A corner name is constructed as <prefix><number>_<alias>_<alias>_... 
	with first corner numbered *enumStart*. 
	
	Example::
	
	  corners=generateCorners(
	    specs=[
	      (
	        'model', 'mos', 
	        ['tm', 'wp', 'ws', 'wo', 'wz'], 
	        ['tm', 'wp', 'ws', 'wo', 'wz']
	      ), 
	      (
	        'model', 'bipolar', 
	        ['weak', 'strong'], 
	        ['w', 's']
	      ), 
	      (
	        'param', 'vdd', 
	        [1.6, 1.8, 2.0], 
	        ['vl', None, 'vh']
	      ), 
	      (
	        'param', 'temperature', 
	        [0.0, 25, 100.0], 
	        ['tl', None, 'th']
	      )
	    ], 
	    heads=['opus'], 
	    prefix='cor', 
	    enumStart=1
	  )
	  
	  # Corners is a dictionary with cc<number> as key and 
	  # corner description as value. The above statement
	  # results in 3*3*5*2=90 corners named c1..-c90.. representing 
	  # the cartesian product of possible mos and bipolar transistor 
	  # models, and vdd and temperature values. 
	  # Every corner is suffixed by _tm, _wp, _ws, _wo, _wz depending 
	  # on the mos model, _w, _s depending on the bipolar model, 
	  # _vl or _vh depending on the vdd value, and _tl, _th depending 
	  # on the temperature value. 
	  # These corners can be passed directly to a PerformanceEvaluator
	  # object. 
	"""
	indices=[ range(len(spec[2])) for spec in specs ]
	
	nameList=[]
	cornerDict={}
	ii=enumStart
	for ilist in itertools.product(*indices):
		ilist=list(ilist)
		name=prefix
		if ii is not None:
			name+=str(ii)
			ii+=1
		
		corner={
			'modules': [], 
			'params': {}, 
			'heads': deepcopy(heads)
		}
		
		for spec in specs:
			stype=spec[0]
			sname=spec[1]
			svals=spec[2]
			
			ndx=ilist.pop(0)
			
			# Add value
			if stype=='model':
				corner['modules'].append(svals[ndx])
			else:
				corner['params'][sname]=svals[ndx]
			
			# Attach alias
			if len(spec)>3:
				alias=spec[3][ndx]
				if alias is not None:
					name+="_"+alias
		
		nameList.append(name)
		cornerDict[name]=corner
	
	return cornerDict, nameList
	
class OptReporter(Reporter):
	def __init__(self, aggregator, saveAll=False):
		Reporter.__init__(self)
		self.aggregator=aggregator
		self.saveAll=saveAll
		
	def reset(self):
		Reporter.reset(self)
		
	def __call__(self, x, ft, opt):
		if (self.saveAll or opt.niter==opt.bestIter) and not self.quiet:
			DbgMsgOut("CBD", "iter %d, f=%e" % (opt.niter, opt.f))
			DbgMsgOut("CBD", formatParameters(paramDict(x, self.aggregator.inputOrder), self.aggregator.inputOrder))
			DbgMsgOut("CBD", self.aggregator.formatResults())

def SQLwaveformDump(sqldb, recordId, pe, folder):
	# Collect waveforms in waveforms folder
	# print("Started recid=", recordId)
	files=pe.collectResultFiles(destination=folder, prefix=str(recordId)+"_", move=True)
	
	# Write to database
	for (corner, analysis), fileName in files.items():
		sqldb.commitWaveform(recordId, corner, analysis, fileName)
	# print("Done")
	
class SQLDumper(Reporter):
	def __init__(self, aggregator, evaluator, sqldb, parentId=None, saveAll=False, waveformsFolder="."):
		Reporter.__init__(self)
		self.aggregator=aggregator
		self.evaluator=evaluator
		self.sqldb=sqldb
		self.parentId=parentId
		self.saveAll=saveAll
		self.waveformsFolder=waveformsFolder
		
	def reset(self):
		Reporter.reset(self)
		
	def __call__(self, x, ft, opt):
		if (self.saveAll or opt.niter==opt.bestIter) and not self.quiet:
			recId=self.sqldb.commit(SQLiteRecord(
				name="Iteration %d" % opt.niter, 
				payload=SQLDataOptIter(
					self.evaluator.inputParams, 
					self.aggregator.results, 
					self.evaluator.results, 
					self.evaluator.componentNames, 
					None
				), 
				parent=self.parentId
			))
			if self.evaluator.storeResults:
				# If we are storing results, we consume them
				# print("Collecting", opt.niter)
				SQLwaveformDump(self.sqldb, recId, self.evaluator, self.waveformsFolder)
		else:
			if self.evaluator.storeResults:
				# If we are storing results we should delete them now
				# Only results corresponding to database entries are stored
				self.evaluator.deleteResultFiles()
	
	
class CornerBasedDesign(object):
	"""
	*paramSpec* is the design parameter specification dictionary 
	with ``lo`` and ``hi`` members specifying the lower and the 
	upper bounds. 
	
	See :class:`~pyopus.evaluator.performance.PerformanceEvaluator` 
	for details on *heads*, *analyses*, *measures*, *corners*, and 
	*variables*. 
	
	Fixed parameters are given by *fixedParams* - a dictionary 
	with parameter name for key and parameter value for value. 
	Alternatively the value can be a dictionary in which case the 
	``init`` member specifies the parameter value. 
	
	If *fixedParams* is a list the members of this list must be 
	dictionaries describing parameters. The set of fixed parameters 
	is obtained by merging the information from these dictionaries. 
	
	The performance constraints are specified as the ``lower`` and 
	the ``upper`` member of the measurement description disctionary. 
	
	*norms* is a dictionary specifying the norms for the 
	performance measures. Every norm is by default equal to the 
	largest absolute specification (lower, upper). If this 
	results in zero 1.0 is used as the norm. *norms* overrides this 
	default. Norms are used in the construction of the 
	:class:`~pyopus.evaluator.aggregate.Aggregator` object. 
	
	*failurePenalty* is the penalty assigned to a failed performance 
	measure. It is used in the construction of the 
	:class:`~pyopus.evaluator.aggregate.Aggregator` object used 
	by the optimization algorithm. 
	
	*tradeoffs* can be a number or a dictionary. It defines the 
	values of the tradeoff weights for the 
	:class:`~pyopus.evaluator.aggregate.Aggregator` object used by 
	the optimization algorithm. By default all tradeoff weights 
	are 0.0. A number specifies the same tradeoff weight for all 
	performance measures. To specify tradeoff weights for individual 
	performance measures, use a dictionay. If a performance measure 
	is not specified in the dictionary 0.0 is used. 
	
	If *exclude* is given it contains the list of names of measures 
	that will not produce contributions to the aggregate cost function. 
	These measures will still be compared with their respective goals 
	and included in the aggregate cost function definition. 
	
	Setting *stopWhenAllSatisfied* to ``True`` makes the optimizer 
	stop as soon as all design requirements (i.e. performance 
	constraints) are satisfied. Setting it to ``False`` makes the 
	algorithm stop when its stopping condition is satisfied. 
	When set to ``None`` the behavior depends on the value of 
	the *tradeoffs* parameter. If it is set to 0, the optimizer 
	stops when all design requirements are satisfied. Otherwise 
	the behavior is the same as for ``False``. 
	
	*initial* is the dictionary specifying the initial point for 
	the optimizer. If not given, the initial point is equal to 
	the mean of the lower and the upper bound. 
	
	*method* can be ``local``, ``global``, or any other supported 
	optimization algorith (currently QPMADS, BoxComplex, ParallelSADE,
	and DifferentialEvolution) and specifies the type of optimization 
	algorithm to use. Setting it to ``'none'`` skips optimization and 
	only performs an initial circuit evaluation. 
	Currently the local method is QPMADS and the global method is 
	ParallelSADE. 
	
	If *fullEvaluation* is set to ```True`` the verification step 
	performs all analyses in all corners. See the *fullEvaluation* 
	option of the :class:`PerformanceEvaluator` class. 
	
	If *forwardSolution* is ``True`` the solution of previous 
	pass is used as the initial point for the next pass. 
	
	If *incrementalCorners* is ``False`` the design is optimized 
	for the complete set of corners in a single optimization run. 
	When set to ``True`` the set of relevant corners is built 
	gradually with multiple optimization runs (which is much faster 
	for designs with many corners). 
	
	*maxiter* is the maximal number of circuit optimizations per 
	optimization run. 
	
	*stepTol* is the step size at which the local optimizer is 
	stopped. 
	
	The difference between the upper and the lower bound an a 
	parameter is divided by *stepScaling* to produce the initial 
	step length for the local optimizer. 
	
	*evaluatorOptions* specifies the option overrides for the 
	:class:`~pyopus.evaluator.performance.PerformanceEvaluator` 
	object. 
	
	*aggregatorOptions* specifies the option overrides for the 
	:class:`~pyopus.evaluator.aggregate.Aggregator` object. 
	
	*optimizerOptions* specifies the option overrides for the 
	optimizer. 
	
	*paramOrder* is a list of parameter names in which the parameters 
	will be ordered when printed in debug messages. 
	
	*measureOrder* is a list of measure names in which the measures 
	will be ordered when printed in debug messages. 
	
	Setting *cleanupAfterJob* to ``False`` leaves the intermediate 
	files on the disk after a run is finished. 
	
	Setting *spawnerLevel* to a value not greater than 1 distributes 
	the full corner evaluation across available computing nodes. 
	It is also passed to the optimization algorithm, if the algorithm 
	supports this parameter. 
	
	*sqldb* is the SQLiteDatabase object for writing the results. 
	
	If *saveAll* is set to ``True`` results of every optimization 
	iteration are stored in the results database (if *sqldb* is given) 
	and printed in the debug output. 
	
	When *sqldb* is specified the results generated by the simulator 
	can be saved for later inspection. Setting *saveWaveforms* to 
	``verification`` saves them as pickled result files for every 
	verification across corners. Setting it to ``always`` saves them 
	for every result that is stored in the database. Setting it to 
	``never`` disables saving pickled result files. 
	
	*parentId* is the sqlite record id of the parent. If ``None`` the 
	parent is the root database entry. 
	
	This is a callable object with no arguments. The return value 
	is a tuple comprising a dictionary with the final values of the 
	design parameters, the :class:`~pyopus.evaluator.aggregate.Aggregator` 
	object used for evaluating the final result across all corners, 
	and the *analysisCount* dictionary. 
	
	Objects of this type store the number of analyses performed 
	during the last call to the object in the *analysisCount* 
	member. 
	"""
		
	def __init__(
		self, paramSpec, heads, analyses, measures, corners=None, 
		fixedParams={}, variables={}, 
		norms=None, failurePenalty=1e6, tradeoffs=0.0, exclude=None, 
		stopWhenAllSatisfied=None, 
		initial=None, method='local', fullEvaluation=False, forwardSolution=True, 
		incrementalCorners=True, maxiter=None, 
		stepTol=0.001, stepScaling=4.0, 
		evaluatorOptions={}, aggregatorOptions={}, optimizerOptions={}, 
		paramOrder=None, measureOrder=None, cornerOrder=None, 
		debug=0, cleanupAfterJob=True, spawnerLevel=1, 
		sqldb=None, saveAll=False, saveWaveforms="never", 
		waveformsFolder="waveforms.pck", 
		parentId=None
	):
		self.heads=heads
		self.analyses=analyses
		self.measures=measures
		self.corners=corners
		self.variables=variables
		self.norms=norms
		self.failurePenalty=failurePenalty
		self.tradeoffs=tradeoffs
		self.exclude=exclude
		self.stopWhenAllSatisfied=stopWhenAllSatisfied
		self.paramSpec=paramSpec
		self.initial=initial
		self.method=method
		self.fullEvaluation=fullEvaluation
		self.forwardSolution=forwardSolution
		self.incrementalCorners=incrementalCorners
		self.debug=debug
		self.evaluatorOptions=evaluatorOptions
		self.aggregatorOptions=aggregatorOptions
		self.optimizerOptions=optimizerOptions
		self.maxiter=maxiter
		self.stepTol=stepTol
		self.stepScaling=stepScaling
		self.cleanupAfterJob=cleanupAfterJob
		self.spawnerLevel=spawnerLevel
		self.paramOrder=paramOrder
		self.measureOrder=measureOrder
		self.cornerOrder=cornerOrder
		self.saveAll=saveAll
		self.saveWaveforms=saveWaveforms
		self.waveformsFolder=waveformsFolder
		self.sqldb=sqldb
		self.parentId=parentId
		
		# Process fixed parameters
		self.fixedParams={}
		if fixedParams is not None:
			if type(fixedParams) is list or type(fixedParams) is tuple:
				lst=fixedParams
			else:
				lst=[fixedParams]
			for entry in lst:
				nameList=list(entry.keys())
				if len(nameList)>0 and type(entry[nameList[0]]) is dict:
					# Extract init
					self.fixedParams.update(
						paramDict(
							listParamDesc(entry, nameList, 'init'), 
							nameList
						)
					)
				else:
					self.fixedParams.update(entry)
		
		# Parameter names and counts
		if self.paramOrder is not None:
			self.paramNames=self.paramOrder
		else:
			self.paramNames=list(self.paramSpec.keys())
			self.paramNames.sort()
		self.nParam=len(self.paramNames)
		
		# Parameter ranges
		self.paramLo=np.array(listParamDesc(self.paramSpec, self.paramNames, "lo"))
		self.paramHi=np.array(listParamDesc(self.paramSpec, self.paramNames, "hi"))
		
		# Initial values
		if initial is None:
			self.paramInit=(self.paramLo+self.paramHi)/2
		else:
			self.paramInit=np.array(paramList(initial, self.paramNames))
	
	def __call__(self):
		# Start timing 
		startTime=time.time()
		
		# Aggregator
		aggDef=[]
		
		# Evaluate measures that are listed in measureOrder
		# If measureOrder is not given, evaluate all measures
		if self.measureOrder is not None:
			measureNames=self.measureOrder
		else:
			measureNames=list(self.measures.keys())
			measureNames.sort()
		
		for measureName in measureNames:
			measure=self.measures[measureName]
			
			# Compute norm
			if self.norms is not None and measureName in self.norms:
				# Norm given
				norm=self.norms[measureName]
			else:
				# Norm not given, use max(abs(lo), abs(hi))
				vall=[]
				if 'lower' in measure:
					vall.append(np.abs(measure['lower']))
				if 'upper' in measure:
					vall.append(np.abs(measure['upper']))
				if len(vall)<1:
					norm=1.0
				else:
					norm=max(vall)
					norm=1.0 if norm==0.0 else norm
			
			# Generate entries in aggregator definition
			if 'lower' in measure:
				if type(self.tradeoffs) is dict:
					# Dictionary of tradeoffs
					tradeoff=self.tradeoffs[measureName] if measureName in self.tradeoffs else 0.0
				else:
					# One tradeoff for all
					tradeoff=self.tradeoffs
				entry={
					'measure': measureName, 
					'norm': Nabove(measure['lower'], norm, self.failurePenalty), 
					'shape': Slinear2(1.0, tradeoff), 
					'reduce': Rworst() if self.exclude is None or measureName not in self.exclude else Rexcluded()
				}
				aggDef.append(entry)
			if 'upper' in measure:
				if type(self.tradeoffs) is dict:
					# Dictionary of tradeoffs
					tradeoff=self.tradeoffs[measureName] if measureName in self.tradeoffs else 0.0
				else:
					# One tradeoff for all
					tradeoff=self.tradeoffs
				entry={
					'measure': measureName, 
					'norm': Nbelow(measure['upper'], norm, self.failurePenalty), 
					'shape': Slinear2(1.0, tradeoff), 
					'reduce': Rworst() if self.exclude is None or measureName not in self.exclude else Rexcluded()
				}
				aggDef.append(entry)
			if 'lower' not in measure and 'upper' not in measure:
				# No requirements, exclude from cost function
				pass
		
		if self.sqldb is not None:
			cbdId=self.sqldb.commit(SQLiteRecord(
				name="Aggregator setup", 
				payload=SQLDataTaskCBD(
					aggDef, 
				), 
				parent=self.parentId
			))
		
		# Evaluator
		fullPe=PerformanceEvaluator(
			self.heads, self.analyses, self.measures, self.corners, 
			self.fixedParams, self.variables, activeMeasures=measureNames, 
			cornerOrder=self.cornerOrder, fullEvaluation=self.fullEvaluation, 
			spawnerLevel=self.spawnerLevel, 
			storeResults=(self.saveWaveforms in ["verification", "always"]), 
			resultsFolder=None, # Store in system TEMP
			resultsPrefix="pyopus_tmp_result_", 
			cleanupAfterJob=self.cleanupAfterJob, 
			**self.evaluatorOptions
		)
		pe=None
		
		fullAgg=Aggregator(fullPe, aggDef, self.paramNames, **self.aggregatorOptions)
		
		# Initial parameters, step size
		atParam=self.paramInit.copy()
		lastStep=1.0
		
		# Prepare a copy of measures
		measures=deepcopy(self.measures)
		
		# Set up empty corner lists if incrementalCorners is enabled
		if self.incrementalCorners:
			for measureName, measure in measures.items():
				measure['corners']=[]
			
		# Set up analysis counters
		self.analysisCount={}
		
		atPass=1
		while True:
			# List of added worst corners when corners are built incrementally
			addedCornerList={ mName: [] for mName in measures.keys() }
			
			# We need a full evaluation if
			# - we build the relevant corners list incrementally (incrementalCorners=True)
			# - this is the beginning of the second pass with incrementalCorners=False
			#   (just before we exit we need a full evaluation)
			if (
				self.incrementalCorners or
				(not self.incrementalCorners and atPass==2)
			):
				# Evaluate all corners at current point
				if self.debug:
					if self.incrementalCorners:
						DbgMsgOut("CBD", "Pass %d, full corner evaluation" % atPass)
					else:
						DbgMsgOut("CBD", "Final result evaluation")
				
				# Evaluate all corners
				fullAgg(atParam)
				
				# Dump to sql 
				if self.sqldb is not None:
					passId=self.sqldb.commit(SQLiteRecord(
						name="Pass %d verification" % atPass, 
						payload=SQLDataOptIter(
							fullPe.inputParams, 
							fullAgg.results, 
							fullPe.results, 
							fullPe.componentNames, 
							None
						), 
						parent=self.parentId
					))
					if fullPe.storeResults:
						# If verification waveforms are stored, we consume them (move them to waveforms folder)
						SQLwaveformDump(
							self.sqldb, 
							passId, 
							fullPe, 
							self.waveformsFolder
						)
				
				# Colect results
				res=fullAgg.results
				
				# Update analysis counts
				updateAnalysisCount(self.analysisCount, fullPe.analysisCount)
				
				if self.debug:
					if self.incrementalCorners:
						DbgMsgOut("CBD", "Pass %d, corner summary" % atPass)
					else:
						DbgMsgOut("CBD", "Result summary")
					DbgMsgOut("CBD", fullAgg.formatResults())
				
				# Stop if user wants no optimization
				if self.method=='none':
					break
				
				# Stop if this is pass 2 with incrementalCorners=False
				if not self.incrementalCorners and atPass==2:
					break
				
				# Get worst corners, update measures
				if self.debug:
					DbgMsgOut("CBD", "Pass %d, updating corner lists" % atPass)
				
				cornerAdded=False
				for ii in range(len(aggDef)):
					component=aggDef[ii]
					measureName=component['measure']
					measure=measures[measureName]
					# No tradeoffs, performance measure satisfies goal, and it has at least one corner listed
					if self.tradeoffs==0.0 and res[ii]['contribution']<=0.0 and len(measure['corners'])>0:
						# Skip this performance measure
						continue
					
					# Add a corner for this performance measure
					# First check if this measure was successfully evaluated across all corners 
					if res[ii]['worst'] is None:
						# The worst value is None, measure failed to evaluate in at least one corner
						# worst_corner is an array of corners where the measure failed to evaluate
						# Corners where we failed to evaluate the measure are stored as 1-D worst_corner_vector
						# The first corner where we failed to evaluate the measure is stored as worst_corner
						worstCorner=fullAgg.cornerList[res[ii]['worst_corner']]
					else:
						# Measure was evaluated in all corners
						# For scalar measures worst_corner_vector is a scalar 
						# For vector measures worst_corner__vector is a n-D vector holding the worst corner for every component of vector measure
						# The worst corner across all components is stored in worst_corner
						worstCorner=fullAgg.cornerList[res[ii]['worst_corner']]
						
					worstCorner=fullAgg.cornerList[res[ii]['worst_corner']]
					if 'corners' not in measure:
						measure['corners']=[]
					if worstCorner not in measure['corners']:
						measure['corners'].append(worstCorner)
						addedCornerList[measureName].append(worstCorner)
						cornerAdded=True
					if self.debug:
						DbgMsgOut("CBD", "  %s: %s" % (measureName, str(measure['corners'])))
					# Add a corner to all dependencies
					if 'depends' in measure and measure['analysis'] is None:
						for depName in measure['depends']:
							dep=measures[depName]
							if 'corners' not in dep:
								dep['corners']=[]
							if worstCorner not in dep['corners']:
								dep['corners'].append(worstCorner)
								addedCornerList[depName].append(worstCorner)
								cornerAdded=True
							if self.debug:
								DbgMsgOut("CBD", "  dep %s: %s" % (depName, str(dep['corners'])))
				
				# If no corner added, we are done
				if not cornerAdded:
					if self.debug:
						DbgMsgOut("CBD", "Corners unchanged, stopping")
					break
			
			if self.sqldb is not None:
				# Prepare lists of corners for all measures
				measureCorners={}
				for mName in measures.keys():
					if 'corners' in measures[mName]:
						# Measure corners are specified
						measureCorners[mName]=measures[mName]['corners']
					else:
						# No corners specified for measure, use all
						measureCorners[mName]=list(self.corners.keys())
				
				# Write to database
				optId=self.sqldb.commit(SQLiteRecord(
					name="Pass %d optimization" % atPass, 
					payload=SQLDataCorners(measureCorners, addedCornerList), 
					parent=self.parentId
				))
			
			if self.incrementalCorners:
				if self.debug:
					DbgMsgOut("CBD", "Pass %d, optimization" % atPass)
			else:
				if self.debug:
					DbgMsgOut("CBD", "Designing with full set of corners in one pass.")
				
			# Construct new evaluator and aggregator
			pe=PerformanceEvaluator(
				self.heads, self.analyses, measures, self.corners, 
				self.fixedParams, self.variables, activeMeasures=measureNames, 
				cornerOrder=self.cornerOrder, 
				storeResults=(self.saveWaveforms=="always"), 
				resultsFolder=None, # Store in system TEMP
				resultsPrefix="pyopus_tmp_result_", 
				cleanupAfterJob=self.cleanupAfterJob, 
				**self.evaluatorOptions
			)
			agg=Aggregator(pe, aggDef, self.paramNames, **self.aggregatorOptions)
			
			# Prepare optimizer
			if self.method in ['local', 'QPMADS']:
				scale=(self.paramHi-self.paramLo)/self.stepScaling
				optimizerDefaults={
					#'stepBase': 8.0, 'meshBase': 32.0, 'initialMeshDensity': 32.0, 
					#'maxStep': 1.0, 'stopStep': 0.01, 
					'startStep': lastStep, 
					'stepBase': 4.0, 'meshBase': 16.0, 'initialMeshDensity': 2.0*20, # 16384.0,
					'maxStep': 1.0, 
					'protoset': 2, # minimal=0, maximal=1
					'unifmat': 5, # 5 = nxn Sobol
					'generator': 2, # UniMADS
					'rounding': 0, 'modelOrdering': True, 'lastDirectionOrdering': True, 
					'roundOnFinestMeshEntry': True, 
					'speculativePollSearch': True, 'speculativeModelSearch': False, 
					'model': True, 
					'HinitialDiag': 0.0, 
					'boundSnap': True, 'boundSlide': True, 
					'qpFeasibilityRestoration': False, 
					'stepCutAffectsUpdate': True, 'speculativeStepAffectsUpdate': True, 
					'rho':16, 'rhoNeg': 1.0, 
					'linearUpdate': True, 'simplicalUpdate': True, 'powellUpdate': False, 
					'boundStepMirroring': False, 
					'linearUpdateExtend': False, 
					'forceRegression': True, 
					'scaling': scale, 
					# 'debug': 2, 
					'hmax': 100.0, 
					'cache': True, 
				}
				optimizerDefaults.update(self.optimizerOptions)
				optimizerDefaults.update({
					'maxiter': self.maxiter, 
					'stopStep': self.stepTol,
				})
				opt=optimizerClass("QPMADS")(
					agg, self.paramLo, self.paramHi, 
					**optimizerDefaults
				)
			elif self.method in [ 'BoxComplex' ]: 
				optimizerDefaults={}
				optimizerDefaults.update(self.optimizerOptions)
				optimizerDefaults.update({
					'maxiter': self.maxiter, 
					'gamma_stop': self.stepTol, 
					'initial_box': 1.0/self.stepScaling, 
				})
				opt=optimizerClass("BoxComplex")(
					agg, self.paramLo, self.paramHi, 
					**optimizerDefaults
				)
			elif self.method in [ 'HookeJeeves' ]: 
				scale=(self.paramHi-self.paramLo)/self.stepScaling
				optimizerDefaults={}
				optimizerDefaults.update(self.optimizerOptions)
				optimizerDefaults.update({
					'maxiter': self.maxiter, 
					'minstep': self.stepTol, 
					'step0': scale, 
				})
				opt=optimizerClass("HookeJeeves")(
					agg, self.paramLo, self.paramHi, 
					**optimizerDefaults
				)
			elif self.method in [ 'DifferentialEvolution' ]: 
				optimizerDefaults={}
				optimizerDefaults.update(self.optimizerOptions)
				# stepTol not used by DE
				# stepScaling not used by DE
				optimizerDefaults.update({
					'maxiter': self.maxiter, 
				})
				opt=optimizerClass("DifferentialEvolution")(
					agg, self.paramLo, self.paramHi, 
					spawnerLevel=self.spawnerLevel, 
					**optimizerDefaults
				)
			else:
				optimizerDefaults={}
				optimizerDefaults.update(self.optimizerOptions)
				# stepTol not used by PSADE
				# stepScaling not used by PSADE
				optimizerDefaults.update({
					'maxiter': self.maxiter, 
				})
				opt=optimizerClass("ParallelSADE")(
					agg, self.paramLo, self.paramHi, 
					spawnerLevel=self.spawnerLevel, 
					**optimizerDefaults
				)
			
			# Install aggregator annotator (for parallel optimization algorithms)
			opt.installPlugin(agg.getAnnotator())
			
			# Install evaluator annotator
			opt.installPlugin(pe.getAnnotator())
			
			# Install reporter 
			if self.debug:
				opt.installPlugin(OptReporter(agg, saveAll=self.saveAll))
			
			if self.sqldb is not None:
				opt.installPlugin(
					SQLDumper(agg, pe, self.sqldb, optId, saveAll=self.saveAll, waveformsFolder=self.waveformsFolder)
				)
			
			# Install annotator for sending analysis count to the spawning host
			opt.installPlugin(AnCountAnnotator(pe))
			
			# Stop as soon as 0 is found if no tradeoffs are required
			if (
				(self.stopWhenAllSatisfied is None and self.tradeoffs==0.0) or 
				self.stopWhenAllSatisfied is True
			):
				opt.installPlugin(agg.getStopWhenAllSatisfied())
			
			# Set initial point
			if self.forwardSolution:
				opt.reset(atParam)
			else:
				opt.reset(self.paramInit)
			
			# Run
			opt.run()
			
			# Collect result
			atParam=opt.x
			
			# Update analysis counts
			updateAnalysisCount(self.analysisCount, pe.analysisCount, opt.niter)
			
			atPass+=1
			
		# Clean up
		if self.cleanupAfterJob:
			fullPe.finalize()
			if pe is not None:
				pe.finalize()
			
		# Convert parameters to dictionary
		self.atParam=paramDict(atParam, self.paramNames)
		self.passes=atPass-1
		
		if self.debug:
			DbgMsgOut("CBD", "Analysis count: %s" % str(self.analysisCount))
			DbgMsgOut("CBD", "Result:")
			DbgMsgOut("CBD", formatParameters(self.atParam, self.paramNames))
			DbgMsgOut("CBD", fullAgg.formatResults())
		
		if self.sqldb is not None:
			# Write conclusion
			self.sqldb.commit(SQLiteRecord(
				name="Task summary", 
				payload=SQLDataConclusion(self.analysisCount, time.time()-startTime), 
				parent=self.parentId
			))
	
		# Return fullAgg regardless of incrementalCorners
		# because the final result is always evaluated with fullAgg
		return (self.atParam, fullAgg, self.analysisCount)
	

if __name__=='__main__':
	corners, names = generateCorners(
		specs=[
			(
			'model', 'mos', 
			['tm', 'wp', 'ws', 'wo', 'wz'], 
			[None, 'wp', 'ws', 'wo', 'wz']
			), 
			(
			'model', 'bipolar', 
			['weak', 'strong'], 
			['w', 's']
			), 
			(
			'param', 'vdd', 
			[1.6, 1.8, 2.0], 
			['vl', None, 'vh']
			), 
			(
			'param', 'temperature', 
			[0.0, 25, 100.0], 
			['tl', None, 'th']
			)
		], 
		heads=['opus'], 
		prefix='cor', 
		enumStart=1
	)
		
	print(names)
	from pprint import pprint
	pprint(corners)
