# Test performance evaluator

from pyopus.evaluator.performance import PerformanceEvaluator
from pyopus.evaluator.aggregate import formatParameters

if __name__=='__main__':
	# Here we define the simulators that are used (in our case just SpiceOpus), 
	# circuit dscription fragments (or so-called modules), simulator settings 
	# passed to the simulator interface class at construction, simulator 
	# options valid for all analyses, and parameters that will be passed to 
	# the circuit description. 
	heads = {
		'opus': {
			'simulator': 'SpiceOpus', 
			'settings': {
				'debug': 0
			}, 
			'moddefs': {
				'def':     { 'file': 'opamp.inc' }, 
				'tb':      { 'file': 'topdc.inc' }, 
				'mos_tm': { 'file': 'cmos180n.lib', 'section': 'tm' }, 
				'mos_wp': { 'file': 'cmos180n.lib', 'section': 'wp' }, 
				'mos_ws': { 'file': 'cmos180n.lib', 'section': 'ws' }, 
				'mos_wo': { 'file': 'cmos180n.lib', 'section': 'wo' }, 
				'mos_wz': { 'file': 'cmos180n.lib', 'section': 'wz' }
			}, 
			'options': {
				'method': 'trap'
			}, 
			'params': {
				'lev1': 0.0,
				'lev2': 0.5,
				'tstart': 1e-9, 
				'tr': 1e-9, 
				'tf': 1e-9, 
				'pw': 500e-9
			}
		}
	}
	
	# This is a dictionary of Python variables that can be accessed in the 
	# expressions as var['name']
	variables={
		'saveInst': [ 'xmn2', 'xmn3', 'xmn1' ], 
		'saveProp': [ 'vgs', 'vth', 'vds', 'vdsat' ]
	}
	
	# List of circuit analyses
	# For every analysis we specify the head (simulator to use), 
	# modules that constitute the circuit description, 
	# simulator options (that can override the options in the 
	# heads structure), parameters passed to the circuit description 
	# (override those specified in the heads structure), the list 
	# of extra quantities to save during the simulation, and the 
	# command that invokes the simulation. 
	analyses = {
		'op': {
			'head': 'opus', 
			'modules': [ 'def', 'tb' ], 
			'options': {
				'method': 'gear'
			}, 
			'params': {
				'rin': 1e6,
				'rfb': 1e6
			},
			# Save current through vdd. Save voltages at inp, inn, and out. 
			# Save vgs, vth, vds, and vdsat for mn2, mn3, and mn1. 
			'saves': [ 
				"i(['vdd'])", 
				"v(['inp', 'inn', 'out'])", 
				"p(ipath(saveInst, 'x1', 'm0'), saveProp)"
			],  
			'command': "op()"
		}, 
		'dc': {
			'head': 'opus', 
			'modules': [ 'def', 'tb' ], 
			'options': {
				'method': 'gear'
			},
			'params': {
				'rin': 1e6,
				'rfb': 1e6
			},	
			'saves': [ ], 
			'command': "dc(-2.0, 2.0, 'lin', 100, 'vin', 'dc')"
		}
	}

	# Here we define the corner points where the performances will be evaluated. 
	# Every corner point can specify its own modules that are added to the modules 
	# listed for an analysis. Parameters Specified here override those specified in 
	# the heads structure, but get overridden by the parameters specified in the 
	# analysis structure. 
	corners = {
		'nominal': {
			'heads': [ 'opus' ], 
			'modules': [ 'mos_tm' ], 
			'params': {
				'temperature': 25, 
				'vdd': 1.8, 
			}
		},
		'worst_power': {
			'heads': [ 'opus' ], 
			'modules': [ 'mos_wp' ], 
			'params': {
				'temperature': 100, 
				'vdd': 2.0, 
			}
		},
		'worst_speed': {
			'heads': [ 'opus' ], 
			'modules': [ 'mos_ws' ], 
			'params': {
				'temperature': 100, 
				'vdd': 1.8, 
			}
		}, 
		'worst_zero': {
			'heads': [ 'opus' ], 
			'modules': [ 'mos_wz' ], 
			'params': {
				'temperature': 100, 
				'vdd': 1.8, 
			}
		}, 
		'worst_one': {
			'heads': [ 'opus' ], 
			'modules': [ 'mos_wo' ], 
			'params': {
				'temperature': 100, 
				'vdd': 1.8, 
			}
		}
	}
	
	# Finally, we define what we want to measure. For every performance 
	# we specify the analysis that generates the simulation results 
	# from which the performance is extracted. We can specify the formula 
	# for extracting the result as either a Python expression or a Python 
	# script that stores the result in the __result variable. 
	# For every performance we also specify the list of corners for which 
	# the performance will be evaluated. If no corners are apecified the 
	# performance is evaluated across all listed corners. 
	# Performances are scalars by default. For vector performances this 
	# must be specified explicitly. 
	measures = {
		# Supply current
		'isup': {
			'analysis': 'op', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed' ], 
			'expression': "__result=-i('vdd')"
		}, 
		# Output voltage at zero input voltage
		'out_op': {
			'analysis': 'op', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed' ], 
			'expression': "v('out')"
		},
		# Vgs overdrive (Vgs-Vth) for mn2, mn3, and mn1. 
		'vgs_drv': {
			'analysis': 'op', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed', 'worst_one', 'worst_zero' ], 
			'expression': "array(list(map(m.Poverdrive(p, 'vgs', p, 'vth'), ipath(saveInst, 'x1', 'm0'))))", 
			'vector': True
		}, 
		# Vds overdrive (Vds-Vdsat) for mn2, mn3, and mn1. 
		'vds_drv': {
			'analysis': 'op', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed', 'worst_one', 'worst_zero' ], 
			'expression': "array(list(map(m.Poverdrive(p, 'vds', p, 'vdsat'), ipath(saveInst, 'x1', 'm0'))))", 
			'vector': True
		}, 
		# DC swing where differential gain is above 50% of maximal gain
		'swing': {
			'analysis': 'dc', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed', 'worst_one', 'worst_zero' ], 
			'expression': "swing=m.DCswingAtGain(v('out'), v('inp', 'inn'), 0.5, 'out')"
		},
		# Surface area occupied by the current mirrors
		'mirr_area': {
			'analysis': None, 
			'corners': [ 'nominal' ], 
			'expression': (
				"param['mirr_w']*param['mirr_l']*(2+2+16)"
			)
		}
	}

	# Order in which the performance mesures are printed. 
	outOrder = [ 
		'mirr_area', 'isup', 'out_op', 
		'vgs_drv', 'vds_drv', 
		'swing', 
	]

	# Input parameters
	inParams={
		'mirr_w': 7.46e-005, 
		'mirr_l': 5.63e-007
	}

	# Order in which input parameters are printed.
	inOrder=[ 'mirr_w', 'mirr_l' ]

	# Construct an evaluator. Turn on debugging so we get a printout 
	# on what is happening. 
	pe=PerformanceEvaluator(heads, analyses, measures, corners, variables=variables, debug=2)

	# Evaluate the circuit for parameter values specified in inParams. 
	# These values have the lowest priority and are overridden by the 
	# parameters specified in the heads, corners, and analyses structures. 
	(results, anCount)=pe(inParams)

	# Print the parameters and the results. 
	print("")
	print(formatParameters(inParams, inOrder))
	print(pe.formatResults(outOrder, nMeasureName=10, nCornerName=15))
	
	# Print analysis count 
	print("Analysis count: "+str(anCount))
	
	# Note that you can also pick out the results manually from 
	# the results structure. To get the isup value in the nominal
	# corner, one would write
	print("Isup in nominal corner: %e" % results['isup']['nominal'])

	pe.finalize()
