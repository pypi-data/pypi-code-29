# Optimize simple amplifier - response linearization

# Imports
from pyopus.evaluator.performance import PerformanceEvaluator
from pyopus.evaluator.aggregate import *
from pyopus.optimizer import optimizerClass
import pyopus.wxmplplot as pyopl
import numpy as np
# End imports

def plotResponse(x, y, title):
	ideal=y[0]+(x-x[0])*(y[-1]-y[0])/(x[-1]-x[0])
	
	# Create first figure (plot window). This is now the active figure. 
	f1=pyopl.figure(windowTitle=title, figpx=(600,400), dpi=100)	
	
	# Lock GUI
	pyopl.lock(True)
	
	# Check if figure is alive
	if pyopl.alive(f1):
		ax1=f1.add_axes((0.12,0.12,0.76,0.76))
		ax1.plot(x/1e-6, y, '-', label='amplifier', color=(1,0,0))
		ax1.plot(x/1e-6, ideal, '--', label='ideal', color=(0,0.8,0))
		ax1.set_xlabel('I1 [uA]')
		ax1.set_ylabel('V(3) [V]')
		ax1.legend(loc='upper left')
		ax1.set_xlim([-100,100])
		f1.suptitle(title)
		pyopl.draw(f1)
		
	# Unlock GUI
	pyopl.lock(False)
	
if __name__=='__main__':
	heads = {
		'opus': {
			'simulator': 'SpiceOpus', 
			# Circuit definition
			'moddefs': {
				'def':     { 'file': 'amp.inc' }, 
			}, 
			# Parameter values (global)
			'params': {
				'vcc': 12.0,
				'temperature': 25
			}
		}
	}
	
	analyses = {
		# DC sweep of I1
		'dc': {
			'head': 'opus', 
			'modules': [ 'def' ], 
			'command': "dc(-100e-6, 100e-6, 'lin', 100, 'i1', 'dc')"
		}, 
	}

	measures = {
		# Input current
		'x': {
			'analysis': 'dc', 
			'expression': 'scale()', 
			'vector': True
		}, 
		# Output voltage
		'y': {
			'analysis': 'dc', 
			'expression': 'v("3")', 
			'vector': True
		}, 
		# Gain
		'gain': {
			'analysis': 'dc', 
			'expression': '(v("3")[-1]-v("3")[0])/(scale().max()-scale().min())', 
			
		}, 
		# Maximal departure from linear response
		'absdif': {
			'analysis': None, 
			'expression': """
x=result['x'][cornerName]
y=result['y'][cornerName]
slope=result['gain'][cornerName]
ideal=(x-x[0])*slope+y[0]
absdif=np.abs(y-ideal).max()
""", 
		},
	}

	costDefinition = [
		{
			'measure': 'absdif', 
			'norm': Nbelow(0.0, 1.0),	
			'shape': Slinear2(1.0,0.0),
		},
		{
			'measure': 'gain', 
			'norm': Nabove(20e3, 10e3),	
			'shape': Slinear2(1.0,0.0),
		},
	]

	# Main program
	# Performance evaluator
	pe=PerformanceEvaluator(heads, analyses, measures, debug=0)
	
	# pe({'r1': 45e3, 'r2': 195e3})
	# print(pe.formatResults())
	
	inOrder=['r1', 'r2']
	xlow= np.array([5e3,  20e3])
	xhi=  np.array([50e3, 200e3])
	xinit=np.array([45e3, 195e3])
	
	# Cost evaluator
	ce=Aggregator(pe, costDefinition, inOrder, debug=0)
	
	# ce([45e3, 195e3])
	# print(ce.formatParameters())
	# print("")
	# print(ce.formatResults())
	
	pyopl.init()
	
	# Initial evaluation and plot
	cf=ce(xinit)
	plotResponse(pe.results['x']["default"], pe.results['y']["default"], "Initial response")

	# Optimizer (Hooke-Jeeves). xlo and xhi must be numpy arrays. 
	opt=optimizerClass("HookeJeeves")(ce, xlo=xlow, xhi=xhi, maxiter=1000)

	# Set initial point. Must be a numpy array. 
	opt.reset(xinit)

	# Install reporter plugin. 
	# Print cost. Also print performance every time the cost is decreased. 
	opt.installPlugin(ce.getReporter())
	
	# Run
	opt.run()

	# Optimization result
	xresult=opt.x
	iterresult=opt.bestIter
		
	# Final evaluation at xresult. 
	cf=ce(xresult)
	plotResponse(pe.results['x']["default"], pe.results['y']["default"], "Final response")
		
	# Print results. 
	print("\n\nFinal cost: "+str(cf)+", found in iter "+str(iterresult)+", total "+str(opt.niter)+" iteration(s)")
	print(ce.formatParameters())
	print(ce.formatResults(nMeasureName=10, nCornerName=15))
	print("")
	
	# Cleanup intemediate files
	pe.finalize()
	
	# Wait for plot windows to close
	pyopl.join()
	
