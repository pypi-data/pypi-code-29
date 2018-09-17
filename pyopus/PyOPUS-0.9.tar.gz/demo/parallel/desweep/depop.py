# Runs differential evolution on problems in glbc for population 
# sizes from 10 to 100. Every run is repeated 50 times. 
# The runs are performed in parallel by means of MPI library. 
# 
# The cost function history is pickled in files named fhist_fx_py_rz.pck 
# where x is the function index, y is the population size and z is the run 
# number. The file contains a pickled1 1D array of cost function values. 
#
# The summary is pickled in fsummary.pck. It contains a dictionary 
# with the following members: 
# * funcIndices - list of function indices from global test problem suite
# * names - list of function names
# * dims - list of function dimension 
# * populationSizes - population sizes list 
# * finalf - final (best) function value array 
#     first index - function index 
#     second index - population size index 
#     third index - run index
# 
# Every run evaluates 75000 candidates or evolves 1500 generations, depending 
# on the nGen and maxIter settings. 
# Produces a large number of fhist*.pck files (around 60GB) if writeFhist is 
# set to True. 
#
# To run in parallel, type
#
#  mpirun -hostfile hosts.openmpi -n 8 python3 depop.py
#
# Under Windows you should use Microsoft MPI. mpiexec and python should be in 
# the system path. 
#
#   mpiexec /machinefile hosts.msmpi /np <number of processes> python depop.py

# Imports
import os
from numpy import array, zeros, arange
from pickle import dump
from pyopus.problems import glbc
from pyopus.parallel.cooperative import cOS 
from pyopus.parallel.mpi import MPI
import funclib
# End imports

# Settings 
# First three problems of GlobalBCsuite
funcIndicesList=[0,1,2] 
# For the whole GlobalBCsuite uncomment this
# range(len(glbc.GlobalBCsuite))

# Population sizes for which we want to evaluate the performance of DE
popSizeList=[10, 20] # range(10, 101, 40) 

# Number of runs
nRun=3 

# Number of generations (unlimited)
nGen=None # or a number to limit the number of generations

# Maximal number of function evaluations
maxIter=75000 # or None for no limit

# Do we want to write function evaluation history to files (one file per run)
writeFhist=True
# End settings

def jobGenerator():
	for atFunc in range(len(funcIndicesList)):
		for atPopSize in range(len(popSizeList)):
			for atRun in range(nRun):
				yield (
					funclib.deRun, 
					[], 
					{
						'prob': glbc.GlobalBCsuite[funcIndicesList[atFunc]](), 
						'popSize': popSizeList[atPopSize], 
						'runIndex': atRun, 
						'maxiter': maxIter, 
						'maxGen': nGen, 
					},
					# Extra data not passed to deRun
					(atFunc, atPopSize, atRun)
				)

def resultsCollector(finalF):
	try:
		while True:
			index, job, result = yield
			atFunc, atPopSize, atRun = job[3] # Get extra data
			fBest, fHistory = result
			
			print("Received results for %s, run=%2d, popsize=%3d " % (
				glbc.GlobalBCsuite[funcIndicesList[atFunc]].name, 
				atRun+1, 
				popSizeList[atPopSize]
			))
			
			if writeFhist:
				with open("fhist_f%d_p%d_r%d.pck" % (funcIndicesList[atFunc], popSizeList[atPopSize], atRun), "wb") as fp:
					dump(fHistory, fp, protocol=-1)
				
			
			finalF[atFunc][atPopSize][atRun]=fBest
	except GeneratorExit:
		print("No more results to collect.")
	
# Main program
if __name__=='__main__':
	cOS.setVM(MPI(startupDir=os.getcwd()))
	
	# Prepare results storage
	finalF=zeros((len(funcIndicesList), len(popSizeList), nRun))
	
	# Dispatch jobs
	cOS.dispatch(
		jobList=jobGenerator(), 
		collector=resultsCollector(finalF), 
		remote=True 
	)
	
	# Prepare function names
	names=[]
	dims=[]
	for i in funcIndicesList:
		prob=glbc.GlobalBCsuite[i]()
		names.append(prob.name)
		dims.append(prob.n)
	
	# Store summary
	summary={
		'funcIndices': funcIndicesList, 
		'names': names, 
		'dims': dims, 
		'populationSizes': popSizeList, 
		'finalF': finalF
	}
	with open("fsummary.pck", "wb") as fp:
		dump(summary, fp, protocol=-1)
	
	cOS.finalize()
