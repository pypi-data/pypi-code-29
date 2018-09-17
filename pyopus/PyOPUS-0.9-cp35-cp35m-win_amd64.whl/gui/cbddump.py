from .dumptools import QPDumpError, processParams, getVariables, formatNameList, readNumeric
from .dumptools import validateLowercaseIdentifier

__all__ = [ 'dumpCBD' ]

# TODO: detect empty tasks

def dumpCorners(description, task, localsDict={}):
	names=[]
	nameIndices={}
	
	if len(task[1]['corners'])<=0:
		raise QPDumpError("No corner defined.")
	
	cornersDict={}
	for ii in range(len(task[1]['corners'])):
		c=task[1]['corners'][ii]
		name=c[0]
		
		# Map from head name to set of names of defined modules
		modulesMap={ h[0]: set([m[0] for m in h[1]['moddefs'] ]) for h in description['heads'] }
		
		try:
			if name in nameIndices:
				jj=nameIndices[name]
				raise QPDumpError("Corner name is not unique. First appearance is in row "+str(jj+1)+".")
			
			names.append(name)
			nameIndices[name]=ii
			
			# Check if corner name contains uppercase letters
			if not validateLowercaseIdentifier(name):
				raise QPDumpError("Corner name '"+name+"' in row "+str(ii+1)+" is not a lowercase identifier.")
			
			cdict={}
			
			# Check all modules across all heads listed for this corner
			for mr in c[1]['modules']:
				modName=mr[0].strip()
				found=False
				for h in c[1]['heads']:
					hName=h[0].strip()
					if modName in modulesMap[hName]:
						found=True
						break
					
				if not found:
					raise QPDumpError("Input module '"+modName+"' is not defined in any of the simulator setups specified for corner '"+name+"'.")
			
			# Dump heads
			cdict['heads']=[h[0].strip() for h in c[1]['heads']]
			
			# Dump modules
			cdict['modules']=[m[0].strip() for m in c[1]['modules']]
			
			# Dump params
			pdict, _ = processParams(c[1]['params'], "Parameter", localsDict)
			cdict['params']=pdict
			
			cornersDict[name]=cdict
			
		except QPDumpError as e:
			raise QPDumpError("In definition of corner '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
		
	return cornersDict, names
	
def dumpRequirements(description, task, localsDict={}):
	# Build corner sets for all heads, blank for now
	cornersForHead={ h[0].strip(): [] for h in description['heads']}
	# All corners defined in this task
	allCorners=set([])
	for c in task[1]['corners']:
		cname=c[0].strip()
		allCorners.add(cname)
		for h in c[1]['heads']:
			hname=h[0].strip()
			if hname not in cornersForHead:
				raise QPDumpError("Simulator setup '"+hname+"' referenced by corner '"+cname+"' is not defined.")
			cornersForHead[hname].append(cname)
	for h in cornersForHead.keys():
		cornersForHead[h]=set(cornersForHead[h])
	
	# Build measureName to index map 
	m2index={}
	for ii in range(len(description['measures'])):
		m2index[description['measures'][ii][0].strip()]=ii
	
	# Build analysisName to index map 
	a2index={}
	for ii in range(len(description['analyses'])):
		a2index[description['analyses'][ii][0].strip()]=ii
	
	# Verify if measures exist in project setup, check for duplicates
	names=[]
	nameIndices={}
	for ii in range(len(task[1]['requirements'])):
		mr=task[1]['requirements'][ii]
		name=mr[1].strip()
		
		if name in nameIndices:
			jj=nameIndices[name]
			raise QPDumpError("Requirement '"+name+"' from row "+str(ii+1)+" appears twice. \nFirst apeparance is in row "+str(jj+1)+".")
		
		nameIndices[name]=ii
		names.append(name)
		
		# Verify if it is listed in measures table
		if name not in m2index:
			raise QPDumpError("No measure is defined for requirement '"+name+"' in row "+(ii+1)+".")
		
		# No need to check requirement names (they were checked when the project was dumped)
	
	# Build corner sets for independent measures
	for m in task[1]['requirements']:
		name=m[1].strip()
		mi=m2index[name]
		cset=set([])
		# Get analysis
		anName=description['measures'][mi][1]['analysis'].strip()
		if len(anName)<1:
			# No analysis, check if it depends on anything
			if len(description['measures'][mi][1]['depends'])>0:
				# Yes, skip it for now
				continue
			else:
				# Depends on nothing, all corners apply
				cset=cset.union(allCorners)
				# Corner dump already checked that there is at least one corner
		else:
			# Analysis is given, get its index
			ai=a2index[anName]
			# Get head
			hname=description['analyses'][ai][1]['head'].strip()
			# Add corners to corner set
			cset=cset.union(cornersForHead[hname])
			if len(cset)<=0:
				raise QPDumpError("No corners are defined for requirement '"+name+"' using simulator setup '"+hname+"'.")
	
	# Build corner sets for dependent measures
	for m in task[1]['requirements']:
		name=m[1].strip()
		mi=m2index[name]
		anName=description['measures'][mi][1]['analysis'].strip()
		# No analysis is given, depends on at least one measure
		if len(anName)<1 and len(description['measures'][mi][1]['depends'])>0:
			# Dependencies need not be included. They will be added when the task is run. 
			cset=set([])
			first=True
			# The corner set is the intersection across heads corresponding to dependencies
			for dep in description['measures'][mi][1]['depends']:
				depName=dep[0].strip()
				# Get measure, analysis, and head
				dmi=m2index[depName]
				depAnName=description['measures'][dmi][1]['analysis'].strip()
				dai=a2index[depAnName]
				dhname=description['analyses'][dai][1]['head'].strip()
				# For the first time use union, later use intersection
				if first:
					cset=cset.union(cornersForHead[dhname])
					first=False
				else:
					cset=cset.intersection(cornersForHead[dhname])
					
			if len(cset)<=0:
				txt="No corners are defined for requirement '"+name+"'. \n"
				txt+="At least one corner must be defined that is valid for all simulator setups on which this requirement depends."
				raise QPDumpError(txt)
			
	# Verify lower/upper/norm/tradeoff
	lowerDict={}
	upperDict={}
	normDict={}
	tradeoffDict={}
	excludeList=[]
	for m in task[1]['requirements']:
		name=m[1]
		
		# Read
		includeMeasure=m[0]
		
		s=m[2].strip()
		lo=None
		if len(s)>0:
			try:
				lo=readNumeric(s)
			except Exception as e:
				raise QPDumpError("Lower bound for requirement '"+name+"' is not a number. \n"+str(e))
		
		s=m[3].strip()
		hi=None
		if len(s)>0:
			try:
				hi=readNumeric(s)
			except Exception as e:
				raise QPDumpError("Upper bound for requirement '"+name+"' is not a number. \n"+str(e))
			
		s=m[4].strip()
		norm=None
		if len(s)>0:
			try:
				norm=readNumeric(s)
			except Exception as e:
				raise QPDumpError("Norm for requirement '"+name+"' is not a number. \n"+str(e))
			
		s=m[5].strip()
		tradeoff=None
		if len(s)>0:
			try:
				tradeoff=readNumeric(s)
			except Exception as e:
				raise QPDumpError("Tradeoff for requirement '"+name+"' is not a number. \n"+str(e))
			
		# Verify
		if lo is not None and hi is not None and lo>hi:
			raise QPDumpError("Lower bound is greater than upper bound for requirement '"+name+"'.")
		if norm is not None and norm<=0:
			raise QPDumpError("Norm is not greater than zero for requirement '"+name+"'.")
		if tradeoff is not None and tradeoff<0:
			raise QPDumpError("Tradeoff is not positive for requirement '"+name+"'.")
		if lo is None and hi is None and includeMeasure:
			raise QPDumpError("Requirement '"+name+"' is to be optimized, but no lower or upper bound is specified.")
		
		# Write
		if lo is not None:
			lowerDict[name]=lo
		if hi is not None:
			upperDict[name]=hi
		if norm is not None:
			normDict[name]=norm
		if tradeoff is not None:
			tradeoffDict[name]=tradeoff
		if not includeMeasure:
			excludeList.append(name)
	
	# Dump
	reqData={}
	
	# Excluded measures (not subject to optimization)
	reqData['exclude']=excludeList
	
	# Lower bounds
	reqData['lower']=lowerDict
	
	# Upper bounds
	reqData['upper']=upperDict
	
	# Norms
	reqData['norm']=normDict
	
	# Tradeoffs
	reqData['tradeoff']=tradeoffDict
	
	return reqData, names

def dumpParameters(description, task, localsDict={}):
	pdict={}
	
	# Collect design parameters from project
	designPar={ row[0]: (readNumeric(row[2]), readNumeric(row[3])) for row in description['designpar']}
	
	names=[]
	nameIndices={}
	optNames=[]
	fixedNames=[]
	for ii in range(len(task[1]['designpar'])):
		p=task[1]['designpar'][ii]
		name=p[0].strip()
		
		try:
			if name in nameIndices:
				jj=nameIndices[name]
				raise QPDumpError("Design parameter appears twice. First apeparance is in row "+str(jj+1)+".")
			
			nameIndices[name]=ii
			names.append(name)
			
			# Get initial
			pTxt=p[1].strip()
			if len(pTxt)<=0:
				raise QPDumpError("Initial value is not specified.")
			try:
				pIni=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Initial value is not valid.")
			
			# Get low
			pTxt=p[2].strip()
			try:
				if len(pTxt)<=0:
					pLo=None
				else:
					pLo=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Lower limit is not valid.")
				
			# Get high
			pTxt=p[3].strip()
			try:
				if len(pTxt)<=0:
					pHi=None
				else:
					pHi=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Upper limit is not valid.")
			
			if pLo is not None and pHi is not None:
				# If both are specified, check initial value consistency
				if pLo>=pHi:
					raise QPDumpError("Lower limit is not smaller than upper limit.")
				if pIni<pLo:
					raise QPDumpError("Initial value is below lower limit.")
				if pIni>pHi:
					raise QPDumpError("Initial value is above upper limit.")
				
				# Check consistency of limits with those of the design parameters in the project
				if name in designPar:
					if pLo<designPar[name][0]:
						raise QPDumpError("Lower limit is below the lower limit defined in the common part of the project.")
					if pLo>designPar[name][1]:
						raise QPDumpError("Lower limit is above the upper limit defined in the common part of the project.")
					if pHi<designPar[name][0]:
						raise QPDumpError("Upper limit is below the lower limit defined in the common part of the project.")
					if pHi>designPar[name][1]:
						raise QPDumpError("Upper limit is above the upper limit defined in the common part of the project.")
				
				# Do not check consistency for operating and statistical parameters
				
				# Add to list of optimization parameters
				optNames.append(name)
			elif pLo is None and pHi is None:
				# If none is specified add to list of fixed parameters
				fixedNames.append(name)
			else:
				raise QPDumpError("Lower and upper limit must both be specified or unspecified.")
			
			# Dump parameter
			pdict[name]={
				'lo': pLo, 
				'hi': pHi, 
				'init': pIni
			}
			
		except QPDumpError as e:
			raise QPDumpError("In definition of design parameter '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
	
	return pdict, names, optNames, fixedNames
	
def dumpSettings(description, task, localsDict={}):
	sdict={}
	
	# Failure penalty
	s=task[1]['settings']['failurepenalty']
	try:
		fp=readNumeric(s)
	except Exception as e:
		raise QPDumpError("Failure penalty must be a number. \n"+str(e))
	if fp<=0:
		raise QPDumpError("Failure penalty must be positive.")
	sdict['failurepenalty']=fp
	
	# Stop when all requirements are satisfied
	b=task[1]['settings']['stopsatisfied']
	sdict['stopsatisfied']=b
	
	# Method
	s=task[1]['settings']['method']
	sdict['method']=s
	
	# Forward solution
	b=task[1]['settings']['forwardsolution']
	sdict['forwardsolution']=b
	
	# Relevant corners
	b=task[1]['settings']['relevantcorners']
	sdict['incrementalcorners']=b
	
	# Maxiter
	s=task[1]['settings']['maxiter'].strip()
	if len(s)<=0:
		fp=None
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("Maximal number of iterations is not a number. \n"+str(e))
		if fp<0:
			raise QPDumpError("Maximal number of iterations must be positive.")
	sdict['maxiter']=fp
	
	# Stoptol
	s=task[1]['settings']['stoptol'].strip()
	if len(s)<=0:
		raise QPDumpError("Optimizer stoping tolerance must be specified.")
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("Optimizer stoping tolerance is not a number. \n"+str(e))
		if fp<0:
			raise QPDumpError("Optimizer stoping tolerance must be positive.")
	sdict['stoptol']=fp
	
	# initialstep
	s=task[1]['settings']['initialstep'].strip()
	if len(s)<=0:
		raise QPDumpError("Optimizer initial step size must be specified.")
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("Initial step is not a number. \n"+str(e))
		if fp==0:
			raise QPDumpError("Initial step must be nonzero.")
	sdict['initialstep']=fp
	
	# Tradeoffmultiplier
	s=task[1]['settings']['tradeoffmultiplier'].strip()
	try:
		fp=readNumeric(s)
	except Exception as e:
		raise QPDumpError("Tradeoff multiplier must be a number. \n"+str(e))
	if fp<0:
		raise QPDumpError("Tradeoff multiplier must be positive.")
	sdict['tradeoffmultiplier']=fp
	
	# evaluator settings
	pdict, _ = processParams(task[1]['settings']['evaluatorsettings'], "Evaluator setting", localsDict)
	sdict['evaluatorsettings']=pdict
		
	# aggregator settings
	pdict, _ = processParams(task[1]['settings']['aggregatorsettings'], "Aggregator setting", localsDict)
	sdict['aggregatorsettings']=pdict
	
	# optimizer settings
	pdict, _ = processParams(task[1]['settings']['optimizersettings'], "Optimizer setting", localsDict)
	sdict['optimizersettings']=pdict
	
	return sdict

def dumpOutput(description, task, localsDict={}):
	odict={}
	
	# simulatordebug
	s=task[1]['output']['simulatordebug'].strip()
	if len(s)<=0:
		fp=None
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("Simulator debug level is not a number. \n"+str(e))
		if fp<0:
			raise QPDumpError("Simulator debug level must be positive.")
	odict['simulatordebug']=fp
	
	# evaluatordebug
	s=task[1]['output']['evaluatordebug'].strip()
	if len(s)<=0:
		fp=None
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("Evaluator debug level is not a number. \n"+str(e))
		if fp<0:
			raise QPDumpError("Evaluator debug level must be positive.")
	odict['evaluatordebug']=fp
	
	# aggregatordebug
	s=task[1]['output']['aggregatordebug'].strip()
	if len(s)<=0:
		fp=None
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("Aggregator debug level is not a number. \n"+str(e))
		if fp<0:
			raise QPDumpError("Aggregator debug level must be positive.")
	odict['aggregatordebug']=fp
	
	# optimizerdebug
	s=task[1]['output']['optimizerdebug'].strip()
	if len(s)<=0:
		fp=None
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("Optimizer debug level is not a number. \n"+str(e))
		if fp<0:
			raise QPDumpError("Optimizer debug level must be positive.")
	odict['optimizerdebug']=fp
	
	# taskdebug
	s=task[1]['output']['taskdebug'].strip()
	if len(s)<=0:
		fp=None
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("Task debug level is not a number. \n"+str(e))
		if fp<0:
			raise QPDumpError("Task debug level must be positive.")
	odict['taskdebug']=fp
	
	b=task[1]['output']['keepfiles']
	odict['keepfiles']=b
	
	b=task[1]['output']['saveallresults']
	odict['saveallresults']=b
	
	b=task[1]['output']['savewaveforms']
	odict['savewaveforms']=b
	
	return odict

def dumpCBD(description, task, varDict={}):
	taskData={}
	
	taskData['name']=task[0].strip()
	taskData['type']=task[1]['type']
	
	workDict={ name: val for (name, val) in varDict.items() }
	rdict, names = dumpRequirements(description, task, workDict)
	taskData['requirements']=rdict
	taskData['requirementNames']=names
	
	workDict={ name: val for (name, val) in varDict.items() }
	pdict, names, optNames, fixedNames = dumpParameters(description, task, workDict)
	taskData['parameters']=pdict
	taskData['parameterNames']=names
	taskData['optParameterNames']=optNames
	taskData['fixedParameterNames']=fixedNames
	
	workDict={ name: val for (name, val) in varDict.items() }
	cdict, names = dumpCorners(description, task, workDict)
	taskData['corners']=cdict
	taskData['cornerNames']=names
	
	workDict={ name: val for (name, val) in varDict.items() }
	sdict = dumpSettings(description, task, workDict)
	taskData['settings']=sdict
	
	workDict={ name: val for (name, val) in varDict.items() }
	odict = dumpOutput(description, task, workDict)
	taskData['output']=odict
	
	# Check if there are any parameters defined for the optimizer
	if len(optNames)<=0 and task[1]['settings']['method'] not in ["none", "noneFull"]:
		raise QPDumpError("No optimization parameters defined.\n")

	return taskData


if __name__ == '__main__':
	from sampledata import data
	from pprint import pprint
	
	try:
		varDict={}
		pprint(dumpCBD(data, data['tasks'][0], varDict))
	except QPDumpError as e:
		raise QPDumpError("Error dumping task '"+data['tasks'][0][0]+"'.\n"+str(e))
	
	
