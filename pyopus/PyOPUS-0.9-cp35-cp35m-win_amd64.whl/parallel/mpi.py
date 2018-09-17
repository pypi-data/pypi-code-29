"""
.. inheritance-diagram:: pyopus.parallel.mpi
    :parts: 1
	
**A virtual machine based on MPI and mpi4py (PyOPUS subsystem name: MPI)**

Attempts to import :mod:`mpi4py`. If import fails the mpi4py wrapper for the 
MPI library is not available on the computer and an arror is raised. 
"""

# MPI launcher module
from ..misc.dbgprint import MessagePrinter
from ..misc.debug import DbgDefaultPrint, DbgSetDefaultPrinter, DbgMsgOut, DbgMsg

from . import base
from .base import VirtualMachine, HostID, TaskID, MsgTaskExit, MsgTaskResult, getNumberOfCores

# Try importing MPI support. If it fails, raise our own exception. 
try:
	from mpi4py import MPI as mpi
except ImportError:
	raise PyOpusError(DbgMsg("MPI", "Failed to import mpi4py module. MPI not supported."))

if base.firstVM is not None:
	raise PyOpusError(DbgMsg("MPI", "MPI does not coexist with other VM types."))
	
import sys, os, shutil
from time import time
from ..misc.env import environ
from ..misc import identify
from .. import PyOpusError

__all__ = [ 'MPIHostID', 'MPITaskID', 'MPI' ] 


class MPIHostID(HostID):
	"""
	A MPI host ID class based on the :class:`~pyopus.parallel.base.HostID` 
	class. 
	
	In the MPI library does not provide host IDs so we use hostnames. Invalid 
	host ID has ``None`` for hostname. 
	
	The actual hostname can be accessed as the :attr:`name` member. 
	
	See the :class:`~pyopus.parallel.base.HostID` class for more information. 
	"""
	@staticmethod
	def bad():
		"""
		A static member function. Called with ``MPIHostID.bad()``. Returns an 
		invalid host ID. 
		"""
		return MPIHostID(None)
	
	def __init__(self, name):
		self.name=name
	
	def __eq__(self, other):
		if self is None or other is None:
			return self is None and other is None
		return self.name==other.name
			
	def __ne__(self, other):
		if self is None or other is None:
			return not (self is None and other is None)
		return self.name!=other.name
		
	def __hash__(self):
		return hash(self.name)
		
	def __str__(self):
		if self.valid():
			return "%s" % (self.name)
		else: 
			return "MPI_NOHOST"
	
	def __repr__(self):
		return "MPIHostID("+repr(self.name)+")"
		
	def valid(self):
		"""
		Returns ``True`` if this :class:`MPIHostID` object is valid. 
		"""
		if self.name is None:
			return False
		else:
			return True


class MPITaskID(TaskID):
	"""
	A MPI task ID class based on the :class:`~pyopus.parallel.base.TaskID` 
	class. 
	
	A task ID is composed of MPI rank and task number which is assigned by the 
	spawner. Valid task IDs have nonnegative rank. 
	
	The actual rank and task number can be accessed as :attr:`rank` 
	and :attr:`number` members. 
	
	See the :class:`~pyopus.parallel.base.TaskID` class for more information. 
	"""
	@staticmethod
	def bad():
		"""
		A static member function. Called with ``MPITaskID.bad()``. Returns an 
		invalid task ID. 
		"""
		return MPITaskID(-1)
		
	def __init__(self, rank, number=None):
		if rank is None or rank<0:
			rank=-1
		self.rank=rank
		self.number=number
		
	def __eq__(self, other):
		return self.rank==other.rank and self.number==other.number
		
	def __ne__(self, other):
		return self.rank!=other.rank or self.number!=other.number
	
	def __hash__(self):
		return self.rank+self.number
	
	def __nonzero__(self):
		return self.rank is not None and self.rank>=0
		
	def __str__(self):
		if self.valid():
			return "%d:%d" % (self.rank, self.number)
		else: 
			return "MPI_NOTASK"
	
	def __repr__(self):
		return "MPITaskID("+repr(self.rank)+", "+repr(self.number)+")"
	
	def valid(self):
		"""
		Returns ``True`` if this :class:`MPITaskID` object is valid. 
		"""
		if self.rank<0:
			return False
		else:
			return True
		
		
