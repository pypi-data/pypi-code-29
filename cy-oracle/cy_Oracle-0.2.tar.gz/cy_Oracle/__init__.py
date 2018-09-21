# -*- coding: utf-8 -*-
""" An extension to the module cx_Oracle
	 

	cy_Oracle is a simple Python module that improves the handling of
	Oracle object types compared to cx_Oracle.
	cy_Oracle supports a central declaration of a mapping between
	Python classes and Oracle object types. This mapping can be
	used in DML (SELECT, UPDATE, INSERT) as well as with PL/SQL
	functions and procedures.

	See help(cy_Oracle.OracleDB.addTypemap) for details.

	The entry point for the client is the class cy_Oracle.OracleDB.
	Here you define the connection parameter to the Oracle database
	(User, Password, URL). 

	See help(cy_Oracle.OracleDB) for details.

	The class cy_Oracle.Connection derives from cx_Oracle.Connection.
	It does not add any new methods, but override the method "cursor()".
	Here we return an object of the class cy_Oracle.Cursor. 

	See help(cy_Oracle.Connection.cursor) for details.

	The class cy_Oracle.Cursor derives from cx_Oracle.Cursor.
	Here we setup the input and output handlers to mapo between
	Oracle object types and Python classes. 

	See help(cy_Oracle.Cursor) for details.

	:copyright: (c) 2018 by Nuuk Zweiundvierzig
	:license: BSD, see LICENSE for more details.
"""

# name of the package
name = "cy_Oracle"

# Core classes
from .cyOracle import NoTypemapEntryException, \
		InvalidParameterTypeException, \
		NoTypemapEntryException, \
		Attribute, \
		Collection, \
		OracleDB, \
		Connection, \
		Cursor

