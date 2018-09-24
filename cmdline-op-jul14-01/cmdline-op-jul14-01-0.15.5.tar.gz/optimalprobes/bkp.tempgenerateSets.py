import glob
import mdtraj as md
import numpy as np
import os
import sys
from msmbuilder.utils import io

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
#	1 and R-1 to avoid the ACE and NME type conditions (what if there are ACE and NME in between, user is advised to remove them :P)
#	If there are no ACE, or NME? use range(0,R) and range(i,R)
#	Even if we assume 1 and R-1 then, only the first and the last residues are ignored
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
	
	#Include this if using trajectories and not npy files
#	
#	f_log.write("Starting to read trajectory ...\n")
#	print "Starting to read trajectory ...\n"
#
#	for file in glob.glob(traj_path+'/*'+trajectory_format):
#		f_log.write("Reading "+file+" ...\n")
#		t=md.load(file,top=topology_file)[::20]
#		f_log.write("Computing distances ...\n")
#		dist=md.compute_contacts(t,cont,scheme="closest-heavy")
#		f_log.write("Featurizing trajectory based on all contacts ...\n")
#		ftr=[np.ndarray.tolist(dist[0][i][:]) for i in range(len(dist[0]))]
#		outfile=file.replace(traj_path+"/","",1)
#		np.save(outfile+'.npy', ftr)

## ----	
	# IF npy files are available with contact distances
#
#	"""
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
#	"""
## -----

#	#Include this if using trajectories and not npy files
#		for i in range(0,len(cont)):
#			x=min([dist[0][object][i] for object in range(0,t.n_frames)])
#			min_array[i].append(x)
#			x=max([dist[0][object][i] for object in range(0,t.n_frames)])
#			max_array[i].append(x)
#
#	f_log.write("Saving distances as pkl file in folder all_contact_featurization ...")
#	print "Saving distances as pkl file in folder all_contact_featurization ..."
#	
#	dataset=[]
#	for i in sorted(glob.glob('*.npy')):
#		a = np.load(i)
#		dataset.append(a)
#	io.dump(dataset,'dataset.pkl')
#
#	cmd="rm -rf "+working_directory+"/all_contact_featurization"
#	os.system(cmd)
#	cmd="mkdir "+working_directory+"/all_contact_featurization"
#	os.system(cmd)
#	cmd="mv *.npy "+working_directory+"/all_contact_featurization/"
#	os.system(cmd)
## -------

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

if __name__ == "__main__":
## Log file
	f_log=open("generateSets.log","wb")
## Reading input file
	if len(sys.argv)==2:
		f=open(sys.argv[1],'rb')
		for line in f:
			exec line
		f.close()
	else:
		print "This script needs exactly one arguments, aborting"
		f_log.write("This script needs exactly one arguments, aborting\n")
		sys.exit()
	cmd="ls "+traj_path+"/*."+trajectory_format+" > temp_trajectories.txt"
	os.system(cmd)
	with open('temp_trajectories.txt', 'rb') as f:
		sample_traj_file = f.readline().strip('\n')
	f_log.write("Elements ... \n")
	f_log.write(str(elements)+'\n')
	f_log.write("Not allowed regions ... \n")
	f_log.write(str(not_allowed)+'\n')
	f_log.write("Extra-cellular ... \n")
	f_log.write(str(extra)+'\n')
	f_log.write("Intra-cellular ... \n")
	f_log.write(str(intra)+'\n')
	working_directory=os.getcwd()

## Check if prev information if available for different elemtents(?) or same
	check_prev_information()		

## Reading topology
	R=0
	f_log.write("Loading Topology ...\n")
	topology=md.load(sample_traj_file,top=topology_file).topology
	f_log.write("Defining constants ...\n")
	R=topology.n_residues
## Mapping
	mapping()
## Sets file names
	compatible_sets_file="temp_compatible_sets.txt"
	compatible_sets_sorted_file="temp_sorted_compatible_sets.txt"
	compatible_sets_final_file="compatible_sets.txt"
## Calling distance calculation and featurization function
	cont=[]
	print "FTR-ing"
	distance_ftr()
	print "FTR-ed"
## Compatible sets
	f1=open(compatible_sets_file,"w")
	check_compatibility()
	f1.close()
## Sort, Unique
	cmd='sort -u '+compatible_sets_file+' > '+compatible_sets_sorted_file
	os.system(cmd)
## Minimum and maximum number of probes
	f2=open(compatible_sets_final_file,"w")
	apply_min_max_probes_cutoff()
	f2.close()
## Close log file
	f_log.close()
