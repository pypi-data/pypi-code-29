from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .style import enableWidget
from .table import *
from .delegates import QPComboBox
from .dumptools import validateIdentifier, validateAlphanumeric, readNumeric, QPDumpError

from ..design.cbd import generateCorners
from .. import PyOpusError

import itertools

__all__ = [ "QPWizardCorners" ]


class QPCornerGenError(PyOpusError):
	def __init__(self, message, *args):
		super(QPCornerGenError, self).__init__(message, *args)

class QPWizardCorners(QWizard):
	def __init__(self, data, parent=None, *args):
		QWizard.__init__(self, parent=parent, *args)
		
		self.addPage(HeadsPage(data))
		self.addPage(ModulesPage(data))
		self.addPage(ParametersPage(data))
		self.addPage(NamingPage(data))
		self.pp=PreviewPage(data)
		self.addPage(self.pp)
	
		self.setWindowTitle("Corners Wizard")
		
		self.setMaximumHeight(600)
	
	# No need to define accept, caller can check the ok member
	
	def output(self):
		if self.result()==QDialog.Accepted:
			return self.pp.corners
		else:
			return None
		
class HeadsPage(QWizardPage):
	def __init__(self, data, parent=None, *args):
		QWizardPage.__init__(self, parent=parent, *args)
		
		self.data=data
		
		self.first=True
		
		self.opBox=QCheckBox("Include operating parameters", self)
		self.statBox=QCheckBox("Include statistical parameters", self)
		
		self.setTitle("Simulator setups and parameters")
		
		self.registerField("includeop", self.opBox)
		self.registerField("includestat", self.statBox)
		
		layout=QVBoxLayout(self)
		
		l=QLabel(
			"Simulator setups to generate corners for (select at least one)\n"+ 
			"The set of input file modules is the intersection across selected simulator setups."
		)
		l.setWordWrap(True)
		
		w=QWidget()
		vl=QVBoxLayout(w)
		self.headBoxes=[]
		for ii in range(len(self.data['heads'])):
			hn=self.data['heads'][ii][0]
			cb=QCheckBox(hn, self)
			self.registerField("head"+str(ii), cb)
			self.headBoxes.append(cb)
			cb.stateChanged.connect(self.pageChanged)
			vl.addWidget(cb)
		w.setLayout(vl)
		
		editorScroller=QScrollArea(parent=self)
		editorScroller.setWidgetResizable(True)
		editorScroller.setWidget(w)
		
		layout.addWidget(l)
		layout.addWidget(editorScroller)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(self.opBox)
		layout.addWidget(self.statBox)
		
		layout.addStretch(1)
		self.setLayout(layout)
	
	def initializePage(self):
		# Initialize only the first time this function is called
		if not self.first:
			return
		self.first=False
		
		self.setField("includeop", True)
		self.setField("includestat", True)
		
	# Disable cleanup, keep last set values
	def cleanupPage(self):
		pass
	
	def isComplete(self):
		# At least one head must be selected
		for ii in range(len(self.data['heads'])):
			if self.field("head"+str(ii)):
				return True
		return False
	
	# Trigger when something that affects the state of the Next button is changed
	@pyqtSlot(int)
	def pageChanged(self, flag):
		self.completeChanged.emit()
	
	
class QPModulesTableModel(QPTableModel):
	def __init__(self, data, parent=None, *args):
		QPTableModel.__init__(
			self, data, 
			header=[ "Group name", "Module name", "Alias"], 
			editable=[ True, False, True ], 
			sortingIndices=[], 
			parent=None, *args
		)
	
	def data(self, index, role):
		if not index.isValid():
			return None
		elif role == Qt.DisplayRole or role == Qt.EditRole:
			row=index.row()
			col=index.column()
			return QVariant(self.mylist[row][col])
		else:
			return None
	
	def setData(self, index, value, role):
		row=index.row()
		col=index.column()
		if col>=0 or col<=2:
			self.mylist[row][col]=value
			self.dataChanged.emit(index, index)
			return True
		
		return False
	
