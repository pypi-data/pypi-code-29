# Optimize SchwefelA function with PSADE
# Collect cost function and plot progress
# Run the example with mpirun/mpiexec to use parallel processing

from pyopus.optimizer.psade import ParallelSADE
from pyopus.problems import glbc
from pyopus.optimizer.base import Reporter, CostCollector, RandomDelay
import pyopus.plotter as pyopl
from numpy import array, zeros, arange
from numpy.random import seed
from pyopus.parallel.cooperative import cOS
from pyopus.parallel.mpi import MPI


if __name__=='__main__':
	cOS.setVM(MPI())
	
	ndim=30
	
	prob=glbc.SchwefelA(n=ndim)
	slowProb=RandomDelay(prob, [0.001, 0.010])
	
	opt=ParallelSADE(
		slowProb, prob.xl, prob.xh, debug=0, maxiter=75000, seed=None
	)
	cc=CostCollector()
	opt.installPlugin(cc)
	opt.installPlugin(Reporter(onIterStep=1000))
	opt.reset()
	opt.run()
	cc.finalize()
	
	pyopl.init()
	pyopl.close()
	f1=pyopl.figure()
	pyopl.lock(True)
	if pyopl.alive(f1):
		ax=f1.add_subplot(1,1,1)
		ax.semilogy(arange(len(cc.fval)), cc.fval)
		ax.set_xlabel('evaluations')
		ax.set_ylabel('f')
		ax.set_title('Progress of parallel SADE')
		ax.grid()
		pyopl.draw(f1)
	pyopl.lock(False)
	
	print("x=%s f=%e" % (str(opt.x), opt.f))
	
	pyopl.join()
	
	cOS.finalize()
