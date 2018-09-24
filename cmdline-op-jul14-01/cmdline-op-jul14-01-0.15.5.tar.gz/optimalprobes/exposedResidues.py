import os
import mdtraj as md
import glob
import numpy as np

from macros import *
from checkInputs import *

logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

def funcCreateSasaBenchmarkFile(benchmark_filename_with_path):
	
	f=open(benchmark_filename_with_path,"wb")
	f.writelines([
	"ALA\t129\n",
	"ARG\t274\n",
	"ASN\t195\n",
	"ASP\t193\n",
	"CYS\t167\n",
	"GLU\t223\n",
	"GLN\t225\n",
	"GLY\t104\n",
	"HIS\t224\n",
	"ILE\t197\n",
	"LEU\t201\n",
	"LYS\t236\n",
	"MET\t224\n",
	"PHE\t240\n",
	"PRO\t159\n",
	"SER\t155\n",
	"THR\t172\n",
	"TRP\t285\n",
	"TYR\t263\n",
	"VAL\t174\n"
	])
	f.close()

def funcEditBenchmarkFile(benchmark_filename_with_path):

	edit_benchmarks_flag=raw_input("Do you want to edit "+sasa_benchmark_filename+", Y or N \n")
	
	if edit_benchmarks_flag=="Y" or edit_benchmarks_flag=="":
		cmd="vi "+benchmark_filename_with_path
		os.system(cmd)
	else:
		cmd="cat "+benchmark_filename_with_path
		os.system(cmd)	


def funcTopologyInfo(t):
	
	R=t.topology.n_residues
	
	logging.info("This protein has "+str(R)+" residues.")

	atom_numbers_by_residue=[]
	for i in range(R):
		r=t.topology.select('resid '+str(i))
		atom_numbers_by_residue.append(r)
	
	residue_names=[]
	for i in range(R):
		res=str(t.topology.residue(i))
		residue_names.append(res[:3])

	return R, atom_numbers_by_residue, residue_names


def funcExposedResidues(args):

	inpath=funcCheckPath(args.inpath)
	outpath=funcCheckPath(args.outpath)
	trajtype=args.trajtype
	top=funcCheckFile(args.top)
	subsample=args.subsample
	cutoff=args.cutoff

	logging.info("Writing "+sasa_benchmark_filename)
	benchmark_filename=outpath+'/'+sasa_benchmark_filename
	funcCreateSasaBenchmarkFile(benchmark_filename)
	funcEditBenchmarkFile(benchmark_filename)

	outfolder=outpath+"/"+exposed_residues_sasa_featurization_foldername

	if os.path.isdir(outfolder) == False:
		cmd="mkdir "+outfolder
		os.system(cmd)
	else:
		if len(os.listdir(outfolder) ) != 0:
			cmd="rm -r "+outfolder+"/*"
			os.system(cmd)
		
	logging.info("SASA calculation for all atoms")
	first_traj_flag=0
	for file in sorted(glob.glob(inpath+'/*'+trajtype)):

		logging.info("Reading "+file)
		t=md.load(file,top=top)[::subsample]

		if first_traj_flag==0:
			R, atom_numbers_by_residue, residue_names = funcTopologyInfo(t)
			first_traj_flag=1
		
		sasa=md.shrake_rupley(t)
		logging.info("Featurizing trajectory based on sasa for every atom")
		outfile=outfolder+"/"+file.replace(inpath,"",1)+".npy"
		np.save(outfile,sasa)
	
	logging.info("SASA calculation by residue")
	for file in sorted(glob.glob(outfolder+'/*')):
		logging.info("Reading "+file)
		a=np.load(file)
		sasa_all_res=[]
		for i in range(R):
			sasa_traj=[]
			for j in range(len(a)):
				sasa=0
				for k in atom_numbers_by_residue[i]:
					sasa=sasa+a[j][k]
				sasa_traj.append(sasa*100)
			sasa_all_res.append(sasa_traj)
		outfile=outfolder+"/"+file.split('/')[-1]+'_sasa_by_res.npy'
		np.save(outfile,sasa_all_res)
	
	logging.info("Creating dataset")
	dataset=[]
	for file in sorted(glob.glob(outfolder+'/*sasa_by_res.npy')):
		a=np.load(file)
		dataset.append(a)
		
	logging.info("Calculating volumes.")
	f=open(sasa_benchmark_filename,'rb')
	benchmark_code=[]
	benchmark_vol=[]
	for line in f:
		cols=line.split('\t')
		benchmark_code.append(cols[0])
		benchmark_vol.append(float(cols[1]))
	f.close()

	logging.info("Checking cutoff.")
	solvent_exposed_residues_index=[]

	for i in range(R):
		res=residue_names[i]
		if res not in benchmark_code:
			logging.warning(res+" not a valid residue")
			continue;
		index=benchmark_code.index(res)
		r=[]
		for j in range(len(dataset)):
			for k in range(len(dataset[j][i])):
				r.append(dataset[j][i][k]*100)
		flag=0
		for j in range(len(r)):
			if (r[j]<benchmark_vol[index]*cutoff):
				flag=1
				break;
		if (flag==0):
			solvent_exposed_residues_index.append(i)

	f=open(outpath+'/'+exposedresidues_filename,'wb')

	for i in range(len(solvent_exposed_residues_index)):
		f.write(str(solvent_exposed_residues_index[i])+'\n')
	f.close()


