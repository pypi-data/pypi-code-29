from .dumptools import QPDumpError, processParams, getVariables, formatNameList, readNumeric
from .dumptools import validateLowercaseIdentifier
from . import guiglobals
import platform

__all__ = [ 'dumpMPI', 'generateVMLayout', 'dumpHostsFile' ]


def dumpMPI(description, task, localsDict={}):
	mdict={}
	
	# Number of processors
	s=task[1]['mpi']['processors'].strip()
	if len(s)<=0:
		fp=None
	else:
		try:
			fp=int(readNumeric(s))
		except Exception as e:
			raise QPDumpError("Number of processors murst be a number. \n"+str(e))
		if fp<1:
			raise QPDumpError("Number of processors must be at least 1.")
	nproc=fp
	mdict['processors']=fp
	
	# Mirroring
	b=task[1]['mpi']['mirror']
	mdict['mirror']=b
	
	# Persistent storage
	b=task[1]['mpi']['persistent']
	mdict['persistent']=b
	
	# MPI debug
	s=task[1]['mpi']['vmdebug'].strip()
	if len(s)<=0:
		fp=None
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("MPI debug level is not a number. \n"+str(e))
		if fp<0:
			raise QPDumpError("MPI debug level must be positive.")
	mdict['vmdebug']=fp
	
	# cOS debug
	s=task[1]['mpi']['cosdebug'].strip()
	if len(s)<=0:
		fp=None
	else:
		try:
			fp=readNumeric(s)
		except Exception as e:
			raise QPDumpError("Cooperative OS debug level is not a number. \n"+str(e))
		if fp<0:
			raise QPDumpError("Cooperative OS debug level must be positive.")
	mdict['cosdebug']=fp
	
	return mdict

def generateVMLayout(task):
	vmLayout={}
	
	# Assume processors string is validated (dumpMPI() was successfull)
	nproctxt=task[1]['mpi']['processors'].strip()
	if len(nproctxt)<=0:
		# Not specified, use all available
		cpuAvail=guiglobals.availableCPUcount()
		nproc=cpuAvail-guiglobals.tasksMonitor.usedCPUCount()
	else:
		nproc = int(nproctxt)
	
	toAlloc=nproc
	for h in guiglobals.hosts:
		name=h[0].strip()
		
		# CPU count in hosts table is not validated
		try:
			cpua=int(h[1])
		except:
			raise QPDumpError("CPU count for host '%s' is not an integer." % name)
		
		if cpua<1:
			raise QPDumpError("CPU count for host '%s' must be greater than zero." % name)
		
		if name in guiglobals.tasksMonitor.allocatedHostNames():
			for taskName, tcpu in guiglobals.tasksMonitor.hostLayout(name).items():
				cpua-=tcpu
		
		if cpua>0:
			if cpua<=toAlloc:
				vmLayout[name]=cpua
				toAlloc-=cpua
			else:
				vmLayout[name]=toAlloc
				toAlloc=0
			
		if toAlloc==0:
			break
	
	if toAlloc>0:
		slots=guiglobals.availableCPUcount()
		usedSlots=guiglobals.tasksMonitor.usedCPUCount()
		
		raise QPDumpError(
			"Too few CPUs in cluster (requred %d, available %d). Add more hosts." 
			% (nproc, slots-usedSlots)
		)
	
	return vmLayout

def dumpHostsFile(vmLayout):
	if platform.platform().startswith('Windows'):	
		# Microsoft MPI hosts file
		txt="# Generated Microsoft MPI hosts file\n"
		for h, slots in vmLayout.items():
			txt+="%s %d\n" % (h, slots)
	else:
		# OpenMPI hosts file
		txt="# Generated OpenMPI hosts file\n"
		for h, slots in vmLayout.items():
			txt+="%s slots=%d\n" % (h, slots)
	
	return txt

	
