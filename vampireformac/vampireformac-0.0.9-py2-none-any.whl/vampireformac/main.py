#! C:\Python27
import os
import re
import time
import pandas as pd
import pickle
import random
import numpy as np
from Tkinter import *
from maskreader_new import read_selected_imageset
from bdreg import *
from pca_bdreg import *
from clusterSM import *


def recordIDX(IDX,BuildModel,cpout):
	#cwd = os.path.abspath(os.path.dirname(__file__))
	#UI = pd.read_csv(cwd + '/' + 'masterUI.csv')
	UI = pd.read_csv(cpout + 'masterUI.csv')

	if BuildModel:
		on = UI.build_model
		tag = 'build_model'
	else:
		on = UI.apply_model
		tag = 'apply_model'

	setpath = UI.maskset_path
	index = np.argwhere(on).flatten()

	activeset = setpath[index].tolist()
	activeset = [x for x in activeset if  str(x) != 'nan']
	activefolder = range(len(activeset))
	for i in activefolder:
		activefolder[i] = os.path.dirname(activeset[i])
	ar = np.array(activefolder)
	arr = np.unique(ar)
	for csv in arr: 
		CellsCSV = pd.read_csv(csv + '/Cells.csv')

		idx = np.argwhere(np.isnan(CellsCSV.Location_Center_X))
		idx = idx.flatten()

		if np.isnan(CellsCSV.Location_Center_X.tolist()[-1]):
			IDX = np.append(IDX,np.nan)

		print idx
		IDX = np.insert(IDX,idx,np.nan)
		IDX = np.delete(IDX,-1)

		CellsCSV['IDX']=IDX[range(len(CellsCSV['ImageNumber']))]
		IDX = IDX[range(len(CellsCSV['ImageNumber']))[-1]:]
		CellsCSV.to_csv(csv + '/Cells.csv')
	print ('recorded')
def main(BuildModel,clnum,cpout,entries):
	
	print('analysis initiated')
	if BuildModel:
		entries['Status'].delete(0,END)
		entries['Status'].insert(0,'created the model')
		# if firstrun == True:
		# 	df = read_selected_imageset(cpout,BuildModel) #convert mask to pickle for choosen image set

		#picklejar = os.path.abspath(os.path.dirname(__file__))
		#picklejar = picklejar.replace('sourcecode','picklejar')
		picklejar = cpout + 'picklejar/'

		df = read_selected_imageset(cpout,BuildModel)

		VamModel = {
		"N":[],
		"bdrn":[],
		"mdd":[],
		"sdd":[],
		"pc":[],
		"latent":[],
		"clnum":[],
		"pcnum":[],
		"mincms":[],
		"testmean":[],
		"teststd":[],
		"boxcoxlambda":[],
		"C":[],
		"dendidx":[]
		}

		N = None
		bdpc, bnreg, sc, VamModel = bdreg_main(df,N,VamModel,BuildModel)
		pc , score, latent, VamModel = pca_bdreg_main(bdpc,VamModel,BuildModel)
		pcnum=None
		IDX,bdsubtype,C,VamModel = cluster_main(score,pc,bdpc,clnum,pcnum,VamModel,BuildModel)
		if os.path.exists(picklejar + 'VamModel.pickle'):
			f=open(picklejar + 'VamModel_' + str(random.randint(0,100)) +'.pickle','wb')
			pickle.dump(VamModel,f)
			f.close()
		else:
			f=open(picklejar + 'VamModel.pickle','wb')
			pickle.dump(VamModel,f)
			f.close()

		print 'Model Saved'

		result = recordIDX(IDX,BuildModel,cpout)

	else:
		entries['Status'].delete(0,END)
		entries['Status'].insert(0,'applied the model')
		df = read_selected_imageset(cpout,BuildModel)

		# picklejar = os.path.abspath(os.path.dirname(__file__))
		# picklejar = picklejar.replace('sourcecode','picklejar') +'/'
		picklejar = cpout + 'picklejar/'
		
		f=open(picklejar + 'VamModel.pickle','r')
		VamModel = pickle.load(f)

		N = VamModel['N'] 
		#input bdpc,score,pc in new formats
		bdpc_new, bnreg_new, sc_new, VamModel = bdreg_main(df,N,VamModel,BuildModel)
		pc_new, score_new, latent_new, VamModel = pca_bdreg_main(bdpc_new,VamModel,BuildModel)

		clnum=VamModel['clnum']
		pcnum=VamModel['pcnum']
		#pc_new goes in for sake of placing, but pc from the model is used in cluster_main
		IDX_new,bdsubtype_new,C_new,VamModel = cluster_main(score_new,pc_new,bdpc_new,clnum,pcnum,VamModel,BuildModel)
		result = recordIDX(IDX_new,BuildModel,cpout)
		# build = [bdpc,bdsubtype,bnreg,C,IDX,latent,pc,sc,score]
		# new = [bdpc_new,bdsubtype_new,bnreg_new,C_new,IDX_new,latent_new,pc_new,sc_new,score_new]

		# f=open('build.pickle','wb')
		# pickle.dump(build,f)
		# f.close()

		# f=open('new.pickle','wb')
		# pickle.dump(new,f)
		# f.close()
	return entries