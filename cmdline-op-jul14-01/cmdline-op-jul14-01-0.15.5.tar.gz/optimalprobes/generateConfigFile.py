import logging
import os

from macros import *
from checkInputs import *

logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

def funcGenerateConfigFile(args):

	experiment=args.experiment
	pr=args.pr
	ex=args.ex
	tm=args.tm
	ss=args.ss
	pexp=args.pexp

	f=open(config_filename,"wb")
	
	f.write("experiment=\""+experiment+"\"\n\n")
	
	f.write("## "+experiment+" experimental technique parameters\n\n")
	if experiment=="DEER":
		f.write("DEER_low = \t # value in nm \n")
		f.write("DEER_up = \t # value in nm \n")
	elif experiment=="Fluorescence":
		f.write("quenchval = \t # value in nm \n")
	elif experiment=="LRET":
		f.write("LRET_low = \t # value in nm \n")
		f.write("LRET_up = \t # value in nm \n")
	elif experiment=="TTET":
		f.write("TTET_low = \t # value in nm \n")
		f.write("TTET_up = \t # value in nm \n")
	
	f.write("\n## MD simulation dataset\n\n")
	f.write("contactftrpath = \""+os.getcwd()+"/"+calc_contacts_all_contact_featurization_foldername+"\"\n")

	f.write("\n## Exclude nearby residues\n\n")
	f.write("pr = "+str(pr)+"\n")

	if ss==1:
		f.write("\n## Protein topology\n")
		f.write("## Example: \n") 
		f.write("## secondary_structural_elements=[range(0,10),range(10,15),range(15,30)] \n\n")
		f.write("secondary_structural_elements = []\n")
	
	if ex==1:
		f.write("\n## Excluded residues\n")
		f.write("## Example: \n") 
		f.write("## not_allowed_residues=range(4,9)+range(17,25) or [6,7,8,9,10]\n\n")
		f.write("not_allowed_residues = []\n")

	if tm==1:
		f.write("\n## Intracellular & Extracellular residues\n")
		f.write("## Example: \n") 
		f.write("## intracellular_residues=range(4,9)+range(17,25) or [6,7,8,9,10]\n\n")
		f.write("intracellular_residues = []\n")
		f.write("extracellular_residues = []\n")
	
	if pexp==1:
		f.write("\n## Previous information\n")
		f.write("## Example: \n") 
		f.write("## prev_info=[[5,10],[5,15]]\n\n")
		f.write("prev_info = []\n")

	f.write("\n## Markov state model parameters\n\n")
	f.write("lagtime = \t # number of frames\n")
	f.write("clusters = \t # number of clusters\n")
	
	f.close()
	logging.info(config_filename+" file was written.")

