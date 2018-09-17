
__all_ = [ 'data' ]

data = {
	'info': {
		'version': '1.0', 
		'description': '', 
	}, 
	'files': [
		# name content
		[
			'netlist.cir', {
				'external': False, 
				'content': 'hello world', 
			}
		], 
		[
			'wrapper.inc', { 
				'external': False, 
				'content': 'hello again', 
			}
		], 
#		[
#			'gaga.txt', { 
#				'external': True, 
#				'content': '', 
#			}
#		]
	], 
	'heads': [
		[ 'spectre', {
			'simulator': 'Spectre', 
			'settings': [
				[ 'debug', '0' ],
			], 
			'options': [
				[ 'method', 'trap' ], 
			], 
			'params': [
				[ 'ibias', '100e-6' ], 
				[ 'rload', '100e6' ],
			], 
			'moddefs': [
				[ 'def', 'opamp.inc', '' ], 
				[ 'tm', 'cmos180n.lib', 'tm' ],
				[ 'wp', 'cmos180n.lib', 'wp' ],
				[ 'ws', 'cmos180n.lib', 'ws' ],
				[ 'rlo', 'cmos180n.lib', 'rlo' ],
				[ 'rhi', 'cmos180n.lib', 'rhi' ],
			]
		}], 
		[ 'hspice', {
			'simulator': 'HSPICE', 
			'settings': [
				[ 'debug', '0' ],
			], 
			'options': [
				[ 'method', 'trap' ], 
			], 
			'params': [
				[ 'ibias', '100e-6' ], 
				[ 'rload', '100e6' ],
			], 
			'moddefs': [
				[ 'tm', 'cmos180n.lib', 'tm' ],
				[ 'wp', 'cmos180n.lib', 'wp' ],
				[ 'ws', 'cmos180n.lib', 'ws' ],
			]
		}],
	], 
	'variables': [
		# name num|string|numlist|stringlist|expression pythonic_expression
		[ 'nmoslist', 'mn1 mn2' ],
		[ 'pmoslist', '#["mp1", "mp2"]' ],
		# [ 'apmoslist', '#1/0' ],
	], 
	'analyses': [
		[ 'ac', {
			'head': 'spectre', 
			'modules': [ 
				['def'], 
				['tm']
			], 
			'options': [
				[ 'reltol', '1e-4' ], 
			], 
			'params': [
				[ 'v1', '#1.1' ], 
				[ 'v2', '1.2' ], 
			], 
			'saves': [
				[ 'default', ''],
				[ 'voltage', 'a1 a2 a3' ],
				[ 'devcurrent', 'vdd vin' ],
				[ 'devvar', 'm1 m2 m3 m4 ; vds vgs vdsat vth' ],
				[ 'devvar', '#gaga ; #gugu' ],
				[ 'expression', "p(ipath(var['nmosList'], 'x1', 'm0'), ['vgs', 'vth', 'vds', 'vdsat'])"]
			], 
			'command': "ac(1, 1e12, 'dec', 10)"
		}], 
		[ 'dc', {
			'head': 'spectre', 
			'modules': [ 
				['tm']
			], 
			'options': [], 
			'params': [], 
			'saves': [
				[ 'default', '', '' ],
			], 
			'command': "dc(-2.0, 2.0, 'lin', 100, 'vin', 'dc')"
		}],
		[ 'tran', {
			'head': 'spectre', 
			'modules': [ 
				['def'], 
			], 
			'options': [], 
			'params': [], 
			'saves': [
				[ 'default', '', '' ],
			], 
			'command': "tran(1e-6, 1e-3)"
		}],
	], 
	'measures': [
		[ 'swing', {
			'lower': "0", 
			'upper': "10", 
			'norm': "", 
			'analysis': 'dc', 
			'depends': [], 
			'expression': "m.DCswingAtGain(v('out'), v('inp', 'inn'), 0.5, 'out')", 
			'vector': True, 
			'components': "", 
		}], 
		[ 'gain', {
			'lower': "10", 
			'upper': "20", 
			'norm': "1", 
			'analysis': 'ac', 
			'depends': [], 
			'expression': """
__result=m.ACmag(m.ACtf(v('out'), v('inp', 'inn')))[0]
""", 
			'vector': True, 
			'components': "c1 c2 c3 c4", 
		}], 
		[ 'vgs_drv', {
			'lower': "", 
			'upper': "", 
			'norm': "", 
			'analysis': 'dc', 
			'depends': [], 
			'expression': "vgs_drv=array(list(map(m.Poverdrive(p, 'vgs', p, 'vth'), ipath(var['mosList'], 'x1', 'm0'))))", 
			'vector': True, 
			'components': "#nmoslist", 
		}],
		[ 'cmrr', {
			'lower': "", 
			'upper': "", 
			'norm': "", 
			'analysis': '', 
			'depends': [['gain'], ['swing']],
			'expression': "param['mirr_w']*param['mirr_l']", 
			'vector': False, 
			'components': "", 
		}],
		[ 'area', {
			'lower': "", 
			'upper': "", 
			'norm': "", 
			'analysis': '', 
			'depends': [  ], 
			'expression': "param['mirr_w']*param['mirr_l']", 
			'vector': False, 
			'components': "", 
		}], 
	], 
	'designpar': [
		# name low high initial
		[ 'mirrw', '10e-6', '1e-6', '95e-6' ], 
		[ 'mirrl', '2e-6', '1e-6', '95e-6' ]
	], 
	'oppar': [
		# name low high nominal
		[ 'vdd', '1.8', '1.6', '2.0' ], 
		[ 'temperature', '25', '0', '80' ], 
	], 
	'statpar': [
		# name low high distribution
		[ 'p1', '-10.0', '10.0', 'Normal(0.0,1.0)' ],
		[ 'p2', '-10.0', '10.0', 'Normal(0.0,1.0)' ], 
	], 
	'tasks': [
		[ "nomdes", {
				'type': 'cbd', 
				'description': 'Nominal design', 
				'requirements': [ # name low hi norm tradeoff_weight
					[True, 'gain',  '60.0', '', '10.0', '1'], 
					[True, 'swing', '1.2', '', '0.1', ''], 
				], 
				'designpar': [ # name lo hi initial
					[ 'mirrw', '10e-6', '1e-6', '95e-6' ], 
					[ 'mirrl', '2e-6', '1e-6', '95e-6' ]
				],
				'corners': [
					[ 'nominal', {
						'heads': [ 
							[ 'spectre' ], 
							[ 'hspice' ], 
						], 
						'params': [
							[ 'vdd', '1.8' ], 
							[ 'temperature', '25' ], 
							[ 'p1', '0' ],
							[ 'p2', '0' ], 
						], 
						'modules': [
							[ 'tm' ]
						], 
					}], 
				], 
				'settings': {
					'failurepenalty': '1e6',
					'stopsatisfied': True, 
					'tradeoffmultiplier': '0', 
					'method': 'QPMADS', 
					'initialstep': '0.25',
					'maxiter': '',
					'stoptol': '1e-5', 
					'forwardsolution': True, 
					'relevantcorners': True, 
					'evaluatorsettings': [],
					'aggregatorsettings': [], 
					'optimizersettings': [], 
				}, 
				'output': {
					'simulatordebug': '0', 
					'evaluatordebug': '0', 
					'aggregatordebug': '0',
					'optimizerdebug': '0', 
					'taskdebug': '0', 
					'saveallresults': False, 
					'savewaveforms': 'verification', 
				}, 
			},
		], 
	],
}
