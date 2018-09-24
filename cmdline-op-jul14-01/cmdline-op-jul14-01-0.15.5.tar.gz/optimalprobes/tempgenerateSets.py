import glob
import mdtraj as md
import numpy as np
import os
import sys
from msmbuilder.utils import io

from macros import *

prev_info_flag=[]
prev_information_elements=[]

class Node(object):
	def __init__(self, data):
		self.data = data
		self.children = []
	def add_child(self, obj):
		self.children.append(obj)

def mpf(base,node_in_func,ad_matrix):
	flag=0
	set=node_in_func.data
	incompatible=[]
	incompatible_index=[]
	for k in range(0,len(set)):
		for i in range(k+1,len(set)):
			if (ad_matrix[set[k]][set[i]]==0):
				incompatible.append(set[i])
				incompatible_index.append(i)
		if (len(incompatible)>0):
			break;
	# Termination condition
	if (len(incompatible)==0):
		temp1=[base]+set
		temp=sorted(temp1)
		for object in range(0,len(temp)):
			f1.write(str(temp[object])+'\t')
		f1.write('\n')
		return
	else:
		# Left child
	 	temp=[]
		for i in range(0,len(set)):
			if (set[i] not in incompatible):
				temp.append(set[i])
		child = Node(temp)
		node_in_func.add_child(child)
		mpf(base,child,ad_matrix)
		# Right child
		temp=set[:k]+set[k+1:]
		child = Node(temp)
		node_in_func.add_child(child)
		mpf(base,child,ad_matrix)

def distance_ftr():
	f_log.write("Defining contacts list ...\n")
	print "Defining contacts list ...\n"
	for i in range(1, R-1):
		for j in range(i,R-1):
			temp_list=[]
			temp_list.append(i)
			temp_list.append(j)
			cont.append(temp_list)

	min_array=[]
	max_array=[]

	for i in range(0,len(cont)):
		min_array.append([])
		max_array.append([])
	
	for file in sorted(glob.glob('all_contact_featurization/*.npy')):
#		print file
		temp_dist=[]
		makedist=[]
		ftr=np.load(file)
		for i in range(len(ftr)):
			temp_dist.append(np.asarray(ftr[i]))
		array_temp_dist=np.asarray(temp_dist)
		makedist.append(array_temp_dist)
		makedist.append(cont)
		dist=np.asarray(makedist)
		for i in range(0,len(cont)):
			x=min([dist[0][object][i] for object in range(0,len(ftr))])
			min_array[i].append(x)
			x=max([dist[0][object][i] for object in range(0,len(ftr))])
			max_array[i].append(x)
	
	f_log.write("Calculating minimum and maximum residue distances ...\n")
	print "Calculating minimum and maximum residue distances ...\n"

	for i in range(0,len(min_array)):
		cont[i].append(min(min_array[i]))
		cont[i].append(max(max_array[i]))

def check_compatibility():

	f_log.write("Initializing adjacency matrix ...\n")

	ad_matrix=np.zeros((R, R))

	f_log.write("Populating adjacency matrix based on residue distances ...\n")

	for i in range(0,len(cont)):
		if (cont[i][2]>LRET_low and cont[i][3]<LRET_up):
			ad_matrix[cont[i][0]][cont[i][1]]=1
			ad_matrix[cont[i][1]][cont[i][0]]=1

#	        for i in range(0,len(cont)):
#                if (cont[i][2]>DEER_low and cont[i][3]<DEER_up):
#                        ad_matrix[cont[i][0]][cont[i][1]]=1
#                        ad_matrix[cont[i][1]][cont[i][0]]=1

#	for i in range(0,len(cont)):
#		if (cont[i][2]<quenchval and cont[i][3]>maxval):
#			ad_matrix[cont[i][0]][cont[i][1]]=1
#			ad_matrix[cont[i][1]][cont[i][0]]=1
#	print "max-min"
#	print ad_matrix

	f_log.write("Populating adjacency matrix based on secondary structure ...\n")

	for k in range(0,len(elements)):
		for i in range(0,len(elements[k])):
			for j in range(i,len(elements[k])):
				ad_matrix[elements[k][i]][elements[k][j]]=0
				ad_matrix[elements[k][j]][elements[k][i]]=0

	f_log.write("Populating adjacency matrix based on not allowed residues ...\n")

	for i in range(0,len(not_allowed)):
		ad_matrix[not_allowed[i]]=0
		for j in range(0,R):
			ad_matrix[j][not_allowed[i]]=0
	print "not allowed"
	print ad_matrix

	f_log.write("Populating adjacency matrix to avoid neighbouring residues ...\n")
	
	for i in range(0,R-3):
		for j in range(i,i+3):
			ad_matrix[i][j]=0

	f_log.write("Populating adjacency matrix based on intra & extra cellular constraints .. \n")

	for i in intra:
		for j in extra:
			ad_matrix[i][j]=0
			ad_matrix[j][i]=0
	print "extra-intra"
	print ad_matrix

	
	f_log.write("Populating adjacency matrix based on prev information .. \n")
	
	for p in range(len(prev_info_flag)):
		if prev_info_flag[p]==0:
			continue;
		elif prev_info_flag[p]==1:
			ele=prev_information_elements[p]
			for i in elements[ele[0]]:
				for j in elements[ele[1]]:
					ad_matrix[i][j]=0
					ad_matrix[j][i]=0
						
	print "prev-informatiom"
	print ad_matrix

	for i in range(0,R):
		temp=[]
		for j in range(0,R):
			if (ad_matrix[i][j]==1):
				temp.append(j)
		n=Node(temp)
		f_log.write("Checking sets for residue "+str(i)+'\n')
		mpf(i,n,ad_matrix)


def apply_min_max_probes_cutoff():
	f=open(compatible_sets_sorted_file,"r")
	for line in f:
		columns=line.split()
		columns=[col.strip() for col in columns]
		if (len(columns)>min_probes-1 and len(columns)<max_probes+1):
			for i in range(0,len(columns)):
				f2.write(columns[i]+'\t')
			f2.write('\n')

def mapping():
	f=open("temp_residue_mapping.txt","w")
	for i in range(0,R):
		f.write(str(i)+'\t'+str(topology.residue(i))+'\n')

def check_prev_information():
	for i in range(len(prev_information)) :
		flag_res=[]
		for res in prev_information[i]:
			## check which element does res belong to
			for e in range(len(elements)):
				if res in elements[e]:
					flag_res.append(e)
			prev_information_elements.append(flag_res)
		# Check if the 2 elements are separate
		if flag_res[0]!=flag_res[1]:
			prev_info_flag.append(1)
		else:
			prev_info_flag.append(0)
	print prev_info_flag
	return

logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

def funcGenerateTrials(args):

	print "in funcGenerateTrials"
	
	config_filename=args.config

	f_config=open(config_filename,'rb')
	for line in f_config:
		exec line
	f_config.close()

	print config_filename

#	check_prev_information()		

	## Sets file names
#	compatible_sets_file="temp_compatible_sets.txt"
#	compatible_sets_sorted_file="temp_sorted_compatible_sets.txt"
#	compatible_sets_final_file="compatible_sets.txt"

	## Calling distance calculation and featurization function
#	cont=np.load(contacts_outfilename)
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