class MPI(VirtualMachine): 
	"""
	A virtual machine class based on the mpi4py wrapper for MPI. 
	
	One task (rank 0) is the spawner and does all the spawning. This is the main 
	task that runs the main program. 
	Other tasks (rank>0) are workers. Workers run a spawn loop in which they 
	receive spawn requests from the spawner. A worker can run one spawned task 
	at a time. If the task fails (caught exception), the spawner is notified, 
	upon which the loop expects a new spawn requst. If a task finishes cleanly 
	the spawner is also notified. The point at which the spawner and the 
	workers separate is in the :meth:`spawnerBarrier` method (this is also the 
	place where the worker's spawn loop is entered. The spawner is the only 
	task that returns from :meth:`spawnerBarrier`. Workers exit the spawn loop 
	only when they receive an exit request from the spawner (i.e. only when 
	the MPI application is about to terminate). 
	
	Assumes homogeneous clusters. This means that LINUX32 and LINUX64 are not 
	homogeneous, as well as LINUX32 and WINDOWS32. 
	Inhomogenous clusters are possible if the undelying MPI library has 
	supports for this feature. 
	
	See the :class:`~pyopus.parallel.base.VirtualMachine` class for more 
	information on the constructor. 
	"""
	
	# Static members - only once per every process that uses MPI. 
	
	# Next task number 
	nextTaskNumber=None
	
	# Host name
	host=mpi.Get_processor_name()
	
	# Rank
	rank=None
	
	# Task number
	taskNumber=None
	
	# For spawner
	vmStatus=None
	"""
	Static member that appears once per every Python process using the MPI 
	library. Available only on the spawner. 
	
	Represents the status of the MPI virtual machine. 
	"""
	
	def __init__(self, debug=0, startupDir=None, translateStartupDir=True, mirrorMap=None, persistentStorage=False):
		VirtualMachine.__init__(
			self, debug, startupDir=startupDir, 
			translateStartupDir=translateStartupDir, 
			mirrorMap=mirrorMap, 
			persistentStorage=persistentStorage
		)
		self.setWorkerDebug(debug)
		
		if debug>0:
			DbgMsgOut("MPI", "MPI object created, rank=%d on %s." % (MPI.rank, MPI.host))
		
	
	@staticmethod
	def slots():
		"""
		Returns the number of slots for tasks in a virtual machine. 
		Works only on the spawner. 
		
		Calls mpi.COMM_WORLD.Get_size(). 
		"""
		if MPI.vmStatus is None:
			raise PyOpusError(DbgMsg("MPI", "Task not configured as spawner."))
			
		return mpi.COMM_WORLD.Get_size()
	
	@staticmethod
	def freeSlots():
		"""
		Returns the number of free slots for tasks in the virtual machine. 
		The slot bookkeeping is done by hand.
		
		Works only on the spawner. 
		"""
		if MPI.vmStatus is None:
			raise PyOpusError(DbgMsg("MPI", "Task not configured as spawner."))
			
		return mpi.COMM_WORLD.Get_size()-len(MPI.vmStatus['usedSlots'])
	
	@staticmethod
	def freeSlotsSet():
		"""
		Returns the slot numbers of free slots. 
		
		Works only on the spawner. 
		"""
		return MPI.vmStatus['freeSlots']
	
	@staticmethod
	def hostsWithFreeSlots():
		"""
		Returns set of objects of class :class:`HostID` corresponding 
		to hosts with at least one free slot. 
		
		Works only on the spawner. 
		"""
		return MPI.vmStatus['freeHosts']
		
	@staticmethod
	def hosts():
		"""
		Returns a list of :class:`MPIHostID` objects corresponding to all 
		hosts. 
		
		Works only on the spawner. 
		"""
		if MPI.vmStatus is None:
			raise PyOpusError(DbgMsg("MPI", "Task not configured as spawner."))
		
		lst=[]
		for name in MPI.vmStatus['hosts'].keys():
			lst.append(MPIHostID(name))
		return lst
	
	@staticmethod
	def taskID():
		"""
		Returns the :class:`MPITaskID` object corresponding to the calling task. 
		"""
		return MPITaskID(MPI.rank, MPI.taskNumber)
	
	@staticmethod
	def hostID(taskID=None):
		"""
		Returns the :class:`MPIHostID` object corresponding to *task*. 
		
		If *task* is not specified, the :class:`MPIHostID` object corresponding 
		to the caller task is returned. 
		"""
		if taskID is None:
			return MPIHostID(MPI.host)
		else:
			return MPIHostID(MPI.vmStatus['slot2host'][taskID.rank])
	
	@staticmethod
	def parentTaskID():
		"""
		Returns the :class:`MPITaskID` object corresponding to the task that 
		spawned the caller task. 
		"""
		if MPI.rank==0:
			return MPITaskID(-1,-1)
		else:
			return MPITaskID(0,0)
	
	@staticmethod
	def formatSpawnerConfig():
		"""
		Formats the configuration information gathered by a spawner task as a 
		string. Works only if called by a spawner task.  
		"""
		if MPI.vmStatus is None:
			raise PyOpusError(DbgMsg("MPI", "Task not configured as spawner."))
			
		hosts=MPI.vmStatus['hosts']
		slots=MPI.vmStatus['slots']
		
		txt=""
		for host in hosts.keys():
			txt1=""
			lfree=[]
			for slot in hosts[host]['slots']:
				if slots[slot]['taskNumber']<0:
					# Free slot
					lfree.append(slot)
					
				else:
					txt1+="\tslot=%4d task=%4d\n" % (slot, slots[slot]['taskNumber'])
			txt+="%s ncpu=%d free slots: %s\n" % (host, hosts[host]['ncpu'], str(lfree))
			txt+=txt1
		
		return txt
	
	def setWorkerDebug(self, debug=0):
		"""
		Sets the worker debug message level to *debug*. 
		"""
		comm=mpi.COMM_WORLD
		worldsize=comm.Get_size()
		for rank in range(1, worldsize):
			comm.send(
				debug, 
				dest=rank, 
				tag=MPIMSGTAG_SET_DEBUG
			)
			
	def spawnFunction(self, function, args=(), kwargs={}, count=None, targetList=None, sendBack=True):
		"""
		Spawns *count* instances of a Python *function* on remote hosts and 
		passes *args* and *kwargs* to the function. Spawning a function 
		does not start a new Python interpreter. A worker is running is a spawn 
		loop where spawn requests are executed.
		
		*targetList* specifies the hosts on which the tasks are started. 
		
		If *sendBack* is ``True`` the status and the return value of the 
		spawned function are sent back to the spawner with a 
		:class:`pyopus.parallel.base.MsgTaskResult` message when the spawned 
		function returns. 
		
		Invokes the :func:`runFunctionWithArgs` function on the remote host for 
		starting the spawned function. 
		
		If spawning succeeds, updates the :attr:`vmStatus` attribute. 
		
		Spawns only in free slots. Works only on the spawner. 
		
		Returns a list of :class:`MPITaskID` objects representing the spawned 
		tasks. 
		
		See the :meth:`~pyopus.parallel.base.spawnFunction` method of the 
		:class:`~pyopus.parallel.base.VirtualMachine` class for more 
		information. 
		"""
		if MPI.vmStatus is None:
			raise PyOpusError(DbgMsg("MPI", "Task not configured as spawner."))
		
		# Get a list of free slots on specified hosts/all hosts
		slotlist=[]
		if targetList is None:
			#for host in MPI.vmStatus['hosts'].keys():
			#	slotlist.extend(MPI.vmStatus['hosts'][host]['freeSlots'])
			slotlist=MPI.vmStatus['freeSlots']
		else:
			for hostObj in targetList:
				host=hostObj.name
				slotlist.extend(MPI.vmStatus['hosts'][host]['freeSlots'])
		
		# No tasks spawned for now
		taskIDlist=[]
		
		# Spawn if there is any place left
		comm=mpi.COMM_WORLD
		while len(slotlist)>0:
			# Check number of spawned tasks
			if count is not None and len(taskIDlist)>=count:
				break
				
			# Prepare task number
			taskNumber=MPI.nextTaskNumber
			MPI.nextTaskNumber+=1
			
			# Prepare destination
			slot=slotlist.pop()
			
			# Spawn
			descriptor=self.func2desc(function)
			comm.send(
				(self, descriptor, args, kwargs, sendBack, taskNumber), 
				dest=slot, 
				tag=MPIMSGTAG_SPAWN
			)
			
			# Update vmStatus
			host=MPI.vmStatus['slots'][slot]['host']
			MPI.vmStatus['hosts'][host]['freeSlots'].discard(slot)
			MPI.vmStatus['slots'][slot]['taskNumber']=taskNumber
			if len(MPI.vmStatus['hosts'][host]['freeSlots'])<=0:
				MPI.vmStatus['freeHosts'].discard(MPIHostID(host))
			MPI.vmStatus['usedSlots'].add(slot)
			MPI.vmStatus['freeSlots'].discard(slot)
			
			# Prepare MPITaskID object
			taskIDlist.append(MPITaskID(slot, taskNumber))
			
		return taskIDlist
	
	def checkForIncoming(self, fromDestination=None):
		"""
		Returns ``True`` if there is a message waiting to be received. 
		
		*fromDestination* is the :class:`MPITaskID` of the message source. 
		``None`` implies any source. 
		"""
		fromRank=-1 if fromDestination is None else fromDestination.rank
		val, tag, rank = checkForIncoming(fromRank=fromRank)
		return val
	
	def receiveMessage(self, timeout=-1.0, fromDestination=None):
		"""
		Receives a *message* (a Python object) and returns a tuple 
		(*senderTaskId*, *message*)
		
		The sender of the *message* can be identified through the 
		*senderTaskId* object of class :class:`MPITaskID`. 
		
		If *timeout* (seconds) is negative the function waits (blocks) until 
		some message arrives. If *timeout*>0 seconds pass without receiving a 
		message, an empty tuple is returned. Zero *timeout* performs a 
		nonblocking receive which returns an empty tuple if no message is 
		received. Note that timeout>0 is implemented a bit kludgy with a poll 
		loop. 
		
		In case of an error or discarded message returns ``None``. 
		
		Handles transparently all 
		
		* task exit notification messages
		* spawned function return value messages
		
		Discards all other low-level MPI messages that were not sent with the 
		:meth:`sendMessage` method. 
		"""
		# Some messages are handled transparently
		#  MPIMSGTAG_EXIT
		#  MPIMSGTAG_DBGMSG
		#  all unknown messages
		# On blocking receive we must receive messages until we get a 
		# non-transparently handled message. 
		# On timeout receive we must receive messages until timeout 
		# expires, upon which () is returned to indicate timeout. 
		# On nonblocking receive until first non transparent message is received 
		# or we are out of messages (we return ()). 
		
		# receive any message from any source
		fromRank=-1 if fromDestination is None else fromDestination.rank
		
		# Mark time for receives with timeout
		if timeout>0:
			mark=time()
		timeoutLeft=timeout
		while True:
			# Receive it
			received=receiveMPIMessage(timeoutLeft, fromRank=fromRank)
			
			# None means error. No message. 
			if received is None:
				return None
			
			# Empty tuple means timeout in timeout mode or no message in nonblocking mode
			if len(received)==0:
				# Is this a timeout receive
				if timeout>0:
					# Recompute remaining timeout
					timeoutLeft=timeout-(time()-mark)
					# No more time remaining, return () indicating timeout
					if timeoutLeft<0:
						return ()
				else:
					# Nonblocking receive
					# No more messages, return ()
					return ()
					
			# Unpack tuple
			(source, msgTag, msg)=received
		
			# Handle messages
			# Transparently handling/discarding messages does not return. 
			# For all other handled messages we return. 
			if msgTag==MPIMSGTAG_EXIT:
				# Request to exit spawn loop
				# Ignore if we are the spawner
				if vmStatus is None:
					mpi.Finalize()
					sys.exit()
			elif msgTag==MPIMSGTAG_DBGMSG:
				# Debug message
				transparent=True
				DbgDefaultPrint(msg)
			elif msgTag==MPIMSGTAG_MESSAGE:
				# Unpack task number and message
				(fromTaskNumber, toTaskNumber, message)=msg
				# Discard transparently if toTaskNumber does not match our task number
				if toTaskNumber!=MPI.taskNumber:
					pass
				else:
					return (MPITaskID(source, fromTaskNumber), message)
			elif msgTag==MPIMSGTAG_TASK_RETVAL:
				# Unpack task number, success flag, and response
				(taskNumber, success, response)=msg
				return (MPITaskID(source, taskNumber), MsgTaskResult(success, response))
			elif msgTag==MPIMSGTAG_TASK_EXIT:
				# Unpack task number, success flag, and response
				taskNumber=msg
				if self.debug:
					DbgMsgOut("MPI", "Task "+str(MPITaskID(source, taskNumber))+" exit detected.")
				
				# Update vmStatus if message matches the taskNumber in vmStatus
				if MPI.vmStatus['slots'][source]['taskNumber']==taskNumber:
					MPI.vmStatus['slots'][source]['taskNumber']=-1
					host=MPI.vmStatus['slots'][source]['host']
					MPI.vmStatus['hosts'][host]['freeSlots'].add(source)
					if len(MPI.vmStatus['hosts'][host]['freeSlots'])>0:
						MPI.vmStatus['freeHosts'].add(MPIHostID(host))
					MPI.vmStatus['usedSlots'].discard(source)
					MPI.vmStatus['freeSlots'].add(source)
					
				taskID=MPITaskID(source, taskNumber)
				return (taskID, MsgTaskExit(taskID))
			else: 
				# Unknown message, discard transparently
				pass
			
	def sendMessage(self, destination, message):
		"""
		Sends *message* (a Python object) to a task with :class:`MPITaskID` 
		*destination*. Returns ``True`` on success. 
		
		Sends also our own task number and the destination task number. 
		"""
		return sendMPIMessage(
			destination.rank, MPIMSGTAG_MESSAGE, 
			(MPI.taskNumber, destination.number, message)
		)

		
	@staticmethod
	def finalize():
		"""
		Asks workers to exit politely. Then calls Finalize(). 
		
		See :meth:`VirtualMachine.finalize` for more information.
		"""
		comm=mpi.COMM_WORLD
		for rank in range(1, comm.Get_size()):
			comm.send(0, dest=rank, tag=MPIMSGTAG_EXIT)
		
		mpi.Finalize()


