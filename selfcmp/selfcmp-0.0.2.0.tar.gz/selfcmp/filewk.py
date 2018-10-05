# -*- coding: UTF-8 -*-

import os
import sys, getopt
# import filecmp

conj_y = open('conj.yaml','r')
compile_order = '' 
data_name = ''
ssy_name = ''
datamaker_name = ''
filein_name = ''
fileout_name = ''
fileans_name = ''
ram1 = ''
ram2 = ''
st = 0
en = 0

def help_out():
	print('help: python -m selfcmp.filewk -s <start_num> -t <end_num>\n 输入输出数据请用如\'name1.in\'和\'name1.ans\'格式,name可自行替换')

def init(argv) :
	try:
		opts, args = getopt.getopt(argv,"-h-s:-t:",["--help"])
	except getopt.GetopeError:
		help_out()
		sys.exit(2)
	for opt,val in opts:
		if opt in ('-h','--help') :
			help_out()
			sys.exit()
		elif opt == '-s' :
			st = int(val)
		elif opt == '-t' :
			en = int(val)
	data_name = conj_y.readline().strip()
	ssy_name = conj_y.readline().strip()
	datamaker_name = conj_y.readline().strip()
	compile_order = conj_y.readline()
	os.system(compile_order)
	if ssy_name == 'windows' :os.system('g++ '+data_name+'-std\\\\std.cpp -o' + data_name + '-std\\\\std.exe')
	elif ssy_name == 'linux' :os.system('g++ '+data_name+'-std\\\\std.cpp -o' + data_name + '-std\\\\std')
	filein_name = data_name + '-data\\\\' + data_name
	fileout_name = data_name + '-data\\\\' + data_name + '.out'
	fileans_name = data_name + '-data\\\\' + data_name
	if not os.path.exists(fileout_name) : open(fileout_name,'w')
	loginfo = open('log.info','w')
	stdpath = data_name+'-std\\\\'+'std'
	flag = -1
	for i in range(st,en + 1):
		if flag != -1 : break
		f1 = open(fileans_name+str(i)+'.ans')
		f2 = open(fileout_name)
		if not os.path.exists(filein_name+str(i)+'.in'): 
			print(str(i)+'th Input not found!')
			continue
		if not os.path.exists(fileans_name+str(i)+'.ans'):
			print(str(i)+'th Output not found!')
			continue			
		if ssy_name == 'windows' :
			 os.system(data_name+'-soure\\\\'+data_name+'.exe'+' < '+filein_name+str(i)+'.in'+' > '+fileout_name)
		elif ssy_name == 'linux' :
			os.system(data_name+'-soure\\\\'+data_name+' < '+filein_name+str(i)+'.in'+' > '+fileout_name)
		ram1 = f1.readlines()
		ram2 = f2.readlines()
		if ram1 != ram2 : flag = i
		else : 	print('test '+str(i)+' is AC')	
	if flag != -1 :
		print('You Have WA!! QAQ!!')
		loginfo.write('This '+str(flag)+'.in'+' is WA')
	else : loginfo.write(str(st)+'~'+str(en)+' test is all right!')
		
if __name__ == "__main__":
	init(sys.argv[1:])