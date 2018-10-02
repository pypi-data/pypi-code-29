# -*- coding: UTF-8 -*-

import sys, getopt
import os

def help_out():
	print("help: \'python -m selfcmp.pro -n <soure/problem/data_name> -f <language/format_name> -d <data_maker_name> -o <system_name>\'")
	
data_name = ''
format_name = ''
datamaker_name = ''
ssystem_name = ''
std_name = ''
	
def check_file(argv):
	try:
		opts, args = getopt.getopt(argv,"-h-n:-f:-d:-o:",["--help"])
	except getopt.GetoptError:
		help_out()
		sys.exit(2)
	for opt,val in opts:
		if opt in ('-h','--help'):
			help_out()
			sys.exit()
		elif opt == '-n':
			data_name = val
			if not os.path.exists(data_name+'-data'): os.makedirs(data_name+'-data')
			if not os.path.exists(data_name+'-soure'): os.makedirs(data_name+'-soure')
		elif opt == '-f':
			format_name = val
		elif opt == '-d':
			datamaker_name = val
		elif opt == '-o':
			ssystem_name = val
	if not os.path.exists('conj.yaml') :
		file_out = open('conj.yaml','w')
	if not os.path.exists(data_name+'-std') :
		os.makedirs(data_name+'-std')
	file_out.write(data_name+'\n')
	file_out.write(ssystem_name+'\n')
	file_out.write(datamaker_name+'\n')
	path_name = data_name +'-soure/' + data_name +'.' + format_name +' ' 
	if format_name == 'cpp' :
		if ssystem_name == 'windows' :file_out.write('g++ ' + path_name + '-o '+ data_name + '-soure/' + data_name +'.exe')
		elif ssystem_name == 'linux' :file_out.write('g++ ' + path_name + '-o '+data_name + '-soure/' + data_name)
	if ssystem_name == 'windows' : runner_sp = open('runner.bat','w')
	elif ssystem_name == 'linux' : runner_sp = open('runner.sh','w')
	runner_sp.write('python -m selfcmp.work -t 10\n pause')

if __name__ == "__main__" :
	check_file(sys.argv[1:])