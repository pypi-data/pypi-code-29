from .dumptools import *

from pprint import pprint


__all__ = [ 'dumpPostprocessingPlots', 'dumpPostprocessingMeasures' ]


def dumpTraces(tData):
	names=[]
	nameIndices={}
	for ii in range(len(tData)):
		name=tData[ii][0].strip()
		if name in nameIndices:
			jj=nameIndices[name]
			raise QPDumpError("Trace defined twice. First definition is in row "+str(jj+1)+".")
			
		names.append(name)
		nameIndices[name]=ii

	tStruct={}
	for ii in range(len(tData)):
		t=tData[ii]
		name=t[0].strip()
		
		t1={}
		
		try:
			if not validateIdentifier(name):
				raise QPDumpError("Trace name '"+name+"' is not valid.")
			
			# Analyses TODO
			deplist=[]
			for kk in range(len(t[1]['analyses'])):
				depName=t[1]['analyses'][kk][0].strip()
				
				# Skip blank lines
				if len(depName)<1:
					continue
				
				deplist.append(depName)
				
			t1['analyses']=list(set(deplist))
			
			# Expression/script
			if len(t[1]['expression'].strip())>0:
				failed=False
				try:
					c=compileCode(t[1]['expression'], name+" expression", isEval=True)
				except QPDumpError as e:
					# Not an expression
					failed=True
				if failed:
					try: 
						c=compileCode(t[1]['expression'], name+" expression", isEval=False)
					except QPDumpError as e:
						raise QPDumpError("Expression parse failed.\n"+str(e))
				t1['expression']=t[1]['expression']
			else:
				raise QPDumpError("No expression specified.")
			
			# Scale expression/script
			if len(t[1]['scale'].strip())>0:
				failed=False
				try:
					c=compileCode(t[1]['scale'], name+" scale expression", isEval=True)
				except QPDumpError as e:
					failed=True
				if failed:
					try: 
						c=compileCode(t[1]['scale'], name+" scale expression", isEval=False)
					except QPDumpError as e:
						raise QPDumpError("Scale expression parse failed.\n"+str(e))
				t1['scale']=t[1]['scale']
			else:
				t1['scale']=None
		
		except QPDumpError as e:
			raise QPDumpError("In trace definition '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
		
		tStruct[name]=t1
	
	return tStruct

def dumpAxes(aData):
	names=[]
	nameIndices={}
	for ii in range(len(aData)):
		name=aData[ii][0].strip()
		if name in nameIndices:
			jj=nameIndices[name]
			raise QPDumpError("Trace defined twice. First definition is in row "+str(jj+1)+".")
			
		names.append(name)
		nameIndices[name]=ii
	
	aStruct={}
	for ii in range(len(aData)):
		a=aData[ii]
		name=a[0].strip()
		
		a1={}
		
		try:
			if not validateIdentifier(name):
				raise QPDumpError("Axes name '"+name+"' is not valid.")
			
			a1['title']=a[1]['title']
			a1['xlabel']=a[1]['xlabel']
			a1['ylabel']=a[1]['ylabel']
			
			a1['type']=a[1]['type']
			a1['aspect']=a[1]['aspect']
			a1['xgrid']=a[1]['xgrid']
			a1['ygrid']=a[1]['ygrid']

			try:
				fp=int(readNumeric(a[1]['xpos']))
			except Exception as e:
				raise QPDumpError("Axes x position must be a number. \n"+str(e))
			if fp<0:
				raise QPDumpError("Axes x position must be positive.")
			a1['xpos']=fp 
			
			try:
				fp=int(readNumeric(a[1]['xspan']))
			except Exception as e:
				raise QPDumpError("Axes x span must be a number. \n"+str(e))
			if fp<=0:
				raise QPDumpError("Axes x span must be grater than zero.")
			a1['xspan']=fp 
			
			try:
				fp=int(readNumeric(a[1]['ypos']))
			except Exception as e:
				raise QPDumpError("Axes y position must be a number. \n"+str(e))
			if fp<0:
				raise QPDumpError("Axes y position must be positive.")
			a1['ypos']=fp 
			
			try:
				fp=int(readNumeric(a[1]['yspan']))
			except Exception as e:
				raise QPDumpError("Axes y span must be a number. \n"+str(e))
			if fp<=0:
				raise QPDumpError("Axes y span must be greater than zero.")
			a1['yspan']=fp 
			
			
			a1['xlo']=None
			if len(a[1]['xlo'].strip())>0:
				try:
					fp=readNumeric(a[1]['xlo'])
				except Exception as e:
					raise QPDumpError("Axes x lower limit must be a number. \n"+str(e))
				if a1['type'] in ['xlog', 'log'] and fp<=0:
					raise QPDumpError("Logarithmic x-axis lower limit must be positive")
				a1['xlo']=fp
			
			a1['xhi']=None
			if len(a[1]['xhi'].strip())>0:
				try:
					fp=readNumeric(a[1]['xhi'])
				except Exception as e:
					raise QPDumpError("Axes x upper limit must be a number. \n"+str(e))
				if a1['type'] in ['xlog', 'log'] and fp<=0:
					raise QPDumpError("Logarithmic x-axis upper limit must be positive")
				a1['xhi']=fp 
			
			a1['ylo']=None
			if len(a[1]['ylo'].strip())>0:
				try:
					fp=readNumeric(a[1]['ylo'])
				except Exception as e:
					raise QPDumpError("Axes y lower limit must be a number. \n"+str(e))
				if a1['type'] in ['ylog', 'log'] and fp<=0:
					raise QPDumpError("Logarithmic y-axis lower limit must be positive")
				
				a1['xlo']=fp 
			
			a1['yhi']=None
			if len(a[1]['yhi'].strip())>0:
				try:
					fp=readNumeric(a[1]['yhi'])
				except Exception as e:
					raise QPDumpError("Axes y upper limit must be a number. \n"+str(e))
				if a1['type'] in ['ylog', 'log'] and fp<=0:
					raise QPDumpError("Logarithmic y-axis upper limit must be positive")
				a1['xhi']=fp 
			
			if a1['xlo'] is not None and a1['xhi'] is not None:
				if a1['xlo']>=a1['xhi']:
					raise QPDumpError("Axes x lower limit must be below upper limit.")
				
			if a1['ylo'] is not None and a1['yhi'] is not None:
				if a1['ylo']>=a1['yhi']:
					raise QPDumpError("Axes y lower limit must be below upper limit.")
			
			
			a1['traces']=dumpTraces(a[1]['traces'])
		
		except QPDumpError as e:
			raise QPDumpError("In axes definition '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
		
		aStruct[name]=a1
			
	return aStruct
			
def dumpPlots(pData):
	names=[]
	nameIndices={}
	for ii in range(len(pData)):
		name=pData[ii][0].strip()
		if name in nameIndices:
			jj=nameIndices[name]
			raise QPDumpError("Plot defined twice. First definition is in row "+str(jj+1)+".")
			
		names.append(name)
		nameIndices[name]=ii
	
	pStruct={}
	for ii in range(len(pData)):
		p=pData[ii]
		name=p[0].strip()
		
		p1={}
		
		try:
			if not validateIdentifier(name):
				raise QPDumpError("Plot name '"+name+"' is not valid.")
			
			p1['title']=p[1]['title']
			
			p1['axes']=dumpAxes(p[1]['axes'])
			
		except QPDumpError as e:
			raise QPDumpError("In plot definition '"+name+"' (row "+str(ii+1)+"). \n"+str(e))
		
		pStruct[name]=p1
	
	return pStruct

def dumpPostprocessingPlots(ppData):
	ppStruct={
		'plots': dumpPlots(ppData['plots']) 
	}
	
	return ppStruct

def dumpPostprocessingMeasures(ppData):
	measDict, names, lowerDict, upperDict, normDict = dumpMeasures(ppData, checkAnalysis=False)
	ppStruct={
		'measures': measDict, 
		'measureNames': names, 
		'measureLower': lowerDict, 
		'measureUpper': upperDict, 
		'measureNorm': normDict, 
	}
	
	return ppStruct