#
# Message tags
#	

MPIMSGTAG_REQUEST_NCPU=1
"""
The message tag for a cpu count and hostname request. 
"""

MPIMSGTAG_NCPU=2
"""
The message tag for a cpu count and hostname response. 
"""

MPIMSGTAG_EXIT=3
"""
Exit spawn loop (application termination). 
"""

MPIMSGTAG_SPAWN=4
"""
Spawn a task (to worker). 
"""

MPIMSGTAG_TASK_RETVAL=5
"""
The status and return value of a task (to master). 
"""

MPIMSGTAG_TASK_EXIT=6
"""
A task has finished (to master). 
"""

MPIMSGTAG_SET_DEBUG=7
"""
Set the debug level of worker.  
"""
MPIMSGTAG_DBGMSG=8
"""
Debug message that will be printed by rank 0 process.
"""
MPIMSGTAG_MESSAGE=100
"""
Message sent to a task. 
"""


#
# Message handling at MPI level. 
#
	
def sendMPIMessage(rank, msgTag, msg):
	"""
	Sends a message (binary string *msg*) to the task with rank *rank*. 
	The message is tagged with an integer *msgTag*. 
	
	Should never be called by the user if the communication methods of 
	:class:`MPI` are used. 
	"""
	try:
		mpi.COMM_WORLD.send(
			msg, 
			dest=rank, 
			tag=msgTag
		)
		return True
	except KeyboardInterrupt:
		DbgMsgOut("MPI", "keyboard interrupt")
		raise
	except:
		return False
			
