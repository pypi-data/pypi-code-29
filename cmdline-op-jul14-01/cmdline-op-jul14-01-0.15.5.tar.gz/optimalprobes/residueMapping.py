import mdtraj as md

from macros import *
from checkInputs import *

logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

def funcResiduemapping(args):

	traj=funcCheckFile(args.traj)
	top=funcCheckFile(args.top)

	t=md.load(traj,top=top)

	f=open(residuemapping_filename,"wb")
	R=t.topology.n_residues

	for i in range(R):
		f.write(str(i)+"\t"+str(t.topology.residue(i))+"\n")
	f.close()
