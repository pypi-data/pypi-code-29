__version__ = "0.15.5"

import sys
import os
import argparse

from dependencies import *
from help import *
from residueMapping import *
from calcContacts import *
from exposedResidues import *
from generateConfigFile import *
#from generateTrials import *
from scoreTrials import *
from topChoices import *
from macros import *

def main():

	logging.basicConfig(filename=logfilename,level=logging.DEBUG,filemode="a")

	if len(sys.argv)<2:
		funcPrintHelp()

	elif sys.argv[1]=="--help" or sys.argv[1]=="-h":
		funcPrintHelp()

	elif sys.argv[1]=="--version" or sys.argv[1]=="-v":
		print("Optimal Probes version %s" % __version__)

	elif sys.argv[1]=="--dependencies":
		print("Optimal Probes version %s" % __version__)
		if len(sys.argv)==3:
			if sys.argv[2]=="check":
				funcRunDependenciesCheck()
			else:
				funcPrintHelp()
		else:
			funcPrintDependencies()

	elif sys.argv[1]=="residue_mapping":
		parser = argparse.ArgumentParser()
		subparser = parser.add_subparsers()
		residue_mapping = subparser.add_parser('residue_mapping',description='View residue mapping')
		residue_mapping.add_argument('-traj',metavar='TRAJ_FILE',help='provide a trajectory file',required=True,nargs=1)
		residue_mapping.add_argument('-top',metavar='TOP_FILE',help='provide topology file',required=True,nargs=1)
		args = parser.parse_args()
	
		funcResiduemapping(args)
		
	elif sys.argv[1]=="calc_contacts":
		parser = argparse.ArgumentParser()
		subparser = parser.add_subparsers()
		calc_contacts = subparser.add_parser('calc_contacts',description='Featurize dataset for contacts')
		calc_contacts.add_argument('-inpath',metavar='IN_PATH',help='specify input path',default=os.getcwd())
		calc_contacts.add_argument('-outpath',metavar='OUT_PATH',help='specify outpath path',default=os.getcwd())
		calc_contacts.add_argument('-trajtype',metavar='TRAJ_FILETYPE',help='provide trajectory file format',required=True)
		calc_contacts.add_argument('-top',metavar='TOP_FILE',help='provide topology file',required=True,nargs=1)
		calc_contacts.add_argument('-scheme',metavar='SCHEME',help='scheme for contact calculation, default=\"ca\"',default="ca")
		calc_contacts.add_argument('-subsample',metavar='SUBSAMPLE_FACTOR',help='factor for subsampling trajectory, default=1',default=1,type=int)
		calc_contacts.add_argument('-ter',metavar='INCLUDE TER_RESIDUES',help='include terminal residues, default=False',default=1,type=bool)
		args = parser.parse_args()
		funcCalcContacts(args)

	elif sys.argv[1]=="exposed_residues":
		parser = argparse.ArgumentParser()
		subparser = parser.add_subparsers()
		exposed_residues = subparser.add_parser('exposed_residues',description='Find solvent exposed residues')
		exposed_residues.add_argument('-inpath',metavar='IN_PATH',help='specify input path',default=os.getcwd())
		exposed_residues.add_argument('-outpath',metavar='OUT_PATH',help='specify outpath path',default=os.getcwd())
		exposed_residues.add_argument('-trajtype',metavar='TRAJ_FILETYPE',help='provide trajectory file format',required=True)
		exposed_residues.add_argument('-top',metavar='TOP_FILE',help='provide topology file',required=True,nargs=1)
		exposed_residues.add_argument('-subsample',metavar='SUBSAMPLE_FACTOR',help='factor for subsampling trajectory, default=1',default=1,type=int)
		exposed_residues.add_argument('-cutoff',metavar='EXPOSURE_CUTOFF',help='percentage of solvent exposure of residue, default=0.8',default=0.8,type=int)
		args = parser.parse_args()
		funcExposedResidues(args)

	elif sys.argv[1]=="generate_config":
		parser = argparse.ArgumentParser()
		subparser = parser.add_subparsers()
		generate_config = subparser.add_parser('generate_config',description='Generate a skeleton of the input file')
		generate_config.add_argument('-experiment',metavar='EXPERIMENT_TYPE',help='provide choice of experiment',required=True,choices=listExperiments)
		generate_config.add_argument('-pr',metavar='PROXIMAL_RESIDUES',help='number of proximal residues to exclude',default=2,type=int)
		generate_config.add_argument('-ex',help='residues to exclude',action='store_true')
		generate_config.add_argument('-tm',help='transmembrane protein',action='store_true')
		generate_config.add_argument('-ss',help='secondary structure information',action='store_true')
		generate_config.add_argument('-pexp',help='previous information',action='store_true')
		args = parser.parse_args()
		funcGenerateConfigFile(args)

	elif sys.argv[1]=="generate_trials":
		parser = argparse.ArgumentParser()
		subparser = parser.add_subparsers()
		generate_trials = subparser.add_parser('generate_trials',description='Generate a list of trial sets')
		generate_trials.add_argument('config',metavar='config',help='provide config file')
		args = parser.parse_args()
		funcGenerateTrials(args)

	elif sys.argv[1]=="score_trials":
		parser = argparse.ArgumentParser()
		subparser = parser.add_subparsers()
		score_trials = subparser.add_parser('score_trials',description='Score trial sets')
		score_trials.add_argument('-benchmark',help='estimate scoring time',action='store_true')
		score_trials.add_argument('-ospreyinput',help='only generate Osprey config file',action='store_true')
		score_trials.add_argument('config',metavar='config',help='provide config file')
		args = parser.parse_args()
		funcScoreTrials(args)

	elif sys.argv[1]=="top_choices":
		parser = argparse.ArgumentParser()
		subparser = parser.add_subparsers()
		top_choices = subparser.add_parser('top_choices',description='Get residue pairs for top N choices')
		top_choices.add_argument('config',metavar='config',help='provide config file')
		top_choices.add_argument('-n',metavar='N_TOP_CHOICES',help='n top choices',default=1,type=int)
		args = parser.parse_args()
		funcTopChoices(args)

	else:
		funcPrintHelp()

	logging.shutdown()

