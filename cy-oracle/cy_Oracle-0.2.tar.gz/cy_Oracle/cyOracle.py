""" Support for using user defined SQL types in the Oracle database

This module is intended to be use with Oracle database applications
that expose an PLSQL-API. 

The class "OracleDB" can be used as base class to implement
a Python API corresponding to the PLSQL-API. 
The class "OracleDB" and the helper classes "Attribute" and
"Collection" provide a simple way to define a mapping between
Oracle user defined types and Python classes.
"""
# import oracle connection
import cx_Oracle
# import python logging
import logging
# import named tuple
from collections import namedtuple
import inspect

#
# Exception: we are unable to map an object of the given type
#
class NoTypemapEntryException(Exception):
	""" Failed to map between an Oracle type and a Python object
	"""
	
	def __init__(self,missgingTypeName):
		""" Setup the name of the type that cant be mapped
		"""
		self.missgingTypeName = missgingTypeName

	def __str__(self):
		""" return the text representation of the exception
		"""
		return "No mapping found for %s" % self.missgingTypeName

#
# Exception: a Parameter for a function/procedure call is of an unexpected type
#
class InvalidParameterTypeException(Exception):
	""" Function/Procedure argument of invalid type

	We expect function/procedure arguments to be of the class
	* Attribute
	* Collection
	"""

	def __init__(self,invalidTypeName):
		""" Setup the name of the type that cant be mapped
		"""
		self.invalidTypeName = invalidTypeName

	def __str__(self):
		""" return the text representation of the exception
		"""
		return "Argument of type %s. Expected are Attribute or Collection" % self.invalidTypeName

#
# Exception: No type information found for a given column name
#
class NoTypeInformationException(Exception):
	""" Unable to receive the Oracle Type for a Column

	The exception is raised if we fail to receive the
	Oracel data type of the given column name.

	"""

	def __init__(self,invalidColunmName):
		""" Setup the name of the type that cant be mapped
		"""
		self.invalidColunmName = invalidColunmName

	def __str__(self):
		""" return the text representation of the exception
		"""
		return "Failed the get type information for column %s" % self.invalidColunmName

#
# Helper Class Attribute
#
class Attribute(object):
	""" Helper class to define an attribute of a user defined SQL type

	Use this class with OracleDB.addTypemap() to define a 
	attribute of a user defined SQL type.

	The object contains the following attributes:
	* oracleAttrName - name of the oracle attribute
	* attrValue - optional, value of the attribute
	"""

	def __init__(self,name = None, value = None):
		""" setup the name of the Oracle attribute
		"""
		# save all parameters
		self.oracleAttrName = name
		self.attrValue = value
		
	def __repr__(self):
		""" get a text representation of the attribute
		"""
		result = ''
		# check, if we have a value. In this case we return "name=value"
		if self.attrValue != None:
			# Value present. Check if we have a name
			if self.oracleAttrName != None:
				result = "%s=%s" % (self.oracleAttrName,self.attrValue)
			else:
				result = "?=%s" % self.attrValue
		else:
			result = self.oracleAttrName
		return result

class Collection(Attribute):
	""" Helper functon to define a collection attribute

	Use this function with OracleDB.addTypemap() to define a 
	collection attribute of a user defined SQL type.
	"""

	def __init__(self, name=None, oracletype=None, value = None):
		""" setup the name and the Oracle type of the collection
		"""
		Attribute.__init__(self,name, value)
		self.oracleCollectionType = oracletype

	def __repr__(self):
		""" Get a text representation of the Collection object
		"""
		return "(%s is collection of %s)" % (self.oracleAttrName,self.oracleCollectionType)