class ModulesPage(QWizardPage):
	def __init__(self, data, parent=None, *args):
		QWizardPage.__init__(self, parent=parent, *args)
		self.data=data
		
		self.oldHeadNdxs=[]
		
		self.table=[]
		
		self.setTitle("Module groups")
		self.tableModel=QPModulesTableModel(self.table, parent=self)
		self.tableWidget=QPTable(self.tableModel, canCreate=False, canDelete=False, parent=self)
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		
		self.registerField("modulemodel", self.tableWidget, "dataModel")
		
		layout=QVBoxLayout(self)
		
		l=QLabel(
			"Modules are gouped based on the group name in this table. "
			"In every corner one module from every group is included. "+
			"If you don't want any of the listed modules in the generated corners, "+
			"you can delete the row or set the group name to an empty string. "+
			"Aliases can be incorporated into the names of the generated corners. "
		)
		l.setWordWrap(True)
		
		layout.addWidget(l)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(self.tableWidget)
		
		layout.addStretch(1)
		self.setLayout(layout)
		
	def initializePage(self):
		# Initialize always
		headNdxs=[]
		for ii in range(len(self.data["heads"])):
			if self.field("head"+str(ii)):
				headNdxs.append(ii)
		
		# Skip initialization if head index is left unchanged
		if set(self.oldHeadNdxs)==set(headNdxs):
			return 
		self.oldHeadNdxs=headNdxs
		
		# Prepare sets 
		sets=[]
		for ii in headNdxs:
			sets.append(
				set([m[0] for m in self.data['heads'][ii][1]['moddefs']])
			)
		
		# Intersection
		mods=None
		for s in sets:
			if mods is None:
				mods=s
			else:
				mods=mods.intersection(s)
		
		mods=list(mods)
		mods.sort()
		self.table=[['', m, m] for m in mods]
		self.tableModel=QPModulesTableModel(self.table, parent=self)
		self.tableWidget.setModel(self.tableModel)
	
	# Disable cleanup, keep last set values
	def cleanupPage(self):
		pass
	
class QPParamsTableModel(QPTableModel):
	def __init__(self, data, parent=None, *args):
		QPTableModel.__init__(
			self, data, 
			header=[ "Name", "Value", "Alias"], 
			sortingIndices=[], 
			parent=None, *args
		)
	
	def data(self, index, role):
		if not index.isValid():
			return None
		elif role == Qt.DisplayRole or role == Qt.EditRole:
			row=index.row()
			col=index.column()
			return QVariant(self.mylist[row][col])
		else:
			return None
	
	def setData(self, index, value, role):
		row=index.row()
		col=index.column()
		if col>=0 or col<=2:
			self.mylist[row][col]=value
			self.dataChanged.emit(index, index)
			return True
		else:
			return False

class ParametersPage(QWizardPage):
	def __init__(self, data, parent=None, *args):
		QWizardPage.__init__(self, parent=parent, *args)
		self.data=data
		
		self.oldIncl=None
		
		self.table=[]
		
		self.setTitle("Parameter values")
		self.tableModel=QPParamsTableModel(self.table, parent=self)
		self.tableWidget=QPTable(self.tableModel, parent=self)
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		
		self.registerField("parammodel", self.tableWidget, "dataModel")
		
		layout=QVBoxLayout(self)
		
		l=QLabel(
			"Specify the values of parameters that will be used for building corners. "
			"Multiple valeus can be specified for one parameter (one per row). "+
			"Aliases can be incorporated into the names of the generated corners. "
		)
		l.setWordWrap(True)
		
		layout.addWidget(l)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(self.tableWidget)
		
		layout.addStretch(1)
		self.setLayout(layout)
		
	def initializePage(self):
		# Initialize only the first time
		incl=(self.field("includeop"), self.field("includestat"))
		
		if incl == self.oldIncl:
			return
		
		self.oldIncl=incl
		
		self.table=[]
		
		if self.field("includeop"):
			for opp in self.data['oppar']:
				self.table.append([opp[0], opp[2], ''])
				self.table.append([opp[0], opp[3], ''])
		
		if self.field("includestat"):
			for sp in self.data['statpar']:
				self.table.append([sp[0], '0.0', ''])
					
		self.tableModel=QPParamsTableModel(self.table, parent=self)
		self.tableWidget.setModel(self.tableModel)
	
	# Disable cleanup, keep last set values
	def cleanupPage(self):
		pass
	
