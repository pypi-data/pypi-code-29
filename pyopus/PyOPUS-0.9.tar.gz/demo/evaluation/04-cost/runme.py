# Test cost evaluator

# Imports
from pyopus.evaluator.performance import PerformanceEvaluator
from pyopus.evaluator.aggregate import *
from pyopus.evaluator.auxfunc import paramList
# End imports

if __name__=='__main__':
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
			
	variables={
		'saveInst': [ 'xmn2', 'xmn3', 'xmn1' ], 
		'saveProp': [ 'vgs', 'vth', 'vds', 'vdsat' ]
	}
	
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
		}, 
		'dccom': {
			'head': 'opus', 
			'modules': [ 'def', 'tb' ], 
			'options': {
				'method': 'gear'
			},
			'params': {
				'rin': 1e6,
				'rfb': 1e6
			},			
			'saves': [ 
				"v(['inp', 'inn', 'out'])", 
				"p(ipath(saveInst, 'x1', 'm0'), saveProp)"
			], 
			'command': "dc(0, param['vdd'], 'lin', 20, 'vcom', 'dc')"
		}
	}

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

	measures = {
		# Supply current
		'isup': {
			'analysis': 'op', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed' ], 
			'expression': "isup=-i('vdd')"
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
			'expression': "m.DCswingAtGain(v('out'), v('inp', 'inn'), 0.5, 'out')"
		},
		# Surface area occupied by the current mirrors
		'mirr_area': {
			'analysis': None, 
			'corners': [ 'nominal' ], 
			'expression': (
				"param['mirr_w']*param['mirr_l']*(2+2+16)"
			)
		}, 
		# Input differential voltage from dc analysis (vector)
		'dcvin': {
			'analysis': 'dc', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed', 'worst_one', 'worst_zero' ], 
			'expression': "v('inp', 'inn')",
			'vector': True
		},
		# Output voltage from dc analysis (vector)
		'dcvout': {
			'analysis': 'dc', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed', 'worst_one', 'worst_zero' ], 
			'expression': "v('out')",
			'vector': True
		},
		# Input common mode voltage from dccom analysis (vector)
		'dccomvin': {
			'analysis': 'dccom', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed', 'worst_one', 'worst_zero' ], 
			'expression': "v('inp')",
			'vector': True
		},
		# Output voltage from dccom analysis (vector)
		'dccomvout': {
			'analysis': 'dccom', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed', 'worst_one', 'worst_zero' ], 
			'expression': "v('out')",
			'vector': True
		}, 
		# Vds overdrive for xmn1 from dccom analysis (vector)
		'dccom_m1vdsvdsat': {
			'analysis': 'dccom', 
			'corners': [ 'nominal', 'worst_power', 'worst_speed', 'worst_one', 'worst_zero' ], 
			'expression': "p(ipath('xmn1', 'x1', 'm0'), 'vds')-p(ipath('xmn1', 'x1', 'm0'), 'vdsat')",
			'vector': True
		},
	}

	# Order in which mesures are printed. 
	outOrder = [ 
		'mirr_area', 'isup', 'out_op', 
		'vgs_drv', 'vds_drv', 
		'swing', 
	]
	
	# Parameters
	params = { 
		'mirr_w': 7.456e-005, 
		'mirr_l': 5.6e-007, 
		'out_w':  4.801e-005, 
		'out_l':  3.8e-007, 
		'load_w': 3.486e-005, 
		'load_l': 2.57e-006, 
		'dif_w':  7.73e-006, 
		'dif_l':  1.08e-006, 
	}
	# End parameters

	# Parameter order
	inOrder=list(params.keys())
	inOrder.sort()
	# End parameter order

	# Visualisation
	visualisation = {
		# Window list with axes for every window
		# Most of the options are arguments to MatPlotLib API calls
		# Every plot window has its unique name by which we refer to it
		'graphs': {
			# One window for the DC response
			'dc': {
				'title': 'Amplifier DC response', 
				'shape': { 'figsize': (6,8), 'dpi': 80 }, 
				# Define the axes
				# Every axes have a unique name by which we refer to them
				'axes': {
					# The first vertical subplot displays the differential response
					'diff': {
						# Argument to the add_subplot API call
						'subplot': (2,1,1), 
						# Extra options
						'options': {}, 
						# Can be rect (default) or polar, xscale and yscale have no meaning when grid is polar
						'gridtype': 'rect',
						# linear by default, can also be log
						'xscale': { 'type': 'linear' }, 	
						'yscale': { 'type': 'linear' }, 	
						'xlimits': (-3e-3, -1e-3), 
						'xlabel': 'Vdif=Vinp-Vinn [V]', 
						'ylabel': 'Vout [V]', 
						'title': '', 
						'legend': False, 
						'grid': True, 
					}, 
					# The second vertical subplot displays the common mode response
					'com': {
						'subplot': (2,1,2), 
						'options': {}, 
						'gridtype': 'rect', 		
						'xscale': { 'type': 'linear' }, 
						'yscale': { 'type': 'linear' }, 
						'xlimits': (0.0, 2.0),
						'xlabel': 'Vcom=Vinp=Vinn [V]', 
						'ylabel': 'Vout [V]', 
						'title': '', 
						'legend': False, 
						'grid': True, 
					}
				}
			},
			# Another window for the M1 Vds overdrive in common mode
			'm1vds': {
				'title': 'M1 Vds-Vdsat in common mode', 
				'shape': { 'figsize': (6,4), 'dpi': 80 }, 
				'axes': {
					'dc': {
						# This time we define add_axes API call
						'rectangle': (0.12, 0.12, 0.76, 0.76), 
						'options': {}, 
						'gridtype': 'rect', 		# rect (default) or polar, xscale and yscale have no meaning when grid is polar
						'xscale': { 'type': 'linear' }, 	# linear by default
						'yscale': { 'type': 'linear' }, 	# linear by default
						'xlimits': (0.0, 2.0), 
						'xlabel': 'Vcom=Vinp=Vinn [V]', 
						'ylabel': 'M1 Vds-Vdsat [V]', 
						'title': '', 
						'legend': False, 
						'grid': True, 
					}, 
				}
			}
		},
		# Here we define the trace styles. If pattern mathces a combination 
		# of (graph, axes, corner, trace) name the style is applied. If 
		# multiple patterns match one trace the style is the union of matched
		# styles where matched entries that appear later in this list override 
		# those that appear earlier. 
		# The patterns are given in the format used by the :mod:`re` Python module. 
		'styles': [ 
			{
				# A default style (red, solid line)
				'pattern': ('^.*', '^.*', '^.*', '^.*'), 
				'style': {
					'linestyle': '-',
					'color': (0.5,0,0)
				}
			}, 
			{
				# A style for traces representing the response in the nominal corner
				'pattern': ('^.*', '^.*', '^nom.*', '^.*'),
				'style': {
					'linestyle': '-',
					'color': (0,0.5,0)
				}
			}
		], 
		# List of traces. Every trace has a unique name. 
		'traces': {
			# Differential DC response in all corners
			'dc': {
				# Window an axes where the trace will be plotted
				'graph': 'dc', 
				'axes': 'diff', 
				# Result vector used for x-axis data
				'xresult': 'dcvin',
				# Result vector used for y-axis data
				'yresult': 'dcvout', 
				# Corners for which the trace will be plotted
				# If not specified or empty, all corners where xresult is evaluated are plotted
				'corners': [ ],	
				# Here we can override the style matched by style patterns
				'style': {
					'linestyle': '-',
					'marker': '.', 
				}
			}, 
			# Common mode DC response in all corners
			'dccom': {
				'graph': 'dc', 
				'axes': 'com', 
				'xresult': 'dccomvin',
				'yresult': 'dccomvout', 
				'corners': [ ],	
				'style': {	
					'linestyle': '-',
					'marker': '.', 
				}
			},
				# Vds overdrive for M1 in common mode, nominal corner only
			'm1_vds_vdsat': {
				'graph': 'm1vds', 
				'axes': 'dc', 
				'xresult': 'dccomvin',
				'yresult': 	'dccom_m1vdsvdsat', 
				'corners': [ 'nominal' ],	
				'style': {	
					'linestyle': '-',
					'marker': '.', 
				}
			}
		}
	}
	# End visualisation

	# Definition
	definition = [
		{
			# Name of the performance measure
			'measure': 'isup', 
			# How to normalize it 
			#   anything below 1e-3 is negative, while everything above is positive
			#   a change of 0.1e-3 corresponds to contribution of size 1 to the aggregate cost function
			#   a failed measurement results in contribution 10000.0 (default value)
			'norm': Nbelow(1e-3, 0.1e-3, 10000.0),	
			# Shape of the contribution is piecewise linear. It is obtaine by multiplying 
			#   negative normalized values with 0 and 
			#   positive normalized values with 1
			'shape': Slinear2(1.0,0.0),
			# The contribution will be computed, but not added to the aggregate cost function
			# This is good for monitoring a performance
			'reduce': Rexcluded()
		},
		{
			'measure': 'out_op',
			# Output operating point must be below 10 with 0.1e-3 norm
			# This means that violating this requirement results in a positive normalized value
			'norm': Nbelow(10, 0.1e-3),	
			'shape': Slinear2(1.0,0.0), 
			# This one also does not contribute to the aggregate cost function. 
			'reduce': Rexcluded()
		},
		{
			'measure': 'vgs_drv', 
			# This one should be above 1e-3. Failure to achieve the goal is penalized with a 
			# positive normalized value. If norm is not specified (like here) it is equal 
			# to the goal (1e-3 in this case)
			'norm': Nabove(1e-3), 			
			# Take the worst contribution across all corners where vgs_drv is computed and 
			# add it to the aggregate cost function
			# Because we specified no shape the default is used (Slinear2(1.0,0.0))
			'reduce': Rworst()
		},
		{
			# This one should be above 1e-3
			# Because this performance measure is a vector the requirement is enforced on 
			# all of its components. Every component results in one contribution to the 
			# aggregate cost function. 
			'measure': 'vds_drv', 
			'norm': Nabove(1e-3)
		},
		{
			'measure': 'swing', 
			'norm': Nabove(1.6), 
			# If the goal is violated (swing<1.6) we get a positive contribution to the 
			# aggregate cost function obtained by multiplying the normalized value with 1.0. 
			# If, however, swing>1.6 we get a negative contribution obtained by multiplying 
			# the normalized contribution (which is negative) with 0.001. 
			'shape': Slinear2(1.0,0.001), 
		},
		{
			'measure': 'mirr_area', 
			# Mirror area should be below 800e-12 with norm 100e-12
			'norm': Nbelow(800e-12, 100e-12), 
			# Again negative normalized values are multiplied with 0.001 while positive 
			# ones are multiplied with 1. 
			'shape': Slinear2(1.0,0.001)
		}
	]
	# End definition

	# Main program
	# Performance evaluator
	pe=PerformanceEvaluator(heads, analyses, measures, corners, variables=variables, debug=0)

	# Aggregate cost function
	ce=Aggregator(pe, definition, inOrder, debug=1)

	# Vectorize parameters
	x=paramList(params, inOrder)
	
	# Evaluate aggregate function at vector x 
	cf=ce(x)
	
	# Print the results
	print("")
	print("cost=%e" % cf)
	print(ce.formatParameters())
	print(ce.formatResults(nMeasureName=10, nCornerName=15))
	print("")
	
	# Print analysis count 
	print("Analysis count: "+str(pe.analysisCount))
	
	# Cleanup intemediate files
	pe.finalize()
