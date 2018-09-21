""" Example using Oracle Object Types

This example show how we define a simple
mapping between an Oracle object type and
a Python class.

It also shows, how this mapping is used with a SELECT operation.
"""
from cy_Oracle import OracleDB
from cy_Oracle import Attribute

# class to receive the result - one object of type T_COL_INFO.
class ColInfo(object):
	def __init__(self):
		self.name=None
		self.oracleDataType=None
		self.oracleDataLenght=None
	def __str__(self):
		return 'name=%s type=%s(%d)' % \
			(self.name,self.oracleDataType,self.oracleDataLenght)

myDB = OracleDB(user='book', password='book', databaseURL='orcl')
con = myDB.connect()
cur = con.cursor()
# Create a new object type in the database
cur.execute(""" create or replace type T_COL_INFO as object(
		 NAME		varchar2(85 char)
		,DATA_TYPE      varchar2(106 char)
		,DATA_LENGTH	number
		,COMMENTS       varchar2(4000 char))
	    """)
# create a view containing objects of the type T_COL_INFO
cur.execute(""" create or replace view V_COL_INFO as
                  select 
		     c.TABLE_NAME as TABLE_NAME  
		    ,T_COL_INFO(c.COLUMN_NAME,c.DATA_TYPE,c.DATA_LENGTH,m.COMMENTS) 
		     as COL_INFO
                  from USER_TAB_COLUMNS c ,USER_COL_COMMENTS m
                  where c.COLUMN_NAME = m.COLUMN_NAME and c.TABLE_NAME = m.TABLE_NAME
            """)
# Create a type-mapping between T_COL_INFO and the Python object ColInfo
myDB.addTypemap(oracleTypename='T_COL_INFO',pythonClass=ColInfo,attrDict={
	'name' 			: Attribute('NAME'),
	'oracleDataType'	: Attribute('DATA_TYPE'),
	'oracleDataLenght'	: Attribute('DATA_LENGTH'),
	})
# select some objects from the database
for row in cur.execute("""  select TABLE_NAME,COL_INFO from V_COL_INFO order by 1 """):
	print 'Table::%s "%s"::%s' % \
	(row.table_name,row.col_info.__class__.__name__,row.col_info)
cur.close()	
con.close()
