import subprocess
import shlex

def strexe(s):
	if not isinstance(s, str):
		raise TypeError("strexe takes a string command as its only argument")
	out, err = strexetup(s)
	return(out)

def strexetup(s):
	if not isinstance(s, str):
		raise TypeError("strexetup takes a string command as its only argument")
	l = shlex.split(s)
	p = subprocess.Popen(l, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	out, err = p.communicate()
	p.wait()
	return((out.decode('utf-8'), err.decode('utf-8'))

