from pyopus.gui.dumptools import getVariables
from pyopus.design.cbd import CornerBasedDesign
from pyopus.evaluator.aggregate import formatParameters
from pyopus.design.sqlite import *
import os, shutil
from pprint import pprint

__all__ = [ 'runCBD' ]

def runCBD(project, task, sqldb):
	# Convert unicode strings to utf-8
	project=project
	task=task
	
	# Pickled results folder
	shutil.rmtree('waveforms.pck', ignore_errors=True)
	os.mkdir('waveforms.pck')	
					
	# Prepare database
	taskEntryId=None
	if sqldb is not None:
		sqldb.reset()
	
		# Write task entry
		taskEntryId=sqldb.commit(SQLiteRecord(
			name=task['name'], payload=SQLDataTask(project, task)
		))
		
	#
	# Prepare data (project part)
	#
	
	# Evaluate variable expressions to get variable values
	variables=getVariables(project['variables'])
	
	# Heads, analyses, and measures
	heads=project['heads']
	analyses=project['analyses']
	measures=project['measures']
	
	#
	# Prepare data (task part)
	#
	corners=task['corners']
	
	# Build design and fixed parameters
	fixedParams={ name: task['parameters'][name]['init'] for name in task['fixedParameterNames']}
	designParams={ name: task['parameters'][name] for name in task['optParameterNames'] }
	
	# Initial parameter values (they are all defined, or dump resulted in an error)
	initialDesignParams={ name: task['parameters'][name]['init'] for name in task['optParameterNames'] }
	
	# Build measures
	activeMeasures=task['requirementNames']
	for name in activeMeasures:
		# Lower bound
		if name in task['requirements']['lower']:
			measures[name]['lower']=task['requirements']['lower'][name]
		
		# Upper bound
		if name in task['requirements']['upper']:
			measures[name]['upper']=task['requirements']['upper'][name]
	
	# Get norms, purge None
	norms={}
	for name in activeMeasures:
		if name in task['requirements']['norm']:
			norms[name]=task['requirements']['norm'][name]
	# No norms defined
	if len(norms)==0:
		norms=None
	
	# Get tradeoffs, purge None 
	tradeoffs={}
	for name in activeMeasures:
		if name in task['requirements']['tradeoff']:
			tradeoff[name]=task['requirements']['tradeoff'][name]*task['settings']['tradeoffmultiplier']
	# Default tradeoff (always a nonnegative number) if no tradeoffs defined
	if len(tradeoffs)==0:
		tradeoffs=task['settings']['tradeoffmultiplier']
	
	# Get settings
	evaluatorSettings=task['settings']['evaluatorsettings']
	aggregatorSettings=task['settings']['aggregatorsettings']
	optimizerSettings=task['settings']['optimizersettings']
	
	# Handle debug overrides
	if task['output']['simulatordebug'] is not None:
		for headName, head in heads.items():
			head['settings']['debug']=task['output']['simulatordebug']
	if task['output']['evaluatordebug'] is not None:
			evaluatorSettings['debug']=task['output']['evaluatordebug']
	if task['output']['aggregatordebug'] is not None:
			aggregatorSettings['debug']=task['output']['aggregatordebug']
	if task['output']['optimizerdebug'] is not None:
			optimizerSettings['debug']=task['output']['optimizerdebug']
			
	# Invoke CBD 
	method=task['settings']['method']
	cbd=CornerBasedDesign(
		paramSpec=designParams, heads=heads, analyses=analyses, measures=measures, 
		corners=corners, fixedParams=fixedParams, variables=variables, 
		norms=norms, 
		failurePenalty=task['settings']['failurepenalty'], 
		tradeoffs=tradeoffs, 
		measureOrder=task['requirementNames'], 
		paramOrder=task['optParameterNames'], 
		cornerOrder=task['cornerNames'], 
		exclude=task['requirements']['exclude'], 
		stopWhenAllSatisfied=task['settings']['stopsatisfied'], 
		initial=initialDesignParams, 
		method='none' if method in ['none', 'noneFull'] else method, 
		fullEvaluation=(method=='noneFull'), 
		forwardSolution=task['settings']['forwardsolution'], 
		incrementalCorners=task['settings']['incrementalcorners'], 
		maxiter=task['settings']['maxiter'], 
		stepScaling=1.0/task['settings']['initialstep'], 
		stepTol=task['settings']['stoptol'], 
		evaluatorOptions=evaluatorSettings, 
		aggregatorOptions=aggregatorSettings, 
		optimizerOptions=optimizerSettings, 
		debug=task['output']['taskdebug'] if task['output']['taskdebug'] is not None else 0, 
		cleanupAfterJob=not task['output']['keepfiles'], 
		sqldb=sqldb, parentId=taskEntryId, 
		saveAll=task['output']['saveallresults'], 
		saveWaveforms=task['output']['savewaveforms'], 
		waveformsFolder="waveforms.pck"
	)
		
	atDesign, aggregator, analysisCount = cbd()
	
