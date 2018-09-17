# Optimize shifted quadratic function with Hooke-Jeeves optimizer. 

import numpy as np
from pyopus.optimizer.hj import HookeJeeves

def f(x):
	return (x[0]-1.0)**2+(x[1]-2)**2
	
if __name__=='__main__':
	opt=HookeJeeves(f, debug=1, maxiter=100000, step0=1e-1, minstep=1e-6)
	x0=np.array([5.0,5.0])
	opt.reset(x0)
	opt.run()

	print("x=%s f=%e" % (str(opt.x), opt.f))
