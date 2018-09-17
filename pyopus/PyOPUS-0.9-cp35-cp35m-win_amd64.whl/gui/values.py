from .translator import Translator
from ..simulator import detectSimulators

__all__ = [ 
	'simulators', 'optimizers', 'blankFile', 'blankHead', 
	'blankVariable', 
	'blankStatParam', 'blankOpParam', 'blankDesignParam', 
	'blankAnalysis', 'blankSave', 'blankDepends', 
	'blankMeasure', 'blankCorner', 
	'simulatorTranslator', 
	'blankProject', 
	'blankPostprocessing', 'blankPlot', 'blankAxes', 'blankTrace', 
	'version', 
]	

version="1.0"

# List of [Description, ClassName]
simulators=[ [t[2], t[0]] for t in detectSimulators() ]

optimizers = [
	[ 'Evaluate only (required corner-analysis pairs)',	'none' ], 
	[ 'Evaluate only (all corner-analysis pairs)',		'noneFull' ], 
	[ 'PSADE (global)', 				'ParallelSADE' ],
	[ 'Differential evolution (global)', 		'DifferentialEvolution' ], 
	[ 'QPMADS',					'QPMADS' ], 
	[ 'Box\'s constrained simplex', 		'BoxComplex' ],
	[ 'Hooke-Jeeves', 				'HookeJeeves' ],
]

simulatorTranslator = Translator(simulators, defaultSuffix=" (unknown)")

saveTypes = [
	[ 'Default', 	'default' ], 
	[ 'Node Voltage', 	'voltage' ], 
	[ 'Device Current', 	'devcurrent' ],
	[ 'Device Property', 	'devvar' ], 
	[ 'Advanced (Expression)',	'expression' ]
]

saveTypeTranslator = Translator(saveTypes)

cbdSaveWaveforms = [
	[ 'Never', 'never' ], 
	[ 'Only for verification across corners', 'verification' ],
	[ 'For every saved result', 'always' ], 
]

blankFile = [ "New file", { 'external': True, 'content': "" } ]

blankHead = [ "New setup", {
	'simulator': "SpiceOpus", 
	'settings': [], 
	'options': [], 
	'params': [], 
	'moddefs': [], 
}]

blankVariable=[ 'New variable', '' ]

blankStatParam=[ '', '-10.0', '10.0', 'Normal(0.0,1.0)' ]

blankOpParam=[ '', '', '', '' ]

blankDesignParam=[ '', '', '', '' ]

blankAnalysis=[
	"New analysis", {
		'head': '', 
		'modules': [], 
		'options': [], 
		'params': [], 
		'saves': [], 
		'command': ""
	}
]
	
blankSave=[ 'default', '' ]

blankDepends=[ '' ]

blankMeasure=[
	"New measure", {
		'analysis': '', 
		'depends': [], 
		'expression': "", 
		'vector': False, 
		'components': "", 
		'lower': "", 
		'upper': "", 
		'norm': "", 
	}
]
	
blankCorner=[
	'New corner', {
		'heads': [], 
		'params': [], 
		'modules': [], 
	}
]
	
axesTypes = [
	[ 'Linear', 'lin' ], 
	[ 'Semi-logarithmic (x)', 'xlog' ],
	[ 'Semi-logarithmic (y)', 'ylog' ], 
	[ 'Logarithmic', 'log' ], 
]

axesTypeTranslator = Translator(axesTypes, defaultSuffix=" (unknown)")

blankPlot=[
	'New_plot',  {
		'title': "", 
		'axes': [], 
	}
]

blankAxes=[
	'New_axes', {
		'title': "", 
		'xlabel': "x", 
		'ylabel': "y", 
		'type': 'lin', 
		'aspect': False, 
		'xpos': "0", 
		'ypos': "0", 
		'xspan': "1", 
		'yspan': "1", 
		'xlo': "", 
		'xhi': "", 
		'ylo': "", 
		'yhi': "", 
		'xgrid': True, 
		'ygrid': True, 
		'traces': []
	}
]

blankTrace=[
	'New_trace', {
		'expression': "", 
		'scale': "", 
		'analyses': [ [ "" ] ], 
	}
]	
	

blankInfo = {
	'version': version, 
	'description': '', 
}

blankPostprocessing={
	'version': version, 
	'measures': [], 
	'plots': [], 
}

blankProject = {
	'info': blankInfo, 
	'files': [], 
	'heads': [], 
	'variables': [], 
	'analyses': [], 
	'measures': [], 
	'designpar': [], 
	'oppar': [], 
	'statpar': [], 
	'tasks': [],
}
