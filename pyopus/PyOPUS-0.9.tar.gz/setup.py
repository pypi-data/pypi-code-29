#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from setuptools import setup, Extension
import platform
import os, sys, shutil, glob
from pkg_resources import get_build_platform

# Detect platform, set up include directories and preprocessor macros, modify options (disable warnings)
if platform.system()=='Windows':
	import numpy as np
	define_macros=[('WINDOWS', None)]
	include_dirs=[os.path.join(*(np.__path__+['core', 'include']))]
	f2clib=["vcf2c"]
	cxxlib=[]
else:
	define_macros=[('LINUX', None)]
	include_dirs=[]
	f2clib=["f2c"]
	cxxlib=["stdc++"]
	
# 	# Get rid of warnings and other options
# 	cfg_vars = distutils.sysconfig.get_config_vars()
# 	for key, value in cfg_vars.items():
# 		if type(value) == str:
# 			processedValue = value
# 			
# 			processedValue = processedValue.replace("-Wstrict-prototypes", "")
# 			processedValue = processedValue.replace("-Wall", "")
# 			processedValue = processedValue.replace("-Werror=format-security", "")
# 			processedValue = processedValue.replace("-Wformat", "")
# 			processedValue = processedValue.replace("-Wunused-result", "")
# 			processedValue = processedValue.replace("-D_FORTIFY_SOURCE=2", "")
# 			
# 			cfg_vars[key] = processedValue
# 			
# 			#if value!=processedValue:
# 			#	print key, ":", value


# Build libf2c
if platform.system()=='Windows':
	if get_build_platform()=="win-amd64":
		libf2cpath=os.path.join("src", "libf2c")
	else:
		libf2cpath=os.path.join("src", "libf2c.win32")
else:
	libf2cpath=os.path.join("src", "libf2c")
	
if not os.path.exists(os.path.join(libf2cpath, "vcf2c.lib")):
	libf2cOK=False
	wd=os.getcwd()
	
	if platform.system()=='Windows':
		if get_build_platform()=="win-amd64":
			# Windows AMD64
			os.chdir("src")
			os.chdir("libf2c")
		else:
			# Windows 32-bit
			# Copy to src/libf2c.win32
			src=os.path.join("src", "libf2c")
			dest=libf2cpath
			if not os.path.isdir(dest):
				os.mkdir(dest)
				for pat in [ "*.add", "*.c", "*.h", "*.h0", "*.hvc", "*.lbc", "*.out", "*.plan9", "*.sy", "*.u", "*.vc", "*.wat", "*.bat" ]:
					for file in glob.glob(os.path.join(src, pat)):
						shutil.copy(file, dest)
			# Go to folder
			os.chdir(dest)
			
		if os.system("nmake -f makefile.vc"):
			print("Failed to compile libf2c.")
		else:
			print("Compiled libf2c successfully.")
			libf2cOK=True
	else:
		os.chdir("src")
		os.chdir("libf2c")
			
		if os.system("make -f makefile.u"):
			print("Failed to compile libf2c.")
		else:
			print("Compiled libf2c successfully.")
			libf2cOK=True
	
	os.chdir(wd)
else:
	libf2cOK=True


# Dependencies (skip Qt5 for Linux to avoid Debian bug)
dependencies=[
        'numpy', 
        'scipy', 
        'matplotlib', 
        'greenlet', 
        'mpi4py', 
        'cvxopt', 
        'pyqtgraph', 
        'lxml', 
]

if True or platform.system()!="Linux":
       dependencies.append("pyqt5")


