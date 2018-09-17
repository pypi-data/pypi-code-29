from copy import deepcopy

__all__ = [ 'newCBDTask', 'blankCBDTask' ]

blankCBDTask={
	'type': 'cbd', 
	'description': "", 
	'requirements': [], 
	'designpar': [],
	'corners': [], 
	'settings': {
		'aggregatorsettings': [],
		'evaluatorsettings': [],
		'failurepenalty': '1e6',
		'forwardsolution': True,
		'maxiter': '',
		'stoptol': '1e-5',
		'initialstep': '0.25', 
		'method': 'noneFull',
		'optimizersettings': [],
		'relevantcorners': True,
		'stopsatisfied': True,
		'tradeoffmultiplier': '0',
	}, 
	'output': {
		'aggregatordebug': '0',
		'evaluatordebug': '0',
		'optimizerdebug': '0',
		'keepfiles': False, 
		'saveallresults': False,
		'savewaveforms': 'verification',
		'simulatordebug': '0',
		'taskdebug': '1'
	}, 
	'mpi': {
		'processors': '',
		'mirror': True, 
		'persistent': True, 
		'vmdebug': '0', 
		'cosdebug': '0'  
	},
	'postprocessing': {
		'measures': [], 
		'plots': []
	}
}

def newCBDTask(root):
	#task=[ "NewTask", {
		#'type': 'cbd', 
		#'description': "", 
		#'requirements': [], 
		#'designpar': [],
		#'corners': [], 
		#'settings': {
			#'aggregatorsettings': [],
			#'evaluatorsettings': [],
			#'failurepenalty': '1e6',
			#'forwardsolution': True,
			#'maxiter': '',
			#'stoptol': '1e-5',
			#'initialstep': '0.25', 
			#'method': 'none',
			#'optimizersettings': [],
			#'relevantcorners': True,
			#'stopsatisfied': True,
			#'tradeoffmultiplier': '0',
		#}, 
		#'output': {
			#'aggregatordebug': '0',
			#'evaluatordebug': '0',
			#'optimizerdebug': '0',
			#'keepfiles': False, 
			#'saveallresults': False,
			#'savewaveforms': 'verification',
			#'simulatordebug': '0',
			#'taskdebug': '1'
		#}, 
		#'mpi': {
			#'processors': '',
			#'mirror': True, 
			#'persistent': True, 
			#'vmdebug': '0', 
			#'cosdebug': '0'  
		#},
	#}]
	task=deepcopy([ "New_task", blankCBDTask ])
	
	# Copy measures as requirements
	tmp=[]
	for row in root['measures']:
		tmp.append([True, row[0], row[1]['lower'], row[1]['upper'], row[1]['norm'], ''])
		
	task[1]['requirements']=tmp
	
	# Copy design parameters
	tmp=[]
	for row in root['designpar']:
		tmp.append([row[0], row[1], row[2], row[3]])
		
	task[1]['designpar']=tmp
	
	# Create nominal corner
	
	tmp=[]
	for row in root['oppar']:
		tmp.append([row[0], row[1]])
	
	for row in root['statpar']:
		tmp.append([row[0], "0.0"])
	
	tmpheads=[]
	for head in root['heads']:
		tmpheads.append([ head[0] ])
		
	corner=[ 
		'nominal', {
			'heads': tmpheads, 
			'modules': [], 
			'params': tmp, 
		}
	]
	
	task[1]['corners'].append(corner)
	
	return task