def receiveMPIMessage(timeout=-1.0, msgTag=-1, fromRank=-1):
	"""
	Receives a message (binary string) with tag *msgTag* (integer) from a 
	task with rank given by *fromRank* (integer). If *fromRank* is negative 
	messages from all tasks are accepted. If *msgTag* is negative messages 
	with any tag are accepted. 
	
	If the message is not received within *timout* seconds, returns an empty 
	tuple. Negative values of *timeout* stands for infinite timeout. 
	
	If a message is received a tuple (*source*, *tag*, *msg*) is returned 
	where *source* is the rank of the sender, *tag* is the message tag, and 
	*msg* is the message. 
	
	Should never be called by the user if the communication methods of 
	:class:`MPI` are used. 
	"""
	if msgTag<0:
		tag=mpi.ANY_TAG
	else:
		tag=msgTag
	
	if fromRank<0:
		rank=mpi.ANY_SOURCE
	else:
		rank=fromRank
	
	# Communicator
	comm=mpi.COMM_WORLD
	
	rcvd=False
	st=mpi.Status()
	try:
		if timeout>0.0:
			# This is ugly. Don't use timeout with MPI. 
			mark=time()
			while True:
				val, tag1, rank1 = checkForIncoming(msgTag=tag, fromRank=rank)
				if val:
					msg=comm.recv(source=rank1, tag=tag1, status=st)
					rcvd=True
					break
				if time()-mark>timeout:
					break
		elif timeout==0.0:
			# Non-blocking
			val, tag1, rank1 = checkForIncoming(msgTag=tag, fromRank=rank)
			if val:
				msg=comm.recv(source=rank1, tag=tag1, status=st)
				rcvd=True
		else:
			# Blocking
			msg=comm.recv(source=rank, tag=tag, status=st)
			rcvd=True

	except KeyboardInterrupt:
		raise
	except:
		return None
	
	if rcvd:
		return (st.Get_source(), st.Get_tag(), msg)
	elif timeout>=0.0:
		# Timeout, return empty tuple
		return ()
	else: 
		# Error, return None
		return None