# Extensions
ext_modules=[
	Extension(
		'pyopus.simulator._rawfile', 
		['src/rawfile/rawfile.c'], 
		include_dirs=include_dirs, 
		define_macros=define_macros
	), 
	Extension(
		'pyopus.simulator._hspice_read', 
		['src/hspicefile/hspice_read.c'], 
		include_dirs=include_dirs, 
		define_macros=define_macros
	), 
	Extension( 
		'pyopus.misc._ghalton', 
		["src/ghalton/Halton_wrap.cpp", "src/ghalton/Halton.cpp"], 
		include_dirs=include_dirs, 
		define_macros=define_macros
	),
	Extension( 
		'pyopus.misc._sobol', 
		["src/sobol/sobol.c"], 
		include_dirs=include_dirs, 
		define_macros=define_macros, 
		libraries = cxxlib, 
	),
	Extension( 
		'pyopus.problems._mads', 
		["src/mads/mads.c", "src/mads/mdo.cpp",
		 "src/mads/styrene/bb.cpp", 
		 "src/mads/styrene/burner.cpp",
		 "src/mads/styrene/cashflow.cpp",
		 "src/mads/styrene/chemical.cpp",
		 "src/mads/styrene/column.cpp",
		 "src/mads/styrene/combrx.cpp",
		 "src/mads/styrene/flash.cpp",
		 "src/mads/styrene/heatx.cpp",
		 "src/mads/styrene/mix.cpp",
		 "src/mads/styrene/pfr.cpp",
		 "src/mads/styrene/profitability.cpp", 
		 "src/mads/styrene/pump.cpp", 
		 "src/mads/styrene/reaction.cpp", 
		 "src/mads/styrene/servor.cpp", 
		 "src/mads/styrene/split.cpp", 
		 "src/mads/styrene/stream.cpp", 
		 "src/mads/styrene/thermolib.cpp"
		], 
		include_dirs=include_dirs, 
		define_macros=define_macros, 
		libraries = cxxlib, 
	),
	Extension( 
		'pyopus.problems._cec13', 
		["src/cec13/test_func.cpp", 
		 "src/cec13/cec13.cpp",
		], 
		include_dirs=include_dirs, 
		define_macros=define_macros, 
		libraries = cxxlib, 
	), 
]

if libf2cOK:
	# TODO: compile .f files to .c using f2c
	# Currently all .f files are precompiled with f2c. 
	
	# f2c is included via a proxy f2c.h file because adding libf2c to the include path triggers infinite include 
	# recursion under MSVC. 
	
	# Add FORTRAN modules built with f2c
	ext_modules.extend([
		Extension( 
			'pyopus.problems._mwbm', 
			["src/mwbm/mwbm.c", "src/mwbm/dfovec.c", "src/mwbm/dfoxs.c"], 
			include_dirs=include_dirs, 
			define_macros=define_macros, 
			libraries = f2clib,
			library_dirs = [libf2cpath],
		), 
		Extension( 
			'pyopus.problems._lvu', 
			["src/lvu/lvu.c", "src/lvu/test28.c"], 
			include_dirs=include_dirs, 
			define_macros=define_macros, 
			libraries = f2clib,
			library_dirs = [libf2cpath],
		), 
		Extension( 
			'pyopus.problems._lvns', 
			["src/lvns/lvns.c", "src/lvns/lvlcmm.c", "src/lvns/lvumm.c", "src/lvns/lvuns.c"], 
			include_dirs=include_dirs, 
			define_macros=define_macros, 
			libraries = f2clib,
			library_dirs = [libf2cpath],
		),
		Extension( 
			'pyopus.problems._karmitsa', 
			["src/karmitsa/karmitsa.c", "src/karmitsa/tnsboc.c", "src/karmitsa/tnsiec.c", "src/karmitsa/tnsunc.c"], 
			include_dirs=include_dirs, 
			define_macros=define_macros, 
			libraries = f2clib,
			library_dirs = [libf2cpath],
		), 
	])
else:
	print("FORTRAN modules _mwbm, _lvu, _lvns. and _karmitsa will not be built.")


