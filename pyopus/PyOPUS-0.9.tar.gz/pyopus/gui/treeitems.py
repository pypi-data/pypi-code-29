from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from copy import deepcopy
import inspect

# Default values
from .values import *

# Editors
from .editnone import *
from .editinfo import *
from .editfiles import *
from .editfile import *
from .editheads import *
from .edithead import *
from .editvars import *
from .editvar import *
from .editanalyses import *
from .editanalysis import *
from .editmeasures import *
from .editmeasure import *
from .editdesignpar import *
from .editoppar import *
from .editstatpar import *

from .edittask import *

from .editcbdreq import *
from .editcbddesignpar import *
from .editcbdcorner import *
from .editcbdcorners import *
from .editcbdsettings import *
from .editcbdoutput import *

from .editmpi import *

from .editpostplots import *
from .editpostplot import *
from .editpostaxes import *
from .editposttrace import *

from .reswaveforms import *

from .rescbdcor import *
from .rescbdpar import *
from .rescbdperf import *
from .rescbdcost import *

# Task creators
from .cbdnew import *


__all__ = [ "QPTreeItem", "QPTreeItemProjectRoot", "QPTreeItemTasksRoot", "QPTreeItemInfo", 
		    "QPTreeItemSimulators", "QPTreeItemSimulator", "QPTreeItemFiles", "QPTreeItemFile", 
		    "QPTreeItemVariables", "QPTreeItemVariable", "QPTreeItemAnalyses", "QPTreeItemAnalysis", 
		    "QPTreeItemMeasures", "QPTreeItemMeasure", "QPTreeItemDesignPar", 
		    "QPTreeItemOpPar", "QPTreeItemStatPar", 
		    
		    "QPTreeItemTaskCBD", "QPTreeItemCBDRequirements", "QPTreeItemCBDDesignPar", 
		    "QPTreeItemCBDCorners", "QPTreeItemCBDCorner", "QPTreeItemCBDSettings",    
		    "QPTreeItemCBDOutput", "QPTreeItemMPI", 
		    
		    "QPTreeItemPostprocRoot", "QPTreeItemPostprocAspects", 
		    "QPTreeItemPostprocAspect", "QPTreeItemPostprocMeasures", 
		    "QPTreeItemPostprocPlots", "QPTreeItemPostprocPlot", 
		    "QPTreeItemPostprocAxes", "QPTreeItemPostprocTrace", 
		    
		    "itemEditorMap", "DefaultEditorClass", "name2class", "lowercasename2class", 
		    "taskItemTypes"
	]


# Some of the icons are from / based on
#   https://icons8.com

from pprint import pprint

def buildDictKeyIndex(dictKeys):
	if dictKeys is None:
		return None, None
	else:
		key2index={}
		for ii in range(len(dictKeys)):
			key, itemType = dictKeys[ii]
			key2index[key]=ii
			
		return dictKeys, key2index
	
