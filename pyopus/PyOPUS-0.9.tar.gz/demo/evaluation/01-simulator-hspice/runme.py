# Test HSPICE simulator interface

from pyopus.simulator import simulatorClass

if __name__=='__main__':
	# Job list for simulator
	jobList=[
		{	# First job - op analysis
			'name': 'dcop', 
			'definitions': [
				{ 'file': 'cmos180n.lib', 'section': 'tm' }, 
				{ 'file': 'opamp.cir' }
			], 
			'params': {
				'vdd': 1.8, 
				'temperature': 25
			}, 
			'options': {
				'method': 'trap'
			}, 
			'saves': [
			], 
			'command': 'op()'
		},
		{	# Second job - op analysis with different temperature
			'name': 'dcop100', 
			'definitions': [
				{ 'file': 'cmos180n.lib', 'section': 'tm' }, 
				{ 'file': 'opamp.cir' }
			], 
			'params': {
				'vdd': 1.6, 
				'temperature': 100
			}, 
			'options': {
				'method': 'trap'
			}, 
			'saves': [
			], 
			'command': 'op()'
		},
		{	# Third job - op analysis with different supply voltage
			'name': 'dcopv33', 
			'definitions': [
				{ 'file': 'cmos180n.lib', 'section': 'tm' }, 
				{ 'file': 'opamp.cir' }
			], 
			'params': {
				'vdd': 2.0, 
				'temperature': 25
			}, 
			'options': {
				'method': 'trap'
			}, 
			'saves': [
			], 
			'command': 'op()'
		},
		{	# Fourth job - op analysis with different library
			'name': 'dcopff', 
			'definitions': [
				{ 'file': 'cmos180n.lib', 'section': 'ws' }, 
				{ 'file': 'opamp.cir' }
			], 
			'params': {
				'vdd': 2.0, 
				'temperature': 25
			}, 
			'options': {
				'method': 'trap'
			}, 
			'saves': [
			], 
			'command': 'op()'
		}, 
		{	# Fifth job - op analysis with different library
			'name': 'dcopff100', 
			'definitions': [
				{ 'file': 'cmos180n.lib', 'section': 'ws' }, 
				{ 'file': 'opamp.cir' }
			], 
			'params': {
				'vdd': 2.0, 
				'temperature': 100
			}, 
			'options': {
				'method': 'trap'
			}, 
			'saves': [
			], 
			'command': 'op()'
		}
	]

	# Input parameters
	inParams={
		'mirr_w': 7.46e-005, 
		'mirr_l': 5.63e-007
	}

	# Create simulator, load HSpice class on demand. 
	sim=simulatorClass("HSpice")(debug=10)

	# Set job list and optimize it
	sim.setJobList(jobList)

	# Print optimized job groups - need to get them manually from simulator
	# because jobGroupCount() and jobGroup() behave as if there is only one 
	# job group holding all jobs. All simulations are performed with a single 
	# simulator call. 
	# Internally jobs are grouped according to the circuit topology. 
	# We display here this internal grouping.  
	jobSeq=sim.jobSequence
	print("\nJob Groups:")
	for i in range(len(jobSeq)):
		group=jobSeq[i]
		gstr=''
		for j in group:
			gstr+=" %d (%s), " % (j, jobList[j]['name'])
		print("  %d: %s" % (i, gstr))

	print("")
	# Set input parameters
	sim.setInputParameters(inParams)

	# Go through all job groups, write file, run it and collect results
	ngroups=sim.jobGroupCount()
	for i in range(ngroups):
		# Run jobs in job group. 
		(jobIndices, status)=sim.runJobGroup(i)
		
		print("")
		for j in jobIndices:
			# Job name
			jobName=jobList[j]['name']
			# Load results
			res=sim.readResults(j, status)
			# Print results
			if res is not None:
				print("Job %d (%s): Vout=%e" % (j, jobName, res.v("out")))
			else:
				print("Job %d (%s): no results" % (j, jobName))
		print("")

	sim.cleanup()
