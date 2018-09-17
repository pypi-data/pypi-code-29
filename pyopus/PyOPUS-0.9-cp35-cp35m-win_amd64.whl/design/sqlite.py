# Record
# - id
# - parent id
# - datetime
# - name
# - payload type name
# - pickled payload data (dict, list, tuple)

# Payload types
# - id
# - type name

# Sample record sequence
#   Task (projectData, mpiData, vmLayout)
#   Verification OptIter
#   Folder
#     OptIter
#     OptIter
#     ...
#     OptIter
#   Verification OptIter
#   Folder
#     OptIter
#     OptIter
#     ...
#     OptIter
#   ...
#   Verification OptIter
#   Conclusion

import sqlite3 as lite
import pickle as pickle
import time, uuid, json, pprint, datetime
import numpy as np
from ..evaluator.aggregate import *
from .. import PyOpusError

from ..misc.debug import DbgMsgOut

__all__ = [ 
	'PyOpusSqliteError', 
	'SQLiteRecord', 'SQLiteDatabase', 
	'SQLDataRoot', 'SQLDataTask', 'SQLDataTaskCBD', 
	'SQLDataFolder', 'SQLDataCorners', 'SQLDataOptIter', 
	'SQLDataOptIter', 'SQLDataConclusion'
]

class PyOpusSqliteError(PyOpusError):
	def __init__(self, message, *args):
		super(PyOpusSqliteError, self).__init__(message, *args)


class SQLData(object):
	def __init__(self):
		pass
	
	def typeString(self):
		return type(self).__name__[7:]
	
	def textAspects(self):
		return [ ]
	
	def getAuxiliaryData(self, sqldb, recordId):
		aux={}
		return aux
	
	def formatStr(self, aspect, auxData):
		return None
	

class SQLDataRoot(SQLData):
	def __init__(self):
		SQLData.__init__(self)
		self.uuid=str(uuid.uuid4())
	
	def textAspects(self):
		return [ "uuid" ]
	
	def formatStr(self, aspect, auxData):
		if aspect=='uuid':
			return self.uuid
		else: 
			return None
	
	
class SQLDataTask(SQLData):
	def __init__(self, project, task):
		SQLData.__init__(self)
		self.project=project
		self.task=task
	
	def textAspects(self):
		return [ "project", "task" ]
	
	def formatStr(self, aspect, auxData):
		if aspect=='project':
			return json.dumps(self.project, indent=2)
		elif aspect=="task":
			return json.dumps(self.task, indent=2)
		else: 
			return None

class SQLDataTaskCBD(SQLData):
	# First child of a CBD task
	def __init__(self, aggregatorSetup):
		SQLData.__init__(self)
		self.aggregatorSetup=aggregatorSetup
	
	def textAspects(self):
		return [ "aggregator" ]
	
	def formatStr(self, aspect, auxData):
		if aspect=='aggregator':
			nameW=max([len(c['measure']) for c in self.aggregatorSetup]+[2])
			goalW=max([len(str(c['norm'])) for c in self.aggregatorSetup]+[2])
			reduceW=max([len(str(c['reduce'])) for c in self.aggregatorSetup]+[2])
			
			txt=""
			for c in self.aggregatorSetup:
				txt+="%*s %*s" % (nameW, c['measure'], goalW, str(c['norm']))
				txt+=" norm=%e fp=%e" % (c['norm'].norm, c['norm'].failure)
				txt+=" %*s" % (reduceW, str(c['reduce']))
				txt+=" "+str(c['shape'])
				txt+="\n"
			
			return txt
		else: 
			return None

class SQLDataFolder(SQLData):
	def __init__(self):
		SQLData.__init__(self)
		

