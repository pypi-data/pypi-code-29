import sys
from modelestimator._parse_arguments import parse_arguments
from modelestimator._controller import controller

USAGE_STRING ="""Usage: python -m modelestimator <format> <options> infiles

<format> should be either FASTA, STOCKHOLM or PHYLIP
Output is a rate matrix and residue distribution vector.
        
Options:
    -threshold or -t <f> Stop when consecutive iterations do not change by more
                     than <f>. Default is 0.001.
    -bootstrap or -b <r> Perform bootstrapping on multialignment with <r> resamplings.
                         Only one infile should be given in this mode. Returns
                         bootstrap norm.

Example usage:
    modelestimator fasta -t 0.001 file1.fa file2.fa file3.fa
    modelestimator fasta -b 200 file.fa"""

def main():
    ARGUMENT_LIST = sys.argv[1:]
      
    if len(ARGUMENT_LIST) == 0:
        print(USAGE_STRING)
        exit()
            
    try:
        FORMAT, BOOTSTRAP, RESAMPLINGS, THRESHOLD, FILE_NAMES = parse_arguments(ARGUMENT_LIST)
    except Exception as e:
        print("Wrong format on input\n")
        print(USAGE_STRING)
        exit()
        
    try:
        OUTPUT_STRING = controller(FORMAT, BOOTSTRAP, RESAMPLINGS, THRESHOLD, FILE_NAMES)
    except Exception as e:
        print("Error: ", e)
        exit()

    print(OUTPUT_STRING)