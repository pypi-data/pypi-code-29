
# tasksMonitor.vmLayout(taskName) returns a dictionary
#   - startTime - timestamp at which the task was started
#   - pid       - task's master pid
#   - vmLayout  - dictionary with host as key and ncpu as value

# tasksMonitor.hostLayout(hostName) returns a dictionary 
# with taskName as key and ncpu as value

from shutil import which
import platform
import socket, multiprocessing

tasksMonitor=None

# Get localhost name
try:
	fqdn=socket.gethostbyaddr(socket.gethostname())[0]
	hostname=fqdn.split(".")[0]
except:
	hostname="localhost"

# Get noumber of CPUs
try:
	localCPUcount=multiprocessing.cpu_count()
except:
	localCPUcount=1
	
# Default hosts list
# hostname, cpus
hosts=[[hostname, localCPUcount]]

def availableCPUcount():
	slots=0
	for h in hosts:
		try:
			ncpu=int(h[1])
		except:
			# Bad CPU count, skip host
			continue
		slots+=ncpu
	
	return slots

if platform.platform().startswith('Windows'):
	mpiLauncher=which("mpiexec.exe")
else:
	mpiLauncher=which("mpirun")

mpiSupported=mpiLauncher is not None