class SQLDataCorners(SQLData):
	def __init__(self, measureCorners, addedCorners):
		SQLData.__init__(self)
		self.measureCorners=measureCorners
		self.addedCorners=addedCorners
	
	def getAuxiliaryData(self, sqldb, recordId):
		aux={}
		
		# Get task record
		taskRec=sqldb.getAncestorByType(recordId, SQLDataTask)
		aux['project']=taskRec.payload.project
		aux['task']=taskRec.payload.task
		
		return aux
	
	def textAspects(self):
		return [ "corners" ]
	
	def formatStr(self, aspect, auxData):
		task=auxData['task']
		
		if aspect=="corners":
			reqLen=max([len(s) for s in task['requirementNames']]+[1])
			
			nameList=task['requirementNames']
				
			txt=""
			for name in nameList:
				txt1="%-*s : " % (reqLen, name)
				if len(self.measureCorners[name])>0:
					txt1+=" ".join([c for c in self.measureCorners[name]])
				else:
					txt1+="no corners"
				if len(self.addedCorners[name]):
					txt2="%-*s + " % (reqLen, "")
					txt2+=" ".join([c for c in self.addedCorners[name]])+"\n"
				else:
					txt2=""
				txt+=txt1+"\n"+txt2
				
			return txt
		
		else:
			return None


