# Dispatches tasks to computational nodes until specified result is reached or exceeded
# This example also demonstrates the use of a collector. 
#  mpirun -n 4 python3 04-dyndispatch.py
#
# Under Windows you should use Microsoft MPI. mpiexec and python should be in 
# the system path. 
#
#   mpiexec /np <number of processes> python 04-dyndispatch.py

from pyopus.parallel.cooperative import cOS
from pyopus.parallel.mpi import MPI
from funclib import dynJobGenerator, resultsCollector

if __name__=='__main__':
	# Set up MPI
	cOS.setVM(MPI())

	# This list will be filled with results
	results=[]

	# Dispatch the jobs
	# Note that when a results collector is specified a dispatch does not return a list 
	# with job results, unless you pass the buildResultList option and set it to True. 
	cOS.dispatch(
		jobList=dynJobGenerator(start=0, step=1), # Start at 0, increase by one
		collector=resultsCollector(results, stopAtResult=150), 
		remote=True
	)

	print("Results: "+str(results))

	# Finish, need to do this if MPI is used
	cOS.finalize()
