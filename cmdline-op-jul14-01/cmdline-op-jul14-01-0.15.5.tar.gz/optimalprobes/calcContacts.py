import mdtraj as md
import os
import glob
import numpy as np
import logging

from macros import *
from checkInputs import *

logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

def funcContactList(R,ter):
	cont=[]
	if ter==False:
		start=0
		end=R
	else:
		start=1
		end=R-1
	for i in range(start, end):
		for j in range(i+1,end):
			temp_list=[]
			temp_list.append(i)
			temp_list.append(j)
			cont.append(temp_list)
	return cont


def funcCalcContacts(args):
		
	inpath=funcCheckPath(args.inpath)	
	outpath=funcCheckPath(args.outpath)	
	top=funcCheckFile(args.top)
	trajtype=args.trajtype
	scheme=args.scheme
	subsample=args.subsample
	ter=args.ter

	outfolder=outpath+"/"+calc_contacts_all_contact_featurization_foldername
	if os.path.isdir(outfolder) == False:
		cmd="mkdir "+outfolder
		os.system(cmd)
	else:
		if len(os.listdir(outfolder) ) != 0:
			cmd="rm -r "+outfolder+"/*"
			os.system(cmd)

	first_traj_flag=0
	for file in sorted(glob.glob(inpath+'/*'+trajtype)):

		logging.info("Reading "+file)
		t=md.load(file,top=top)[::subsample]

		if first_traj_flag==0:
			first_traj_flag=1
			R=t.topology.n_residues
			logging.info("This protein has "+str(R)+" residues.")
			cont=funcContactList(R,ter)
			np.save(contacts_outfilename,cont)
			logging.info("Proceeding to compute "+str(len(cont))+" contacts.")

		dist=md.compute_contacts(t,cont,scheme=scheme)
		logging.info("Featurizing trajectory based on all contacts")
		ftr=[np.ndarray.tolist(dist[0][i][:]) for i in range(len(dist[0]))]
		outfile=outfolder+"/"+file.replace(inpath,"",1)+".npy"
		np.save(outfile, ftr)
