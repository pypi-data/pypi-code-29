import logging

from macros import *

logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

def funcWriteOspreyConfig(lagtime,clusters):

	f=open(osprey_config_filename,"wb")

	f.write("# osprey configuration file."+'\n'
			+"#---------------------------"+'\n'
			+"# usage:"+'\n'
			+"#  osprey worker config.yaml"+'\n'
			+"estimator:"+'\n'
			+"    eval: |"+'\n'
			+"        Pipeline(["+'\n'
			+"                ('cluster', MiniBatchKMeans()),"+'\n'
			+"                ('msm', MarkovStateModel(n_timescales=5, verbose=False)),"+'\n'
			+"        ])"+'\n'
			+'\n'
			+"# for eval, a python package containing the estimator definitions"+'\n'
			+"    eval_scope: msmbuilder"+'\n'
			+'\n'
			+'\n'
			+"strategy:"+'\n'
			+"    name: random # or moe, hyperopt_tpe"+'\n'
			+'\n'
			+"search_space:"+'\n'
		      )
		
	f.write("  cluster__n_clusters:"+'\n'
			+"    min: "+str(clusters)+'\n'
			+"    max: "+str(clusters)+'\n'
			+"    type: int"+'\n'
			+'\n'
		      )

	f.write("  msm__lag_time:"+'\n'
			+"      min: "+str(lagtime)+'\n'
			+"      max: "+str(lagtime)+'\n'
			+"      type: int"+'\n'
			+'\n'
		      )
	f.write("cv:"+'\n'
			+"  name: shufflesplit"+'\n'
			+"  params:"+'\n'
			+"    n_splits: 5"+'\n'
			+"    test_size: 0.5"+'\n'
			+'\n'
			+"dataset_loader:"+'\n'
			+"  name: joblib"+'\n'
		      )

	f.write("  params:"+'\n'
			+"    filenames: dataset.pkl"+'\n'
			+'\n'
		      )

	f.write("trials:"+'\n'
			+"  uri: sqlite:///osprey.db"+'\n'
		      )
	
	logging.info(osprey_config_filename+" file was written.")
	return
