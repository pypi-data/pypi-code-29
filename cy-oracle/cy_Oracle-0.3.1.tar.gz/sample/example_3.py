""" Example using Oracle Object Types

This example shows how to map composit
Oracle object types as well collections
to Python objects using cy_Oracle.
"""
from cy_Oracle import OracleDB
from cy_Oracle import Attribute
from cy_Oracle import Collection

# class to receive the result - one object of type T_COL_INFO.
class ColInfo(object):
	def __init__(self):
		self.name=None
		self.oracleDataType=None
		self.oracleDataLenght=None
	def __str__(self):
		return 'name=%s type=%s(%d)' % \
			(self.name,self.oracleDataType,self.oracleDataLenght)

# Class the receive the result - one object of type T_TAB_INFO
class TabInfo(object):
	def __init__(self):
		self.name=None
		self.pctFree=None
		self.colInfo=None
	def __str__(self):
		result = 'name=%s free=%d(%%)' % (self.name,self.pctFree)
		for col in self.colInfo:
			result = '%s\n    %s' % (result,col)
		return result

myDB = OracleDB(user='book', password='book', databaseURL='bookdb')
con = myDB.connect()
cur = con.cursor()

# to be able to run this program more then once we must drop the existing types
try:
	cur.execute(""" drop type T_TAB_INFO """)
except:
	pass
try:
	cur.execute(""" drop type T_COL_INFO_NT """)
except:
	pass

# Create a object type in the database
cur.execute(""" create or replace type T_COL_INFO as object(
		 NAME		varchar2(85 char)
		,DATA_TYPE      varchar2(106 char)
		,DATA_LENGTH	number
		,COMMENTS       varchar2(4000 char))
	    """)
# Create a collection type in the database
cur.execute(""" create or replace type T_COL_INFO_NT as table of T_COL_INFO """)
# Create the type that describes one table 
cur.execute(""" create or replace type T_TAB_INFO as object(
		 NAME varchar2(30 char),
		 PCT_FREE number,
		 COL_INFO T_COL_INFO_NT)
	    """)
# create a view containing objects of the type T_COL_INFO
cur.execute(""" create or replace view V_TAB_INFO as 
                select T_TAB_INFO(
                   t.TABLE_NAME 
                  ,t.PCT_FREE
                  ,cast(MULTISET( 
	                SELECT T_COL_INFO(c.COLUMN_NAME,c.DATA_TYPE,c.DATA_LENGTH
			,m.COMMENTS) from 
	                USER_TAB_COLUMNS c,USER_COL_COMMENTS m
	                where c.TABLE_NAME=t.TABLE_NAME and c.TABLE_NAME=m.TABLE_NAME)
                   as T_COL_INFO_NT )
                ) as TAB_INFO
                from user_tables t
            """)

# Create a type-mapping between T_COL_INFO and the Python object ColInfo
myDB.addTypemap(oracleTypename='T_COL_INFO',pythonClass=ColInfo,attrDict={
	'name' 			: Attribute('NAME'),
	'oracleDataType'	: Attribute('DATA_TYPE'),
	'oracleDataLenght'	: Attribute('DATA_LENGTH'),
	})
# Create a type-mapping between T_TAB_INFO and the Python object ColInfo
myDB.addTypemap(oracleTypename='T_TAB_INFO',pythonClass=TabInfo,attrDict={
	'name' 			: Attribute('NAME'),
	'pctFree'		: Attribute('PCT_FREE'),
	'colInfo'		: Collection('COL_INFO','T_COL_INFO_NT')
	})

# select some objects from the database
for row in cur.execute("""  select TAB_INFO  from V_TAB_INFO """):
	print '\n%s' %  (row.tab_info)
cur.close()	
con.close()
