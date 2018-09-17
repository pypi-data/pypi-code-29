# Sizing across corners

from definitions import *
from pyopus.design.cbd import CornerBasedDesign, generateCorners
from pyopus.evaluator.aggregate import formatParameters
# If MPI is imported an application not using MPI will behave correctly
# (i.e. only slot 0 will run the program) even when started with mpirun/mpiexec
from pyopus.parallel.mpi import MPI
from pyopus.parallel.cooperative import cOS


if __name__=='__main__':
	# Prepare statistical parameters dictionary with nominal values (0)
	nominalStat={ name: 0.0 for name, desc in statParams.items() }
	
	# Prepare operating parameters dictionary with nominal values
	nominalOp={ name: desc['init'] for name, desc in opParams.items() }
	
	# Prepare initial design parameters dictionary
	# Uncomment this if you want to use initial values from definitions.py
	# initialDesign={ name: desc['init'] for name, desc in designParams.items() }
	# Uncomment this if you want to use lower bounds for initial values of design parameters
	# initialDesign={ name: desc['lo'] for name, desc in designParams.items() }
	# Uncomment this if you want to use the result of nominal design as initial point
	initialDesign={
		'c_out':    4.496976e-12, 
		'diff_l':   3.237868e-06, 
		'diff_w':   1.541743e-05, 
		'load_l':   3.077559e-06, 
		'load_w':   5.160282e-05, 
		'mirr_l':   2.677943e-06, 
		'mirr_ld':  3.758176e-06, 
		'mirr_w':   5.644932e-05, 
		'mirr_wd':  8.414813e-06, 
		'mirr_wo':  3.312984e-05, 
		'out_l':    1.272839e-06, 
		'out_w':    1.719281e-05, 
		'r_out':    2.216717e+04, 
	}
	
	# Prepare corners, cartesian product of 
	#   MOS model:    wp, ws, wo, and wz (named wp, ws, wo, and wz)
	#   voltages:     1.7 and 2.0        (named vl and vh)
	#   temperatures: 0 and 100          (named tl and th)
	corners, names = generateCorners(
		specs=[
			(
				'model', 'mos', 
				['wp', 'ws', 'wo', 'wz'], 
				['wp', 'ws', 'wo', 'wz']
			), 
			(
				'param', 'vdd', 
				[opParams['vdd']['lo'], opParams['vdd']['hi']], 
				['vl', 'vh'], 
			), 
			(
				'param', 'temperature', 
				[opParams['temperature']['lo'], opParams['temperature']['hi']], 
				['tl', 'th'], 
			), 
		], 
		heads=[ 'opus' ], 
	)
	
	# Add nominal corner (model tm, 1.8V, 25degC)
	nominalCorner={
		'nom': {
			'heads': [ 'opus' ], 
			'modules': [ 'tm' ], 
			'params': {
				'vdd': opParams['vdd']['init'], 
				'temperature': opParams['temperature']['init']
			}, 
		}
	}
	corners.update(nominalCorner)
	
	# Now we have 4x2x2+1=17 corners, print their names
	print("Corner names")
	print(sorted(corners.keys()))
	
	# Area should be evauated only in corner 'nom'
	measures['area']['corners']=[ 'nom' ]
	
	# Prepare parallel environment
	cOS.setVM(MPI(mirrorMap={'*':'.'}, persistentStorage=False))
	
	# Design it, nominal statistical parameters are treated as fixed parameters
	cbd=CornerBasedDesign(
		designParams, heads, analyses, measures, corners, 
		fixedParams=[nominalStat], variables=variables, norms={ 'area': 100e-12 }, 
		# tradeoff=1e-6, 
		# stepTol=1e-4, 
		initial=initialDesign, 
		method='global', 
		incrementalCorners=True, 
		evaluatorOptions={'debug': 0}, 
		debug=1
	)
	
	# Run optimization
	atDesign, aggregator, analysisCount = cbd()
	
	# Print design parameters and performance measures
	print(formatParameters(atDesign))
	print(aggregator.formatResults())
	
	# Finalize cOS parallel environment
	cOS.finalize()
	
