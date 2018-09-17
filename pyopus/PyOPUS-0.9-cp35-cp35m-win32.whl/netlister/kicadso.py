# -*- coding: UTF-8 -*-
"""
Outputs a Spice Opus netlist from data imported from a kicad XML netlist. 

Make sure pyopus.lib and pyopus.dcm are installed. Add pyopus to your  
libraries list by selecting Preferences/Component Libraries in the 
Eeschema menu and clicking Add. This will add the pyopus symbols to 
the list of libraries so that you can use them in the schematic editor. 

One KiCad sheet with its subsheets (one schematic project) defines one 
subcircuit or one toplevel circuit. The following symbols are available.

Built-in devices:

* RES           - resistor specified by resistance
* RES_SEMI      - semiconductor resistor specified by model and dimensions
* CAP           - capacitor specified by capacitance
* CAP_SEMI      - semiconductor capacitor specified by model and dimensions
* IND           - inductor
* IND_COUPLING  - inductive coupling 
* VSRC          - independent voltage source. Its function is specifid with 
                  SPICE syntax by setting the Specification field
* ISRC          - independent current source. Its function is specifid with 
                  SPICE syntax by setting the Specification field
* VCVS          - voltage-controlled voltage source
* CCVS          - current-controlled voltage source
* VCCS          - voltage-controlled current source
* CCCS          - current-controlled current source
* VSRC_NONLIN   - nonlinear controlled voltage source
* ISRC_NONLIN   - nonlinear controlled current source
* SW            - voltage-controlled switch
* CSW           - current-controlled switch
* NPN, PNP      - bipolar junction transistor
* NMOS, PMOS    - MOSFET
* NJF, PJF      - JFET
* NMF, PMF      - MESFET
* LOSSLESS_LINE - lossless transmission line 
* LOSSY_LINE    - lossless transmission line 
* URC_LINE      - uniform distributed RC line

Subcircuits:
* OPAMP         - operational amplifier 
* OPAMP_DIFF    - operational amplifier with diff. output
* OTA           - operational transconductance amplifier
* OTA_DIFF      - operational transconductance amplifier with diff. output

If a device is not known to the netlister (not defined in the ``Mapping`` 
memeber of the configuration) it is treated as a subcircuit. 

The ``Value`` field is the name of the subcircuit definition. 
By default pins are assigned in increasing pin number order. This can be 
customized by setting the ``PinMap`` field which must be a space-separated 
list of pin numbers. 
The netlister assumes the subcircuit has no parameters. The space-separated 
list of allowed parameters can be specified with the ``Parameters`` field. 
Note that ``Parameters`` must be defined in order for the netlister to count 
the passed parameters and decide if the instance needs the ``param:`` keyword 
or not. 
Parameters values are passed by setting the corresponding fields of the 
component. Arbitrary strings can be appended to the end of the subcircuit 
instance with the ``Specification`` field. 

Special directives:

* INCLUDE      - includes an external file
* LIB          - includes a section of an external library file
* MODEL        - defines a model
* SUPPRESS_END - does not add ``.end`` at the end of netlists that do not
                 define a subcircuit. Useful for netlisting a top-level circuit 
                 as an include file. The ``.end`` can also be suppressed by 
                 setting ``SuppressEnd`` in the configuration to ``True``. 
* SUBCKT       - specifies this sheet and its subsheets define a subcircuit. 
                 The subcircuit name and pin order are fields of this
                 component. Pins are specified with the corresponding net 
                 names. To specify a net name for a net, use a global label. 
* SUBCKT PARAM - defines a subcircuit parameter and its default value. 
* PARAM        - defines a new parameter whose value is defined by an 
                 expression. 
* OUTPUT_FILE  - specifies the output file name for the netlister. Overrides 
		 the file name chosen in the Netlist Export dialog. The file 
		 name specified in the dialog is used for the intermediate 
		 XML netlist, but not for the final output file. 
		 The output file can be a relative path (relative to the 
		 folder where the XML netlist is stored). Absolute paths are 
		 not allowed. 
		 
All special directives have a refdes of the form ``A<number>``. INCLUDE and 
LIB directives also have a ``Position`` field which places the directive 
at the top (bottom) of the netlist when set to ``top`` (``bottom``). 
INCLUDE and LIB directives are grouped by their position (top, bottom) and 
dumped in the order specified by the refdes number. 

Parameter definitions specified by the PARAM directive are dumped in the order 
defined by the refdes number. If the sheet defines a subcircuit they are 
placed inside the subcircuit definition (they are local parameters). 

Subcircuit parameters are also ordered by their refdes numbers. 

MODEL definitions are dumped before the instances. If the sheet defines a 
subcircuit all model definitions are placed inside the subcircuit definition 
(they are local models). 

Instances are grouped by sheets. 

Ground nets defined in the *configuration* are mapped to node 0. They are 
treated as global nodes. 

The netlister can also include verbatim text from the schematic. Verbatim texts 
must have first line of the form
``Text<number> position=top|bottom`` followed by a newline and the verbatim 
text that should be included in the netlist. Block number must be unique. 

The complete hierarchy is searched for verbatim text blocks. For the search 
to to work all schematic files must be in the same folder and the netlister 
must be started in that folder (because sheet source file name is dumped by 
KiCad without full path). 

The collected blocks are grouped by their specified position (top, bottom) and 
ordered by their number. Top blocks are dumped after the last top INCLUDE/LIB 
directive. Bottom blocks are dumped before the first bottom INCLUDE/LIB directive. 

Verbatim text blocks can be used for including a ``.control`` block in the 
netlist. 
"""

