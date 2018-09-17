# Optimize with cost evaluator 

# Imports
from pyopus.evaluator.performance import PerformanceEvaluator, updateAnalysisCount
from pyopus.evaluator.aggregate import *
from pyopus.evaluator.auxfunc import listParamDesc
from pyopus.optimizer import optimizerClass
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

	# Input parameters
	costInput = { 
		'mirr_w': {
			'init': 7.456e-005, 
			'lo':	1e-6, 
			'hi':	95e-6, 
		},
		'mirr_l': {
			'init': 5.6e-007, 
			'lo':	0.18e-6, 
			'hi':	4e-6, 
		},
		'out_w': {
			'init': 4.801e-005, 
			'lo':	1e-6, 
			'hi':	95e-6, 
		},
		'out_l': {
			'init': 3.8e-007, 
			'lo':	0.18e-6, 
			'hi':	4e-6, 
		},
		'load_w': {
			'init': 3.486e-005, 
			'lo':	1e-6, 
			'hi':	95e-6, 
		},
		'load_l': {
			'init': 2.57e-006, 
			'lo':	0.18e-6, 
			'hi':	4e-6, 
		},
		'dif_w': {
			'init': 7.73e-006, 
			'lo':	1e-6, 
			'hi':	95e-6, 
		},
		'dif_l': {
			'init': 1.08e-006, 
			'lo':	0.18e-6, 
			'hi':	4e-6, 
		},
	}
	# End input parameters

	# Parameter order
	inOrder=list(costInput.keys())
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

	costDefinition = [
		{
			'measure': 'isup', 
			'norm': Nbelow(1e-3, 0.1e-3, 10000.0),	
			'shape': Slinear2(1.0,0.0),
			'reduce': Rexcluded()
		},
		{
			'measure': 'out_op',
			'norm': Nbelow(10, 0.1e-3),	
			'shape': Slinear2(1.0,0.0), 
			'reduce': Rexcluded()
		},
		{
			'measure': 'vgs_drv', 
			'norm': Nabove(1e-3), 
			'reduce': Rworst()
		},
		{
			'measure': 'vds_drv', 
			'norm': Nabove(1e-3)
		},
		{
			'measure': 'swing', 
			'norm': Nabove(1.5), 
			'shape': Slinear2(1.0,0.001), 
		},
		{
			'measure': 'mirr_area', 
			'norm': Nbelow(800e-12, 100e-12), 
			'shape': Slinear2(1.0,0.001)
		}
	]

	# Main program
	# Performance evaluator
	pe=PerformanceEvaluator(heads, analyses, measures, corners, variables=variables, debug=0)

	# Cost evaluator
	# Input parameter order in vector x is defined by inOrder. 
	ce=Aggregator(pe, costDefinition, inOrder, debug=0)

	# Vectors of initial, low, and high values of input parameters. 
	xlow=listParamDesc(costInput, inOrder, "lo")
	xhi=listParamDesc(costInput, inOrder, "hi")
	xinit=listParamDesc(costInput, inOrder, "init")
	
	# Optimizer (Hooke-Jeeves). xlo and xhi must be numpy arrays. 
	opt=optimizerClass("HookeJeeves")(ce, xlo=xlow, xhi=xhi, maxiter=1000)

	# Set initial point. Must be a numpy array. 
	opt.reset(xinit)

	# Install reporter plugin. 
	# Print cost. Also print performance every time the cost is decreased. 
	opt.installPlugin(ce.getReporter())

	# Install stopper plugin. 
	# Stop run when all requirements are satisfied (all cost contributions are 0 or less) 
	opt.installPlugin(ce.getStopWhenAllSatisfied())

	# Run
	opt.run()

	# Optimization result
	xresult=opt.x
	iterresult=opt.bestIter
		
	# Final evaluation at xresult. 
	cf=ce(xresult)
		
	# Print results. 
	print("\n\nFinal cost: "+str(cf)+", found in iter "+str(iterresult)+", total "+str(opt.niter)+" iteration(s)")
	print(ce.formatParameters())
	print(ce.formatResults(nMeasureName=10, nCornerName=15))
	print("")
	print("Performance in corners")
	print(pe.formatResults(outOrder, nMeasureName=10, nCornerName=15))
	print("")
	
	# Every call to pe results in the same analysis count. 
	# Therefore we can multiply the analysis count of a single pe call
	# with the number of calls to get the actual analysis count. 
	acnt={}
	updateAnalysisCount(acnt, pe.analysisCount, opt.niter+1)
	print("Analysis count: "+str(acnt))
	
	# Cleanup intemediate files
	pe.finalize()
