from .cbddump import dumpCBD
from .cbdrun import runCBD
from .cbdnew import *

__all__ = [ 'taskTitle', 'blankTask', 'taskDumper', 'taskRunner' ]


taskTitle = {
	'cbd': 'Design/evaluation across corners', 
}

blankTask = {
	'cbd': blankCBDTask, 
}

taskDumper = {
	'cbd': dumpCBD, 
}

taskRunner = {
	'cbd': runCBD, 
}
