from . import values
from .tasks import blankTask
from copy import deepcopy

from pprint import pprint


__all__ = [ 'projectFixer', 'postprocessingFixer' ]


def dictFixer(data, ruleName):
	# print("Starting dict with rule", ruleName)
	# pprint(data)
	rule=fixers[ruleName]
	for key, protoVal in rule['prototype'].items():
		# Add missing dictionary entry
		if key not in data:
			data[key]=deepcopy(protoVal)
			
	for key, childRuleName in rule['children'].items():
		childRule=fixers[childRuleName]
		engine=childRule['engine']
		engine(data[key], childRuleName)
		
def listFixer(data, ruleName):
	# print("Starting list with rule", ruleName)
	# pprint(data)
	rule=fixers[ruleName]
	# Ignore entry[0] which is the name
	childRuleName=rule['children']['*']
	childRule=fixers[childRuleName]
	engine=childRule['engine']
	for entry in data:
		engine(entry[1], childRuleName)
		
def tasksFixer(data, ruleName):
	# print("Starting tasks with rule", ruleName)
	# pprint(data)
	rule=fixers[ruleName]
	for task in data:
		# Assume task type is in the 'type' member
		taskType=task[1]['type']
		# Task prototype
		childProtoType=blankTask[taskType]
		# Rule
		childRuleName=taskType
		# Ignore entry[0] which is the task name
		dictFixer(task[1], childRuleName)
	
def fixer(data, ruleName):
	rule=fixers[ruleName]
	engine=rule['engine']
	engine(data, ruleName)
	
# Add missing fields to project
fixers = {
	'project': {
		# For a dictionary prototype, dictFixer() is used. 
		# For a list entry prototype
		#   First member of list prototype is entry name and is ignored. 
		#   Second member is the entry data. 
		#     If it is a dict, dictFixer() is used with list entry data. 
		#     If it is a list, 
		'prototype': values.blankProject, 
		'engine': dictFixer, 
		'children': {
			'info': 'project:info', 
			'files': 'project:files', 
			'heads': 'project:heads',
			# 'variables': 'project:variables', 
			'analyses': 'project:analyses', 
			'measures': 'project:measures', 
			# 'designpar': 'project:designpar', 
			# 'oppar': 'project:oppar',
			# 'statpar': 'project:statpar',
			'tasks': 'project:tasks', 
		}
	}, 
	'project:info': {
		'prototype': values.blankInfo, 
		'engine': dictFixer, 
		'children': {}
	}, 
	'project:files': {
		'prototype': values.blankFile, 
		'engine': listFixer, 
		'children': {
			'*': 'project:files:file'
		}
	},
	'project:heads': {
		'prototype': values.blankHead, 
		'engine': listFixer, 
		'children': {
			'*': 'project:heads:head'
		}
	},
	'project:heads:head': {
		'prototype': values.blankHead[1], 
		'engine': dictFixer, 
		'children': {}
	},
	'project:files:file': {
		'prototype': values.blankFile[1], 
		'engine': dictFixer, 
		'children': {}
	},
	'project:analyses': {
		'prototype': values.blankAnalysis, 
		'engine': listFixer, 
		'children': {
			'*': 'project:analyses:analysis'
		}
	},
	'project:analyses:analysis': {
		'prototype': values.blankAnalysis[1], 
		'engine': dictFixer, 
		'children': {}
	},
	'project:measures': {
		'prototype': values.blankMeasure, 
		'engine': listFixer, 
		'children': {
			'*': 'project:measures:measure'
		}
	},
	'project:measures:measure': {
		'prototype': values.blankMeasure[1], 
		'engine': dictFixer, 
		'children': {}
	},
	
	'project:tasks': {
		'engine': tasksFixer, 
	},
	
	'cbd': {
		'prototype': blankTask['cbd'], 
		'engine': dictFixer, 
		'children': {
			'settings': 'cbd:settings', 
			'output': 'cbd:output', 
			'mpi': 'cbd:mpi', 
		}
	},
	'cbd:settings': {
		'prototype': blankTask['cbd']['settings'], 
		'engine': dictFixer, 
		'children': {}
	},
	'cbd:output': {
		'prototype': blankTask['cbd']['output'], 
		'engine': dictFixer, 
		'children': {}
	},
	'cbd:mpi': {
		'prototype': blankTask['cbd']['mpi'], 
		'engine': dictFixer, 
		'children': {}
	},
	
	'postprocessing': {
		# For a dictionary prototype, dictFixer() is used. 
		# For a list entry prototype
		#   First member of list prototype is entry name and is ignored. 
		#   Second member is the entry data. 
		#     If it is a dict, dictFixer() is used with list entry data. 
		#     If it is a list, 
		'prototype': values.blankPostprocessing, 
		'engine': dictFixer, 
		'children': {
			'measures': 'postprocessing:measures', 
			'plots': 'postprocessing:plots', 
		}
	}, 
	'postprocessing:measures': {
		'prototype': values.blankMeasure, 
		'engine': listFixer, 
		'children': {
			'*': 'postprocessing:measures:measure'
		}
	},
	'postprocessing:measures:measure': {
		'prototype': values.blankMeasure[1], 
		'engine': dictFixer, 
		'children': {}
	},
	'postprocessing:plots': {
		'prototype': values.blankPlot, 
		'engine': listFixer, 
		'children': {
			'*': 'postprocessing:plots:plot'
		}
	},
	'postprocessing:plots:plot': {
		'prototype': values.blankPlot[1], 
		'engine': dictFixer, 
		'children': {
			'axes': 'postprocessing:plots:plot:axeslist'
		}
	},
	'postprocessing:plots:plot:axeslist': {
		'prototype': values.blankAxes, 
		'engine': listFixer, 
		'children': {
			'*': 'postprocessing:plots:plot:axeslist:axes'
		}
	},
	'postprocessing:plots:plot:axeslist:axes': {
		'prototype': values.blankAxes[1], 
		'engine': dictFixer, 
		'children': {
			'traces': 'postprocessing:plots:plot:axeslist:axes:traces'
		}
	},
	'postprocessing:plots:plot:axeslist:axes:traces': {
		'prototype': values.blankTrace, 
		'engine': listFixer, 
		'children': {
			'*': 'postprocessing:plots:plot:axeslist:axes:traces:trace'
		}
	},
	'postprocessing:plots:plot:axeslist:axes:traces:trace': {
		'prototype': values.blankTrace[1], 
		'engine': dictFixer, 
		'children': {}
	},
}

def projectFixer(project):
	fixer(project, 'project')
	
def postprocessingFixer(postprocessing):
	fixer(postprocessing, 'postprocessing')
	
