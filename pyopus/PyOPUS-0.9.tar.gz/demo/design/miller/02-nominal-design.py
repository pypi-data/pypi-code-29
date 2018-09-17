# Nominal design

from definitions import *
from pyopus.design.cbd import CornerBasedDesign
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
	initialDesign={ name: desc['init'] for name, desc in designParams.items() }
	
	# Prepare one corner, module 'tm', nominal op parameters
	corners={
		'nom': {
			'heads': [ 'opus' ], 
			'params': nominalOp, 
			'modules': ['tm']
		}
	}
	
	# Prepare parallel environment
	cOS.setVM(MPI(mirrorMap={'*':'.'}))
	
	# Design it, nominal statistical parameters are treated as fixed parameters
	cbd=CornerBasedDesign(
		designParams, heads, analyses, measures, corners, 
		fixedParams=[nominalStat], variables=variables, norms={ 'area': 100e-12 }, 
		initial=initialDesign, 
		method='global', 
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
	
