import sys
import os

def funcPrintDependencies():

	print '''Tested with,

Python 2.7.11
Numpy 1.10.4
MDTraj 1.7.2
MSMBuilder 3.4.0
osprey 1.0.0.dev0

Developers do not guarantee Optimal Probes to run with different versions for the required softwares and libraries.'''

def funcRunDependenciesCheck():
	# Python
	print "Python "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])
	# Numpy
	import numpy
	print "Numpy "+numpy.version.version
	# MDTraj
	import mdtraj
	print "MDTraj "+mdtraj.version.full_version
	# MSMBuilder
	import msmbuilder.version
	print "MSMBuilder "+msmbuilder.version.full_version
	# Osprey
	cmd="osprey --version"
	print os.popen(cmd).read()
