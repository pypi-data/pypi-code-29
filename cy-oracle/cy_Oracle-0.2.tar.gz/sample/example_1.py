""" Hello Oracle

This is the 'Hello World' example
for the module cy_Oracle. 

"""
from cy_Oracle import OracleDB
# setup the DB connection
myDB = OracleDB(user='book', password='book', databaseURL='orcl')
# connect to DB
con = myDB.connect()
# select some data from the view 'USER_OBJECTS'
cur = con.cursor()
cur.execute('SELECT object_name, created from user_objects')
# loop the result
for row in cur:
	print ('%s --> %s' % (row.object_name, row.created))
# close down
cur.close()	
con.close()
