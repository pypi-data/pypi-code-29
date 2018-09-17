import os, os.path, time, math, json, signal, sys, subprocess, platform

__all__ = [ 
	'fileInfo', 'listDir', 'formatPassedTime', 
	'daemonLaunch'
]


def fileInfo(path):
	p=os.path.expanduser(path)
	
	result={}
	
	# Absolute path (get rid of up-level references, redundant separators, ...)
	result['abspath']=os.path.abspath(p)
	
	# Get rid of symlinks
	result['realpath']=os.path.realpath(p)
		
	# Type refers to the type of the symlink target
	if not os.path.exists(p):
		result['type']=None
		result['symlink']=None
		result['mtime']=None
	else:
		if os.path.isdir(p):
			result['type']='dir'
		else:
			result['type']='file'
		result['symlink']=os.path.islink(p)
		
		# Get last modification time
		result['mtime']=os.path.getmtime(p)
		
	return result 

def listDir(path):
	root, dirs, files = next(os.walk(path))
	dirs.sort()
	files.sort()
	
	return dirs, files
	
def formatPassedTime(t):
	dt=time.time()-t
	# Format in days, h, m, s
	days=math.floor(dt/3600/24)
	dt=dt-days*3600*24
	hours=math.floor(dt/3600)
	dt=dt-hours*3600
	minutes=math.floor(dt/60)
	seconds=dt-minutes*60
	
	return "%d day(s) %2d:%02d:%02d" % (days, hours, minutes, seconds)

# Stage 1 of launching. Spawn Python module pyopus.gui.daemonize with cmd line arguments
def daemonLaunch(cmdLineList):
	if platform.platform().startswith('Windows'):
		# Under Windows start as detached process
		info = subprocess.STARTUPINFO()
		info.dwFlags |= subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NEW_CONSOLE
		info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		info.wShowWindow = subprocess.SW_HIDE
		p=subprocess.Popen(cmdLineList, startupinfo=info)
	else:
		# Under Linux daemonize it with double fork, wait for stage 1 to return
		p=subprocess.Popen([sys.executable, '-m', 'pyopus.gui.daemonize']+cmdLineList)
		p.wait()