# class with the DB API to the "bookmonkey" database
class OracleDB:
	""" API to the Oracle database.

	This class is used to define the mapping between
	Oracle Object Types and Python classes.

	Use the function addTypemap() to define a mapping
	for each Oracle Object Type that is used.

	The workflow is:

	# 1. Create an instance ob OracleDB
	myDB = OracleDB(....)

	# 2. define the mapping
	myDB.addTypemap(....)
	myDB.addTypemap(....)
	....

	# 3. Connect to the Oracle database
	con = myDB.connect()

	# 4. get a cursor to perfom the calls to the database
	cur = con.cursor()

	# 5. call PL/SQL functions / procedures
	result = cur.callFunction(....)
	....

	# 5. close the connection
	con.commit()
	con.close()

	"""

	def __init__(self, user, password, databaseURL):
		""" Create the instance and connet to the database

		The following attributes are set from the parameters
		of the constructor:
		* user        - Oracle user/schema name
		                Example: myschema
		* password    - password 
		                Example: *******
		* databaseURL - location of the Oracle database.
		                Example: server:/pdbinpol:pooled
		
		The following attributes are initialized:
		* typemapOracleToPython
		* typemapPythonToOracle
		* logger
		"""

		self.logger = logging.getLogger(self.__class__.__name__)

		# save all attribute values
		self.user=user
		self.password=password
		self.databaseURL=databaseURL

		# define a class for the two typemaps: Oracle <--> python
		self.typemapEntryClass = namedtuple('TypemapEntry'
				,( 'destinationClass'
					,'attributeMap' 
					,'objectFactory'
					,'attributeLoader') )

		# start with an empty type map: oracle --> python
		# The key for this map is the oracle object type name
		self.typemapOracleToPython = {}

		# startof with an empty type map: python --> oracle
		# The key for this man is the python class object
		self.typemapPythonToOracle = {}

		# create a dict to map from the Oracle Type Names to the 
		# types provided by cx_Oracle
		# 
		# The map is used by the function "_getOracleTypeFromName"
		self.baseTypes = {
			# Check for type RAW. We return "cx_Oracle.BINRAY" in this case
			'RAW': cx_Oracle.BINARY,
			# Check for type BLOB. We return "cx_Oracle.BLOB
			'BLOB': cx_Oracle.BLOB,
			# check for type BOOLEAN. We return "cx_Oracle.BOOLEAN"
			'BOOLEAN': cx_Oracle.BOOLEAN,
			# check for type CLOB. we return "cx_Oracle.CLOB"
			'CLOB': cx_Oracle.CLOB,
			# check for type CURSOR. We return "cx_Oracle.ORACLE"
			'CURSOR': cx_Oracle.CURSOR,
			# check for type DATETIME. We return "cx_Oracle.DATETIME"
			'DATETIME': cx_Oracle.DATETIME,
			# check for type CHAR. We return "cx_Oracle.FIXED_CHAR"
			'CHAR': cx_Oracle.FIXED_CHAR,
			# check for type NCHAR. We return "cx_Oracle.FIXED_NCHAR"
			'NCHAR': cx_Oracle.FIXED_NCHAR,
			# check for type INTERVAL. We return "cx_Oracle.INTERVAL"
			'INTERVAL': cx_Oracle.INTERVAL,
			# check for type CLOB. We return "cx_Oracle.LOB"
			'CLOB' : cx_Oracle.LOB,
			# check for type BLOB. We return "cx_Oracle.LOB"
			'BLOB' : cx_Oracle.LOB,
			# check for type LONG. We return "cx_Oracle.LONG_STRING"
			'LONG' : cx_Oracle.LONG_STRING,
			# check for type BINARY_FLOAT. We return "cx_Oracle.NATIVE_FLOAT
			'BINARY_FLOAT' : cx_Oracle.NATIVE_FLOAT,
			# check for type BINARY_DOUBLE. We return "cx_Oracle.NATIVE_FLOAT"
			'BINARY_DOUBLE' : cx_Oracle.NATIVE_FLOAT,
			# check for type PLS_INTEGER. We return "cx_Oracle.NATIVE_INT"
			'PLS_INTEGER' : cx_Oracle.NATIVE_INT,
			# check for type BINARY_INTEGER. We return "cx_Oracle.NATIVE_INT"
			'BINARY_INTEGER' : cx_Oracle.NATIVE_INT,
			# check for type NVARCHAR2. We return "cx_Oracle.NCHAR"
			'NVARCHAR2' : cx_Oracle.NCHAR,
			# check for type NCLOB. We return "cx_Oracle.NCLOB"
			'NCLOB' : cx_Oracle.NCLOB,
			# check for type NUMBER. We return "cx_Oracle.NUMBER"
			'NUMBER' : cx_Oracle.NUMBER,
			# check for type ROWID. We return "cx_Oracle.ROWID"
			'ROWID' : cx_Oracle.ROWID,
			# check for VARCHAR2. We return "cx_Oracle.STRING"
			'VARCHAR2' : cx_Oracle.STRING,
			# check for TIMESTAMP. We return "cx_Oracle.TIMESTAMP"
			'TIMESTAMP': cx_Oracle.TIMESTAMP
			}


	# dump an object of the class "typemapEntryClass"
	def _dumpTypemapEntry(self, typemapEntry):
		pass
		print("destinationClass = %s" % typemapEntry.destinationClass)
		# loop the attribute map
		for attrKey in typemapEntry.attributeMap.keys():
			# display key --> value
			print("    Key: %s --> %s"  % (attrKey
				,typemapEntry.attributeMap[attrKey]))

	# generic object factory
	def _createInstanceFromClassObject(self,classObject):
		self.logger.debug(' classObject = %s' % (classObject.__name__,) )
		result = object.__new__(classObject)
		result.__init__()
		return result

	# generic attribute loading
	def _loadInstanceAttributes(self, instance, values):
		for attrName in values.keys():
			instance.__setattr__(attrName, values[attrName])
		return instance

	# util function: find ora-type name
	def _getTypemapEntryForPyObject(self, pythonObject):
		"""
		Find the matching oracle type for a given python class
		The function will return a TypemapEntry object.

		If we dont have a mapping for the class of the given python object,
		we return None
		"""
		## self.logger.debug('>for %s' % (type(pythonObject),))

		result = None

		# get the class of the given object
		pythonClass = type(pythonObject)

		# loop the type-map
		if self.typemapPythonToOracle.has_key(pythonClass):
			result = self.typemapPythonToOracle[pythonClass]
			## self.logger.debug('< %s ' % result.destinationClass)
		else:
			pass
			## self.logger.debug('< None ')
		return result


	#
	# ===================== P u b l i c   I n t e r f a c e ====================================
	#

	# setup the type map
	def addTypemap(self,oracleTypename, pythonClass,  attrDict):
		""" Setup a mapping between an user defind Oracle SQL type and a Python class.

		Call this function to setup one mapping between
		a Oracle SQL type and a Python class. Call this
		function once for each Oracle type that is used
		in the API. 

		If an attribute of an Oracle SQL type is itself
		a user defined SQL type, you need to define a mapping
		for this type as well.

		Parameters:
		* oracleTypename - Name of the Oracle SQL type
		                   Example: "BOOKMONKY.T_BOOK"  
		* pythonClass    - corresponding python class		
		                   Example: Book
				   Note: the Python class needs: 
					 - "object" as base class
				         - a constructor without parameters
		* attrDict       - a dictionary with all attributes of the 
		                   type that will be moved between the python
				   object and the Oracle SQL object. The "key"
				   is the name of the attribute of the python
				   object. 
				   If the attribute of the Oracle SQL object 
				   contains a single value, use the helper class
				   "Attribute". 
				   If the attribute of the Oracle SQL object is
				   a collection, use the helper class "Collection".
				   Example: {"isbn"   : Attribute("ISBN"),
					     "title"  : Attribute("BOOK_TITLE"),
					     "authors": Collection("AUTHORS","T_NAME_NT")
					     }

		We are creating two mapping:
		* Oracle --> Python - this goes into the map typemapOracleToPython
		* Python --> Oracle - this goes into the map typemapPythonToOracle
		
		Both entries are instances of the class "typemapEntryClass".
		"""
		self.logger.debug('> %s <--> %s' % (oracleTypename,pythonClass.__name__) )

		# Check: The python class must derive from Object
		assert object in inspect.getmro(pythonClass), "The given Python class (Parameter pythonClass, value=%s) must derive from 'object' " % pythonClass.__name__


		# The attribute map has tuples of (name,typ) as value. For the Oracle-->Python map, we
		# reduce this to a map of "oracle attribute name" --> "python attribute name"
		oracleToPythonAttrMap = {}
		for pythonAttrName in attrDict.keys():
			# get the tuple (oracle-name,oracle-collection-Type)
			attribute = attrDict[pythonAttrName]
			# save one new entry 
			# (like oracleToPythonAttrMap["T_BOOK_NT"] = "books"
			oracleToPythonAttrMap[attribute.oracleAttrName] = pythonAttrName

		# create a new "TypemapEntry" object to map Oracle --> Python
		typemapEntry = self.typemapEntryClass(
				 destinationClass=pythonClass
				,attributeMap = oracleToPythonAttrMap
				,objectFactory = lambda connection:self._createInstanceFromClassObject(pythonClass)
				,attributeLoader=self._loadInstanceAttributes) 
		# store in dict
		self.typemapOracleToPython[oracleTypename] = typemapEntry

		#
		# create a typemapEntry for the reverse mapping Python --> Oracle
		#

		# create the object factory
		oraObjectFactory = lambda connection: connection._gettype(oracleTypename).newobject()

		# create the revers typmap entry
		reverseTypemapEntry = self.typemapEntryClass(
				 destinationClass=oracleTypename
				,attributeMap = attrDict
				,objectFactory = oraObjectFactory
				,attributeLoader=None) 

		# add the entry to the typemap
		self.typemapPythonToOracle[pythonClass] = reverseTypemapEntry 
		## self._dumpTypemapEntry(reverseTypemapEntry)

		self.logger.debug('<')

	# open the database connection. This may raise an exception
	def connect(self):
		""" Connect to the database. 
		
		The function connect to the Oracle database and returns
		a "Connection" object.

		The implementation calls "cx_Oracle.connect()"
		"""
		self.logger.debug('> to: %s' % self.databaseURL)
		con = Connection._mkSimpleConnection(db=self,user=self.user, password=self.password, dsn=self.databaseURL)
		self.logger.debug('<')
		return con


