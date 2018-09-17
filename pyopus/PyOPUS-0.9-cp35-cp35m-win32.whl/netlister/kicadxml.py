# -*- coding: UTF-8 -*-
"""
Module for importing KiCAD XML netlist. It also opens all .sch files
in the hierarchy including and under the sheet for which the XML file 
was generated and collects verbatim text blocks. 

The .sch files are assumed to be in the same folder as the intermediate XML 
netlist.  
"""

try:
	from lxml import etree
	# print("running with lxml.etree")
except ImportError:
	try:
		# Python 2.5
		import xml.etree.cElementTree as etree
		# print("running with cElementTree on Python 2.5+")
	except ImportError:
		try:
			# Python 2.5
			import xml.etree.ElementTree as etree
			# print("running with ElementTree on Python 2.5+")
		except ImportError:
			try:
				# normal cElementTree install
				import cElementTree as etree
				# print("running with cElementTree")
			except ImportError:
				try:
					# normal ElementTree install
					import elementtree.ElementTree as etree
					# print("running with ElementTree")
				except ImportError:
					raise ImportError("Failed to import ElementTree from any known place")	

import re, sys, os
from pyopus.netlister import PyNetlisterError


__all__ = [ "readKicadXML" ]


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def readSheet(node):
	sheet={}
	
	sheet["attrib"]=node.attrib 
	
	tblock=node.find("title_block")
	for cname in ["title", "company", "rev", "date", "source"]:
		el=tblock.find(cname)
		sheet[cname]=el.text
	
	n=[]
	t=[]
	for c in tblock.findall("comment"):
		a=c.attrib
		n.append(a["number"])
		t.append(a["value"])
	ii=argsort(n)
	sheet["comments"]=[t[ndx] for ndx in ii]
	
	return sheet
	
def readDesign(node):
	sheets={}
	sheetOrder=[]
	data={ 
		"sheets": sheets, 
		"sheetOrder": sheetOrder, 
	}
	
	for c in node:
		if c.tag in set(["source", "date", "tool"]):
			data[c.tag]=c.text
		elif c.tag=="sheet":
			sheet=readSheet(c)
			name=sheet["attrib"]["name"]
			sheets[name]=sheet
			sheetOrder.append(name)
			
	return data

def readComponents(node):
	components={}
	componentOrder=[]
	for c in node:
		ref=c.attrib["ref"]
		desc={}
		for ca in c:
			if ca.tag=="fields":
				fields={}
				for f in ca:
					name=f.attrib["name"]
					fields[name]=f.text
				desc["fields"]=fields
			elif ca.tag=="libsource":
				desc["libsource"]=(ca.attrib["lib"], ca.attrib["part"])
			elif ca.tag=="sheetpath":
				d={}
				d.update(ca.attrib)
				desc["sheetpath"]=d
			else:
				 # Ordinary attribute
				 desc[ca.tag]=ca.text
		components[ref]=desc
		componentOrder.append(ref)
		
	return components, componentOrder

def readLibparts(node):
	libparts={}
	for c in node:
		tag=(c.attrib["lib"], c.attrib["part"])
		df=c.find("description")
		description=df.text if df is not None else None
		fields={}
		for field in c.find("fields"):
			fields[field.attrib["name"]]=field.text
		pins={}
		pinOrder=[]
		pn=c.find("pins")
		if pn is not None:
			for pin in c.find("pins"):
				d={}
				d.update(pin.attrib)
				if "num" in d:
					num=int(d["num"])
					del d["num"]
				pins[num]=d
				pinOrder.append(num)
		
		libparts[tag]={
			"fields": fields, 
			"pins": pins, 
			"pinOrder": sorted(pinOrder)
		}
	
		# Get aliases, link alias entries to original
		al=c.find("aliases")
		if al is not None:
			for alias in al:
				tag1=(tag[0],alias.text)
				libparts[tag1]=libparts[tag]
			
	
	return libparts

def readLibraries(node):
	libraries={}
	for c in node:
		name=c.attrib["logical"]
		src=c.find("uri").text
		libraries[name]=src
		
	return libraries

def readNets(node):
	nets={}
	for c in node:
		code=c.attrib["code"]
		name=c.attrib["name"]
		
		pinlist=[]
		for n in c:
			pinlist.append(
				(n.attrib["ref"], int(n.attrib["pin"]))
			)
		nets[name]={
			"code": code, 
			"pins": pinlist
		}
		
	return nets

textSchPat=re.compile("^Text Notes .*$", flags=re.MULTILINE)
verbatimTextPat=re.compile(r"^\s*Text([1-9][0-9]*)[ \t]+position[ \t]*=[ \t]*(top|bottom)\s*(.*)$", flags=re.MULTILINE)

def collectTexts(xmlFile, data):
	data["texts"]={}
	
	# Look in the input XML file folder
	head, tail = os.path.split(xmlFile)
	
	# Go through sheets, open schematic files, and extract text blocks
	for name, sheet in data["design"]["sheets"].items():
		source=sheet["source"]
		
		try:
			with open(os.path.join(head, source), "r") as f:
				txt=f.read(-1)
		except IOError:
			raise PyNetlisterError("Failed to read schematic file '"+source+"'.")
		
		# Find text blocks
		for match in textSchPat.finditer(txt):
			if match:
				pos=match.end()
				#print("1-")
				#print(txt[pos:pos+100])
				#print("--1")
				
				# Parse text block
				match=verbatimTextPat.search(txt, pos)
				if match:
					num=int(match.group(1))
					position=match.group(2)
					# Get rid of escape sequences
					text=match.group(3).encode("utf-8").decode("unicode_escape").strip()
					# print("Number:   %d" % num)
					# print("Position: "+position)
					# print("Text:     "+text)
					# print("")
					textDesc={
						"position": position, 
						"text": text, 
						"sheet": name
					}
					data["texts"][num]=textDesc
	
def readKicadXML(filename):
	"""
	Reads a KiCAD XML netlist from file *filename* and returns the netlist 
	as a Python structure. 
	"""
	data={}
	try:
		with open(filename, "r") as f:
			tree=etree.parse(filename)
			
			# <export>
			root=tree.getroot()
			data["version"]=root.attrib["version"]
			
			# Children (design, components, libparts, libraries, nets)
			for c in root:
				if c.tag=="design":
					data["design"]=readDesign(c)
				elif c.tag=="components":
					data["components"], data["componentOrder"] = readComponents(c)
				elif c.tag=="libparts":
					data["libparts"]=readLibparts(c)
				elif c.tag=="libraries":
					data["libraries"]=readLibraries(c)
				elif c.tag=="nets":
					data["nets"]=readNets(c)
		
		collectTexts(filename, data)
		
	except IOError:
		raise PyNetlisterError("Failed to open input file '"+filename+"'.")
		
	return data
		
if __name__ == "__main__":
	from pprint import pprint
	
	infile=sys.argv[1]
	
	pprint(readKicadXML(infile))
	
