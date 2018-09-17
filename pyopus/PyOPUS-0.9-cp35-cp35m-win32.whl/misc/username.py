"""
**Username retrieval module**

This module portably retrieves the username of the user that is running 
the process. Currently Windows and Linux are supported. 

The username is stored in the *username* variable when this module is 
imported. 
"""

from .. import PyOpusError
from platform import system

__all__ = [ 'username' ]

username=None
"""
Username (string). 
"""

if system()=='Windows':
	# This should be rewritten. Currently it uses environmental variables. 
	import getpass
	username=getpass.getuser()
elif system()=='Linux':
	# Uses the password database
	import os, pwd
	username=pwd.getpwuid( os.getuid() )[0]
else:
	raise PyOpusError(DbgMsg("USERNAME", "Unsupported OS/platform: "+system()))