# ==========================================================
class Connection(cx_Oracle.Connection):

	# Constructor
	def __init__(self):
		""" Constructor - for internal use only

		Note: do not try to create "Connection" objects directly.
		Use the OracleDB.connect() to get a Connection object.
		"""
		# create and store a new logger for our object
		self.logger = logging.getLogger(self.__class__.__name__)

		# we need the back-pointer to the OracleDB object that has created this connection
		# we use this to get access to the type-mapping
		self.db = None

		# we are cashing type information. Create an empty cash
		self.typeCash = {}

	# Static method: create a new Connection object
	def _mkSimpleConnection(db,user,password,dsn,cclass='HOL',purity=cx_Oracle.ATTR_PURITY_SELF):
		""" INTERNAL, static : create a new Connection object. 

		Parameters:

		db   		- Reference to an OracleDB object that is used to create this connection
		
		user		- User/Schema name in the Oracle Database
		                  Example: "book"

		password        - Password for the schema specified with the parameter "user"
				  Example: "mypasswd"

		dsn		- data source name
				  Example: "oracl"
		
		Create a new Connection object. Init its base class "cx_Oracle.Connection".
		"""

		# create the Connection object
		con = Connection()
		# init the base class
		cx_Oracle.Connection.__init__(con,user=user,password=password,dsn=dsn,cclass=cclass,purity=purity)
		# save the back-pointer to the OracleDB object
		con.db = db
		# return the new Connection
		return con

	# util function: get Oracle type of a given type name
	def _getOracleTypeFromName(self, typeName):
		""" Get the Oracle type from a given type name

		The function will return one of the predefined types
		from cx_Oracle.

		Example: "VARCHAR2" will return cx_Oracle.STRING

		User defined type will return cx_Oracle.OBJECT
		"""
		# check, if the map "" contains a type definition for the requested type.
		# If not, we return cx_Oracle.OBJECT. This is the case for all user
		# defined types
		if self.db.baseTypes.has_key(typeName.upper()):
			# found. Return value from map
			return self.db.baseTypes[typeName.upper()]
		else:
			# not found. Return generic object type
			return cx_Oracle.OBJECT

	# get type information for a given type name. 
	def _gettype(self,typeName):
		"""
		Get the Type Object for a given type name.
		Example: getType("BOOKMONKEY.T_BOOK")

		The function returns an object of the class "cx_Oracle.ObjectType"
		The object has the following attributes:

		* attributes   - a list of "cx_Oracle.ObjectAttribute" elements
		* elementType  - for collections: type of element (cx_Oracle.ObjectType) ; otherwise: None
		* iscollection - True, if the type reresents a collection (Example: nested table)
		* name         - Type name. Example: "T_BOOK"
		* schema       - Schema name. Example: "BOOKMONKEY"
		"""

		# check cash
		if self.typeCash.has_key(typeName) == False:
			# read from DB
			self.typeCash[typeName] = self.gettype(typeName)

		# found in cash
		return self.typeCash[typeName]

	# Map map a Python collection to an Oracle collection
	def _pythonCollectionToOracleCollection(self, level, pythonCollection, oraCollectionTypeName):
		""" Map a Python collection to an Oracle collection

		The method assums that the Python collection has an iterator
		"""
		self.logger.debug('> mapping a Python collection of type %s to an Oracle collection of type %s' % (type(pythonCollection),oraCollectionTypeName) )
		# create the oracle collection. First, get the type
		oraCollectionType = self._gettype(oraCollectionTypeName)
		# now, create an instance
		oraCollection = oraCollectionType.newobject()

		# if the input-parameter pythonCollection is not emptry,
		# we loop it, convert each object from Python to an Oracle type 
		# and add the Oracle object to the Oracle collection

		if pythonCollection is not None:
			# loop the elements of the python collection into the oracle collection
			for pythonCollectionEntry in pythonCollection:
				# map each collection entry
				oraCollection.append( self._pythonToOracle(pythonCollectionEntry,level+1))
		# return the result
		self.logger.debug('<')
		return oraCollection

	# map a single python value to an oracle values
	def _pythonToOracle(self, pythonObject, level=1):
		""" Map a single python object to the corresponding oracle object.

		If no mapping is needed, we just return the pythonObject
		which we got as input parmeter
		"""
		# formatting of log-message: indent
		blanks = ' '*level

		self.logger.debug('%s> %s' % (blanks, type(pythonObject) ))

		# the resulting oracle object
		oraObject = None
		oraTypeName = 'generic'

		# get the typemap entry for the python object
		typemapEntry = self.db._getTypemapEntryForPyObject(pythonObject)

		# check if a mapping is defined
		if typemapEntry != None:
			# found: map
			oraTypeName = typemapEntry.destinationClass
			# create a new object
			oraObject = typemapEntry.objectFactory(self)
			# if we do have a mapping to an oracle type, we need to care the attributes of the type as well...
			for pythonAttrName in typemapEntry.attributeMap.keys():

				# get the python attribute
				pythonAttr = pythonObject.__getattribute__(pythonAttrName)

				# we take care of the following cases:
				# a) the attribute is a collection. 
				# b) the attribute is not a collection 
				
				# check for collection. Oracle has no generic collection - we need to know to type of the collection
				# get the oracle attribute name and type
				oraAttr = typemapEntry.attributeMap[pythonAttrName]
				oraAttrName = oraAttr.oracleAttrName

				self.logger.debug('%s  Python --> Ora :  %s --> %s' % (blanks,pythonAttrName,oraAttrName))

				# check, if we are dealing with a collection
				if oraAttr.__class__ == Collection:
					# map a collection. first, get the oracle type of the collection
					oraCollectionTypeName = oraAttr.oracleCollectionType
					self.logger.debug('%s  Mapping to collection of type: %s' %(blanks, oraCollectionTypeName))
					
					# if the python collection is None, the oracle collection will be None as well
					if pythonAttr is not None:
						# create the oracle collection. First, get the type
						oraCollection = self._pythonCollectionToOracleCollection(level,pythonAttr,oraCollectionTypeName)
						oraObject.__setattr__(oraAttrName, oraCollection)
					else:
						self.logger.debug('%s python collection is None' % blanks)
				else:
					# map the attribute
					oraObject.__setattr__(oraAttrName, self._pythonToOracle(pythonAttr,level+1))
		else:
			# not found: just assign
			oraObject = pythonObject

		# return the oracle object
		self.logger.debug('%s< %s' % (blanks,oraTypeName) )
		return oraObject

	# Util function: map attributes from a cx_Oracle.Object to a user defined class
	def _oracleToPython(self,objectAttribute, level=1):
		""" Map a cx_Oracle.Object to a user defined Python object
		
		The function maps a object of the class "cx_Oracle.ObjectAttribute"
		to an object of a user defined class. The function returns a 
		instance of the this user defined class.

		Python basic types are returned as they are... 
		"""

		# formatting of log-message: indent
		blanks = ' '*level

		self.logger.debug('%s> objectAttribute=%s' % (blanks,objectAttribute))

		# check type
		if type(objectAttribute) != cx_Oracle.Object:
			self.logger.debug('%s< - generic type' % blanks)
			return objectAttribute

		# extract the name of the type from the attribute
		oraTypeNameRaw = "%s" % objectAttribute.type
		oraTypeName = oraTypeNameRaw.split(" ")[1][:-1]
		oraTypeNameWithoutSchema = oraTypeName.split(".")[-1]
		
		# get the cx_Oracle.ObjectType object for the given type name
		oraType = self._gettype(oraTypeName) 

		# check, if this attribute is a collection
		if oraType.iscollection:
			self.logger.debug('%s  ORACLE-Collection-Type = %s' % (blanks,oraTypeName))
			# we are returning a List of elements
			result = []
			for objectAttributeItem in objectAttribute.aslist():
				# convert each element 
				result.append(self._oracleToPython(objectAttributeItem,level+1))
			self.logger.debug("%s<_oracleToPython - returning List with %d elements" % (blanks,len(result)))
			return result				

		# not a collection. Create a new instance of the user defined class
		self.logger.debug('%s  ORACLE-Type = %s' % (blanks,oraTypeNameWithoutSchema))

		#
		# get the class the caller wants us to map to
		#

		# first, check if we can map the oracle type to a Python class
		if self.db.typemapOracleToPython.has_key(oraTypeNameWithoutSchema)==False:
			self.logger.debug('%s no map entry for %s' % (blanks,oraTypeNameWithoutSchema))
			raise NoTypemapEntryException(oraTypeNameWithoutSchema)

		# get the entry from the typemap. The entry has:
		typemapEntry = self.db.typemapOracleToPython[oraTypeNameWithoutSchema]

		# not a collection. Create a new instance of the user defined class
		self.logger.debug('%s  ORACLE-Type  %s mapped to %s' % (blanks,oraTypeNameWithoutSchema,typemapEntry.destinationClass))

		# create a new object using the factory provided typ the TypemapEntry
		userObject = typemapEntry.objectFactory(self)
		self.logger.debug('%s  Class of userObject %s' % (blanks,type(userObject)) )

		# Attribute mapping between a Oracle-Type and a Python object.
		local_mapOracleAttributeName = typemapEntry.attributeMap

		# Loop all attributes of the Oracle Type (oraType). 
		# If a mapping to an attribute in the Python-Object (userObject) exists then:
		#   - read the attributes value
		#   - map it to a python object
		#   - store the python object in the corresponding attribute of userObject
		attrValues = {}
		for oraAttrName in map(lambda x: x.name,oraType.attributes):

			# check, if the name occures in the destination python object
			if local_mapOracleAttributeName.has_key(oraAttrName):
				# found: read the attributes value
				self.logger.debug('%s  reading attribute: %s' % (blanks,oraAttrName) )
				attrValue = objectAttribute.__getattribute__(oraAttrName)
				# map the attribute and save it
				attrValues[local_mapOracleAttributeName[oraAttrName]] = self._oracleToPython(attrValue,level+1)
			else:
				# not found - skip it
				self.logger.debug('%s  no mapping found for %s.%s - skipping.' % (blanks, oraTypeNameWithoutSchema, oraAttrName) )

		self.logger.debug('%s< - returning user defined object of python class %s' % (blanks,typemapEntry.destinationClass))
		return typemapEntry.attributeLoader(userObject, attrValues)

	# map function parameters - here we extract the positional parameters
	def _mapArguments(self, args):
		""" Extract the positional (unnamed) arguments and the named arguments
		
		We get a sequence of objects of the class:
		- Attribute
		- Collection

		If the attribute has no name, we:
		1. map it to the corresponding Oracle object
		2. add it to the list "positionalArguments" that we return as result of this function

		If the attribute has a name, we
		1. map it to the corresponding Oracle object
		2. add it the dict "namedArguments" that we return as result of this function as well

		"""
		self.logger.debug('>')

		# resulting collections
		positionalArguments = []
		namedArguments = {}

		# loop all arguments
		for arg in args:
			# current attribute - converted to Oracle type
			oraAttr = None
			# first, check the type
			if type(arg) == Attribute:
				# Attribute - map the value an add to resulting collection
				oraAttr = self._pythonToOracle(arg.attrValue)
			else:
				# check for collection
				if type(arg) == Collection:
					# Collections in Oracle are typed - Python
					# collections are generic. To be able to do
					# the mapping we need the information, which
					# Oracle type must be used.
					self.logger.debug('using Oracle Type: %s' % arg.oracleCollectionType)
					oraAttr = self._pythonCollectionToOracleCollection(1,arg.attrValue,arg.oracleCollectionType)	
				else:
					# invalid 
					raise InvalidParameterTypeException(type(arg))
			# check if named or unnamed
			if arg.oracleAttrName == None:
				# no name - add to positional arguments
				positionalArguments.append(oraAttr)
			else:
				# named argument
				namedArguments[arg.oracleAttrName] = oraAttr
		self.logger.debug('< %d positional argumentd; %d named arguments' % (len(positionalArguments),len(namedArguments)) )
		return positionalArguments, namedArguments



	# create a new Cursor object
	def cursor(self):
		""" Create a new Cursor object

		Create a new Cursor object which is linked to this
		Connection object. See the description of the Cursor class
		for details.

		"""
		return Cursor(self)

	# Create a static function to create an instance of the db.Connection object
	_mkSimpleConnection = staticmethod(_mkSimpleConnection)