class SQLDataOptIter(SQLData):
	def __init__(self, parameters, aggregatorData, evaluatorData, componentNames, waveformData=None):
		SQLData.__init__(self)
		self.parameters=parameters
		self.aggregatorData=aggregatorData
		self.componentNames=componentNames
		self.evaluatorData=evaluatorData
		# List of corner names refered to by indices in aggregator is 
		# passed to CBD as cornerOrder and forwarded to PerformanceEvaluator. 
		# From there it is read by the Aggregator. 
		self.waveformData=waveformData
	
	def getAuxiliaryData(self, sqldb, recordId):
		aux={}
		
		# Get task record
		taskRec=sqldb.getAncestorByType(recordId, SQLDataTask)
		aux['project']=taskRec.payload.project
		aux['task']=taskRec.payload.task
		
		# Get first child of task record (task setup record)
		tsrRec=sqldb.getFirstChild(taskRec.recordId)
		aux['aggregatorSetup']=tsrRec.payload.aggregatorSetup
		
		return aux
	
	def textAspects(self):
		return [ "parameters", "performance", "cost" ]
	
	def boundText(self, task, name, ev):
		if ev is None:
			return "Failed"
		
		if (
			name in task['requirements']['lower'] and
			ev<task['requirements']['lower'][name]
		):
				return "Low"
		if (
			name in task['requirements']['upper'] and
			ev>task['requirements']['upper'][name]
		):
			return "High"
		
		return ""
	
	def formatStr(self, aspect, auxData):
		project=auxData['project']
		task=auxData['task']
		aggregatorSetup=auxData['aggregatorSetup']
		
		# Length of parameter, measure, and corner names
		parLen=max([len(s) for s in task['parameterNames']]+[1])
		reqLen=max([len(s) for s in task['requirementNames']]+[1])
		cLen=max([len(s) for s in task['cornerNames']]+[1])
		
		# Length of component names
		cnLen=0
		for m in self.componentNames.keys():
			if self.componentNames[m] is not None:
				for cn in self.componentNames[m]:
					cn1=len(cn)
					if cn1>cnLen:
						cnLen=cn1
						
		# Length of default component names (indices)
		for measureName, row in self.evaluatorData.items():
			for ev in row.values():
				if project['measures'][measureName]['vector']:
					if type(ev) is np.ndarray:
						cn1=int(np.ceil(np.log10(ev.shape[0])))
					else:
						cn1=1
					if cn1>cnLen:
						cnLen=cn1
		
		if aspect=="parameters":
			txt=""
			for name in task['parameterNames']:
				txt1="%-*s = %e\n" % (parLen, name, self.parameters[name])
				txt+=txt1
			
			return txt
			
		elif aspect=="performance":
			nameList=task['requirementNames']
				
			txt=""
			# Evaluator results
			for name in nameList:
				firstName=True
				if name not in self.evaluatorData:
					continue
				evMeas=self.evaluatorData[name]
				
				for cName in task['cornerNames']:
					firstCorner=True
					if cName not in evMeas:
						continue
					
					ev=evMeas[cName]
					
					# Prefix with name and corner
					txt1="%-*s: %-*s" % ( 
						reqLen, name if firstName else "", 
						cLen, cName if firstCorner else ""
					)
					
					if ev is None:
						# No result
						bt=self.boundText(task, name, ev)
						txt1+=(" "*(cnLen+2))+" = "+(" "*(14))+" "+bt+"\n"
					elif project['measures'][name]['vector']:
						# Vector by definition
						if type(ev) is np.ndarray:
							# Vector is ndarray
							txt1=""
							for ii in range(ev.shape[0]):
								# Prefix (again, skip name and corner when not needed)
								txt1+="%-*s: %-*s" % ( 
									reqLen, name if firstName else "", 
									cLen, cName if firstCorner else ""
								)
								
								# Component name
								lst=self.componentNames[name] if name in self.componentNames else None
								if lst is not None and len(lst)>ii:
									compName="%-*s" % (cnLen, lst[ii])
								else:
									compName="%-*d" % (cnLen, ii)
								
								# Value
								valTxt="%14e" % ev[ii] if ev[ii] is not None else " "*14
								
								# Put together
								bt=self.boundText(task, name, ev[ii])
								txt1+=("[%s]" % compName)+" = "+valTxt+" "+bt+"\n"
								
								firstName=False
								firstCorner=False
						else:
							# Vector is not ndarray (is scalar)
							lst=self.componentNames[name] if name in self.componentNames else None
							if lst is not None and len(lst)>0:
								compName="%-*s" % (cnLen, lst[0])
							else:
								compName="%-*d" % (cnLen, 0)
							
							valTxt="%14e" % ev if ev is not None else " "*14
							bt=self.boundText(task, name, ev)
							txt1+=("[%s]" % compName)+" = "+valTxt+" "+bt+"\n"
					else:
						# Scalar by definition
						valTxt="%14e" % ev
						bt=self.boundText(task, name, ev)
						txt1+=(" "*(cnLen+2))+" = "+valTxt+" "+bt+"\n"
					
					firstName=False
					firstCorner=False
					
					txt+=txt1
			return txt
		
		elif aspect=="cost":
			txt=""
			names=task['requirementNames']
			cost=0.0
			for ii in range(len(aggregatorSetup)):
				name=aggregatorSetup[ii]['measure']
				norm=aggregatorSetup[ii]['norm']
				reduction=aggregatorSetup[ii]['reduce']
				data=self.aggregatorData[ii]
				goal=norm.goal
				
				typeChar=">" if type(norm)is Nabove else "<"
				txt1="%*s %s %e" % (reqLen, name, typeChar, goal)
				
				contrib=data['contribution']
				cost+=contrib
				
				if data['worst'] is None:
					statusText=reduction.flagFailure()
					failedCount=len(data['worst_corner_vector'])
					worst="in %d corner(s)" % (failedCount, )
					cornerList=[task['cornerNames'][ci] for ci in data['worst_corner_vector']]
					if len(cornerList)>3:
						cornerText=(" ".join(cornerList[:3]))+" ..."
					else:
						cornerText=(" ".join(cornerList))
				else:
					statusText=reduction.flagSuccess(data['fulfilled'])
					worst="worst=%e" % data['worst']
					cornerText=task['cornerNames'][data['worst_corner']]
				
				txt1+=" %s %-20s cf=%-14e %s" % (statusText, worst, contrib, cornerText)
				txt+=txt1+"\n"
			
			txt+="\n%s = %e\n" % ("cost function value", cost)
			
			return txt
		
		else:
			return None
		

class SQLDataConclusion(SQLData):
	def __init__(self, analysisCount, time):
		SQLData.__init__(self)
		self.analysisCount=analysisCount
		self.time=time
	
	def textAspects(self):
		return [ "summary" ]
	
	def formatStr(self, aspect, auxData):
		if aspect=="summary":
			anLen=max([ len(a) for a in self.analysisCount.keys() ]+[1])
			
			txt="Analysis counts\n"
			
			for name in self.analysisCount.keys():
				txt+="%-*s : %d\n" % (anLen, name, self.analysisCount[name])
				
			txt+="\nTask took %d seconds\n" % (self.time)
			
			return txt
		
		else:
			return None

		