# Base class for tree items
# Contains information what can be done with a node in the tree
# What can be done in the editor is defined in editor classes
class QPTreeItem(object):
	# dictKeys is a list of tuples/lists holding
	#  - data structure key 
	#  - item class 
	# for items whose children are stored in a dictionary. 
	# Index in this list is the child index. 
	
	# For every child index it provides a dictionary key and an item class
	
	# key2index is a map from data structure key to child index
	
	dictKeys, key2index = buildDictKeyIndex(None)
	
	def __init__(self, data, rootData, parentItem):
		self.data=data
		self.rootData=rootData
		self.parentItem=parentItem
		
	# Default implementation
	def name(self):
		return "Unnamed"
	
	# Parent item
	def parent(self):
		return self.parentItem
	
	# Default implementation
	def countChildren(self):
		return 0
	
	# Return data structure holding children
	# Assume no children are available and return None
	def childrenRepository(self):
		return None
	
	# Must override this method
	def childItem(self, ndx):
		return None
	
	# Icon
	def icon(self):
		return QIcon(":resources/file.png")
	
	def canRenameChildren(self):
		return False
	
	# Can delete children
	def canDeleteChildren(self):
		return False
	
	# Can move children 
	def canMoveChildren(self):
		return False
	
	# Can create children
	def canCreateChildren(self):
		return False
	
	# Can copy children
	def canCopyChildren(self):
		return True
	
	# Can select multiple children
	def canSelectMultipleChildren(self):
		return True
	
	# Rename child default implementation 
	# (assumes list of children, name is first element of child list)
	def renameChild(self, ndx, name):
		self.childrenRepository()[ndx][0]=name
		return True
	
	# Delete child default implementation (assumes list of children)
	def deleteChild(self, ndx):
		del self.childrenRepository()[ndx]
		return True
		
	# Move child default implementation (assumes list of children)
	def moveChild(self, src, dest):
		childrenRepository=self.childrenRepository()
		el=childrenRepository[src]
		childrenRepository.insert(dest, el)
		if src<=dest:
			childrenRepository.pop(src)
		else:
			childrenRepository.pop(src+1)
		return True
	
	# Create a child, no default implementation
	def createChild(self, ndx):
		pass
	
	# Return child template (by default no template is defined)
	def childTemplate(self):
		return None
	
	def copyChildren(self, indices):
		children=[]
		if self.dictKeys is not None:
			for ndx in indices:
				child=self.childItem(ndx)
				key=self.dictKeys[ndx][0]
				children.append((key, child.data))
		else:
			for ndx in indices:
				child=self.childItem(ndx)
				children.append(child.data)
		
		# Return payload (parent type name, [(child type name, data), ...])
		return (type(self).__name__, children)
	
	def pasteOverwrites(self):
		if self.dictKeys is not None:
			return True
		else:
			return False
	
	def canPasteChildren(self, lcItemClassName, position=-1):
		return lcItemClassName == type(self).__name__.lower()
			
	# Paste children, position is ignored when pasting in a dictionary. 
	# The type name is used instead for positioning a child. 
	# Position specifies the paste position (index assigned to the first pasted entry)
	# -1 denotes the entry after the current last entry
	def pasteChildren(self, payload, position=-1):
		if position<0:
			position+=self.countChildren()+1
		
		# Get children children repository 
		children=self.childrenRepository()
		
		# Build a list of pairs (index, data)
		ndxs=[]
		if self.dictKeys is not None:
			# Children in a dict
			for entry in payload[1]:
				key, data = entry
				ndx=self.key2index[key]
				cls=self.dictKeys[ndx][1]
				children[key]=data
				ndxs.append(ndx)
		else: 
			# Children in a list
			for ndx in range(len(payload[1])):
				data=payload[1][ndx]
				children.insert(position+ndx, data)
				ndxs.append(position+ndx)
			
		return ndxs
			 
# Level one items
	
