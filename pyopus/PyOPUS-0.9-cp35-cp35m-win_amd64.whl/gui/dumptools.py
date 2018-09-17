import ast, string, re, traceback, sys, shutil, os.path

from .fstools import fileInfo
from .. import PyOpusError

# TODO: detect empty projects

__all__ = [ 
	"compileCode", 
	"validateIdentifier", "validateLowercaseIdentifier", "validateAlphanumeric", "isNumber", 
	"readNumeric", "QPDumpError", "writeFiles", "dumpProject", "dumpMeasures", "getVariables", 
	"formatNameList" 
]

from pprint import pprint

class QPDumpError(PyOpusError):
	def __init__(self, message, *args):
		super(QPDumpError, self).__init__(message, *args)

# Check if a string is a boolean	
def isBoolean(txt):
	if txt =='True' or txt=='False':
		return True
	else:
		return False

# Check if a string is a number (int or float)
def isNumber(txt):
	# Starts with a digit
	if txt[0]>='0' and txt[0]<='9':
		return True
	# Starts with a dot followed by a digit
	elif txt[0]=='.':
		if txt[1]>='0' and txt[1]<='9':
			return True
	# Starts with a sign followed by a dot followed by a digit
	elif (txt[0]=='+' or txt[0]=='-'):
		if txt[1]>='0' and txt[1]<='9':
			return True
		elif txt[1]=='.':
			if txt[2]>='0' and txt[2]<='9':
				return True
	else:
		return False

# Check if a string is a Python expression (prefixed by #)
def isPythonExpression(txt):
	if len(txt)>0 and txt[0]=='#':
		return True
	else:
		return False

# Check if a string is a space-separated list
def isList(txt):
	# Contains a space, tab, or cr/lf
	return any(c.isspace() for c in txt)

# Read a numeric literal
def readNumeric(txt):
	try:
		return ast.literal_eval(txt)
	except:
		raise QPDumpError("Failed to evaluate numeric literal.")

# Read a list of space separated elements (strings, numbers, or booleans)
def readList(txt):
	ret=[]
	# Split at whitespace, drop empty strings
	ii=1
	for token in txt.split():
		if isNumber(token) or isBoolean(token):
			# Number or boolean
			try:
				val=readNumeric(token)
			except QPDumpError as e:
				raise QPDumpError("Error at list member "+str(ii)+":\n"+str(e))
				
			ret.append(val)
			ii+=1
		else:
			# String
			ret.append(token)
	
	return ret

reIdentifier=re.compile(r"^[^\d\W]\w*\Z")
reLCIdentifier=re.compile(r"^[a-z_][a-z0-9_]*\Z")
reAlphanumeric=re.compile(r"^[a-zA-Z0-9]+\Z")

# Is string a valid identifier
def validateIdentifier(txt):
	return re.match(reIdentifier, txt)

# Is string a valid all-lowercase identifier
def validateLowercaseIdentifier(txt):
	return re.match(reLCIdentifier, txt)

# Is string a valid alphanumeric string
def validateAlphanumeric(txt):
	return re.match(reAlphanumeric, txt)

# parameters
#   1) #literal_string representing a Python expression
#   2) space separated list of items 3)-6)
#   3) float 
#   4) int
#   5) boolean
#   6) string_without_whitespace

# Compile expression/script
def compileCode(txt, name, isEval=True):
	try:
		return compile(txt, name, "eval" if isEval else "exec")
	except Exception as e:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		tback="".join(traceback.format_exception(exc_type, exc_value, exc_traceback, 0))
		raise QPDumpError(str(e)+"\n"+tback)

# Run expression/script
def runCode(c, name, globalsDict={}, localsDict={}, isEval=True):
	try:
		val=eval(c, globalsDict, localsDict)
		return val
	except Exception as e:
		raise QPDumpError("Evaluation failed: "+str(e))
	