class NamingPage(QWizardPage):
	def __init__(self, data, parent=None, *args):
		QWizardPage.__init__(self, parent=parent, *args)
		self.data=data
		
		self.first=True
		
		self.setTitle("Naming the corners")
		
		self.prefixBox=QLineEdit(self)
		self.enumerateCheckbox=QCheckBox(self)
		self.startBox=QLineEdit(self)
		
		self.registerField("prefix", self.prefixBox, "text")
		self.registerField("enumerate", self.enumerateCheckbox)
		self.registerField("start", self.startBox)
		
		layout=QVBoxLayout(self)
		
		l=QLabel(
			"Set the prefix and enumeration of corners. If module name and parameter value "+
			"alisases will be included in the corner name. "
		)
		l.setWordWrap(True)
		
		layout.addWidget(l)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Name prefix", self))
		layout.addWidget(self.prefixBox)
		layout.addSpacing(2*layout.spacing())
		self.enumerateCheckbox.setText("Enumerate corners")
		layout.addWidget(self.enumerateCheckbox)
		layout.addSpacing(2*layout.spacing())
		layout.addWidget(QLabel("Start enumeration at", self))
		layout.addWidget(self.startBox)
		
		self.enumerateCheckbox.stateChanged.connect(self.onEnumerateChanged)
		
		layout.addStretch(1)
		self.setLayout(layout)
	
	@pyqtSlot(int)
	def onEnumerateChanged(self, newVal):
		enableWidget(self.startBox, newVal)
	
	def initializePage(self):
		# Initialize only the first time this function is called
		if not self.first:
			return
		self.first=False
		
		self.setField("prefix", "c")
		self.setField("enumerate", True)
		self.setField("start", 1)
		
	# Disable cleanup, keep last set values
	def cleanupPage(self):
		pass
	
