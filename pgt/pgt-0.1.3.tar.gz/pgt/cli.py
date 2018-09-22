# -*- coding: utf-8 -*-

from .CompileEnv import CompileEnv
import json
import time
import os
from codecs import open

LICENSE_DOC = u'''\
     PUDDING EATER PREROGATIVE LICENSE
        Version 2, September 2018

For the the highest good, the great liberation 
of human, the achieve of communism,
Everybody who has eaten pudding allow to use,
copy or apply this software including its documents 
of, by and for Economical Construction, Political 
Construction, Cultural Construction, Social 
Construction, Ecological Civilization Construction 
honestly and friendly.

             布丁食客特权许可
            第二版， 2018年九月

为了最高善，人类的大解放，共产主义的实现，
所有吃过布丁的人允许使用，复制及应用这个软
件包括其文档为了，通过，以便经济建设，政治
建设，文化建设，社会建设，生态文明建设诚实
地友善地。
'''

def main():
	print('''Pages generate tool
==================
ltaoist 2018.9\n''')

	def test_flag(flag):
		import sys
		for it in sys.argv:
			if it == flag:
				return True
		return False
	all = test_flag('--all')
	
	if test_flag('--help'):
		print('''Code:
@{[] | \\name value \\name value ... }
@<<!+ name ? (value) >>

Command:
$ pgt 
$ pgt --all
$ pgt --init\n
$ pgt --import jQuery underscore
$ pgt --import $github_user.$scaffold''')

	if test_flag('--init'):
		print('Project init:')
		for dir in [CompileEnv.basic_path, CompileEnv.task_path, \
			CompileEnv.united_path, 'css', 'images', 'js']:
			if not os.path.exists(dir):
				print('Mkdir: %s' % dir)
				os.makedirs(dir)
			else:
				print('Exists: %s' % dir)
				
				
				
				
				
				
				
		if not os.path.exists('LICENSE'):
			open('LICENSE', 'w', encoding="utf8").write(LICENSE_DOC)
				
	if test_flag('--import'):
		import requests
		import sys
		start = False
		for it in sys.argv:
			if it == '--import':
				start = True
				continue
			if not start:
				continue
			p2 = it.split('.')
			if len(p2) == 1:
				p2 = 'Maintainer1', p2[0]
			p2 = tuple(p2)
			url = 'https://raw.githubusercontent.com/%s/pgt/master/scaffold/%s/_import' % p2
			r = requests.get(url)
			if not r:
				print 'No such scaffold: %s.%s' % p2
				continue
			print("Importing %s:" % p2[1])
			text = r.text
			for line in text.splitlines():
				q2 = line.split(' => ')
				url2 = 'https://raw.githubusercontent.com/%s/pgt/master/scaffold/%s/%s' % (p2[0], p2[1], q2[0])
				text1 = requests.get(url2).content
				savepath = q2[1]
				basedir = os.path.dirname(savepath)
				if basedir and not os.path.exists(basedir):
					os.makedirs(basedir)
				open(savepath, 'w').write(text1)
				print('Merging: %s' % q2[1])
				
	cv = CompileEnv('.')
	task_path = os.path.join(cv._root, cv.task_path)
	list = os.listdir(task_path)
	
	last_path = os.path.join(cv._root, cv.task_path, '_compile_last')
	if os.path.exists(last_path):
		last = json.loads(open(last_path).read())
	else:
		last = {}

	for fn in list:
		if os.path.basename(fn)[:1] == '_' :
			continue
		fnf = os.path.join(task_path, fn)
		statinfo = os.stat(fnf)
		if (not all) and (fn in last) and (last[fn] > statinfo.st_mtime) \
			and (last[fn] > statinfo.st_ctime) :
			continue
		ret = cv.prog(os.path.join(cv.task_path, fn), {})
		basedir = os.path.dirname(fn)
		if basedir and not os.path.exists(basedir):
			os.makedirs(basedir)
		print 'Update: %s' % fn
		open(fn, 'w').write(ret)
		last[fn] = max(time.time(), statinfo.st_mtime, statinfo.st_ctime)
	open(last_path,'w').write(json.dumps(last))

