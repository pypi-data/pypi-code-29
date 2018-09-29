from sys import version_info

if version_info.major == 3:
	from super_debugger.super_debugger import super_debugger
elif version_info.major == 2:
	from super_debugger import super_debugger
else:
	exit("Unknown version of Python")