# Info tree item
class QPTreeItemInfo(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Information"
	
	def icon(self):
		return QIcon(":resources/info.png")
	
# Files tree item
class QPTreeItemFiles(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Files & folders"
	
	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		return QPTreeItemFile(self.childrenRepository()[ndx], self.rootData, self)
	
	def icon(self):
		return QIcon(":resources/folder-open.png")
	
	def canRenameChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		self.childrenRepository().insert(ndx, deepcopy(self.childTemplate()))
		return True
	
	def childTemplate(self):
		return blankFile
	
# Heads tree item
class QPTreeItemSimulators(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Simulator setups"
	
	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		return QPTreeItemSimulator(self.childrenRepository()[ndx], self.rootData, self)
	
	def icon(self):
		return QIcon(":resources/heads.png")
	
	def canRenameChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		self.childrenRepository().insert(ndx, deepcopy(self.childTemplate()))
		return True
	
	def childTemplate(self):
		return blankHead
	
# Variables tree item
class QPTreeItemVariables(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Predefined variables"
	
	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		return QPTreeItemVariable(self.childrenRepository()[ndx], self.rootData, self)
	
	def icon(self):
		return QIcon(":resources/variables.png")
	
	def canRenameChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		self.childrenRepository().insert(ndx, deepcopy(self.childTemplate()))
		return True
	
	def childTemplate(self):
		return blankVariable
		
# Analyses tree item
class QPTreeItemAnalyses(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Analyses"
	
	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		return QPTreeItemAnalysis(self.childrenRepository()[ndx], self.rootData, self)
	
	def icon(self):
		return QIcon(":resources/analyses.png")
	
	def canRenameChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		self.childrenRepository().insert(ndx, deepcopy(self.childTemplate()))
		return True
	
	def childTemplate(self):
		return blankAnalysis
	
# Measures tree item
class QPTreeItemMeasures(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Measures"
	
	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		return QPTreeItemMeasure(self.childrenRepository()[ndx], self.rootData, self)
	
	def icon(self):
		return QIcon(":resources/measure.png")
	
	def canRenameChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		self.childrenRepository().insert(ndx, deepcopy(self.childTemplate()))
		return True
	
	def childTemplate(self):
		return blankMeasure
	
# Design parameters tree item
class QPTreeItemDesignPar(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Design parameters"
	
	def icon(self):
		return QIcon(":resources/designpar.png")
	
# Operating parameters tree item
class QPTreeItemOpPar(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Operating parameters"
	
	def icon(self):
		return QIcon(":resources/oppar.png")
	
# Statistical parameters tree item
class QPTreeItemStatPar(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Statistical parameters"
	
	def icon(self):
		return QIcon(":resources/statpar.png")
	
# Level two items

# File tree item
class QPTreeItemFile(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return self.data[0]

# Head tree item
class QPTreeItemSimulator(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return self.data[0]
	
	def icon(self):
		return QIcon(":resources/head.png")

# Variable tree item
class QPTreeItemVariable(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return self.data[0]
	
	def icon(self):
		return QIcon(":resources/variable.png")
	
# Analysis tree item
class QPTreeItemAnalysis(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return self.data[0]
	
	def icon(self):
		return QIcon(":resources/analysis.png")

# Measure tree item
class QPTreeItemMeasure(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return self.data[0]
	
	def icon(self):
		return QIcon(":resources/caliper.png")


# CBD requirements tree item
class QPTreeItemCBDRequirements(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Requirements"
	
	def icon(self):
		return QIcon(":resources/requirements.png")

# CBD design parameters tree item
class QPTreeItemCBDDesignPar(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Parameters"
	
	def icon(self):
		return QIcon(":resources/designpar.png")
	
# CBD corners tree item
class QPTreeItemCBDCorners(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Corners"	
	
	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		return QPTreeItemCBDCorner(self.childrenRepository()[ndx], self.rootData, self)
	
	def icon(self):
		return QIcon(":resources/corners.png")
	
	def canRenameChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		self.childrenRepository().insert(ndx, deepcopy(self.childTemplate()))
		return True
	
	def childTemplate(self):
		return blankCorner
	
# CBD settings tree item
class QPTreeItemCBDSettings(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Task settings"
	
	def icon(self):
		return QIcon(":resources/settings.png")
	
# CBD output tree item
class QPTreeItemCBDOutput(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Output"
	
	def icon(self):
		return QIcon(":resources/output.png")

# CBD output tree item
class QPTreeItemMPI(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "MPI settings"
	
	def icon(self):
		return QIcon(":resources/hosts.png")

# CBD corner tree item
class QPTreeItemCBDCorner(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return self.data[0]	
	
	def icon(self):
		return QIcon(":resources/corner.png")

# CBD task
class QPTreeItemTaskCBD(QPTreeItem):
	dictKeys, key2index = buildDictKeyIndex(
		[
			[ 'requirements', QPTreeItemCBDRequirements ],
			[ 'designpar', QPTreeItemCBDDesignPar ],
			[ 'corners', QPTreeItemCBDCorners ],
			[ 'settings', QPTreeItemCBDSettings ],
			[ 'output', QPTreeItemCBDOutput ],
			[ 'mpi', QPTreeItemMPI ],
		]
	)
	
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return self.data[0]
	
	def countChildren(self):
		return len(QPTreeItemTaskCBD.dictKeys)
	
	def childrenRepository(self):
		return self.data[1]
	
	def childItem(self, ndx):
		childKey=QPTreeItemTaskCBD.dictKeys[ndx][0]
		child=self.childrenRepository()[childKey]
		childClass=QPTreeItemTaskCBD.dictKeys[ndx][1]
		return childClass(child, self.rootData, self)
	
	def icon(self):
		return QIcon(":resources/cbd.png")

# Root project tree item	
class QPTreeItemProjectRoot(QPTreeItem):
	dictKeys, key2index = buildDictKeyIndex(
		[
			[ 'info', QPTreeItemInfo ],
			[ 'files', QPTreeItemFiles ],
			[ 'variables', QPTreeItemVariables ],
			[ 'heads', QPTreeItemSimulators ],
			[ 'analyses', QPTreeItemAnalyses ],
			[ 'measures', QPTreeItemMeasures ],
			[ 'designpar', QPTreeItemDesignPar ],
			[ 'oppar', QPTreeItemOpPar ],
			[ 'statpar', QPTreeItemStatPar ],
		]
	)
	
	def __init__(self, title, data, rootData, parentItem=None):
		QPTreeItem.__init__(self, data, rootData, parentItem)
		self.nodeName=title
	
	def name(self):
		return self.nodeName
	
	def countChildren(self):
		return len(QPTreeItemProjectRoot.dictKeys)
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		childData=self.childrenRepository()[QPTreeItemProjectRoot.dictKeys[ndx][0]]
		ChildClass=QPTreeItemProjectRoot.dictKeys[ndx][1]
		return ChildClass(childData, self.rootData, self)

# Root tasks tree item	
class QPTreeItemTasksRoot(QPTreeItem):
	def __init__(self, data, rootData, parentItem=None):
		QPTreeItem.__init__(self, data, rootData, parentItem)
		
	def name(self):
		return "Design tasks"
	
	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		childData=self.childrenRepository()[ndx]
		return QPTreeItemTaskCBD(childData, self.rootData, self)
	
	def canRenameChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		# Start a wizard, for now only create a new CBD task
		tmp=newCBDTask(self.rootData)
		self.childrenRepository().insert(ndx, tmp)
		return True

		
#
# Result viewer aspects
#

aspectIconMap={
	("SQLDataTaskCBD", "aggregator"): ":resources/scales.png", 
	
	("SQLDataCorners", "corners"): ":resources/corners.png",
	
	("SQLDataOptIter", "parameters"): ":resources/designpar.png",
	("SQLDataOptIter", "performance"): ":resources/measure.png",
	("SQLDataOptIter", "cost"): ":resources/scales.png", 
	
	("SQLDataConclusion", "summary"): ":resources/sum.png", 
}
		
# Aspects tree item
class QPTreeItemPostprocAspect(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
		# Aspect name is data, root record is rootData
		
	def name(self):
		return self.data
	
	def icon(self):
		key=(self.rootData['record'].typename, self.data)
		if key in aspectIconMap:
			return QIcon(aspectIconMap[key])
		else:
			return QPTreeItem.icon(self)
	
class QPTreeItemAspectProject(QPTreeItemPostprocAspect):
	def __init__(self, data, rootData, parentItem):
		QPTreeItemPostprocAspect.__init__(self, data, rootData, parentItem)

class QPTreeItemAspectTask(QPTreeItemPostprocAspect):
	def __init__(self, data, rootData, parentItem):
		QPTreeItemPostprocAspect.__init__(self, data, rootData, parentItem)

class QPTreeItemAspectAggregator(QPTreeItemPostprocAspect):
	def __init__(self, data, rootData, parentItem):
		QPTreeItemPostprocAspect.__init__(self, data, rootData, parentItem)

class QPTreeItemAspectCorners(QPTreeItemPostprocAspect):
	def __init__(self, data, rootData, parentItem):
		QPTreeItemPostprocAspect.__init__(self, data, rootData, parentItem)
	
class QPTreeItemAspectCBDParameters(QPTreeItemPostprocAspect):
	def __init__(self, data, rootData, parentItem):
		QPTreeItemPostprocAspect.__init__(self, data, rootData, parentItem)

class QPTreeItemAspectCBDPerformance(QPTreeItemPostprocAspect):
	def __init__(self, data, rootData, parentItem):
		QPTreeItemPostprocAspect.__init__(self, data, rootData, parentItem)

class QPTreeItemAspectCBDCost(QPTreeItemPostprocAspect):
	def __init__(self, data, rootData, parentItem):
		QPTreeItemPostprocAspect.__init__(self, data, rootData, parentItem)

class QPTreeItemAspectSummary(QPTreeItemPostprocAspect):
	def __init__(self, data, rootData, parentItem):
		QPTreeItemPostprocAspect.__init__(self, data, rootData, parentItem)

# Aspect tree item map
aspectItemMap={
	("SQLDataTask", "project"): QPTreeItemAspectProject,
	("SQLDataTask", "task"): QPTreeItemAspectTask,
	
	("SQLDataTaskCBD", "aggregator"): QPTreeItemAspectAggregator,
	
	("SQLDataCorners", "corners"): QPTreeItemAspectCorners,
	
	("SQLDataOptIter", "parameters"): QPTreeItemAspectCBDParameters,
	("SQLDataOptIter", "performance"): QPTreeItemAspectCBDPerformance, 
	("SQLDataOptIter", "cost"): QPTreeItemAspectCBDCost, 
	
	("SQLDataConclusion", "summary"): QPTreeItemAspectSummary, 
}

# Aspects tree item
class QPTreeItemPostprocAspects(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Result aspects"
	
	def canCopyChildren(self):
		return False
	
	def canPasteChildren(self, lcItemClassName, position=-1):
		return False
	
	def canSelectMultipleChildren(self):
		return False
	
	# We do not have a childrenRepository() because children are constructed from root data
	def countChildren(self):
		rec=self.rootData['record']
		if rec is None:
			return 0
		else:
			return len(rec.textAspects())
		
	def childItem(self, ndx):
		rec=self.rootData['record']
		aspect=rec.textAspects()[ndx]
		Cls=aspectItemMap[(rec.typename, aspect)]
		# Aspect name is data, root record is rootData
		return Cls(aspect, self.rootData, self)
	
	def icon(self):
		return QIcon(":resources/performance.png")

class QPTreeItemPostprocMeasures(QPTreeItemMeasures):
	def __init__(self, data, rootData, parentItem):
		QPTreeItemMeasures.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return "Measures (post)"
	
	def copyChildren(self, indices):
		ret=QPTreeItemMeasures.copyChildren(self, indices)
		# Return payload of type QPTreeItemMeasures
		return (QPTreeItemMeasures.__name__, ret[1])
	
	def canPasteChildren(self, lcItemClassName, position=-1):
		# Accept payload of type QPTreeItemMeasures
		return lcItemClassName == QPTreeItemMeasures.__name__.lower()
	
class QPTreeItemPostprocPlots(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
		
	def name(self):
		return "Plots (post)"

	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		return QPTreeItemPostprocPlot(self.childrenRepository()[ndx], self.rootData, self)
	
	def canRenameChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		self.childrenRepository().insert(ndx, deepcopy(self.childTemplate()))
		return True
	
	def childTemplate(self):
		return blankPlot
	
	def icon(self):
		return QIcon(":resources/plots.png")

class QPTreeItemPostprocPlot(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
		
	def name(self):
		return self.data[0]
	
	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data[1]["axes"]
	
	def childItem(self, ndx):
		return QPTreeItemPostprocAxes(self.childrenRepository()[ndx], self.rootData, self)
	
	def canRenameChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		self.childrenRepository().insert(ndx, deepcopy(self.childTemplate()))
		return True
	
	def childTemplate(self):
		return blankAxes
	
	def icon(self):
		return QIcon(":resources/plot.png")

class QPTreeItemPostprocAxes(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
		
	def name(self):
		return self.data[0]
	
	def countChildren(self):
		return len(self.childrenRepository())
	
	def childrenRepository(self):
		return self.data[1]["traces"]
	
	def childItem(self, ndx):
		return QPTreeItemPostprocTrace(self.childrenRepository()[ndx], self.rootData, self)
	
	def canRenameChildren(self):
		return True
	
	def canMoveChildren(self):
		return True
	
	def canDeleteChildren(self):
		return True
	
	def canCreateChildren(self):
		return True
	
	def createChild(self, ndx):
		self.childrenRepository().insert(ndx, deepcopy(self.childTemplate()))
		return True
	
	def childTemplate(self):
		return blankTrace
	
	def icon(self):
		return QIcon(":resources/axes.png")

class QPTreeItemPostprocTrace(QPTreeItem):
	def __init__(self, data, rootData, parentItem):
		QPTreeItem.__init__(self, data, rootData, parentItem)
	
	def name(self):
		return self.data[0]
	
	def icon(self):
		return QIcon(":resources/trace.png")

# Root postprocessing tree item	
class QPTreeItemPostprocRoot(QPTreeItem):
	dictKeys, key2index = buildDictKeyIndex(
		[
			[ 'aspects', QPTreeItemPostprocAspects ],
			[ 'measures', QPTreeItemPostprocMeasures ],
			[ 'plots', QPTreeItemPostprocPlots ],
		]
	)
		
	def __init__(self, rootData, parentItem=None):
		QPTreeItem.__init__(self, rootData, rootData, parentItem)
	
	def name(self):
		return "Postprocessing"
	
	def setRecord(self, rec):
		self.childrenRepository()['record']=rec
	
	def countChildren(self):
		# Either 1 or 3
		if self.childrenRepository() is None:
			return 0
		else:
			return 3
	
	def childrenRepository(self):
		return self.data
	
	def childItem(self, ndx):
		if ndx==0:
			return QPTreeItemPostprocAspects(
				None, 
				self.rootData, 
				self
			)
		elif ndx==1:
			return QPTreeItemPostprocMeasures(
				self.data['measures'], 
				self.data, 
				self
			)
		elif ndx==2:
			return QPTreeItemPostprocPlots(
				self.data['plots'], 
				self.data, 
				self
			)
		
	def copyChildren(self, indices):
		# Drop index 0 (do not copy aspects)
		if 0 in indices:
			indices.remove(0)
			
		return QPTreeItem.copyChildren(self, indices)


# Map from item type to editor class
itemEditorMap={
	QPTreeItemInfo: QPEditInfo, 
	QPTreeItemFiles: QPEditFiles, 
	QPTreeItemFile: QPEditFile, 
	QPTreeItemSimulators: QPEditHeads,
	QPTreeItemSimulator: QPEditHead,
	QPTreeItemVariables: QPEditVariables,
	QPTreeItemVariable: QPEditVariable,
	QPTreeItemAnalyses: QPEditAnalyses,
	QPTreeItemAnalysis: QPEditAnalysis,
	QPTreeItemMeasures: QPEditMeasures,
	QPTreeItemMeasure: QPEditMeasure,
	QPTreeItemDesignPar: QPEditDesignPar,
	QPTreeItemOpPar: QPEditOpPar, 
	QPTreeItemStatPar: QPEditStatPar, 
	
	QPTreeItemTaskCBD: QPEditTask,
	QPTreeItemCBDRequirements: QPEditCBDRequirements,
	QPTreeItemCBDDesignPar: QPEditCBDDesignPar,
	QPTreeItemCBDCorner: QPEditCBDCorner,
	QPTreeItemCBDCorners: QPEditCBDCorners,
	QPTreeItemCBDSettings: QPEditCBDSettings,
	QPTreeItemCBDOutput: QPEditCBDOutput, 
	
	QPTreeItemMPI: QPEditMPI, 
	
	QPTreeItemPostprocMeasures: QPEditMeasures,
	
	QPTreeItemPostprocPlots: QPEditPostPlots,
	QPTreeItemPostprocPlot: QPEditPostPlot,
	QPTreeItemPostprocAxes: QPEditPostAxes,
	QPTreeItemPostprocTrace: QPEditPostTrace, 
		
	QPTreeItemPostprocAspects: QPResultsWaveforms, 
	
	# Results viewers (items derived from QPTreeItemPostprocAspect)
	# QPTreeItemAspectProject: None, 
	# QPTreeItemAspectTask: None, 
	QPTreeItemAspectCorners: QPCBDResultsCorners,
	QPTreeItemAspectCBDParameters: QPCBDResultsParameters,
	QPTreeItemAspectCBDPerformance: QPCBDResultsPerformance,
	QPTreeItemAspectCBDCost: QPCBDResultsCost,
	# QPTreeItemAspectSummary: None 
}

taskItemTypes=set([
	QPTreeItemTaskCBD
])

	

DefaultEditorClass=QPEditNone

# Class name to class map 
name2class={}
for className in __all__:
	if className.find("QPTreeItem")!=0:
		continue
	cls=eval(className)
	if inspect.isclass(cls) and QPTreeItem in cls.mro():
		name2class[className]=cls

lowercasename2class = { (k.lower(), v) for k, v in name2class.items() }