# Extract value from a string, automatically detect type  (list, number, boolean, string, expression)
#   1) #literal_string representing a Python expression
#   2) space separated list of items 3)-6)
#   3) float 
#   4) int
#   5) boolean
#   6) string_without_whitespace
# A string with a leading # (pythonic expression) is evaluated immediately
# Setting asExpression to True returns an expression that after evaluation will yield the extracted value
def extractValue(name, valstr, localsDict={}, asExpression=False):
	if isPythonExpression(valstr):
		c=compileCode(valstr[1:], name+" expression", True)
		if asExpression:
			return valstr[1:]
		else:
			return runCode(c, globals(), localsDict)
	elif isList(valstr):
		
		val=readList(valstr)
	elif isNumber(valstr) or isBoolean(valstr):
		val=readNumeric(valstr)
	else:
		# literal string
		val=valstr
	
	if asExpression:
		return repr(val)
	else:
		return val

#
# End generic part 
#

# Process parameter, option, setting, and variable values
# Setting asExpression to True returns a dictionaty whose members must be evaluated to yield the extracted values
def processParams(paramTab, item, localsDict={}, asExpression=False):
	ii=0
	names=[]
	nameIndices={}
	pdict={}
	for row in paramTab:
		name=row[0].strip()
		
		if not validateIdentifier(name):
			raise QPDumpError(item+" name '"+name+"' is not valid. See row "+str(ii+1)+".")
		if name in nameIndices:
			jj=nameIndices[name]
			raise QPDumpError(item+" '"+name+"' redefined. See rows "+str(jj+1)+" and "+str(ii+1)+".")
		
		names.append(name)
		nameIndices[name]=ii
		
		# Extract value
		valstr=row[1].strip()
		
		if len(valstr)<=0:
			raise QPDumpError(item+" name '"+name+"' is not defined. See row "+str(ii+1)+".")
		
		try:
			exValue=extractValue(name, valstr, localsDict, asExpression=asExpression)
		except QPDumpError as e:
			raise QPDumpError(item+" processing failed for '"+name+"' (row "+str(ii)+"):\n"+str(e))
		
		pdict[name]=exValue
		
		ii+=1
	
	return pdict, names

# Process modules
def processModules(modulesTab):
	ii=0
	names=[]
	nameIndices={}
	mdict={}
	for row in modulesTab:
		name=row[0].strip()
		if not validateIdentifier(name):
			raise QPDumpError("Input module name '"+name+"' is not valid. See row "+str(ii+1)+" in input files table.")
		if name in nameIndices:
			jj=nameIndices[name]
			raise QPDumpError("Input module '"+name+"' redefined. See rows "+str(jj+1)+" and "+str(ii+1)+" in input files table.")
		
		names.append(name)
		nameIndices[name]=ii
		
		# Dump it
		mdict[name]={
			'file': row[1].strip(), 
		}
		if len(row)>2 and len(row[2].strip())>0:
			mdict[name]['section']=row[2].strip()
		
	return mdict, names

