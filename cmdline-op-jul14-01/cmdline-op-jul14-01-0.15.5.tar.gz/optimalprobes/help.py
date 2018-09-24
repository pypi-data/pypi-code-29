def funcPrintHelp():

	print '''usage: optimalprobes [-h] [-v] command ...
	
Optimal Probes
  --help, -h     		Show this help message
  --version, -v  		Show program's version number
  --dependencies 		List of dependencies for running the program
  --dependencies check   	Check for dependencies on the user's machine

  command
    calc_contacts
    exposed_residues
    generate_config
    generate_trials
    score_trials
    top_choices
    residue_mapping'''
