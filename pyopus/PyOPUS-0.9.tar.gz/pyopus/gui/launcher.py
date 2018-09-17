from ..misc.dbgprint import FileMessagePrinter
from ..misc.debug import DbgMsgOut, DbgSetup

from pprint import pprint
import sys, os, subprocess, time
from socket import gethostname
import uuid, json, platform

# Launch a task, collect output in a log

if __name__=='__main__':
	name=sys.argv[1]
	
	os.chdir(name)
	cwd=os.getcwd()
	
	# Set debug output format (print time, one decimal place)
	DbgSetup(True, 1)
	
	# Open log, line-buffered
	with open(name+".log", "w", 1) as f:
		fpr=FileMessagePrinter(f)
		f.write(str(uuid.uuid4())+"\n")
		lnchPid=os.getpid()
		lnchHost=gethostname()
		DbgMsgOut("LNCH", "Logging started by launcher process on host %s, pid=0x%x (%d)" % (lnchHost, lnchPid, lnchPid), fpr)
		DbgMsgOut("LNCH", "Folder "+cwd, fpr)
		
		_, executable = os.path.split(sys.executable)
		if len(sys.argv)<=2:
			p=subprocess.Popen([sys.executable, 'runme.py'], stdout=f, bufsize=1)
			executable = executable+" runme.py"
		else:
			if platform.platform().startswith('Windows'):
				p=subprocess.Popen([
					'mpiexec', '/machinefile', 'hosts', 
					executable, 'runme.py'], stdout=f, bufsize=1)
				executable="mpiexec "+executable+" runme.py"
			else:
				p=subprocess.Popen([
					'mpirun', '--hostfile', 'hosts', 
					executable, 'runme.py'], stdout=f, bufsize=1)
				executable="mpirun "+executable+" runme.py"
		
		pid=p.pid
		DbgMsgOut("LNCH", "Engine process (%s) started on host %s, pid=0x%x (%d)" % (executable, lnchHost, pid, pid), fpr)
		
		# Write to lock.response
		with open("lock.response", "w") as fl:
			fl.write("%.1f started %d (0x%x)\n" % (time.time(), pid, pid))
		DbgMsgOut("LNCH", "lock.response file created at task start.", fpr)
		
		# p.communicate()
		st=p.wait()
		
		# OS dependent
		if st==0:
			sttxt="OK"
		elif st==-15:
			# Only for single CPU runs, mpirun from OpenMPI returns 1 on SIGINT
			sttxt="INTERRUPTED"
		else:
			sttxt="FAILED"
			
		DbgMsgOut("LNCH", "", fpr)
		DbgMsgOut("LNCH", "Task finished with exit status %d (%s)" % (st, sttxt), fpr)
		
		# Write to lock.response
		with open("lock.response", "a") as fl:
			fl.write("%.1f finished %d\n" % (time.time(), st))
		DbgMsgOut("LNCH", "lock.response file updated at task exit.", fpr)
		
	