def dumpHeads(description, localsDict={}):
	names=[]
	head2sim={}
	nameIndices={}
	nheads=len(description['heads'])
	
	if nheads<1:
		raise QPDumpError("No simulator setup defined.")
	
	headsDict={}
	for ii in range(nheads):
		h=description['heads'][ii]
		name=h[0].strip()
		try:
			if not validateIdentifier(name):
				raise QPDumpError("Simulator setup name is not valid.")
			
			if name in nameIndices:
				jj=nameIndices[name]
				raise QPDumpError("Simulator setup defined twice. First definition is in row "+str(jj+1)+".")
			
			names.append(name)
			nameIndices[name]=ii
			
			# OK, start building a head
			hdict={}
			
			# Simulator
			hdict['simulator']=h[1]['simulator']
			
			# Settings
			sdict, _ = processParams(h[1]['settings'], "Setting", localsDict)
			hdict['settings']=sdict
			
			# Options
			odict, _ = processParams(h[1]['options'], "Option", localsDict)
			hdict['options']=odict
			
			# Params
			pdict, _ = processParams(h[1]['params'], "Parameter", localsDict)
			hdict['params']=pdict
			
			# Modules
			mdict, _ = processModules(h[1]['moddefs'])
			hdict['moddefs']=mdict
			
			# Add to heads structure
			headsDict[name]=hdict
			
			# Add to head2sim structure
			head2sim[name]=hdict['simulator']
			
		except QPDumpError as e:
			raise QPDumpError("In simulator definition '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
	
	return headsDict, names, head2sim

def dumpVariables(description):
	# Variables are not evaluated here, only a string that must be evaluated to get the variable is stored
	try:
		vdict, names1 = processParams(description['variables'], "Variable", {}, asExpression=True)
	except QPDumpError as e:
		raise QPDumpError("In variables definition: \n"+str(e))
	
	return vdict, names1

def getVariables(vdict):
	# Returns a dictionary of evaluated variables
	varDict={}
	for name, defstr in vdict.items():
		try:
			c=compileCode(defstr, "variable '"+name+"' definition", isEval=True)
		except QPDumpError as e:
			raise QPDumpError("Expression parse failed.\n"+str(e))
		
		try:
			v=runCode(
				c, "variable '"+name+"' definition", 
				globalsDict={}, localsDict={}, 
				isEval=True
			)
			varDict[name]=v
		except QPDumpError as e:
			raise QPDumpError("In variable evaluation of '"+name+"'. \n"+str(e))
	
	return varDict

# A hash prefixed string specifies a variable expression whose result is the list of object names
def dumpSave(saveRow):
	saveTxt=saveRow[1].strip()
	
	if saveRow[0]=='default':
		if len(saveTxt)>0:
			raise QPDumpError("Default save directive requires no detailed specification.")
		return 'all()'
	
	if len(saveTxt)<=0:
			raise QPDumpError("Directive description is an empty string.")
		
	if saveRow[0]=='voltage':
		if isPythonExpression(saveTxt):
			saveTxt=saveTxt[1:].strip()
			if len(saveTxt)<=1:
				raise QPDumpError("Expression is an empty string.")
			try:
				compileCode(saveTxt, "node name list expression", isEval=True)
			except QPDumpError as e:
				raise QPDumpError("Expression parse failed.\n"+str(e))
			
			return "v("+saveTxt+")"
		else:
			vlist=saveTxt.split()
			if len(vlist)<=0:
				raise QPDumpError("Need at least one node name.")
			return "v("+formatNameList(vlist)+")"
	elif saveRow[0]=='devcurrent':
		if isPythonExpression(saveTxt):
			saveTxt=saveTxt[1:].strip()
			if len(saveTxt)<=1:
				raise QPDumpError("Expression is an empty string.")
			try:
				compileCode(saveTxt, "device name list expression", isEval=True)
			except QPDumpError as e:
				raise QPDumpError("Expression parse failed.\n"+str(e))
			
			return "v("+saveTxt+")"
		else:
			if len(saveTxt)<=0:
				raise QPDumpError("Need at least one instance name.")
			ilist=saveTxt.split()
			return "i("+formatNameList(ilist)+")"
	elif saveRow[0]=='devvar':
		# Split into device and propery list
		splitList=saveTxt.split(";")
		if len(splitList)!=2:
			raise QPDumpError("Two semicolon-separated lists are required for saving device properties.")
		devList, propList = [ x.strip() for x in splitList ]
		
		if len(devList)<1:
			raise QPDumpError("Need at least one device name.")
		if len(propList)<1:
			raise QPDumpError("Need at least one property name.")
		
		if isPythonExpression(devList):
			devFormat=devList[1:].strip()
			if len(devFormat)<1:
				raise QPDumpError("Device name expression has zero length")
			try:
				compileCode(devFormat, "device name list expression", isEval=True)
			except QPDumpError as e:
				raise QPDumpError("Expression parse failed.\n"+str(e))
		else:
			istr=[iname.strip() for iname in devList.split()]
			devFormat=formatNameList(istr)
		
		if isPythonExpression(propList):
			propFormat=propList[1:].strip()
			if len(propFormat)<1:
				raise QPDumpError("Property name expression has zero length")
			try:
				compileCode(devFormat, "device property name list expression", isEval=True)
			except QPDumpError as e:
				raise QPDumpError("Expression parse failed.\n"+str(e))
		else:
			istr=[iname.strip() for iname in propList.split()]
			propFormat=formatNameList(istr)
		
		return "p("+devFormat+", "+propFormat+")"
	else:
		# Expression
		if len(saveTxt)<=1:
			raise QPDumpError("Expression is an empty string.")
		try:
			compileCode(saveTxt, "save expression", isEval=True)
		except QPDumpError as e:
			raise QPDumpError("Expression parse failed.\n"+str(e))
			
		return saveTxt
	
	
def dumpAnalyses(description, localsDict={}):
	analysesTab=description['analyses']
	
	# Collect head names, build index map
	headsSet=set([h[0].strip() for h in description['heads']])
	headIndexMap={}
	for ii in range(len(description['heads'])):
		h=description['heads'][ii]
		headIndexMap[h[0].strip()]=ii
	
	ansDict={}
	
	names=[]
	an2head={}
	nameIndices={}
	nanalyses=len(analysesTab)
	
	if nanalyses<1:
		raise QPDumpError("No analysis defined.")
	
	for ii in range(nanalyses):
		h=analysesTab[ii]
		name=h[0].strip()
		try:
			if not validateIdentifier(name):
				raise QPDumpError("Analysis name is not valid.")
			
			if name in nameIndices:
				jj=nameIndices[name]
				raise QPDumpError("Analysis defined twice. First definition is in row "+str(jj+1)+".")
			
			names.append(name)
			nameIndices[name]=ii
			
			# OK, start building an analysis
			adict={}
			
			# Simulator
			simHead=h[1]['head'].strip()
			if simHead not in headsSet:
				raise QPDumpError("Analysis is using an undefined simulator setup '"+simHead+"'.")
			adict['head']=simHead
			
			# Collect module names
			modulesSet=set([mod[0].strip() for mod in description['heads'][headIndexMap[simHead]][1]['moddefs']])
			
			# Modules
			mlist=[]
			for kk in range(len(h[1]['modules'])):
				row=h[1]['modules'][kk]
				modTxt=row[0].strip()
				if modTxt not in modulesSet:
					raise QPDumpError("Analysis is using an undefined input module '"+modTxt+"' (row "+str(kk+1)+").\nThe input module should be defined in the '"+simHead+"' simulator setup.")
				mlist.append(modTxt)
			adict['modules']=mlist
			
			# Options
			odict, _ = processParams(h[1]['options'], "Option", localsDict)
			adict['options']=odict
			
			# Params
			pdict, _ = processParams(h[1]['params'], "Parameter", localsDict)
			adict['params']=pdict
			
			# Saves
			slist=[]
			for kk in range(len(h[1]['saves'])):
				saveRow=h[1]['saves'][kk]
				try:
					saveTxt=dumpSave(saveRow)
					slist.append(saveTxt)
				except QPDumpError as e:
					raise QPDumpError("Bad save directive in row "+str(kk+1)+". \n"+str(e))
			adict['saves']=slist
			
			# Command
			commandTxt=h[1]['command'].strip()
			try:
				compileCode(commandTxt, name+" command", isEval=True)
			except QPDumpError as e:
				raise QPDumpError("Command parse failed.\n"+str(e))
			adict['command']=commandTxt
			
			# Add to analyses to head map
			an2head[name]=simHead
			
			# Add to analyses dict
			ansDict[name]=adict
			
		except QPDumpError as e:
			raise QPDumpError("In analysis definition '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
			
	return ansDict, names, an2head

def dumpMeasures(description, localsDict={}, checkAnalysis=True):
	measuresTab=description['measures']
	
	# Collect head names, build index map
	if checkAnalysis:
		analysesSet=set([a[0].strip() for a in description['analyses']])
		for ii in range(len(description['analyses'])):
			a=description['analyses'][ii]
	
	measDict={}
	
	# Need names immediately, remember also if measures are dependent
	names=[]
	nameIndices={}
	isDependent=[]
	for ii in range(len(measuresTab)):
		name=measuresTab[ii][0].strip()
		if name in nameIndices:
			jj=nameIndices[name]
			raise QPDumpError("Measure defined twice. First definition is in row "+str(jj+1)+".")
			
		names.append(measuresTab[ii][0].strip())
		nameIndices[name]=ii
		isDependent.append(len(measuresTab[ii][1]['analysis'].strip())<1)
	
	lowerDict={}
	upperDict={}
	normDict={}
		
	for ii in range(len(measuresTab)):
		m=measuresTab[ii]
		name=m[0].strip()
		
		try:
			if not validateIdentifier(name):
				raise QPDumpError("Measure name '"+name+"' is not valid.")
			
			# OK, start building a measure
			mdict={}
			
			# Lower
			lo=None
			if len(m[1]['lower'].strip())>0:
				try:
					lo=readNumeric(m[1]['lower'])
					lowerDict[name]=lo
				except Exception as e:
					raise QPDumpError("Lower bound for measure '"+name+"' is not a number. \n"+str(e))
				
			# Upper
			hi=None
			if len(m[1]['upper'].strip())>0:
				try:
					hi=readNumeric(m[1]['upper'])
					upperDict[name]=hi
				except Exception as e:
					raise QPDumpError("Upper bound for measure '"+name+"' is not a number. \n"+str(e))
			
			# Norm
			norm=None
			if len(m[1]['norm'].strip())>0:
				try:
					norm=readNumeric(m[1]['norm'])
					normDict[name]=norm
				except Exception as e:
					raise QPDumpError("Norm for measure '"+name+"' is not a number. \n"+str(e))
				
			# Verify
			if lo is not None and hi is not None and lo>hi:
				raise QPDumpError("Lower bound is greater than upper bound for measure '"+name+"'.")
			if norm is not None and norm<=0:
				raise QPDumpError("Norm is not greater than zero for measure '"+name+"'.")
			
			# Analysis
			anName=m[1]['analysis'].strip()
			if len(anName)<1:
				# No analysis
				dependent=True
			else:
				dependent=False
			if checkAnalysis and not dependent and anName not in analysesSet:
				raise QPDumpError("Measure is using an undefined analysis '"+anName+"'.")
			mdict['analysis']=anName if not dependent else None
			
			# Depends on measures
			if dependent:
				deplist=[]
				for kk in range(len(m[1]['depends'])):
					depName=m[1]['depends'][kk][0].strip()
					if depName not in names:
						raise QPDumpError("Measure depends on an undefined measure '"+depName+"'.")
					if isDependent[names.index(depName)]:
						raise QPDumpError("Measure is dependent and depends on '"+depName+"' which is also dependent.")
					deplist.append(depName)
				mdict['depends']=list(set(deplist))
			
			# Type
			mdict['vector']=bool(m[1]['vector'])
			
			# Component names
			compTxt=m[1]['components'].strip()
			if len(compTxt)>0 and mdict['vector']:
				if isPythonExpression(compTxt):
					# Extract expression, compile
					try:
						c=compileCode(compTxt[1:], "component names expression", True)
					except QPDumpError as e:
						raise QPDumpError("Component names expression parse failed.\n"+str(e))
					mdict['components']=compTxt[1:]
				else:
					mdict['components']=formatNameList(compTxt.split())
			
			# Expression/script
			failed=False
			try:
				c=compileCode(m[1]['expression'], name+" expression", isEval=True)
			except QPDumpError as e:
				# Not an expression
				failed=True
			if failed:
				try: 
					c=compileCode(m[1]['expression'], name+" expression", isEval=False)
				except QPDumpError as e:
					raise QPDumpError("Expression parse failed.\n"+str(e))
			mdict['expression']=m[1]['expression']
			
			# Add to measures dict
			measDict[name]=mdict
		
		except QPDumpError as e:
			raise QPDumpError("In measure definition '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
	
	return measDict, names, lowerDict, upperDict, normDict

def dumpDesignParameters(description):
	pdict={}
	names=[]
	nameIndices={}
	for ii in range(len(description['designpar'])):
		p=description['designpar'][ii]
		name=p[0].strip()
		
		try:
			if not validateIdentifier(name):
				raise QPDumpError("Parameter name '"+name+"' is not valid.")
			
			if name in nameIndices:
				jj=nameIndices[name]
				raise QPDumpError("Parameter defined twice. First definition is in row "+str(jj+1)+".")
			
			names.append(name)
			nameIndices[name]=ii
			
			# Get low
			pTxt=p[2].strip()
			try:
				pLo=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Lower limit is not valid.")
			
			# Get high
			pTxt=p[3].strip()
			try:
				pHi=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Upper limit is not valid.")
			
			if pLo>=pHi:
				raise QPDumpError("Lower limit is not smaller than upper limit.")
			
			# Get initial
			pTxt=p[1].strip()
			if len(pTxt)<1:
				pIni=None
			else:
				try:
					pIni=readNumeric(pTxt)
				except Exception as e:
					raise QPDumpError("Initial value is not valid.")
				
				if pIni<pLo or pIni>pHi:
					raise QPDumpError("Initial value outside limits.")
			
			pdict[name]={
				'lo': pLo, 
				'hi': pHi, 
				'init': pIni
			}
			
		except QPDumpError as e:
			raise QPDumpError("In definition of design parameter '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
			
	return pdict, names

def dumpOperatingParameters(description):
	pdict={}
	names=[]
	nameIndices={}
	for ii in range(len(description['oppar'])):
		p=description['oppar'][ii]
		name=p[0].strip()
		
		try:
			if not validateIdentifier(name):
				raise QPDumpError("Parameter name '"+name+"' is not valid.")
			
			if name in nameIndices:
				jj=nameIndices[name]
				raise QPDumpError("Parameter defined twice. First definition is in row "+str(jj+1)+".")
			
			names.append(name)
			nameIndices[name]=ii
			
			# Get low
			pTxt=p[2].strip()
			try:
				pLo=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Lower limit is not valid.")
			
			# Get high
			pTxt=p[3].strip()
			try:
				pHi=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Upper limit is not valid.")
			
			if pLo>=pHi:
				raise QPDumpError("Lower limit is not smaller than upper limit.")
			
			# Get nominal
			pTxt=p[1].strip()
			try:
				pIni=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Nominal value is not valid.")
				
			if pIni<pLo or pIni>pHi:
				raise QPDumpError("Nominal value outside limits.")
			
			pdict[name]={
				'lo': pLo, 
				'hi': pHi, 
				'nominal': pIni
			}

		except QPDumpError as e:
			raise QPDumpError("In definition of operating parameter '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
			
	return pdict, names

def dumpStatisticalParameters(description):
	pdict={}
	names=[]
	nameIndices={}
	for ii in range(len(description['statpar'])):
		p=description['statpar'][ii]
		name=p[0].strip()
		
		try:
			if not validateIdentifier(name):
				raise QPDumpError("Parameter name '"+name+"' is not valid.")
			
			if name in nameIndices:
				jj=nameIndices[name]
				raise QPDumpError("Parameter defined twice. First definition is in row "+str(jj+1)+".")
			
			names.append(name)
			nameIndices[name]=ii
			
			# Get low
			pTxt=p[1].strip()
			try:
				pLo=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Lower limit is not valid.")
			
			# Get high
			pTxt=p[2].strip()
			try:
				pHi=readNumeric(pTxt)
			except Exception as e:
				raise QPDumpError("Upper limit is not valid.")
			
			if pLo>=pHi:
				raise QPDumpError("Lower limit is not smaller than upper limit.")
			
			pdict[name]={
				'lo': pLo, 
				'hi': pHi, 
				'distribution': p[3].strip()
			}
			
		except QPDumpError as e:
			raise QPDumpError("In definition of statistical parameter '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
			
	return pdict, names

def designOpStatDuplicatesCheck(description):
	dlist=set([p[0].strip() for p in description['designpar']])
	olist=set([p[0].strip() for p in description['oppar']])
	slist=set([p[0].strip() for p in description['statpar']])
	
	x=dlist.intersection(olist)
	if len(x):
		raise QPDumpError("Parameter '"+x.pop()+"' is defined as design parameter and operating parameter.")
	x=dlist.intersection(slist)
	if len(x):
		raise QPDumpError("Parameter '"+x.pop()+"' is defined as design parameter and statistical parameter.")
	x=olist.intersection(slist)
	if len(x):
		raise QPDumpError("Parameter '"+x.pop()+"' is defined as operating parameter and statistical parameter.")

# Head and analysis params/options/settings can be given as Python expressions
# Vector components can be given as Python expressions
# Design/op/stat param values must be numerical constants

def dumpMirrorMap(description):
	mmdict={}
	names=[]
	nameIndices={}
	for ii in range(len(description['files'])):
		p=description['files'][ii]
		name=p[0].strip()
		
		try:
			if name in nameIndices:
				jj=nameIndices[name]
				raise QPDumpError("File/folder listed twice. First appearance is in row "+str(jj+1)+".")
			
			names.append(name)
			nameIndices[name]=ii
			
			if p[1]['external']:
				info=fileInfo(name)
				if info['type'] is None:
					raise QPDumpError("External file/folder not found.")
			
			mmdict[name]='.'
			
		except QPDumpError as e:
			raise QPDumpError("In definition of file/folder '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
			
	return mmdict, names

def checkTasks(description):
	names=[]
	nameIndices={}
	
	for ii in range(len(description['tasks'])):
		t=description['tasks'][ii]
		name=t[0]
		
		if not validateIdentifier(name):
			raise QPDumpError("Design task name '"+name+"' is not a valid identifier.")
		
		if name in nameIndices:
			jj=nameIndices[name]
			raise QPDumpError("Design task name '"+name+"' in row ("+str(ii+1)+") is not unique. First appearance is in row "+str(jj+1)+".")
	
		names.append(name)
		nameIndices[name]=ii
	
def writeFiles(description, destination):
	for ii in range(len(description['files'])):
		p=description['files'][ii]
		name=p[0].strip()
		
		try:
			if p[1]['external']:
				info=fileInfo(name)
				if info['type'] is None:
					raise QPDumpError("External file/folder '"+name+"' not found.")
				try:	
					if info['type']=='dir':
						shutil.copytree(name, destination)
					else:
						shutil.copy(name, destination)
				except Exception as e:
					raise QPDumpError("Failed to copy '"+name+"' to '"+destination+"'.")
			else:
				try:
					with open(os.path.join(destination, name), 'w') as f:
						f.write(p[1]['content'])
						f.close()
				except Exception as e:
					raise QPDumpError("Failed to write '"+name+"' to folder '"+destination+"'.")
			
		except QPDumpError as e:
			raise QPDumpError("Error preparing file '"+name+"' (row "+str(ii+1)+"). \n"+str(e))

def formatNameList(names):
	return "["+(", ".join([repr(name) for name in names]))+"]"

def dumpProject(description):
	projData={}
	
	mmdict, names = dumpMirrorMap(description)
	projData['mirrormap']=mmdict
	
	vdict, names = dumpVariables(description)
	projData['variables']=vdict
	projData['variableNames']=names
	varDict=getVariables(vdict)
	
	workDict={ name: val for (name, val) in varDict.items() }
	hdict, names, head2sim = dumpHeads(description, workDict)
	projData['heads']=hdict
	projData['headNames']=names
	
	workDict={ name: val for (name, val) in varDict.items() }
	adict, names, an2head = dumpAnalyses(description, workDict)
	projData['analyses']=adict
	projData['analysisNames']=names
	
	mdict, names, lowerDict, upperDict, normDict = dumpMeasures(description)
	projData['measures']=mdict
	projData['measureNames']=names
	projData['measureLower']=lowerDict
	projData['measureUpper']=upperDict
	projData['measureNorm']=normDict
	
	pdict, names = dumpDesignParameters(description)
	projData['designPar']=pdict
	projData['designParNames']=names
	
	pdict, names = dumpOperatingParameters(description)
	projData['opPar']=pdict
	projData['opParNames']=names
	
	pdict, names = dumpStatisticalParameters(description)
	projData['statPar']=pdict
	projData['statParNames']=names
	
	designOpStatDuplicatesCheck(description)
	
	checkTasks(description)
	
	return projData, varDict
	
	
if __name__=='__main__':	
	from sampledata import data
	from pprint import pprint

	try:
		pdict, varDict = dumpProject(data)
		pprint(pdict)
		
	except QPDumpError as e:
		print("Error dumping problem description.\n"+str(e))
		sys.exit(0)



