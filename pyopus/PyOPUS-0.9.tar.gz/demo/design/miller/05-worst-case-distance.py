# Worst case distance

from definitions import *
from pyopus.design.wcd import WorstCaseDistance
# If MPI is imported an application not using MPI will behave correctly
# (i.e. only slot 0 will run the program) even when started with mpirun/mpiexec
from pyopus.parallel.mpi import MPI
from pyopus.parallel.cooperative import cOS


if __name__=='__main__':
	# Result of sizing across corners
	atDesign={
		#'c_out':    6.737942e-13,
		#'dif_l':    2.170269e-06,
		#'dif_w':    4.396577e-06,
		#'load_l':    2.800742e-06,
		#'load_w':    6.228898e-05,
		#'mirr_l':    3.378882e-07,
		#'mirr_ld':    2.072842e-06,
		#'mirr_w':    5.311666e-05,
		#'mirr_wd':    1.979695e-06,
		#'mirr_wo':    4.983195e-05,
		#'out_l':    6.257517e-07,
		#'out_w':    3.441845e-05,
		#'r_out':    1.402169e+05
		
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
	
	# Prepare parallel environment
	cOS.setVM(MPI(mirrorMap={'*':'.'}))
	
	# 3-sigma worst case
	wc=WorstCaseDistance(
		heads, analyses, measures, statParams, opParams, variables=variables, 
		fixedParams=atDesign, 
		debug=2, spawnerLevel=2
	)
	wcresults, analysisCount = wc(wcList)
	print(wc.formatResults())
	print(wc.analysisCount)
	
	# Finalize cOS parallel environment
	cOS.finalize()
	