import re, os, json
from copy import deepcopy
from .kicadxml import readKicadXML
from .kicadsocfg import config as defaultConfig
from pyopus.netlister import PyNetlisterError

__all__ = [ "NetlisterKicadSpiceOpus" ]


numberPat=re.compile("^[0-9]+$")
badCharsPat=re.compile("[^a-z0-9_]")
nodeCharsPat=re.compile("^[a-z0-9_]+$")
nodePat=re.compile("^(([a-z_][0-9a-z_]*)|([1-9][0-9]*)|0)$")
instPat=re.compile("^([a-z_][0-9a-z_]*)$")
paramPat=re.compile("^([a-z_][0-9a-z_]*)$")
modelPat=re.compile("^([a-z_][0-9a-z_]*)$")
macroPat=re.compile(r"#([A-Z_][A-Z0-9_]*)\(([A-Za-z0-9_ ]*)\)")

# symbolLib="pyopus" # Special components in pyopus library are ignored
symbolLib=None  # Special components in all libraries are ignored
specialComponents=set(["INCLUDE", "LIB", "PARAM", "SUBCKT", "SUBCKT_PARAM", "MODEL", "SUPPRESS_END", "OUTPUT_FILE"])

class NetlisterKicadSpiceOpus(object):
	def __init__(self, userConfig={}):
		# Copy default config
		self.config=deepcopy(defaultConfig)
		
		# Merge with default config
		self.updateConfig(userConfig)
	
	def updateConfig(self, cfg):
		# Extract Mapping, merge userConfig with default
		tmp={}
		tmp.update(cfg)
		if "Mapping" in tmp:
			mapping=tmp["Mapping"]
			del tmp["Mapping"]
		else:
			mapping={}
		
		self.config.update(tmp)
		self.config["Mapping"].update(mapping)
		
	def configToJSON(self):
		cfg={}
		cfg.update(self.config)
		cfg["Mapping"]=[ [key[0], key[1], self.config["Mapping"][key] ] for key in self.config["Mapping"].keys() ]
		return json.dumps(cfg, indent=4)
			
	def configFromJSON(self, jsontxt, update=True):
		cfg=json.loads(jsontxt)
		
		if "Mapping" in cfg:
			cfg["Mapping"]={ (e[0], e[1]): e[2] for e in cfg["Mapping"] }
		
		if not update:
			# Set config to basic config
			self.config=deepcopy(defaultConfig)
		
		# Merge with current config
		self.updateConfig(cfg)
						
	def macroText(self, errorTemplate, seq, mCommand, mArgs, dm, comp, specials):
		# Split arguments
		args=mArgs.split(" ") if len(mArgs)>0 else []
		
		# Get fields
		fields=comp["fields"] if "fields" in comp else {}
		
		if mCommand=="REF":
			return comp["name"]
		if mCommand=="REFORIG":
			return comp["nameOrig"]
		elif mCommand=="PINS":
			if len(args)==0:
				if "PinMap" in fields:
					try:
						order=[int(pinstr) for pinstr in fields["PinMap"].split()]
					except:
						raise PyNetlisterError(
							"%s, macro %d, argument %d: PinMap field has an invalid value." %
							(errorTemplate, seq+1, ii+1)
						)
				elif "PinMap" in dm:
					order=dm["PinMap"]
				else:
					order=sorted(list(comp["slots"].keys()))
			else:
				order=[]
				for ii in range(len(args)):
					arg=args[ii]
					try:
						jj=int(arg)
					except:
						raise PyNetlisterError(
							"%s, macro %d, argument %d: Cannot convert argument to integer" %
							(errorTemplate, seq+1, ii+1)
						)
					order.append(jj)
					
			nets=[]
			for ii in order:
				try:
					nets.append(comp["slots"][ii])
				except:
					raise PyNetlisterError(
						"(%s, macro %d: Bad pin number %d." %
						(errorTemplate, seq+1, ii)
					)
				
			return " ".join(nets)
		elif mCommand=="MODEL":
			if comp["modelName"] is not None:
				return comp["modelName"]
			else:
				raise PyNetlisterError("%s, macro %d: No model is defined for this instance." %
					(errorTemplate, seq+1)
				)
		elif mCommand=="PARAM":
			if len(comp["specifiedParameters"])>0:
				return "param:"
			else:
				return ""
		elif mCommand=="PV":
			if len(args)!=1:
				raise PyNetlisterError(
					"%s, macro %d: Macro requires one argument." %
					(errorTemplate, seq+1)
				)
			
			parName=args[0]
			
			if parName not in fields:
				return ""
			
			pv=fields[parName]
			
			if pv=="true":
				# Treat "true" as boolean parameter set to True
				# Dump parameter name
				return parName
			elif pv=="false":
				# Treat "false" as boolean parameter set to False
				# Dump nothing
				return ""
			else:
				# All other cases
				return str(pv)
		elif mCommand=="PNV":
			if len(args)>1:
				raise PyNetlisterError(
					"%s, macro %d: Macro can have at most one argument." %
					(errorTemplate, seq+1)
				)
			
			if len(args)==1:
				parNames=args
			else:
				parNames=comp["parameters"]
				
			txtList=[]
			for parName in parNames:
				if parName not in fields:
					continue
				
				pv=fields[parName]
				
				if pv=="true":
					# Treat "true" as boolean parameter set to True
					# Dump parameter name
					txtList.append(parName)
				elif pv=="false":
					# Treat "false" as boolean parameter set to False
					# Dump nothing
					pass
				else:
					# All other cases
					txtList.append(parName+"="+str(pv))
			
			return " ".join(txtList)
		else:
			raise PyNetlisterError(
				"%s, macro %d: Unknown macro %s." %
				(errorTemplate, seq+1, mCommand)
			)
		
	def substituteMacros(self, txt, errorTemplate, dm, comp, specials):
		out=""
		pos=0
		
		copyTo=0
		seq=0
		while True:
			m=macroPat.search(txt, pos)
			
			if m is not None:
				# Copy text before macro
				out+=txt[pos:m.start()]
				
				# Handle macro
				mCommand=m.group(1)
				mArgs=m.group(2)
				expTxt=self.macroText(errorTemplate, seq, mCommand, mArgs, dm, comp, specials)
				out+=expTxt
				
				pos=m.end()
				seq+=1
			else:
				# Copy the rest and stop
				out+=txt[pos:]
				break
		return out

	def nameNets(self, nets):
		netMap={}
		conflictMap={}
		renamePattern=re.compile(self.config["RenameNetPattern"])
		groundNets=set(self.config["GroundNets"])
		ndx=1
		for name in nets.keys():
			# Check if it is a ground node
			if name in groundNets:
				name2="0"
				netMap[name]=name2
				continue
			
			# Lowercase
			name2=name.lower()
			
			if renamePattern.search(name):
				# Generated net (matches RenamedNetPatter)
				if self.config["EnumerateNets"]:
					if self.config["NetNumbers"] is not None:
						name2="%s%0*d" % (self.config["NetPrefix"], self.config["NetNumbers"], ndx)
					else:
						name2="%s%d" % (self.config["NetPrefix"], ndx)
					ndx+=1
				else:
					# Translate +- to pn
					name2=name2.replace("+", "p")
					name2=name2.replace("-", "n")
					
					# Replace bad characters
					name2=badCharsPat.sub("_", name2)
			else:
				# Strip leading slash, 
				if name2[0]=="/":
					name2=name2[1:]
					
				# Convert slashes to underscores
				name2=name2.replace("/", "_")
				
				# Translate +- to pn
				name2=name2.replace("+", "p")
				name2=name2.replace("-", "n")
				
				# Replace bad characters
				name2=badCharsPat.sub("_", name2)
				
			if not nodeCharsPat.search(name2):
				# Bad chars found
				raise PyNetlisterError("Net name '"+name2+"' is not valid.")
			
			if not nodePat.search(name2):
				# No bad chars, but needs a leading underscore
				name2="_"+name2
				
			netMap[name]=name2
			
			if name2 in conflictMap:
				raise PyNetlisterError("Node name conflict at translated node '"+name2+"'. Check nodes '"+conflictMap[name2]+"' and '"+name2+"'.")
			
			conflictMap[name2]=name
			
		return netMap

	def scanComponents(self, data, netMap):
		# Scan components, prepare slots for nets
		comps={}
		for name, desc in data["components"].items():
			libsource=desc["libsource"]
			fields=desc["fields"] if "fields" in desc else {}
			
			# Special devices are handled separately
			if ((symbolLib is None or libsource[0]==symbolLib) and libsource[1] in specialComponents):
				continue
				
			# Lowercase name
			name1=name.lower()
			
			# Find in config["Mapping"]
			if libsource in self.config["Mapping"]:
				# Exact match 
				dm=self.config["Mapping"][libsource]
			elif (None, libsource[1]) in self.config["Mapping"]:
				# Component name matches Mapping entry with None library (any library)
				dm=self.config["Mapping"][None, libsource[1]]
			else:
				# Default device map
				dm=self.config["Mapping"][None, None]
			
			# Check name validity (lowercase name), report error with original name
			if not instPat.search(name1):
				raise PyNetlisterError("Component name '"+name+"' is not valid.") 
			
			# Check first character of name
			if "NamePrefix" in fields:
				pfx=fields["NamePrefix"].lower()
			elif "NamePrefix" in dm:
				pfx=dm["NamePrefix"].lower()
			else:
				pfx=None
			if pfx is not None and name1[0].lower()!=pfx:
				# Prepend letter
				name1=pfx+name1
			
			comps[name]={
				"nameOrig": name.lower(), 
				"name": name1, 
				"slots": {}, 
				"libsource": libsource, 
				"modelName": None, 
				"fields": desc["fields"] if "fields" in desc else {}
			}
			
			# Parameters field
			if "Parameters" in fields:
				parameters=fields["Parameters"].split(" ")
			elif "Parameters" in dm:
				parameters=dm["Parameters"]
			else:
				parameters=[]
			
			# Handle value as parameter
			if "ValueField" in fields:
				valuefield=fields["ValueFields"]
			elif "ValueField" in dm:
				valuefield=dm["ValueField"]
			else:
				valuefield=None
			
			# Add value as a new field named valuefield
			if valuefield is not None and "value" in desc: 
				# Get value
				fields[valuefield]=desc["value"]
			
			# Handle fields
			params={}
			ptmp=set(parameters)
			specifiedParameters=[]
			for fieldName, fieldValue in fields.items():
				# Handle Model field (SPICE model override)
				if fieldName=="Model":
					comps[name]["modelName"]=fieldValue
				if fieldName in ptmp:
					specifiedParameters.append(fieldName)
			
			# List of allowed parameter names
			comps[name]["parameters"]=parameters
			
			# List of specified parameters
			comps[name]["specifiedParameters"]=specifiedParameters
			
		# Scan nets, connect pins
		for name, desc in data["nets"].items():
			# SPICE net name
			netName=netMap[name]
			
			for comp, pinnum in desc["pins"]:
				comps[comp]["slots"][pinnum]=netName
		
		# Group components by sheets
		compList={}
		for sheet in data["design"]["sheetOrder"]:
			compList[sheet]=[]
		
		# Go through original names
		for compName in data["componentOrder"]:
			# For specials
			if compName not in comps:
				continue
			
			desc=comps[compName]
			sheetpath=data["components"][compName]["sheetpath"]["names"]
			
			compList[sheetpath].append(compName)
		
		return compList, comps

	def scanSpecials(self, data):
		specials={
			'includeTop': [], 
			'includeBottom': [], 
			'include': {}, 
			
			'paramTop': [], 
			'param': {}, 
			
			'subckt': None, 
			
			'subcktParamTop': [], 
			'subcktParam': {}, 
			
			'modelTop': [], 
			'model': {}, 
			
			'outFile': None, 
			
			'suppressEnd': False, 
		}
		
		for name, desc in data["components"].items():
			libsource=desc["libsource"]
			
			# Skip components that are not special symbols
			if not ((symbolLib is None or libsource[0]==symbolLib) and libsource[1] in specialComponents):
				continue
			
			# Extract number
			if name[0]!="a" and name[0]!="A":
				raise PyNetlisterError("Bad directive refdes (should start with 'A').")
			if not numberPat.search(name[1:]):
				raise PyNetlisterError("Bad directive refdes. 'A' should be followed by a number.")
			refnum=int(name[1:])
			
			# Extract position
			fields=desc["fields"] if "fields" in desc else {}
			positionTop=False
			if "Position" in fields:
				if fields["Position"]=='top':
					positionTop=True
				elif fields["Position"]=='bottom':
					positionTop=False
				else:
					raise PyNetlisterError("Position field should be 'top' or 'bottom'.")
			
			# Handle directive
			if libsource[1] in ["INCLUDE", "LIB"]:
				refnumList=specials["includeTop"] if positionTop else specials["includeBottom"]
				refnumList.append(refnum)
				if libsource[1]=="INCLUDE":
					specials["include"][refnum]=fields["Filename"]
				else:
					specials["include"][refnum]=(fields["Filename"], fields["Section"])
			elif libsource[1]=="MODEL": 
				specials["modelTop"].append(refnum)
				
				mname=fields["Name"].lower()
				if not modelPat.search(mname):
					raise PyNetlisterError("Model name '"+mname+"' is not valid.") 
				
				# NPN PNP NJF PJF NMT PMT NMOS PMOS SW CSW R C D LTRA URC
				mtype=fields["Type"].lower()
				
				mdef=fields["Specification"].lower()
				
				specials["model"][refnum]=(mname, mtype, mdef)
			elif libsource[1]=="PARAM": 
				specials["paramTop"].append(refnum)
				
				pname=fields["Name"]
				if not paramPat.search(pname):
					raise PyNetlisterError("Parameter name '"+pname+"' is not valid.") 
				
				specials["param"][refnum]=(pname, fields["Expression"])
			elif libsource[1]=="SUBCKT_PARAM": 
				specials["subcktParamTop"].append(refnum)
				
				pname=fields["Name"]
				if not paramPat.search(pname):
					raise PyNetlisterError("Subcircuit parameter name '"+pname+"' is not valid.") 
				defval=fields["Default"] if "Default" in fields and len(fields["Default"])>0 else None
				
				specials["subcktParam"][refnum]=(pname, defval)
			elif libsource[1]=="SUBCKT": 
				if specials["subckt"] is not None:
					raise PyNetlisterError("There can be only one SUBCKT directive per hierarchy.") 
				
				sname=fields["Name"]
				if not modelPat.search(sname):
					raise PyNetlisterError("Subcircuit name '"+sname+"' is not valid.") 
				specials["subckt"]=(sname, fields["Pins"])
			elif libsource[1]=="OUTPUT_FILE": 
				if specials["outFile"] is not None:
					raise PyNetlisterError("There can be only one OUTPUT_FILE directive per hierarchy.") 
				
				fname=fields["Name"]
				if os.path.isabs(fname):
					raise PyNetlisterError("OUTPUT_FILE may not be an absolute path.") 
				specials["outFile"]=fname
			elif libsource[1]=="SUPPRESS_END": 
				specials["suppressEnd"]=True
			
		# Sort by refdes number
		specials["includeTop"].sort()
		specials["modelTop"].sort()
		specials["includeBottom"].sort()
		specials["paramTop"].sort()
		specials["subcktParamTop"].sort()
		
		# Organize texts
		textTop=[]
		textBottom=[]
		for num, textDesc in data["texts"].items():
			if textDesc["position"]=="top":
				textTop.append(num)
			else:
				textBottom.append(num)
				
		specials["textTop"]=sorted(textTop)
		specials["textBottom"]=sorted(textBottom)
		
		return specials

	def dump(self, data, compList, comps, specials):
		txt=""
		
		# Dump include/lib top
		for refnum in specials["includeTop"]:
			inc=specials["include"][refnum]
			if type(inc) is tuple:
				txt+=".lib '"+inc[0]+"' "+inc[1]+"\n"
			else:
				txt+=".include "+inc+"\n"
		if len(specials["includeTop"])>0:
			txt+="\n"
		
		# Dump top verbatim texts (ordered by number)
		for num in specials["textTop"]:
			textDesc=data["texts"][num]
			txt+="* Verbatim block Text%d from sheet %s\n" % (num, textDesc["sheet"])
			txt+=textDesc["text"]
			txt+="\n"
		if len(specials["textTop"])>0:
			txt+="\n"
			
		# Dump subckt head
		if specials["subckt"] is not None:
			sub=specials["subckt"]
			txt+=".subckt "+sub[0]+" "+sub[1]
			
			# Dump parameters
			subpar=specials["subcktParamTop"]
			if len(subpar)>0:
				txt+="\n+ param: "
				txt+=" ".join(
					[
						specials["subcktParam"][num][0]+
						(
							("="+specials["subcktParam"][num][1])
							if specials["subcktParam"][num][1] is not None
							else ""
						)
						for num in subpar
					]
				)
			txt+="\n"
		txt+="\n"
		
		# Dump params
		for num in specials["paramTop"]:
			par=specials["param"][num]
			txt+=".param "+par[0]+"="+par[1]+"\n"
		if len(specials["paramTop"])>0:
			txt+="\n"
			
		# Dump models
		for num in specials["modelTop"]:
			par=specials["model"][num]
			txt+=".model "+par[0]+" "+par[1]+" ("+par[2]+")\n"
		if len(specials["modelTop"])>0:
			txt+="\n"
		
		# Dump components
		for sheetName in data["design"]["sheetOrder"]:
			txt+="* Sheet: "+sheetName+"\n"
			# Go through components by their original name
			for compName in compList[sheetName]:
				desc=comps[compName]
				fields=desc["fields"] if "fields" in desc else {}
				
				# Get libsource
				libsource=desc["libsource"]
				
				# Use default config["Mapping"] entry if exact match is not found
				if libsource in self.config["Mapping"]:
					# Exact match
					dm=self.config["Mapping"][libsource]
				elif (None, libsource[1]) in self.config["Mapping"]:
					# Match the entry with None library (any library)
					dm=self.config["Mapping"][(None, libsource[1])]
				else:
					# Default mapping
					dm=self.config["Mapping"][None, None]
				
				# Build error template
				if libsource in self.config["Mapping"]:
					# Exact match
					errorTemplate="(%s,%s) %s, using exact mapping match" % (libsource[0], libsource[1], compName)
				elif (None, libsource[1]) in self.config["Mapping"]:
					# Match entry with None for library (any library)
					errorTemplate="(%s,%s) %s, using any library mapping match" % (libsource[0], libsource[1], compName)
				else:
					# Default entry
					errorTemplate="(%s,%s) %s, using default mapping" % (libsource[0], libsource[1], compName)
					
				if "OutPattern" in fields: 
					pattern=fields["OutPattern"]
				elif "OutPattern" in dm:
					pattern=dm["OutPattern"]
				else:
					raise PyNetlisterError(
						"%s: OutPattern is not defined." % (errorTemplate)
					)
				txt+=self.substituteMacros(pattern, errorTemplate, dm, desc, specials)+"\n"
			txt+="\n"
			
		# Dump subckt tail
		if specials["subckt"] is not None:
			txt+=".ends\n\n"
		
		# Dump bottom verbatim texts (ordered by number)
		for num in specials["textBottom"]:
			textDesc=data["texts"][num]
			txt+="* Verbatim block Text%d from sheet %s\n" % (num, textDesc["sheet"])
			txt+=textDesc["text"]
			txt+="\n"
		if len(specials["textBottom"])>0:
			txt+="\n"
		
		# Dump include/lib bottom
		for refnum in specials["includeBottom"]:
			inc=specials["include"][refnum]
			if type(inc) is tuple:
				txt+=".lib '"+inc[0]+"' "+inc[1]+"\n"
			else:
				txt+=".include "+inc+"\n"
		if len(specials["includeBottom"])>0:
			txt+="\n"
		
		# Suffix (.end)
		if not (self.config["SuppressEnd"] or specials["suppressEnd"] or specials["subckt"] is not None):
			txt+=".end\n"
		
		return txt
		
	
	def __call__(self, inFile, outFile, configFile=None):
		"""
		Returns a string representing the Spice Opus netlist generated from 
		the data structure read from a KiCAD XML netlist. 
		"""
		# Read XML netlist
		data=readKicadXML(inFile)
		
		# Generate nice names for nets
		netMap=self.nameNets(data["nets"])
		
		# Go through all devices
		compList, comps = self.scanComponents(data, netMap)
		
		# Scan specials
		specials=self.scanSpecials(data)
		
		# Determine output file
		head, tail = os.path.split(outFile)
		if specials["outFile"] is not None:
			outFile=os.path.join(head, specials["outFile"])
		
		txt=""
		txt+="*********\n"
		txt+="* SPICE OPUS netlister for KiCad\n"
		txt+="* (c)2017 EDA Lab FE Uni-Lj\n"
		txt+="*\n"
		txt+="* Netlister : KiCad -> Spice Opus\n"
		
		if configFile is None:
			txt+="* Config    : default used\n"
		else:
			txt+="* Config    : %s\n" % (configFile)
		
		txt+="* Source    : "+data["design"]["source"]+"\n"
		txt+="* XML input : "+inFile+"\n"
		txt+="* Output    : "+outFile+"\n"
		txt+="* Date      : "+data["design"]["date"]+"\n"
		txt+="* Tool      : "+data["design"]["tool"]+"\n"
		ii=1
		for shname in data["design"]["sheetOrder"]:
			shsrc=data["design"]["sheets"][shname]["source"]
			txt+="* Sheet %-3d : %s -- %s\n" % (ii, shname, shsrc)
			ii+=1
		txt+="*********\n\n"
		
		# Dump
		txt+=self.dump(data, compList, comps, specials)
		
		return txt, outFile
	

if __name__=="__main__":
	from kicadxml import readKicadXML
	import sys
	
	filename=sys.argv[1]
	
	data=readKicadXML(filename)
	txt=spiceOutput(data)
	
	print(txt)