class PreviewPage(QWizardPage):
	def __init__(self, data, parent=None, *args):
		QWizardPage.__init__(self, parent=parent, *args)
		self.data=data
		
		self.ok=False
		
		self.reportBox=QPlainTextEdit(self)
		self.reportBox.setReadOnly(True)
		
		layout=QVBoxLayout(self)
		
		l=QLabel(
			"Set the prefix and enumeration of corners. If module name and parameter value "+
			"alisases will be included in the corner name. "
		)
		l.setWordWrap(True)
		
		layout.addWidget(self.reportBox)
		
		self.setLayout(layout)
		
	def initializePage(self):
		# Collect module groups
		headNames=[]
		for ii in range(len(self.data['heads'])):
			if self.field("head"+str(ii)):
				headNames.append(self.data['heads'][ii][0])
		
		self.ok=False
		
		try:
			# Collect aliases, verify module names, collect groups
			groups={}
			groupAliases={}
			groupOrder=[]
			modNameSet=set([])
			for row in self.field("modulemodel").dataTable():
				grpName=row[0].strip()
				modName=row[1].strip()
				alias=row[2].strip()
				
				# Skip modules with no group
				if len(grpName)<=0:
					continue
				
				if not validateIdentifier(modName):
					raise QPCornerGenError("Module name '"+modName+"' is not a valid identifier.")
				
				if modName in modNameSet:
					raise QPCornerGenError("Module name '"+modName+"' appears twice in modules table.")
				modNameSet.add(modName)
				
				if grpName not in groups:
					groupOrder.append(grpName)
					groups[grpName]=[]
					groupAliases[grpName]=[]
				
				groups[grpName].append(modName)
				
				if len(alias)>0:
					if not validateAlphanumeric(alias):
						raise QPCornerGenError("Alias '"+alias+"' for module '"+modName+"' is not an alphanumeric string.")
					groupAliases[grpName].append(alias.lower())
				else:
					groupAliases[grpName].append(None)
				
			# Collect parameters
			params={}
			paramAliases={}
			paramOrder=[]
			for row in self.field("parammodel").dataTable(): 
				paramName=row[0].strip()
				paramValue=row[1].strip()
				alias=row[2].strip()
				
				if not validateIdentifier(paramName):
					raise QPCornerGenError("Parameter name '"+modName+"' is not a valid identifier.")
				
				try:
					paramParsed=readNumeric(paramValue)
				except QPDumpError as e:
					raise QPCornerGenError("Failed to parse value '"+paramValue+"' for parameter '"+paramName+"'. \n"+str(e))
				
				if paramName not in params:
					paramOrder.append(paramName)
					params[paramName]=[]
					paramAliases[paramName]=[]
				
				params[paramName].append((paramValue, paramParsed))
			
				if len(alias)>0:
					if not validateAlphanumeric(alias):
						raise QPCornerGenError("Alias '"+alias+"' for '"+paramName+"'='"+paramValue+"' is not an alphanumeric string.")
					paramAliases[paramName].append(alias.lower())
				else:
					paramAliases[paramName].append(None)
				
			pfx=self.field("prefix")
			if not validateIdentifier(pfx):
				raise QPCornerGenError("Corner name prefix '"+pfx+"' is not a valid identifier.")
			
			enum=self.field("enumerate")
			
			try:
				start=int(self.field("start"))
			except Exception as e:
				raise QPCornerGenError("Bad initial value for enumeration.\n"+str(e))
			
			
			# Generate corners
			specs=[]
			for grpName in groups:
				specs.append(
					( 'model', grpName, groups[grpName], groupAliases[grpName] )
				)
			for paramName in params:
				specs.append(
					('param', paramName, [param[0] for param in params[paramName]], paramAliases[paramName])
				)
			cdict, cnames = generateCorners(specs, headNames, pfx.lower(), start if enum else None)
			
			s=set([])
			corners=[]
			txtc=''
			for cname in cnames:
				txtc+='  '+cname+'\n'
				if cname in s:
					raise QPCornerGenError(
						"Duplicate corner name '"+cname+"'. \n"+
						"Turn on corner numbering or check all module names and parameter values have unique aliases. \n\n"+
						"Generated corner names: \n"+txtc
					)
				
				s.add(cname)
				c=cdict[cname]
				corner={ 
					'heads': [ [ hn ] for hn in headNames], 
					'modules': [ [ m ] for m in c['modules'] ], 
					'params': [ [ pname, c['params'][pname] ] for pname in paramOrder  ], 
				}
				corners.append([cname, corner ])
			
			# Prepare output
			txt=str(len(cnames))+" corner(s) generated. \n"
			txt+=txtc
				
			self.ok=True
			self.corners=corners
			
		except QPCornerGenError as e:
			txt=str(e)
		
		self.reportBox.setPlainText(txt)
		if self.ok:
			self.setTitle("Confirm generated corners")
		else: 
			self.setTitle("Error")
	
	def isComplete(self):
		return self.ok
	
if __name__ == '__main__':
	from pprint import pprint
	import sip 
	import sys
	import sampledata
	sip.setdestroyonexit(True)

	app = QApplication(sys.argv)
	
	w=QPWizardCorners(sampledata.data)
	w.setModal(True)
	w.exec_()
	
	corners = w.output()
	if corners is not None:
		pprint(corners)
	else:
		print("Failed")
		
	
	
	
	