# =========================================================0


# Helper Class. Used to represent one row of a DB-Table
class Row(object):
	pass

# Class OracleCursor - a wrapper for cx_Oracle.Cursor
class Cursor(cx_Oracle.Cursor):

	# Create a input variable from a given Python object (value)
	def _inputhandlerFactory(self,cursor, value, numElements):
		""" Create a input variable from a given Python object (value)

		"""
		var = None
		self.logger.debug('>value=%s class=%s' %(value,value.__class__.__name__))

		# get the typemap entry for the python object
		typemapEntry = self.con.db._getTypemapEntryForPyObject(value)

		if typemapEntry == None:
			self.logger.debug('  not doing any type mapping')
			return None

		# create a new converter function (instance)
		def inputHandlerConverter(value):
			self.logger.debug('>')
			# use the cursor from the context to create a new variable object
			obj = self.con._pythonToOracle(value)
			self.logger.debug('<')
			return obj

		# create a new Variable
		var = self.var(cx_Oracle.OBJECT,inconverter=inputHandlerConverter,typename=typemapEntry.destinationClass)
		self.logger.debug('<')
		return var


	def __init__(self,connection):
		""" Init the new instance of our cursor

		"""

		# call baseclass constructor
		cx_Oracle.Cursor.__init__(self, connection)

		# create and store a new logger for our object
		self.logger = logging.getLogger(self.__class__.__name__)

		# we need a back-pointer to the connection object to gain
		# access to the type-mapping information
		self.con = connection


	# Used by the "execute" function
	def _rowhandlerFactory(self):
		""" Create and return a function instance that converts raw data from the database into "Row" objects
		
		We do this:
		- get a list of all column names from the cursor using the "Cursor.description" attribute
		- create an instance of the function "createRow".  This function is assigned to the 
		  "Cursor.rowfactory" attribute. Each time we fetch a row from the cursor, the function
		  "createRow" gets called.

		The function _rowhandlerFactory gets called once for each time we "execute" an SQL statement.
		"""
		
		self.logger.debug('>')

		columnNames = [d[0].lower() for d in self.description]

		# Function instance 
		def createRow(*args):
			""" Function to convert raw data from the database into a Row object

			The returned "Row" object has attributes with the 
			same names as the columns we receive from the database.
			"""
			pythonRow = Row()
			if args != None:
				# reset index into the columnNames list
				ix = 0 
				for arg in args:
					# map the argument
					pythonRow.__setattr__(columnNames[ix], self.con._oracleToPython(arg))
					ix = ix + 1
			return pythonRow
		self.logger.debug('<')
		return createRow


	# Helper: execute a SQL/DDL statement. 
	def execute(self, statement, parameters=None , **keywordParameters):
		""" Execute a statement

		Here we override the cx_Oracle.Cursor.execute() method.

		We are adding two function here:
		* we setup an "inputtypehandler" that converts Python objects into Oracle Object Types
		* we setup a "rowfactory" that converts Oracle Objects Types into Python objects


		"""
		# call the cx_Oracle.Cursor execute function todo the work
		self.logger.debug('> statement=>>>%s<<< parameters=%s keywordParameters=%s' % (statement,parameters,keywordParameters) )

		if (parameters == None) or (len(parameters) == 0):
			if len(keywordParameters) == 0:
				result = cx_Oracle.Cursor.execute(self,statement)
			else:	
				self.inputtypehandler = self._inputhandlerFactory
				result = cx_Oracle.Cursor.execute(self,statement,keywordParameters)
		else:	
			self.inputtypehandler = self._inputhandlerFactory
			result = cx_Oracle.Cursor.execute(self,statement,parameters)


		# setup the rowfactory if we got back any resulting cursor / this is true for SELECT statements
		if result != None:
			result.rowfactory = self._rowhandlerFactory()
		# return the cursor to the caller
		self.logger.debug('<')
		return result


	# Helper: Wrapper for a function call for functions without "OUT" parameters
	def callFunction(self, oracleFunction, oracleReturnType, *args):
		""" Call a PLSQL function. 

		Call a PLSQL function an return a single Python object.

		Parameters:

		oracleFunction   - name of the PLSQL function.
		                   Example: "MYPKG.MYFUNCTION"
		oracleReturnType - name of type of return value of the function.
		                   Example: "T_BOOK"
				   Note: you need to define a mapping for this type
				         using the "addTypemap()" function. 
		args             - Python objects that we:
                                   1. map to Oracle objects
                                   2. pass to the function

		Example: 
		call a function without parameters that returns a BINARY_INTEGER:
	   	result = self.callFunction("DBMS_RANDOM.RANDOM",OracleDB.NATIVE_INT)

		Example:
		call a function with one parameter that returns a user defined
		SQL type:
	   	mybook = self.callFunction("getbook","T_BOOK","123456")
		"""
		self.logger.debug('> %s() : %s' % (oracleFunction, oracleReturnType) )

		# the resulting object 
		resultVar = None 

		# get a variable to store the return value of the function.
		# for user defined types we use "cx_Oracle.OBJECT"
		oraTypeObject = self.con._getOracleTypeFromName(oracleReturnType)
		if oraTypeObject == cx_Oracle.OBJECT:
			oraObject = self.var(oraTypeObject,typename=oracleReturnType)
		else:
			oraObject = self.var(oraTypeObject)

		# call the function
		if len(args) == 0:
			# function without parameters
			self.logger.info('calling function without arguments : %s',oracleFunction)
			oraObject = self.callfunc(oracleFunction,oraObject)
		else:	
			# the parameters may contain python object that we need to map to
			# oracle object types. We create a new list of parameters...
			# map the python object to an oracle object and add to the list of parameters
			#
			# We create two parameter Lists
			# - the positional parameters
			# - the named parameters
			positionalParameters, namedParameters = self.con._mapArguments(args)

			# now, let the database execute the function
			self.logger.info('calling function arguments : %s',oracleFunction)
			oraObject = self.callfunc(oracleFunction,oraObject,positionalParameters,namedParameters)

		# map to user defined python object
		resultVar = self.con._oracleToPython(oraObject)
		self.logger.debug('  done')

		# return the list
		self.logger.debug('< %s() : %s' % (oracleFunction, oracleReturnType) )
		return resultVar
	
	# Helper: Wrapper for a procedure call for procedure without "OUT" parameters
	def callProcedure(self, oracleProcedureName, *args):
		""" Call a PLSQL procedure. 

		Call the PLSQL procedure with the given argument.
		The argument list may be empty.
		The function will return all IN and OUT parameters of 
		the PLSQL function in the given order.

		Parameter:
		oracleProcedureName - name of the PLSQL procedure
		                      Example: "MYPKG.MY_PROC"
	
		args		    - IN and OUT parameters for the procedure.
		"""
		self.logger.debug('> %s()' % (oracleProcedureName, ) )

		# perpare a collection of values that are returned from the procedure call
		resultList = []

		# call the function
		if len(args) == 0:
			# procedure without parameters
			oraObject = self.callproc(oracleProcedureName)
		else:	
			# the parameters may contain python object that we need to map to
			# oracle object types. We create a new list of parameters...
			# map the python object to an oracle object and add to the list of parameters
			#
			# The procedure call has two types of arguments
			# * positional arguments
			# * named arguments (not yet implemented)
			positionalParameters, namedParameters = self.con._mapArguments(args)

			# now, let the database execute the function
			outCollection = self.callproc(oracleProcedureName,positionalParameters,namedParameters)

			# now, check the collection that has been returned. It contains:
			# * the unmodified IN parameters
			# * the OUT parameters
			if outCollection != None:
				self.logger.debug('  procedure returned %d parameters', len(outCollection))
				# the outCollection contains Oracle objects. We map the objects to python
				resultList = map(self.con._oracleToPython, outCollection)

			else:
				self.logger.debug('  procedure did not return any data')

			self.logger.debug('  done')

		# return the list
		self.logger.debug('< %s()' % (oracleProcedureName, ) )
		return resultList

