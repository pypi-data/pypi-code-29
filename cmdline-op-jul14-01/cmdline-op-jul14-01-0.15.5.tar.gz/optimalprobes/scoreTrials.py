import sys
import os
import logging
import random
import time
import numpy as np
import glob
from msmbuilder.utils import io

from writeOspreyConfig import *
from macros import *

logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

def funcGenerateDataset(c):
	
	if "," in c:	# Two-sided choices in membrane protein
		c_separated=c.split(',')
		c_separated_side1=c_separated[0].split('\t')
		c_separated_side2=c_separated[1].split('\t')
		
		pairs=[]
		for i in range(len(c_separated_side1)):
			for j in range(i+1,len(c_separated_side1)):
				pairs.append([int(c_separated_side1[i]), int(c_separated_side1[j])])
		
		for i in range(len(c_separated_side2)):
			for j in range(i+1,len(c_separated_side2)):
				pairs.append([int(c_separated_side2[i]), int(c_separated_side2[j])])
	else:
		c=c.split('\t')[:-1]
		
		pairs=[]
		for i in range(len(c)):
			for j in range(i+1,len(c)):
				pairs.append([int(c[i]), int(c[j])])

	contacts=np.load(contacts_outfilename)

	contactsIdx=[]
	for i in range(len(contacts)):
		item=list(contacts[i])
		if item in pairs:
			contactsIdx.append(i)
	
	dataset=[]
	for file in sorted(glob.glob(calc_contacts_all_contact_featurization_foldername+'/*.npy')):
#	for file in sorted(glob.glob(calc_contacts_all_contact_featurization_foldername+'/*round1_00?.*.npy')):
		f=np.load(file)
		tempDataset=[]
		for frame in range(len(f)):
			tempSingleData=[]
			for idx in contactsIdx:
				tempSingleData.append(f[frame][idx])
			tempDataset.append(tempSingleData)
		dataset.append(np.array(tempDataset))
	
	if os.path.isfile(dataset_pkl_filename):
		cmd="rm "+dataset_pkl_filename
		os.system(cmd)

	io.dump(dataset,dataset_pkl_filename)

def funcScoreTrials(args):
	
	config_filename=args.config

	f_config=open(config_filename,'rb')
	for line in f_config:
		exec(line, globals())
	f_config.close()

	funcWriteOspreyConfig(lagtime,clusters)

	if args.ospreyinput==True:
		sys.exit()
	
	if args.benchmark==True:
		logging.info("Beginning benchmark run.")
		numTrials = sum(1 for line in open(compatible_sets_final_file))
		logging.info("Number of trials is "+str(numTrials))

		lineNum=random.randint(0,numTrials-1)	# This line number is indexed from 0
		f=open(compatible_sets_final_file)
		lines=f.readlines()
		c=lines[lineNum]
		f.close()
		logging.info("Randomly chosen line number is "+str(lineNum)+" which corresponds to: "+c)

		startTime=time.time()
		logging.info("Start time: "+str(startTime))
		
		logging.info("Generating random dataset.")
		funcGenerateDataset(c)

		cmd="osprey worker "+osprey_config_filename
		os.system(cmd)
		
		endTime=time.time()
		logging.info("End time: "+str(endTime))
		
		timeDiff=endTime-startTime
		print "Time for a single trial run: "+str(timeDiff)
		logging.info("Time for a single trial run: "+str(timeDiff))
		
		totalTime=(timeDiff*numTrials)/60.0/60.0
		print "Estimated time for all trials: "+str(totalTime)+" hours."
		logging.info("Time for all trials: "+str(totalTime)+" hours.")
		
		cmd="rm osprey.db"
		os.system(cmd)
	else:
		f=open(compatible_sets_final_file)
		lines=f.readlines()
		f.close()
		for c in lines:
			funcGenerateDataset(c)
			cmd="osprey worker "+osprey_config_filename
			os.system(cmd)
			logging.info("Running osprey for trial: "+c)

		logging.info("Scoring all trials completed.")
		
