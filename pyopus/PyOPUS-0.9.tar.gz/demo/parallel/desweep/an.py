# Load results summary, plot function value history for given function, 
# population size, and run. 
# Run this by typing 
#  python3 an.py

from numpy import array, zeros, arange
from pickle import dump, load
import pyopus.plotter as pyopl
from pprint import pprint

if __name__=='__main__':
	# Which history to load
	findex=0     # Function index
	popsize=10   # Population size
	runindex=0   # Run index (starting with 0)
		
	# Load the summary and print it
	with open("fsummary.pck", "rb") as f:
		summary=load(f)
	pprint(summary)
	
	# Read the history from a file
	with open("fhist_f%d_p%d_r%d.pck" % (findex, popsize, runindex), "rb") as f:
		fhist=load(f)
	
	# Initialize plotting
	pyopl.init()
	pyopl.close()
	
	# Create a figure
	f1=pyopl.figure()
	pyopl.lock(True)
	if pyopl.alive(f1):
		# Draw the history
		ax=f1.add_subplot(1,1,1)
		ax.semilogy(arange(len(fhist))/popsize, fhist)
		ax.set_xlabel('generation')
		ax.set_ylabel('f')
		ax.set_title('Progress of differential evolution')
		ax.grid()
		pyopl.draw(f1)

	pyopl.lock(False)
	
	# Wait for the plot window to close
	pyopl.join()
	
	
