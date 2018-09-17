# Outsources tasks, run this example as
#  mpirun -n 4 python3 02-remote.py
#
# Under Windows you should use Microsoft MPI. mpiexec and python should be in 
# the system path. 
#
#   mpiexec /np <number of processes> python 02-remote.py

from pyopus.parallel.cooperative import cOS
from pyopus.parallel.mpi import MPI
from funclib import printMsgMPI

if __name__=='__main__':
	# Set up MPI
	cOS.setVM(MPI())

	# Spawn two tasks (locally)
	tidA=cOS.Spawn(printMsgMPI, kwargs={'msg': 'Hello A', 'n': 10})
	tidB=cOS.Spawn(printMsgMPI, kwargs={'msg': 'Hello B', 'n': 20})

	# Spawn two remote tasks
	tidC=cOS.Spawn(printMsgMPI, kwargs={'msg': 'Hello C', 'n': 15}, remote=True)
	tidD=cOS.Spawn(printMsgMPI, kwargs={'msg': 'Hello D', 'n': 18}, remote=True)

	# IDs of running tasks
	running=set([tidA,tidB,tidC,tidD])

	# Wait for all tasks to finish
	while len(running)>0:
		# Wait for any task
		retval=cOS.Join()
		# Wait for tasks with specified IDs
		# retval=cOS.Join(running)
		
		# Remove IDs of finished tasks
		for tid in retval.keys():
			print("Task: "+str(tid)+" finished, return value: "+str(retval[tid]))
			running.remove(tid)

	# Cleanup and exit MPI, need to do this if MPI is used
	cOS.finalize()