def checkForIncoming(msgTag=-1, fromRank=-1):
	"""
	Returns a tuple (*b*, *tag*, *src*). *b* is ``True`` if a message with tag 
	*msgTag* is waiting to be received from *fromRank*. *tag* and *rank* are 
	the message tag and the rank of the sender.  
	
	Negative values of *msgTag* and *fromrank* match a message with an arbitrary 
	tag/source. 
	"""
	if msgTag<0:
		tag=mpi.ANY_TAG
	else:
		tag=msgTag
	
	if fromRank<0:
		rank=mpi.ANY_SOURCE
	else:
		rank=fromRank
		
	try:
		st=mpi.Status()
		# Should be Improbe in the future, not implemented yet in OpenMPI
		res=mpi.COMM_WORLD.Iprobe(source=rank, tag=tag, status=st)
		tag=st.Get_tag()
		rank=st.Get_source()
		return (res!=0), tag, rank
		
	except KeyboardInterrupt:
		DbgMsgOut("MPI", "keyboard interrupt")
		raise
	except:
		return False


class MPIMessagePrinter(MessagePrinter):
	"""
	MessagePrinter for sending a message to rank 0 for printing.
	
	Buffers messages. Sends them when the :meth:`flush` method is invoked. 
	"""
	
	def __init__(self):
		MessagePrinter.__init__(self)
		self.buf=[]
	
	def write(self, message):
		self.buf.append(message)
	
	def flush(self):
		txt="".join(self.buf)
		self.buf=[]
		
		# Send
		try:
			mpi.COMM_WORLD.send(
				txt, 
				dest=0, 
				tag=MPIMSGTAG_DBGMSG
			)
		except:
			raise