class SQLiteRecord(object):
	def __init__(self, sqldb=None, recordId=None, parent=None, timestamp=None, name=None, typename=None, payload=None):
		self.sqldb=sqldb
		self.auxData=None
		self.waveforms={}
		
		if type(recordId) is str:
			raise PyOpusError("bum")
		
		self.recordId=recordId
		self.parent=parent
		self.timestamp=timestamp
		self.name=name 
		if typename is None:
			self.typename=type(payload).__name__
		else:
			self.typename=typename
		self.payload=payload
	
	def getAuxiliaryData(self):
		if self.auxData is None:
			if self.sqldb is None:
				raise PyOpusSqliteError("No database specified. Cannot retrieve auxiliary data.")
			self.auxData=self.payload.getAuxiliaryData(self.sqldb, self.recordId)
			self.waveforms=self.sqldb.getWaveforms(self.recordId)
			
	def textAspects(self):
		return self.payload.textAspects()
	
	def formatHead(self):
		dateStr=datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')
		
		tstr=self.payload.typeString() if self.payload is not None else self.typename
		
		txt ="Id      : %d\n" % self.recordId
		txt+="Parent  : %d\n" % self.parent
		txt+="Name    : %s\n" % self.name
		txt+="Type    : %s\n" % tstr
		txt+="Time    : %.2f (%s)\n" % (self.timestamp, dateStr)
		
		return txt
	
	def formatStr(self, aspect=None):
		self.getAuxiliaryData()
		
		aspects=self.textAspects()
		
		# Default aspect
		if aspect is None and len(aspects)>0:
			aspect=aspects[0]
		
		if aspect is not None:
			txtpl=self.payload.formatStr(aspect, self.auxData)
		else:
			txtpl=None
		
		txt=""
		if txtpl is not None:
			# txt1="Content (%s)" % aspect
			# txt+=txt1+"\n"
			# txt+=("-"*len(txt1))+"\n"
			txt+=txtpl
		else:
			if len(aspects)>0:
				txt+="No text found for aspect '%s'." % (aspect)
			else:
				txt+="No text aspects available."
		
		return txt

class SQLiteConnection(object):
	def __init__(self, fpath):
		self.fpath=fpath
		
	def __enter__(self):
		try:
			self.con=lite.connect(self.fpath)
			return self.con
		except lite.Error as e:
			# Log failure
			self.con=None
			PyOpusSqliteError("Failed to open database '"+str(fpath)+"'.")
		
	def __exit__(self, t, value, traceback):
		if self.con is not None:
			self.con.close()
	
