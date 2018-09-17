# Yield targeting

from definitions import *
from pyopus.design.yt import YieldTargeting
from pyopus.evaluator.aggregate import formatParameters
# If MPI is imported an application not using MPI will behave correctly
# (i.e. only slot 0 will run the program) even when started with mpirun/mpiexec
from pyopus.parallel.mpi import MPI
from pyopus.parallel.cooperative import cOS


if __name__=='__main__':
	# Add 'wcd' module to all analyses (we have no corners)
	for name,an in analyses.items():
		an['modules'].append('wcd')
		
	# Worst case performances (skip area, transistor op conditions, and auxiliary measures)
	wcList=list(measures.keys())
	wcList.sort()
	wcList.remove('area')
	wcList.remove('vgs_drv')
	wcList.remove('vds_drv')
	wcList.remove('gain_com')
	wcList.remove('gain_vdd')
	wcList.remove('gain_vss')
	
	# Result of sizing across corners
	atDesign={
		'c_out':    3.293147e-12,
		'dif_l':    1.528948e-06,
		'dif_w':    2.086576e-05,
		'load_l':   3.219635e-06,
		'load_w':   7.017996e-05,
		'mirr_l':   3.179717e-07,
		'mirr_ld':  2.929402e-06,
		'mirr_w':   4.511896e-05,
		'mirr_wd':  1.424699e-05,
		'mirr_wo':  7.112520e-05,
		'out_l':    7.321417e-07,
		'out_w':    9.399774e-05,
		'r_out':    2.305440e+04,
	}
	
	# Prepare parallel environment
	cOS.setVM(MPI(mirrorMap={'*':'.'}))
	
	# 3-sigma target yield
	yt=YieldTargeting(
		designParams, statParams, opParams, 
		heads, analyses, measures, variables=variables, 
		beta=3.0, wcSpecs=wcList, 
		# Comment out to use default initial point (lo+hi)/2
		initial=atDesign, 
		initialNominalDesign=True, 
		# Norms for measures with zero goal
		norms={ 'area': 100e-12, 'vgs_drv': 1e-3, 'vds_drv':1e-3 }, 
		tradeoffs=1e-6, # Tradeoff optimization weight, can be overridden in *CbdOptions
		stopWhenAllSatisfied=True, 
		# Initial nominal optimization
		initialCbdOptions={ 
			'debug': 1, 'method': 'global', 'stepTol': 1e-5, 
		}, 
		# Main optimization
		cbdOptions={ 
			'debug': 1, 'method': 'global', 'stepTol': 1e-5, 
		}, wcOptions={ 'debug': 0 }, 
		debug=2, spawnerLevel=1
	)
	atDesign, agg, wc, anCount = yt()
	print(formatParameters(atDesign))
	print(wc.formatResults())
	print(agg.formatResults())
	print(anCount)
	
	# Finalize cOS parallel environment
	cOS.finalize()
	
