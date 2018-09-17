# -*- coding: UTF-8 -*-
"""
Main KiCad netlister module. 

Invoke it by running
	
	python3 -m pyopus.netlister.kicad <options>

Command line arguments:

* ``-t``, ``--console`` - run in console mode. Displays output and errors in 
  console. By default the netlister runs in GUI mode where the resulting 
  netlist and errors are reported by popping up a window. 
* ``-c``, ``--config-file`` - name of the default config file/name suffix. 
  If not specified ``netlister.json`` is used. This must be a file name, 
  not a path to a file. The config file is assumed to be in the same 
  folder as the intermediate XML netlist file. 
* ``-s``, ``--skip-config`` - do not read a config file in JSON format. 
* ``-n``, ``--no-print-netlist`` - disables displaying the netlist on success. 
* ``-d``, ``--dump-config`` - dumps the configuration in JSON format to an
  output file if it is specified with ``-o``. Otherwise dumps to a popup 
  window or STDOUT (if ``-t`` is specified). 
  This feature is useful for debugging. It can also be used for creating an 
  initial configuration file that is a starting point for customizing netlist 
  generation. 
* ``-i``, ``--input-file`` - input KiCad XML netlist file. 
  Default is ``netlist.xml``. 
* ``-o``, ``--output-file`` - output Spice Opus netlist file
  Default is ``netlist.cir``. 
  Also used for specifying where to store the JSON configuration file. 

By default a JSON config file is read from ``<output file>.netlister.json``. 
If this file is not found the config is read from ``netlister.json``. The 
default configuration file/name suffix can be specified with the ``-c`` 
option. The configuration file is assumed to be in the same folder as the 
intermediate XML netlist. 

The config file is in JSON format. The ``mapping`` member is dumped as a 
list. Every component mapping is a list with 3 elements: library name, 
component name, and an associative array with the same keys as the 
description of an entry in the ``mapping`` member of *config*. 

To use it from KiCad, select Tools/Generate Netlist File in Eeschema menu. 
Click "Add Plugin" and enter::

  python3 -m pyopus.netlister.kicad -i "%I" -o "%O"

as the "Netlist command". For Windows the command should be:: 

  <full path to pythonw.exe> -m pyopus.netlister.kicad -i "%I" -o "%O"

Enter::

  Spice Opus

as the "Title". A new tab named "Spice Opus" will appear. You only need to 
do this once. KiCad will store your settings in its configuration. For Linux 
make sure python3 is in your path. Also make sure PyOPUS installation 
folder is listed in the PYTHONPATH environmental variable if PyOPUS is not 
installed in the Python libraries folder. 

To generate a Spice Opus netlist, select the "Spice Opus" tab, click on 
"Generate" and select an output file for the netlist. A window with the 
generated netlist will pop up. In case of an error the window will show 
the error message. To disable the popup window and show it only in case 
of an error add the ``-n`` option to the netlister. 
"""

import argparse, json, traceback, sys, os

from pyopus.netlister import PyNetlisterError
from .kicadso import NetlisterKicadSpiceOpus as NetlisterClass
from .popup import *


if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description='KiCAD netlister module for outputting Spice Opus netlists.'
	)
	
	parser.add_argument(
		"-t", "--console", 
		help="console mode (errors are printed to stderr)", 
		action="store_true"
	)
	parser.add_argument(
		"-c", "--config-file", 
		type=str, 
		help="default config file name"
	)
	parser.add_argument(
		"-s", "--skip-config", 
		help="do not read config file", 
		action="store_true"
	)
	parser.add_argument(
		"-n", "--no-print-netlist", 
		help="print/display netlist on success", 
		action="store_true"
	)
	
	parser.add_argument(
		"-d", "--dump-config", 
		help="dump configuration in JSON format to output file (-o), STDOUT, or popup window", 
		action="store_true"
	)
	
	parser.add_argument(
		"-i", "--input-file", 
		type=str, 
		help="input XML netlist file (defaults to netlist.xml)"
	)
	parser.add_argument(
		"-o", "--output-file", 
		type=str, 
		help="output netlist file. Defaults to netlist.cir (or netlist.json for -d)."
	)
	
	args=parser.parse_args()
	
	try:
		# Netlister
		netlister=NetlisterClass()
		
		# Output file 
		if args.input_file:
			infile=args.input_file
		else:
			infile="netlist.xml"
			
		# Input file
		if args.output_file:
			outfile=args.output_file
		else:
			outfile="netlist.cir"
		
		# Default config file
		if args.config_file:
			cfgname=args.config_file
		else:
			cfgname="netlister.json"
		
		# Read JSON config file
		cfgread=None
		cfg={}
		if not args.skip_config:
			# Look in the input file folder
			head, tail = os.path.split(infile)
			
			# Try <output file>.json
			f=None
			if args.output_file:
				try:
					cfgtry=os.path.join(head, args.output_file+"."+cfgname)
					f=open(cfgtry, "r")
					cfgread=cfgtry
				except IOError:
					pass
			# Try defualt config file
			if f is None:
				try:
					cfgtry=os.path.join(head, cfgname)
					f=open(cfgtry, "r")
					cfgread=cfgtry
				except IOError:
					pass
			
			# Read file and parse
			if f:
				txt=f.read(-1)
				f.close()
				
				try:
					# Parse and extract configuration, merge with current config
					cfg=netlister.configFromJSON(txt)
				except:
					raise PyNetlisterError("Failed to parse JSON file '"+cfgread+"'.")
					cfgread=None
		
		# Actions
		if args.dump_config:
			# Dump merged config
			if cfgread is not None:
				print("Initial configuration: %s" % (cfgread))
			
			txt=netlister.configToJSON()
			
			if not args.output_file:
				# Write to STDOUT or popup
				if not args.console:
					popup("KiCad netlister configuration", txt)
				else:
					print(txt)
			else:
				print("Dumping to file:       %s" %(outfile))
				with open(outfile, "w") as f:
					f.write(txt)
			
		else:
			# Generate netlist
			txt, outfile = netlister(infile, outfile, cfgread)
			
			with open(outfile, "w") as f:
				f.write(txt)
				
			if not args.no_print_netlist:
				if args.console:
					print(txt)
				else:
					popup("Netlist", txt, simulator="SpiceOpus", simulatorFile=outfile)
	except PyNetlisterError as e:
		txt=str(e)
		if args.console:
			sys.stderr.write(txt+"\n")
			sys.stderr.flush()
		else:
			popup("PyOPUS KiCad netlister error", txt)
	except:
		txt=traceback.format_exc()
		if args.console:
			sys.stderr.write(txt+"\n")
			sys.stderr.flush()
		else:
			popup("PyOPUS KiCad netlister error", txt)
	
		
		
	