# Settings
setup(name='PyOPUS',
	version='0.9',
	description='A simulation-based design optimization library',
	long_description=\
"""
PyOPUS is a library for simulation-based optimization of arbitrary systems. 
It was developed with circuit optimization in mind. The library is the basis 
for the PyOPUS GUI that makes it possible to setup design automation tasks with 
ease. In the GUI you can also view the the results and plot the waveforms 
generated by the simulator. 

PyOPUS provides several optimization algorithms (Coordinate Search, 
Hooke-Jeeves, Nelder-Mead Simplex, Successive Approximation Simplex, PSADE 
(global), MADS, ...). Optimization algorithms can be fitted with plugins that 
are triggered at every function evaluation and have full access to the 
internals of the optimization algorithm. 

PyOPUS has a large library of optimization test functions that can be used for 
optimization algorithm development. The functions include benchmark sets by 
Moré-Garbow-Hillstrom, Lukšan-Vlček (nonsmooth problems), Karmitsa (nonsmooth 
problems), Moré-Wild, global optimization problems by Yao, Hedar, and Yang, 
problems used in the developement of MADS algorithms, and an interface to 
thousands of problems in the CUTEr/CUTEst collection. Benchmark results can 
be converted to data profiles that visualize the relative performance of 
optimization algorithms. 

The ``pyopus.simulator`` module currently supports SPICE OPUS, HSPICE, and 
SPECTRE (supports OP, DC, AC, TRAN, and NOISE analyses, as well as, collecting 
device properties like Vdsat). The interface is simple can be easily extended to 
support any simulator.

PyOPUS provides an extensible library of postprocessing functions which
enable you to easily extract performance measures like gain, bandwidth, rise
time, slew-rate, etc. from simulation results.
The collected performance measures can be further post-processed to obtain
a user-defined cost function which can be used for guiding the optimization
algorithms toward better circuits.

At a higher elvel of abstraction PyOPUS provides sensitivity analysis, 
parameter screening, worst case performance analysis, worst case distance 
analysis (deterministic approximation of parametric yield), and Monte Carlo 
analysis (statistical approximation of parametric yield). Designs can be 
sized efficiently across a large number of corners. PyOPUS fully automates 
the procedure for finding a circuit that exhibits the desired parametric yield. 
Most of these procedures can take advantage of parallel computing which 
significantly speeds up the process. 

Parallel computing is supported through the use of the MPI library. A 
cluster of computers is represented by a VirtualMachine object which
provides a simple interface to the underlying MPI library. Parallel programs 
can be written with the help of a simple cooperative multitasking OS. This 
OS can outsource function evaluations to computing nodes, but it can also 
perform all evaluations on a single processor. 
Writing parallel programs follows the UNIX philosophy. A function can be run 
remotely with the ``Spawn`` OS call. One or more remote functions can be 
waited on with the ``Join`` OS call. The OS is capable of running a parallel 
program on a single computing node using cooperative multitasking or on a set 
of multiple computing nodes using a VirtualMachine object. Parallelism can be 
introduced on multiple levels of the program (i.e. parallel performance 
evaluation across multiple corners, parallel optimization algorithms, solving 
multiple worst case performance problems in parallel, ...). 

PyOPUS provides a plotting mechanism based on MatPlotLib and wxPython with 
an interface and capabilities similar to those available in MATLAB.
The plots are handled by a separate thread so you can write your programs
just like in MATLAB. Professional quality plots can be 
easily exported to a large number of raster and vector formats for inclusion 
in your documents. The plotting capability is used in the ``pyopus.visual`` module 
that enables the programmer to visualize the simulation results after an 
optimization run or even during an optimization run. 
""", 
	author='Árpád Bűrmen',
	author_email='arpadb@fides.fe.uni-lj.si',
	url='http://fides.fe.uni-lj.si/pyopus/',
	platforms='Linux, Windows', 
	license='GPL V3', 
	packages=[
		'pyopus', 
		'pyopus.design',
		'pyopus.gui', 
		'pyopus.evaluator', 
		'pyopus.misc', 
		'pyopus.optimizer',
		'pyopus.parallel', 
		'pyopus.problems', 
		'pyopus.simulator',
		'pyopus.netlister', 
		'pyopus.plotter'
	],
	install_requires=dependencies, 
     entry_points = {
        'console_scripts': [
		'pyog=pyopus.gui.mainwindow:main',
		'pyori=pyopus.design.sqlite:main', 
	]
    }, 
	ext_modules=ext_modules
)