#
# These functions are used only at module import
#

def updateWorkerInfo():
	"""
	Updates the internal information of :class:`MPI` class used by a worker 
	task. 
	"""
	# Get my rank
	try:
		MPI.rank=mpi.COMM_WORLD.Get_rank()
	except KeyboardInterrupt:
		DbgMsgOut("MPI", "Keyboard interrupt.")
		raise
	except:
		MPI.rank=None
	
	# Get my host
	MPI.host=mpi.Get_processor_name()
	
	# Clear vmStatus (we are not a spawner)
	MPI.vmStatus=None

def updateSpawnerInfo():
	"""
	Updates the internal information used by a spawner. 
	
	:attr:`MPI.vmStatus` is a dictionary with three members:
	
	* ``hosts`` - information about the hosts in the virtual machine
	* ``slots`` - information about the task slots in the virtual machine
	* ``freeSlots`` - set of free slots
	* ``usedSlots`` - set of used slots, 
	* ``freeHosts`` - set of objects of class :class:`HostID` corresponding 
	*                 to hosts with at least one free slot
	* ``slot2host`` - a dictionary for getting the hostname from slot number
	
	``hosts`` is a dictionary with ``hostname`` for key and members that 
	are dictionaries with the following members: 
	
	* ``slots``     - the set of all slots on a host
	* ``freeSlots`` - the set of free slots on a host
	* ``ncpu``      - the number of CPU cores in the host
	
	``slots`` is a dictionary with rank for key and members that are 
	dictionaries with the following members:
	
	* ``host``       - the ``hostname`` of the host where this slot resides
	* ``taskNumber`` - the task number of the task in slot (-1=no task)
			
	The ``ncpu`` dictionary members of the ``hosts`` dictionary are 
	obtained with the :meth:`updateCoreCount` method.
	"""
	MPI.taskNumber=0
	MPI.nextTaskNumber=1
	
	comm=mpi.COMM_WORLD
	
	if comm.Get_rank()!=0:
		raise PyOpusError(DbgMsg("MPI", "Task not configured as spawner."))
	
	# Handle spawner slot
	MPI.vmStatus={ 
		'hosts': { 
			MPI.host: {
				'slots': set([0]), 
				'freeSlots': set(), 
				'ncpu': getNumberOfCores()
			} 
		}, 
		'slots': { 
			0: {
				'host': MPI.host, 
				'taskNumber': 0, 
				'pid': identify.pid
				
			} 
		} , 
		'usedSlots': set([0]), 
		'freeSlots': set(), 
		'freeHosts': set(), 
		'slot2host': { 0: MPI.host } 
	}
	
	# Requests the number of CPUs and hostname from every slot, except this one
	worldsize=comm.Get_size()
	for rank in range(1, worldsize):
		comm.send(0, dest=rank, tag=MPIMSGTAG_REQUEST_NCPU)
	
	# Receive responses
	count=0
	while count<worldsize-1:
		st=mpi.Status()
		msg=comm.recv(source=mpi.ANY_SOURCE, tag=MPIMSGTAG_NCPU, status=st)
		src=st.Get_source()
		(ncpu, hostname, pid)=msg
		# hosts
		if hostname not in MPI.vmStatus['hosts']:
			MPI.vmStatus['hosts'][hostname]={'slots': set(), 'freeSlots': set(), 'ncpu': ncpu}
		MPI.vmStatus['hosts'][hostname]['freeSlots'].add(src)
		MPI.vmStatus['hosts'][hostname]['slots'].add(src)
		# slots
		# MPI.vmStatus['slots'][src]={ 'host': hostname, 'taskNumber': -1 }
		MPI.vmStatus['slots'][src]={ 'host': hostname, 'taskNumber': -1, 'pid': pid }
		# Slot to host conversion
		MPI.vmStatus['slot2host'][src]=hostname
		count+=1
	
	# Initial set of free slots
	MPI.vmStatus['freeSlots']=set(range(1, worldsize))
	
	# Initial set of free hosts
	for hostName, desc in MPI.vmStatus['hosts'].items():
		if len(desc['freeSlots'])>0:
			MPI.vmStatus['freeHosts'].add(MPIHostID(hostName))
	
	
