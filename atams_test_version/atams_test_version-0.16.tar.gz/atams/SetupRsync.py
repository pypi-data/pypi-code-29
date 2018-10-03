'''
---------------------------------------------------

	File name: SetupRsync.py

---------------------------------------------------
	Description:   Initializes Rsync daemon to allow pushing of SDB files via Rsync to the specified file path 

---------------------------------------------------	
	Package     : softacu
	Version     : 1.63
	Language    : Python
	Authors		: 

Revision History:

Version		Created 			Modification
-----------------------------------------------------------------
1.63		30-Jan-2018			Initial Release

'''

import getpass
import os
import subprocess,sys
import signal
import time
import pwd,grp

def SDBSetupRsync(FilePath, Password):
	User = getpass.getuser()  # getting username
	
	# creating/opening /etc/rsyncd.conf file if it is not present
	if not os.path.isfile("/etc/rsyncd.conf"):
		file_conf = open('/etc/rsyncd.conf',"w+")
	else:
		file_conf = open('/etc/rsyncd.conf',"a+")

		
	# reading /etc/rsyncd.conf file and copying module data if not present
	if os.stat('/etc/rsyncd.conf').st_size == 0:
		with open('/etc/rsyncd.conf','w+') as file_conf:
			file_conf.write("\nlog file = /var/log/rsyncd.log\n")
			file_conf.write("pid file = /var/run/rsyncd.pid\n")	
			file_conf.write("\n[system-data]\n")
			file_conf.write("    path = %s\n" %FilePath)
			file_conf.write("    comment = ACU System Data Rsync Share\n")
			file_conf.write("    use chroot = false\n")
			file_conf.write("    uid = %s\n" %User)
			file_conf.write("    gid = %s\n" %User)
			file_conf.write("    secrets file = /etc/rsyncd.secrets\n")
			file_conf.write("    auth users = file-manager\n")
		
	file_conf.close()	
	
	# creating/opening /etc/rsyncd.secrets file
	if not os.path.isfile("/etc/rsyncd.secrets"):
		file_secrets = open("/etc/rsyncd.secrets","w+")
	else:
		file_secrets = open("/etc/rsyncd.secrets","a+")
		
	# saving password data to the /etc/rsyncd.secrets file
	with open("/etc/rsyncd.secrets",'w+') as file_secrets:
		file_secrets.write("file-manager: %s" %Password)
	
	file_secrets.close()
	
	os.chmod("/etc/rsyncd.secrets", 600)     #setting read only permissions to the user for /etc/rsyncd.secrets file
	
	#killing rsync deamon pid if it is present
	rsync_process = subprocess.Popen(["pgrep", "-f", "rsync"], stdout=subprocess.PIPE)
	try:
		rsync_pid = int(rsync_process.stdout.read())
	except ValueError:
		rsync_pid = 0
	
	if	rsync_pid is not 0:
		os.kill(rsync_pid, signal.SIGKILL)	
		time.sleep(2)
	
	
	#deleting the rsyncd.pid file if it is present
	if os.path.isfile("/var/run/rsyncd.pid"):
		os.remove("/var/run/rsyncd.pid")
		
	#creating rsyncd.log file
	if not os.path.isfile("/var/log/rsyncd.log"):
		file_log = open("/var/log/rsyncd.log","w+")
	else:
		file_log = open("/var/log/rsyncd.log","a+")
	
	#starting rsync daemon
	proc = subprocess.Popen(["sudo", "-S", "rsync", "--daemon"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	proc.communicate()
		
	file_log.close()
	
	#creating SDB Files folder if not present
	if not os.path.isdir(FilePath):
		proc = subprocess.Popen(["sudo", "-S", "mkdir", "-p", FilePath], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		proc.communicate()
	

	#setting owner permissions to the user for SDB Files folder
	uid = pwd.getpwnam(User).pw_uid
	gid = grp.getgrnam(User).gr_gid
	os.chown(FilePath, uid, gid)
	
	return