import sys

if sys.version_info[0] < 3:
    from charlotte_DB_SDK import *
#If there's an import error then Python 3 is being used
#Python 3 import
else:
    from .charlotte_DB_SDK import *