#
# Mark thet we are the first imported VM
#
if base.firstVM is None:
	base.firstVM=MPI

# There is no portable way to detect whether we were started using mpirun/mpiexec. 

#
# Spawner and worker go separate paths here. 
# This happens at first import of MPI. 
#

updateWorkerInfo()

# A set holding vmIndex values for which the initial mirror-cleanup was performed
firstSpawnDone=set()

# Infinite loop for worker, nothing special for spawner. 
myRank=mpi.COMM_WORLD.Get_rank()
if myRank>0:
	# Worker
	comm=mpi.COMM_WORLD
	
	# Set debug message printer 
	DbgSetDefaultPrinter(MPIMessagePrinter())
	
	# Turn on worker debugging
	workerDebug=0
	
	if workerDebug:
		DbgMsgOut("MPIWORKER", "Entering worker loop, rank=%d on %s" % (myRank, MPI.host))
	
	# Await spawn requests in a loop
	while True:
		st=mpi.Status()
		msg=comm.recv(source=0, tag=mpi.ANY_TAG, status=st) # mpi.ANY_SOURCE
		src=st.Get_source()
		tag=st.Get_tag()
		
		if tag==MPIMSGTAG_SPAWN:
			(mpi_vm, functionDesc, args, kwargs, sendBack, taskNumber)=msg
			
			if mpi_vm.vmIndex not in firstSpawnDone:
				# This is the first time this vm index is spawning
				firstSpawnDone.add(mpi_vm.vmIndex)
				
				# If we are mirroring and using persistent storage
				# remove existing local storage from previous runs with the same pid/vmIndex
				if mpi_vm.mirrorList is not None and mpi_vm.persistentStorage:
					mpi_vm.cleanupEnvironment(mpi_vm.localStoragePath(), forceCleanup=True)
				
			if workerDebug:
				DbgMsgOut("MPIWORKER", "Spawn request received, spawning MPI task id=%d:%d on %s." % (myRank, taskNumber, MPI.host))
				# Flush stdout so parent will receive it. 
				sys.stdout.flush()
			
			# Prepare function
			function=VirtualMachine.desc2func(functionDesc)
			
			# Prepare working environment
			taskStorage=mpi_vm.prepareEnvironment()
			
			# Set task number
			MPI.taskNumber=taskNumber
			
			# Assume spawn failed
			succes=False
			
			# Call function
			try:
				response=function(*args, **kwargs)
				success=True
			except KeyboardInterrupt:
				DbgMsgOut("MPI", "Keyboard interrupt.")
				raise
			except:
				if workerDebug:
					DbgMsgOut("MPIWORKER", "MPI task %d:%d on %s failed." % (myRank, taskNumber, MPI.host))
				raise
			
			if workerDebug:
				DbgMsgOut("MPIWORKER", "MPI task %d:%d on %s finished." % (myRank, taskNumber, MPI.host))
				# Flush stdout so parent will receive it. 
				sys.stdout.flush()
				
			# Clear working environment
			mpi_vm.cleanupEnvironment(taskStorage)
			
			# Default response
			if sendBack is not True:
				response=None
			
			# Flush stdout so parent will receive it. 
			sys.stdout.flush()
			
			# Send back response if requested
			if sendBack:
				comm.send(
					(taskNumber, success, response), 
					dest=0, 
					tag=MPIMSGTAG_TASK_RETVAL
				)
			
			if workerDebug:
				DbgMsgOut("MPIWORKER", "MPI task %d:%d on %s results message sent." % (myRank, taskNumber, MPI.host))
				# Flush stdout so parent will receive it. 
				sys.stdout.flush()
			
			# Send back task exit message
			comm.send(
				taskNumber, 
				dest=0, 
				tag=MPIMSGTAG_TASK_EXIT
			)
			if workerDebug:
				DbgMsgOut("MPIWORKER", "MPI task %d:%d on %s exit message sent." % (myRank, taskNumber, MPI.host))
				# Flush stdout so parent will receive it. 
				sys.stdout.flush()
		elif tag==MPIMSGTAG_REQUEST_NCPU:
			if workerDebug:
				DbgMsgOut("MPIWORKER", "CPU thread count request received.")
				# Flush stdout so parent will receive it. 
				sys.stdout.flush()
				
			comm.send((getNumberOfCores(), MPI.host, identify.pid), dest=src, tag=MPIMSGTAG_NCPU)
			
		elif tag==MPIMSGTAG_EXIT:
			if workerDebug:
				DbgMsgOut("MPIWORKER", "Worker loop exit request received, rank=%d on %s." % (myRank, MPI.host))
				# Flush stdout so parent will receive it. 
				sys.stdout.flush()
				
			break
		
		elif tag==MPIMSGTAG_SET_DEBUG:
			debug=msg
			if workerDebug or debug:
				DbgMsgOut("MPIWORKER", "Setting debug level to %d, rank=%d on %s" % (debug, myRank, MPI.host))
				# Flush stdout so parent will receive it. 
				sys.stdout.flush()
				
			workerDebug=debug
		
		# At this point all MPIMSGTAG_MESSAGE messages are dropped. 
		# They are processed only in spawned functions. 
	
	if workerDebug:
		DbgMsgOut("MPIWORKER", "Leaving worker loop, rank=%d on %s." % (myRank, MPI.host))
		# Flush stdout so parent will receive it. 
		sys.stdout.flush()
	
	# Worker exits here
	mpi.Finalize()
	sys.exit(0)
else:
	# Spawner
	updateSpawnerInfo()