class SQLiteDatabase(object):
	def __init__(self, fpath):
		self.fpath=fpath
		self.rootId=None
		self.rootTypeId=None
		self.uuid=None
		self.processedPayloadTypes={}
		
	def openDb(self):
		try:
			return lite.connect(self.fpath)
		except lite.Error as e:
			# Log failure
			DbgMsgOut("SQLITE", "Failed to open database")
			return None
	
	def payloadTypeId(self, typeName, con):
		cur=con.cursor()
		
		# Did we see it
		if typeName not in self.processedPayloadTypes:
			# No, check if it is in the database
			cur.execute("SELECT id FROM payloads WHERE typename=?", (typeName,))
			row=cur.fetchone()
			if row is None:
				# No it is not, add it
				cur.execute("INSERT INTO payloads (typename) VALUES (?)", (typeName,))
				typeId=cur.lastrowid
				
			else:
				# Yes it is there, get it
				typeId=row[0]
			
			self.processedPayloadTypes[typeName]=typeId
			
		else:
			# Yes, we saw it
			typeId=self.processedPayloadTypes[typeName]
		
		con.commit()
		
		return typeId
			
	# Drop all tables, rebuild database
	def reset(self):
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			# Drop tables
			cur.execute("DROP TABLE IF EXISTS payloads")
			cur.execute("DROP TABLE IF EXISTS data")
			cur.execute("DROP TABLE IF EXISTS waveforms")
			
			# Create tables
			cur.execute("""
				CREATE TABLE payloads(
					id INTEGER PRIMARY KEY, 
					typename TEXT NOT NULL
				)
			""")
			cur.execute("CREATE UNIQUE INDEX idx_typename ON payloads(typename)")
			
			cur.execute("""
					CREATE TABLE data(
						id INTEGER PRIMARY KEY, 
						parent INTEGER, 
						timestamp TIMESTAMP, 
						name TEXT, 
						type INTEGER, 
						data BLOB
					)
			""")
			cur.execute("CREATE INDEX idx_parent ON data(parent)")
			cur.execute("CREATE INDEX idx_timestamp ON data(timestamp)")
			cur.execute("CREATE INDEX idx_name ON data(name)")
			cur.execute("CREATE INDEX idx_type ON data(type)")
			
			cur.execute("""
				CREATE TABLE waveforms(
					id INTEGER, 
					corner TEXT NOT NULL, 
					analysis TEXT NOT NULL, 
					filename TEXT NOT NULL
				)
			""")
			cur.execute("CREATE INDEX idx_id ON waveforms(id)")
			cur.execute("CREATE INDEX idx_corner ON waveforms(corner)")
			cur.execute("CREATE INDEX idx_analysis ON waveforms(analysis)")
			cur.execute("CREATE UNIQUE INDEX idx_filename ON waveforms(filename)")
			
			# Add root type
			self.rootTypeId=self.payloadTypeId(SQLDataRoot.__name__, con)
			
			# Insert root record
			payload=SQLDataRoot()
			tname=type(payload).__name__
			t=time.time()
			cur.execute(
				"INSERT INTO data (id, parent, timestamp, name, type, data) VALUES (0,-1,?,'root',(SELECT rowid FROM payloads WHERE typename=?),?)", 
				(t, tname, lite.Binary(pickle.dumps(payload)))
			)
			con.commit()
			
			self.rootId=cur.lastrowid
			return self.rootId
	
	# Get root entry type id and id
	def root(self):
		# Did we see it
		if self.rootId is None:
			# No, it must already be there. Get it. 
			# with self.openDb() as con:
			with SQLiteConnection(self.fpath) as con:
				cur=con.cursor()
				cur.execute("""
					SELECT payloads.id, data.id, data.data FROM payloads, data 
					WHERE payloads.typename=? AND data.type=payloads.id
				""", (SQLDataRoot.__name__,))
				row=cur.fetchone()
				self.rootTypeId, self.rootId = row[0], row[1]
				obj=pickle.loads(row[2])
				self.uuid=obj.uuid
				
		return self.rootTypeId, self.rootId
	
	def getAncestorByType(self, recordId, ancestorType):
		# with self.openDb() as con:
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			atId=recordId
			
			while True:
				cur.execute(
					"SELECT data.parent, data.timestamp, data.name, payloads.typename, data.data "
					"FROM data, payloads WHERE data.type=payloads.id AND data.id=?", 
					(atId, )
				)
				row=cur.fetchone()
				if row is None:
					return None
				
				if row[3]==ancestorType.__name__:
					# Found it
					obj=pickle.loads(row[4])
					return SQLiteRecord(self, 
						atId, parent=row[0], timestamp=row[1], name=row[2], 
						typename=row[3], 
						payload=obj
					)
				else:
					# Go to parent
					atId=row[0]
					
				if atId<0:
					return None
	
	def getFirstChild(self, recordId):
		# with self.openDb() as con:
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			cur.execute(
				"SELECT data.id, data.parent, data.timestamp, data.name, payloads.typename, data.data "
				"FROM data, payloads WHERE data.type=payloads.id AND data.parent=? "
				"ORDER BY data.id ASC LIMIT 1", 
				(recordId, )
			)
			row=cur.fetchone()
			
			if row is None:
				return None
			else:
				obj=pickle.loads(row[5])
				return SQLiteRecord(self, 
					recordId=row[0], parent=row[1], timestamp=row[2], name=row[3], 
					typename=row[4], 
					payload=obj
				)
			
	# Get a record
	def get(self, recordId, getPayload=True):
		# with self.openDb() as con:
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			if getPayload:
				cur.execute(
					"SELECT data.parent, data.timestamp, data.name, payloads.typename, data.data "
					"FROM data, payloads WHERE data.id=? AND data.type=payloads.id", 
					(recordId, )
				)
				
				row=cur.fetchone()
				if row is None:
					return None
				else:
					obj=pickle.loads(row[4])
					return SQLiteRecord(self, 
						recordId=recordId, parent=row[0], 
						timestamp=row[1], name=row[2], 
						typename=row[3], 
						payload=obj
					)
			else:
				cur.execute(
					"SELECT data.parent, data.timestamp, data.name, payloads.typename "
					"FROM data, payloads WHERE data.id=? AND data.type=payloads.id", 
					(recordId, )
				)
				
				row=cur.fetchone()
				if row is None:
					return None
				else:
					return SQLiteRecord(self, 
						recordId=recordId, parent=row[0], 
						timestamp=row[1], name=row[2], 
						typename=row[3], payload=None
					)
	
	def getWaveforms(self, recordId):
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			cur.execute(
				"SELECT waveforms.corner, waveforms.analysis, waveforms.filename "
				"FROM waveforms WHERE waveforms.id=?", 
				(recordId, )
			)
			
			files={}
			while True:
				row=cur.fetchone()
				if row is None:
					break
				an=row[1]
				# Convert empty string to None
				if an=='':
					an=None
				key=(row[0], an)
				files[key]=row[2]
			
			return files
		
	# Get children with child counts. Does not fetch payloads. 
	def getChildren(self, recordId):
		# with self.openDb() as con:
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			cur.execute(
				"SELECT dp.id, dp.name, payloads.typename, "
				"  (SELECT COUNT(id) FROM data dc WHERE dc.parent=dp.id)"
				"FROM data dp, payloads "
				"WHERE dp.type=payloads.id "
				"AND dp.parent=?", 
				(recordId, )
			)
			
			ids=[]
			names=[]
			types=[]
			childCounts=[]
			
			while True:
				row=cur.fetchone()
				if row is None:
					break
				
				ids.append(row[0])
				names.append(row[1])
				types.append(row[2])
				childCounts.append(row[3])
				
			return ids, names, types, childCounts
	
	# Get children with child counts. Does not fetch payloads. 
	def getNewNodes(self, startId):
		# with self.openDb() as con:
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			cur.execute(
				"SELECT data.id, data.parent, data.name, payloads.typename "
				"FROM data, payloads "
				"WHERE data.type=payloads.id "
				"AND data.id>=?", 
				(startId, )
			)
			
			ids=[]
			parents=[]
			names=[]
			types=[]
			
			while True:
				row=cur.fetchone()
				if row is None:
					break
				
				ids.append(row[0])
				parents.append(row[1])
				names.append(row[2])
				types.append(row[3])
				
			return ids, parents, names, types
	
	def lastId(self):
		# with self.openDb() as con:
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			cur.execute(
				"SELECT max(id) FROM data"
			)
			
			row=cur.fetchone()
			if row is None:
				return 1
			else:
				return row[0]
			
	# Commit a record
	def commit(self, record):
		# Add a record
		if record.timestamp is None:
			record.timestamp=time.time()
			
		tname=type(record.payload).__name__
		
		# Default parent is root
		if record.parent is None:
			_, record.parent = self.root()
		
		# with self.openDb() as con:
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			# Add type
			self.payloadTypeId(tname, con)
			
			# Add entry
			cur.execute(
				"INSERT INTO data (parent, timestamp, name, type, data) VALUES (?,?,?,(SELECT rowid FROM payloads WHERE typename=?),?)", 
				(record.parent, record.timestamp, record.name, tname, pickle.dumps(record.payload))
			)
			
			con.commit()
			
			record.recordId=cur.lastrowid
			
		return record.recordId
	
	def commitWaveform(self, recordId, corner, analysis, fileName):
		with SQLiteConnection(self.fpath) as con:
			cur=con.cursor()
			
			# Convert None to ''
			if analysis is None:
				analysis=''
				
			cur.execute(
				"INSERT INTO waveforms (id, corner, analysis, filename) VALUES (?,?,?,?)", 
				(recordId, corner, analysis, fileName)
			)
			
			con.commit()
			
