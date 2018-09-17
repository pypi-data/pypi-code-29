from .. import PyOpusError
import os, os.path, math

__all__ = [ "QPLogIndexError", "QPLogIndex" ]

class QPLogIndexError(PyOpusError):
	def __init__(self, message, *args):
		super(QPLogIndexError, self).__init__(message, *args)


class QPLogIndex(object):
	def __init__(self, fileName):
		self.index={}
		self.blank()
		self.f=None
		
		self.fileName=fileName
		self.realPath=os.path.realpath(fileName)
		
	def blank(self):
		self.index['rowOffset']=[]
		self.index['hostMap']={}
		self.index['subsystemMap']={}
		self.index['host']=[]
		self.index['pid']=[]
		self.index['tid']=[]
		self.index['subsystem']=[]
		self.index['time']=[]
		self.index['uuid']=None
		self.index['t0']=None
		
		self.index['hostWidth']=1
		self.index['pidWidth']=1
		self.index['tidWidth']=1
		self.index['subsystemWidth']=1
		self.index['timeWidth']=1
		
			
	def openFile(self):
		if self.f is None:
			try:
				# Under Windows logs must be opened as binary files 
				# so that tell() will report correct positions for logs
				# with Unix-style line endings. 
				self.f=open(self.fileName, "rb")
			except:
				raise QPLogIndexError("Failed to open log file '"+self.fileName+"'.")
		else:
			try:
				self.f.seek(0, os.SEEK_SET)
			except:
				raise QPLogIndexError("Failed to seek in log file '"+self.fileName+"'.")
		
	def closeFile(self):
		if self.f is not None:
			self.f.close()
			self.f=None
			
	def getUUID(self):
		try:
			self.f.seek(0, os.SEEK_SET)
		except:
			raise QPLogIndexError("Failed to seek in log file '"+self.fileName+"'.")
		s=self.f.readline()
		if not s:
			return None
		else:
			return s.decode("utf-8").strip()
	
	# Creates/extends log index
	def scan(self):
		self.openFile()
		
		# Read first row containing uuid
		uuid=self.getUUID()
		
		# Return message
		msg=''
		
		# Compare with stored uuid
		if self.index['uuid'] is None:
			self.index['uuid']=uuid
			msg+='New log file detected. '
		elif self.index['uuid']!=uuid:
			self.blank()
			self.index['uuid']=uuid
			msg+='Log file overwritten. '
		else:
			msg+='Log file extended. '
			
		# Fast access
		ro=self.index['rowOffset']
		hm=self.index['hostMap']
		sm=self.index['subsystemMap']
		hl=self.index['host']
		pl=self.index['pid']
		tl=self.index['tid']
		sl=self.index['subsystem']
		ti=self.index['time']
		t0=self.index['t0']
		
		# Are we starting from scratch
		if len(ro)==0:
			try:
				self.f.seek(0, os.SEEK_SET)
			except:
				self.closeFile()
				raise QPLogIndexError("Failed to seek in log file '"+self.fileName+"'.")
			# Skip uuid
			self.f.readline()
		else:
			# Last old row
			pos=ro[-1]
			try:
				self.f.seek(pos, os.SEEK_SET)
			except:
				self.closeFile()
				raise QPLogIndexError("Failed to seek in log file '"+self.fileName+"'.")
			# Skip it
			self.f.readline()
		
		# Position of first new row
		try:
			pos=self.f.tell()
		except:
			self.closeFile()
			raise QPLogIndexError("Failed to get position in log file '"+self.fileName+"'.")
		
		# Read rows while there are any left
		nr=0
		while True:
			try:
				s=self.f.readline()
			except:
				self.closeFile()
				raise QPLogIndexError("Failed to read a line from log file '"+self.fileName+"'.")
			
			if not s:
				break
			
			# Parse
			s=s.decode("utf-8")
			try:
				hdr, txt = s.split(': ', 1)
				tstamp, hostproc, subsys = hdr.split(' ')
				host, pid, tid = hostproc.split('_')
				tx=float(tstamp)
			except:
				# Scanning of this line failed
				tstamp=t0 if t0 is not None else 0.0
				subsys="?"
				host="?"
				pid="?"
				tid="?"
				txt="Log file sync lost - probably due to MPI stdout handling."
				tx=float(tstamp)
				
			# Add host
			if host not in hm:
				ii=len(hm)
				hm[host]=ii
				self.index['hostWidth']=max(self.index['hostWidth'], len(host))
			else:
				ii=hm[host]
			hl.append(ii)
			
			# Add subsystem
			if subsys not in sm:
				ii=len(sm)
				sm[subsys]=ii
				self.index['subsystemWidth']=max(self.index['subsystemWidth'], len(subsys))
			else:
				ii=sm[subsys]
			sl.append(ii)
			
			# Add pid and tid
			pl.append(pid)
			tl.append(tid)
			self.index['pidWidth']=max(self.index['pidWidth'], len(pid))
			self.index['tidwidth']=max(self.index['tidWidth'], len(tid))
			
			# Append offset
			ro.append(pos)
			
			# Append time
			if t0 is None:
				self.index['t0']=tx
				t0=tx
			dt=tx-t0
			ti.append(dt)
			nti=len("%.0f" % dt)
			self.index['timeWidth']=max(self.index['timeWidth'], nti)
			
			nr+=1
			
			try:
				pos=self.f.tell()
			except:
				self.closeFile()
				raise QPLogIndexError("Failed to get position in log file '"+self.fileName+"'.")
		
		msg+=""
		
		self.closeFile()
		
		return nr, msg.strip()
	
	def uuid(self):
		return self.index['uuid']
	
	def nRows(self):
		return len(self.index['rowOffset'])
	
	def startTime(self):
		return self.index['t0']
	
	def widths(self):
		return self.index['timeWidth'], self.index['hostWidth'], self.index['pidWidth'], self.index['tidWidth'], self.index['subsystemWidth'] 
	
	def rows(self, start, stop=-1, full=True):
		indexLength=len(self.index['rowOffset'])
		if start<0:
			start=indexLength+stop
		if stop<0:
			stop=indexLength+stop
		stop=indexLength-1 if stop>=indexLength else stop
		
		if start>=indexLength:
			return []
		if start>stop:
			return []
		
		try:
			self.openFile()
		except:
			raise QPLogIndexError("Failed to open log file '"+self.fileName+"'.")
		
		# Prepare index 2 host map 
		hm={ v: k for k, v in self.index['hostMap'].items()}
		
		# Prepare index 2 subsystem map 
		sm={v: k for k, v in self.index['subsystemMap'].items()}
		
		lst=[]
		for ii in range(start, stop+1):
			try:
				self.f.seek(self.index['rowOffset'][ii], os.SEEK_SET)
			except:
				self.closeFile()
				raise QPLogIndexError("Failed to seek in log file '"+self.fileName+"'.")
			s=self.f.readline()
			if not s:
				break
			
			s=s.decode("utf-8").strip()
			parts = s.split(": ", 1)
			pref=parts[0]
			s=parts[1] if len(parts)>1 else ''
			
			rowInfo = [
				self.index['time'][ii], 
				hm[self.index['host'][ii]], 
				self.index['pid'][ii], 
				self.index['tid'][ii], 
				sm[self.index['subsystem'][ii]], 
				s
			]
			lst.append(rowInfo)
		self.closeFile()
		
		return lst
		
if __name__ == '__main__':
	import sys
	from pprint import pprint
	
	try:
		index=QPLogIndex(sys.argv[1])
	except QPLogIndexError as e:
		print("Failed to open log file. "+str(e))
	
	try:
		nr, msg = index.scan()
	except QPLogIndexError as e:
		print("Log scan failed. "+str(e))
		
	print(msg, str(nr)+" row(s) scanned.")
	
	# pprint(index.index)
	
	w=index.widths()
	
	try:
		rlist=index.rows(0, -1, full=False)
	except QPLogIndexError as e:
		print("Failed to load rows from log file. "+str(e))
		
	print("\n".join([("%*.1f: %s" % (w[0]+2, r[0], r[-1])) for r in rlist]))
	
