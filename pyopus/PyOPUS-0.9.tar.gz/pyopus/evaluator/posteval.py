from .. import PyOpusError
from .performance import PerformanceEvaluator
from ..misc.debug import DbgMsgOut

from sys import exc_info
from traceback import format_exception, format_exception_only
import numpy as np

from types import SimpleNamespace

import os, pickle

from pprint import pprint

# files, key = (corner, analysis), analysis None - holds a NoneSimulatorResults object
#   - file name
#
# measures (see performance evaluator), key = measure name
#   - analysis - analysis name or None
#   - expression
#   - vector - boolean
#   - depends - list of measures this measure depends on, ignored when analysis is not None
#
# traces: key = plot name, axes name, trace name
#   - analyses: list of analysis names or empty corresponds to None analysis)
#   - expression
#   - scale

class QPPostEvalError(PyOpusError):
	def __init__(self, message, *args):
		super(QPPostEvalError, self).__init__(message, *args)

class PostEvaluator:
	def __init__(
		self, 
		files, measures={}, traces={}, 
		resultsFolder=None, 
		debug=2
	):
		self.files=files
		self.measures=measures
		self.traces=traces
		self.resultsFolder=resultsFolder
		self.debug=debug
		
		self.componentNames={}
		
		# Scan all file keys, build
		#   - set of available corners for every analysis
		#   - set of available analyses for every corner
		analysis2corners={}
		corner2analyses={}
		corners=set()
		for corner, analysis in self.files.keys():
			if corner not in corner2analyses:
				corner2analyses[corner]=set()
			if analysis not in analysis2corners:
				analysis2corners[analysis]=set()
			corner2analyses[corner].add(analysis)
			analysis2corners[analysis].add(corner)
			corners.add(corner)
		
		self.analysis2corners=analysis2corners
		self.corner2analyses=corner2analyses
		self.corners=corners
	
	def _compile_measures(self):
		# List of analyses that need to be loaded for measure evaluations
		loadAnalyses=set()
		# List of measures that must be evaluated in an analysis
		measuresForAnalysis={}
		# Both of these include None analysis
		for measureName in self.activeMeasures:
			if measureName not in self.measures:
				raise QPPostEvalError("Measure '"+measureName+"' is not defined.")
			
			measure=self.measures[measureName]
			analysis=measure['analysis']
			
			if analysis not in measuresForAnalysis:
				measuresForAnalysis[analysis]=set()
			measuresForAnalysis[analysis].add(measureName)
			
			loadAnalyses.add(analysis)
			
			# Dependent measure
			if analysis is None and 'depends' in measure:
				for depMeasName in measure['depends']:
					depMeas=self.measures[depMeasName]
					depAn=depMeas['analysis']
					if depAn is None:
						raise QPPostEvalError("Dependent measure '"+measureName+"' depends on another dependent measure '"+depMeasName+"'.")
						
					if depAn not in measuresForAnalysis:
						measuresForAnalysis[depAn]=set()
					measuresForAnalysis[depAn].add(depMeasName)
					
					loadAnalyses.add(depAn)
					
		self.loadAnalyses=loadAnalyses
		self.measuresForAnalysis=measuresForAnalysis
		
		# Build list of corner,analysis pairs (excluding None analysis) 
		# that can be loaded for a corner. 
		keysForCorner={}
		# Build a list of keys that can be loaded for None analysis
		keysForNone=set()
		# Build list of measures to compute for keys that can be loaded
		measuresForKey={}
		for key in self.files.keys():
			corner, analysis = key
			
			if analysis is None:
				keysForNone.add(key)
			else:
				if corner not in keysForCorner:
					keysForCorner[corner]=set()
				keysForCorner[corner].add(key)
				
				# Add measures to measuresForKey (for all but None analysis)
				if analysis in loadAnalyses:
					if key not in measuresForKey:
						measuresForKey[key]=set()
					measuresForKey[key].update(measuresForAnalysis[analysis])
		
		# Add dependent measures to measuresForKey if all dependencies are available
		for measureName in self.activeMeasures:
			measure=self.measures[measureName]
			
			if measure['analysis'] is not None:
				continue
			
			# List of analyses on which this measure depends
			depMeas=measure['depends'] if 'depends' in measure else []
			depAn=[ self.measures[dm]['analysis'] for dm in depMeas ]
			
			# Sweep all corners
			for key in keysForNone:
				corner, _ = key
				
				# Check if all dependent analyses are available
				foundAll=True
				for an in depAn:
					if (corner,an) not in keysForCorner[corner]:
						foundAll=False
						break
				
				# If all analyses available, add to list of measures for key
				if foundAll:
					if key not in measuresForKey:
						measuresForKey[key]=set()
					measuresForKey[key].add(measureName)
		
		self.keysForCorner=keysForCorner
		self.keysForNone=keysForNone
		self.measuresForKey=measuresForKey
		
		# Build isScript flags
		self.isScript={}
		for measureName, measure in self.measures.items():
			c, isScript = PerformanceEvaluator.compileMeasure(
				measureName, measure, self.debug
			)
			self.isScript[measureName]=isScript
	
	def loadResults(self, key):
		cornerName, analysis = key
		
		if analysis is None:
			analysis="<>"
		
		fileName=os.path.join(self.resultsFolder, self.files[key])
				
		try:
			with open(fileName, "rb") as f:
				res=pickle.load(f)
		except:
			res=None
		
		if res is not None:
			DbgMsgOut("POST", "Loaded (%s,%s) : %s" % (cornerName, analysis, fileName))
		else:
			DbgMsgOut("POST", "Failed to load (%s,%s) : %s" % (cornerName, analysis, fileName))
				
		return res
		
		
	def evaluateMeasures(self, activeMeasures=None):
		# List of active measures
		self.activeMeasures=activeMeasures
		if self.activeMeasures is None:
			self.activeMeasures=list(self.measures.keys())
		
		# Prepare ordering
		self._compile_measures()
		
		# Measure results storage
		results={}
		
		# Loop through all corners
		for cornerName, keys in self.keysForCorner.items():
			# Loop through all corner,analysis pairs
			for key in keys:
				_, analysis = key
				
				# Skip pairs with None analysis
				if analysis is None:
					continue
				
				# Do we have any measures to evaluate
				if key not in self.measuresForKey or len(self.measuresForKey[key])<=0:
					continue
				
				# Load results
				res=self.loadResults(key)
				
				# Go through all measures for this key
				for measureName in self.measuresForKey[key]:
					measure=self.measures[measureName]
					
					# Prepare measure storage (first evaluation corner)
					if measureName not in results:
						results[measureName]={}
						
					if res is None:
						# Store None for result
						val=None
						DbgMsgOut("POST", "  %s skipped" % (measureName))
					else:
						# Build component names 
						if 'components' in measure and measure['vector'] and measureName not in self.componentNames:
							self.componentNames[measureName]=PerformanceEvaluator.evaluateComponentNames(
								measureName, measure, res.var()
							)
						
						# Prepare environment 
						evalEnvironment=res.evalEnvironment()
						
						# Evaluate
						measureValue=PerformanceEvaluator.evaluateMeasure(
							evalEnvironment, measureName, measure, 
							self.isScript, self.debug
						)
						
						# Are we expecting a vector?
						isVector=bool(measure['vector']) if 'vector' in measure else False
						
						# Postprocess
						val=PerformanceEvaluator._postprocessMeasure(
							measureValue, isVector, self.debug
						)
						
					# Store
					results[measureName][cornerName]=val
		
		# Prepare independent measure results
		indepResults={}
		indepResults.update(results)
		
		# Handle None analysis - loop through all available corners
		for key in self.keysForNone:
			cornerName, _ = key
			
			# Do we have any measures to evaluate
			if key not in self.measuresForKey or len(self.measuresForKey[key])<=0:
				continue
			
			# Load results
			res=self.loadResults(key)
			
			# Go through all measures for this key
			for measureName in self.measuresForKey[key]:
				measure=self.measures[measureName]
				
				# Prepare measure storage (first evaluation corner)
				if measureName not in results:
					results[measureName]={}	
					
				
				if res is None:
					# Store None for result
					val=None
					DbgMsgOut("POST", "  %s skipped" % (measureName))
				else:
					# Build component names 
					if 'components' in measure and measure['vector'] and measureName not in self.componentNames:
						self.componentNames[measureName]=PerformanceEvaluator.evaluateComponentNames(
							measureName, measure, res.var()
						)
					
					# Prepare environment 
					evalEnvironment=res.evalEnvironment()
					
					# Update result member
					allResults={}
					allResults.update(evalEnvironment['result'])
					allResults.update(indepResults)
					evalEnvironment['result']=allResults
					
					# Add corner name
					evalEnvironment['cornerName']=cornerName
					
					# Evaluate
					measureValue=PerformanceEvaluator.evaluateMeasure(
						evalEnvironment, measureName, measure, 
						self.isScript, self.debug
					)
					
					# Are we expecting a vector?
					isVector=bool(measure['vector']) if 'vector' in measure else False
					
					# Postprocess
					val=PerformanceEvaluator._postprocessMeasure(
						measureValue, isVector, self.debug
					)
				
				# Store
				results[measureName][cornerName]=val
					
		self.results=results		
		
	def _compile_traces(self):
		# Build list of traces for every corner-analysis pair
		#   (also include traces computed from None analysis)
		key2trace={}
		# Build list of traces computed from multiple analyses for every corner
		corner2trace={}
		# List of corner-analysis pairs needed for traces
		keysForCorner={}
		for traceKey in self.activeTraces:
			desc=self.traces[traceKey]
			analyses=desc['analyses']
			if len(analyses)==1:
				# Single analysis
				an=analyses[0]
				cset=self.analysis2corners[an] if an in self.analysis2corners else set()
				for c in cset:
					key=(c, an)
					# Add to key2trace
					if key not in key2trace:
						key2trace[key]=[]
					key2trace[key].append(traceKey)
					# Add to keysForCorner
					if c not in keysForCorner:
						keysForCorner[c]=set()
					keysForCorner[c].add(key)
			elif len(analyses)==0:
				# No analysis
				cset=self.analysis2corners[None] if None in self.analysis2corners else set()
				for c in cset:
					key=(c, None)
					# Add to key2trace
					if key not in key2trace:
						key2trace[key]=[]
					key2trace[key].append(traceKey)
					# Add to keysForCorner
					if c not in keysForCorner:
						keysForCorner[c]=set()
					keysForCorner[c].add(key)
			else:
				# More than one analysis, 
				an=analyses[0]
				cset=set()
				if an in self.analysis2corners:
					cset.update(self.analysis2corners[an])
				for an in analyses[1:]:
					if an in self.analysis2corners:
						cset.intersection_update(self.analysis2corners[an])
					else:
						cset=set()
				for c in cset:
					# Add to corner2trace
					if c not in corner2trace:
						corner2trace[c]=[]
					corner2trace[c].append(traceKey)
					# Add all (c, an) pairs to keysForCorner
					for an in analyses:
						key=(c, an)
						if c not in keysForCorner:
							keysForCorner[c]=set()
						keysForCorner[c].add(key)
					
		self.key2trace=key2trace
		self.corner2trace=corner2trace
		self.keysForCorner=keysForCorner
		
		# Build isScript flags
		self.traceIsScript={}
		self.scaleIsScript={}
		for traceKey, desc in self.traces.items():
			traceName="%s:%s:%s" % traceKey
			
			c, isScript = self.compileTrace(
				traceName, desc['expression'], self.debug
			)
			self.traceIsScript[traceKey]=isScript
			
			if desc['scale'] is not None:
				c, isScript = self.compileTrace(
					"scale of "+traceName, desc['scale'], self.debug
				)
				self.scaleIsScript[traceKey]=isScript
	
	@classmethod
	def compileTrace(cls, traceName, expr, debug):
		# Return compiled measure and isScript flag
		
		# Strip leading and trailing whitespace
		s=expr.strip()
		
		# Zero length means an error
		if len(s)<=0:
			raise PyOpusError(DbgMsg("PE", "Trace expression/script '"+traceName+"' has zero length."))
		# Assume it is an expression
		try:
			c=compile(expr, traceName+" expression/script", "eval")
			isScript=False
		except:
			# Failed, try to compile it as a script
			try:
				c=compile(expr, traceName+" expression/script", "exec")
				isScript=True
			except:
				# Report error
				ei=exc_info()
				txt1="Failed to compile trace '"+traceName+"'.\n"
				for line in format_exception(ei[0], ei[1], ei[2]):
					txt1+=line
				DbgMsgOut("PE", txt1) 
				raise PyOpusError(DbgMsg("PE", "Failed to compile trace '"+traceName+"."))
		
		return c, isScript
	
	@classmethod
	def evaluateTrace(cls, evalEnvironment, traceName, expr, isScript, debug, varName='traceScale'):
		tmpLocals={}
		tmpLocals.update(evalEnvironment)
		
		try:
			if isScript:
				exec(expr, globals(), tmpLocals)
				if "__result" in tmpLocals:
					val=tmpLocals['__result']
				elif varName in tmpLocals:
					val=tmpLocals[varName]
				else:
					val=None
			else:
				val=eval(expr, globals(), tmpLocals)
				
			if debug:
				if val is not None:
					DbgMsgOut("POST", "  %s evaluation OK" % traceName)
				
		except KeyboardInterrupt:
			DbgMsgOut("POST", "Keyboard interrupt.")
			raise
		except:
			val=None
			if debug:
				DbgMsgOut("POST", "  %s FAILED" % traceName)
				ei=exc_info()
				if debug>1:
					for line in format_exception(ei[0], ei[1], ei[2]):
						DbgMsgOut("POST", "  "+line) 
				else:
					for line in format_exception_only(ei[0], ei[1]):
						DbgMsgOut("POST", "  "+line)
		
		return val 
	
	@classmethod
	def _postprocessTrace(cls, val, debug):
		if type(val) in [int, float]:
			# int or float
			return np.array([val])
		elif type(val) is np.ndarray:
			# NumPy vector, is it complex? 
			if np.iscomplexobj(val):
				if np.iscomplex(val).any():
					DbgMsgOut("POST", "    Warning. Using real part of complex vector.") 
				return np.real(val)
			else:
				return val
		else:
			DbgMsgOut("POST", "    Bad result type.") 
			return None
	
	def evaluateTraces(self, activeTraces=None):
		# List of active traces
		self.activeTraces=activeTraces
		if self.activeTraces is None:
			self.activeTraces=list(self.traces.keys())
		
		# Prepare ordering
		self._compile_traces()
		
		# Trace vectors and scales
		trcVecs={}
		sclVecs={}
		
		# Go through all corners
		for cornerName, keys in self.keysForCorner.items():
			# Prepare dictionary for accumulated results
			accuRes={}
			
			# Go through all analyses for every corner
			for key in keys:
				_, analysis = key
				
				# Load data
				res=self.loadResults(key)
				
				# If results failed to load
				if res is None:
					# Blank trace and scale
					for traceKey in self.key2trace:
						trcVecs[traceKey]=None
						sclVecs[traceKey]=None
					
					# Skip to next results file
					continue
				
				# Environment from result
				resEnv=res.evalEnvironment()
				
				# Create namespace
				if analysis is not None:
					ns=SimpleNamespace(**resEnv)
				
					# Check if we must accumulate results for this corner
					if cornerName in self.corner2trace:
						accuRes[analysis]=ns
				
				# Go through all traces
				for traceKey in self.key2trace[key] if key in self.key2trace else []:
					desc=self.traces[traceKey]
					traceName="%s:%s:%s" % traceKey
					
					# Store default blank trace and scale
					trcVec=None
					sclVec=None
					
					# Prepare environment 
					evalEnvironment={}
					evalEnvironment.update(resEnv)
					if analysis is not None:
						evalEnvironment[analysis]=ns
						
					# Evaluate expression
					val=self.evaluateTrace(
						evalEnvironment, traceName, desc['expression'], 
						self.traceIsScript[traceKey], 
						self.debug, traceKey[-1]
					)
					
					# Postprocess trace vector
					trcVec=self._postprocessTrace(val, self.debug)
					
					if desc['scale'] is not None:
						# Evaluate scale
						val=self.evaluateTrace(
							evalEnvironment, "scale of "+traceName, 
							desc['scale'], 
							self.scaleIsScript[traceKey], 
							self.debug
						)
						
						# Postprocess scale
						sclVec=self._postprocessTrace(val, self.debug)
					elif 'scale' in resEnv:
						# Extract default scale from results
						val=self.evaluateTrace(
							evalEnvironment, "scale of "+traceName, 
							'scale()', 
							False, 
							self.debug
						)
						
						# Postprocess scale
						sclVec=self._postprocessTrace(val, self.debug)
					else:
						# No scale
						sclVec=None
					
					if sclVec is None:
						DbgMsgOut("POST", "  %s has no defined scale" % (traceName))
					elif trcVec is None:
						pass
					else:
						# At this point trace and scale are both not None
						# This means they are vectors
						
						# Verify compatibility
						sht=trcVec.shape
						shs=sclVec.shape
						if sht!=shs:
							DbgMsgOut("POST", "  %s trace vector does not match scale vector" % (traceName))
						else:
							# Store
							if traceKey not in trcVecs:
								trcVecs[traceKey]={}
								sclVecs[traceKey]={}
							trcVecs[traceKey][cornerName]=trcVec
							sclVecs[traceKey][cornerName]=sclVec
					
			# No results accumulation, skip to next corner
			if cornerName not in self.corner2trace:
				continue 
			
			# Go through all traces that require two or more analyses to evaluate
			for traceKey in self.corner2trace[cornerName]:
				desc=self.traces[traceKey]
				traceName="%s:%s:%s" % traceKey
				
				# Store default blank trace and scale
				trcVec=None
				sclVec=None
				
				# Prepare environment 
				evalEnvironment={}
				evalEnvironment.update(accuRes)
				
				# Add m and numpy
				repAn=list(accuRes.keys())[0]
				evalEnvironment['m']=accuRes[repAn].m
				evalEnvironment['np']=accuRes[repAn].np
				
				# Evaluate expression
				val=self.evaluateTrace(
					evalEnvironment, traceName, desc['expression'], 
					self.traceIsScript[traceKey], 
					self.debug, traceKey[-1]
				)
				
				# Postprocess trace vector
				trcVec=self._postprocessTrace(val, self.debug)
				
				if desc['scale'] is not None:
					# Evaluate scale
					val=self.evaluateTrace(
						evalEnvironment, "scale of "+traceName, 
						desc['scale'], 
						self.scaleIsScript[traceKey], 
						self.debug
					)
					
					# Postprocess scale
					sclVec=self._postprocessTrace(val, self.debug)
				else:
					# No scale
					sclVec=None
				
				if sclVec is None:
					DbgMsgOut("POST", "  %s has no defined scale" % (traceName))
				elif trcVec is None:
					pass
				else:
					# At this point trace and scale are both not None
					# This means they are vectors
					
					# Verify compatibility
					sht=trcVec.shape
					shs=sclVec.shape
					if sht!=shs:
						DbgMsgOut("POST", "  %s trace vector does not match scale vector" % (traceName))
					else:
						# Store
						if traceKey not in trcVecs:
							trcVecs[traceKey]={}
							sclVecs[traceKey]={}
						trcVecs[traceKey][cornerName]=trcVec
						sclVecs[traceKey][cornerName]=sclVec
				
				
			# Delete accumulated results
			accuRes={}
		
		# First index is trace key, second index is corner name
		self.trcVecs=trcVecs
		self.sclVecs=sclVecs
		
