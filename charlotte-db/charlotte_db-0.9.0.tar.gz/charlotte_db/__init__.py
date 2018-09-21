try:
    from charlotte_DB_SDK import *
    from Matrix_def import *
#If there's an import error then Python 3 is being used
#Python 3 import
except ImportError:
    from .charlotte_DB_SDK import *
    from .Matrix_def import *