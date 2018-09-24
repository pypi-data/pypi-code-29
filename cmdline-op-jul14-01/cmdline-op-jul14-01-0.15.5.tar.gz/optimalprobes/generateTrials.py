import glob
import mdtraj as md
import numpy as np
import os
import sys
from msmbuilder.utils import io
import logging

from macros import *

######################
## global variables ##
######################
experiment=''
pr=0
secondary_structural_elements=[]
not_allowed_residues=[]
intracellular_residues=[]
extracellular_residues=[]
prev_info=[]
lagtime=0
clusters=0
######################

logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

prev_info_flag=[]
prev_information_elements=[]

def funcDEER(cont_unfiltered,low,up):

	print "DEER function: not yet working"	
	return

def funcLRET(cont_unfiltered,LRET_low,LRET_up):

		
	print "in funcLRET"
	## LRET contact filters
	import datetime
	## import contacts npy or pkl file
	for file in sorted(glob.glob(calc_contacts_all_contact_featurization_foldername+'/*.npy')):
		print file
		print datetime.datetime.now().time()	
		a=np.load(file)

#	calc_contacts_all_contact_featurization_foldername

def funcFilterCont(cont_unfiltered):
	
	temp0_filtered=cont_unfiltered[:]

	## Not allowed residues
	temp1_filtered=[]
	for item in temp0_filtered:
		item=item.tolist()
		if (item[0] not in not_allowed_residues) or (item[1] not in not_allowed_residues):
			temp1_filtered.append(item)
	print "After not allowed",
	print len(temp1_filtered)	

	## Proximal residues
	temp2_filtered=[]

	for item in temp1_filtered:
		if item[0]>item[1]:
			if item[0]>item[1]+pr:
				temp2_filtered.append(item)	
		else:
			if item[1]>item[0]+pr:
				temp2_filtered.append(item)	
	print "After proximal",
	print len(temp2_filtered)	
	
	## Secondary structure
	temp3_filtered=temp2_filtered[:]

	for item in temp2_filtered:
		flag=0
		for element in range(len(secondary_structural_elements)):
			if (item[0] in secondary_structural_elements[element]) and (item[1] in secondary_structural_elements[element]):
				flag=1
			if flag==1:
				temp3_filtered.remove(item)
				break;
	
	## Intracellular/Extracellular residues
	temp4_filtered=temp3_filtered[:]

	for item in temp3_filtered:
		if (item[0] in intracellular_residues and item[1] in extracellular_residues) or (item[1] in intracellular_residues and item[0] in extracellular_residues):
			temp4_filtered.remove(item)

	return temp4_filtered

def funcGenerateTrials(args):
	
	config_filename=args.config

	f_config=open(config_filename,'rb')
	for line in f_config:
		exec(line, globals())
	f_config.close()

	cont_unfiltered=np.load(contacts_outfilename)

	print experiment, LRET_low, LRET_up, pr, secondary_structural_elements, not_allowed_residues, intracellular_residues, extracellular_residues, lagtime, clusters, prev_info

	cont_generic_filtered=funcFilterCont(cont_unfiltered)
	logging.info(config_filename+" contacts were filtered.")

	if experiment=="DEER":
		funcDEER(cont_generic_filtered,DEER_low,DEER_up)
	elif experiment=="LRET":
		funcLRET(cont_generic_filtered,LRET_low,LRET_up)
		logging.info(config_filename+" contacts were filtered for experiment "+experiment+" .")
#	elif experiment=="Fluorescence":
#	elif experiment=="TTET":

#	check_prev_information()		

	## Calling distance calculation and featurization function
#	print "FTR-ing"
#	distance_ftr()
#	print "FTR-ed"

	## Compatible sets
#	f=open(compatible_sets_file,"w")
#	check_compatibility()
#	f.close()
	## Sort, Unique
#	cmd='sort -u '+compatible_sets_file+' > '+compatible_sets_sorted_file
#	os.system(cmd)
	## Minimum and maximum number of probes
#	f2=open(compatible_sets_final_file,"w")
#	apply_min_max_probes_cutoff()
#	f2.close()
	## Close log file
#	f_log.close()
