# CEC13 problems test suite

from pyopus.problems.cec13 import *
import numpy as np

if __name__=='__main__':
	print("CEC13 problems, n=10")
	for ii in range(len(CEC13.names)):
		prob=CEC13(number=ii, n=10)
		
		f0=prob(np.zeros(10))
		fmincalc=prob(prob.xmin)
		
		print("%2d: %40s: f0=%14e fmincalc=%14e fmin=%14e" % (ii, prob.name, f0, fmincalc, prob.fmin))
	print()