#
# Main function
#

def dumpChildren(sqldb, recId, level=0, idLen=6):
	ids, names, types, childCounts = sqldb.getChildren(recId)
	
	indent=" "*(level*2)
	for ii in range(len(ids)):
		txt="%-*d: %s%s" % (idLen, ids[ii], indent, names[ii])
		if childCounts[ii]>0:
			txt+=" (%s, children=%d)" % (types[ii][7:], childCounts[ii])
		else:
			txt+=" (%s)" % (types[ii][7:])
		print(txt)
		if childCounts[ii]>0:
			dumpChildren(sqldb, ids[ii], level+1, idLen)
	
def main():
	import sys, math
	
	appName="pyori"
	
	nArgs=len(sys.argv)
	
	ok=True
	
	dbfile=None
	action="tree"
	recId=None
	aspect=None
	if nArgs>=2:
		dbfile=sys.argv[1]
	if nArgs>=3:
		action=sys.argv[2]
	if nArgs>=4:
		try:
			recId=int(sys.argv[3])
		except:
			print("Record id must be an integer")
	if nArgs>=5:
		aspect=sys.argv[4]
	
	ok=True
	
	# Check dbFile
	if dbfile is None:
		print("Need an sqlite database.\n")
		ok=False
	
	# Check action
	if action not in [ "aspects", "print", "tree" ]:
		print("Unknown action '"+action+"'.\n")
		ok=False
	
	# Check aspects and print record id
	if action in ["aspects", "print"] and recId is None:
		print("No record id given.\n")
		ok=False
	
	if not ok:
		print("PyOPUS results database inspector usage:")
		print("  "+appName+" <sqlite file> <action> <option1> <option2> ...")
		print("")
		print("Print the tree")
		print("  "+appName+" <sqlite file>")
		print("  "+appName+" <sqlite file> tree")
		print("")
		print("List available aspects of node <id>")
		print("  "+appName+" <sqlite file> aspects <id>")
		print("")
		print("Print all aspects of node <id>")
		print("  "+appName+" <sqlite file> print <id>")
		print("")
		print("Print <aspect> of node <id>")
		print("  "+appName+" <sqlite file> print <id> <aspect>")
		print("")
		sys.exit(1)
	
	try:
		sqldb=SQLiteDatabase(dbfile)
		
		# Handle tree
		if action=="tree":
			# Default to root node
			if recId is None:
				_, recId = sqldb.root()
				txt="Children of root record"
			else:
				txt="Children of record %d" % recId
			rec=sqldb.get(recId, getPayload=False)
			if rec is None:
				raise PyOpusSqliteError("Record %d not found." % (recId))
			
			lastId=sqldb.lastId()
			idLen=int(math.ceil(math.log10(lastId+1)))+1
			
			print(txt)
			print("-"*len(txt))
			
			dumpChildren(sqldb, recId, 0, idLen)
		
		# Handle aspects
		if action=="aspects":
			rec=sqldb.get(recId)
			if rec is None:
				raise PyOpusSqliteError("Record %d not found." % (recId))
			
			aspects=rec.textAspects()
			if len(aspects)>0:
				print("\n".join(aspects))
			else:
				print("No aspects available.")
		
		# Handle print
		if action=="print":
			rec=sqldb.get(recId)
			if rec is None:
				raise PyOpusSqliteError("Record %d not found." % (recId))
			
			aspects=rec.textAspects()
			if aspect is None:
				aList=aspects
			elif aspect not in aspects:
				raise PyOpusSqliteError("Unknown aspect of record %d" % (recId))
			else:
				aList=[aspect]
			
			print(rec.formatHead())
			if aspect is None:
				n=len(aList)
				for ii in range(n):
					aspect=aList[ii]
					print(rec.formatStr(aspect), end='')
					if ii<n-1:
						print()
			else:
				print(rec.formatStr(aspect))
	
	except PyOpusSqliteError as e:
		print("Failed:", str(e))
		sys.exit(1)
		
	sys.exit(0)
		
if __name__ == '__main__':
	main()
	
