import sys, subprocess

if __name__ == '__main__':
	# Stage 2 of launch, arguments starting with the second one define what to start
	# Do not wait for stage 2 to return 
	p=subprocess.Popen(sys.argv[1:])
	