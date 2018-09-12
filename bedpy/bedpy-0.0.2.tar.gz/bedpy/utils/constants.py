import os

UTILITIES_DIR  = os.path.dirname(os.path.realpath(__file__))
MODULE_DIR     = os.path.join(UTILITIES_DIR, '..')
DATA_DIR       = os.path.join(MODULE_DIR, 'data')
# HG38_FILE      = os.path.join(SOURCE_DIR, 'hg38.fa')
TMP_BED_FILE   = os.path.join(DATA_DIR, '.bed.tmp.bed')
TMP_FASTA_FILE = os.path.join(DATA_DIR, '.seq.tmp.bed')
CHR_SIZES_FILE = os.path.join(DATA_DIR, 'hg38.chrom.sizes')


CHROMOSOME_LENGTHS = {'hg38': {}}
with open(CHR_SIZES_FILE) as f:
    for line in f:
        chr, length = line.rstrip('\n').split('\t')
        CHROMOSOME_LENGTHS['hg38'][chr] = int(length)



DELIM = '\t'
HEADER = False
NEWLINE = '\n'



DEFAULT_SIL_OPTIONS = {
    'length': 40,
    'every': 1000
}


'''
| Nucleic Acid Code |	Meaning        | Mnemonic                    |
|-------------------|---------         |--------------               |
| A | A                                | **A**denine                 |
| C | C                                | **C**ytosine                |
| G | G                                | **G**uanine                 |
| T | T                                | **T**hymine                 |
| U | U                                | **U**ridine                 |
| R | A or G                           | pu**R**ine                  |
| Y | C, T or U                        | p**Y**rimidines             |
| K | G, T, or U                       | bases which are **K**etones |
| M | A or C                           | bases with a**M**ino groups |
| S | C or G                           | **S**trong interaction      |
| W | A, T, or U                       | **W**eak interaction        |
| B | not A (i.e. C, G, T or U)        | **B** comes after A         |
| D | not C (i.e. A, G, T or U)        | **D** comes after C         |
| H | not G (i.e. A, C, T or U)        | **H** comes after G         |
| V | neither T nor U (i.e. A, C or G) | **V** comes after U         |
| N | A C G T U                        | **N**ucleic acid            |
| - | gap of indeterminate length      |                             |
'''
FASTA_CODEX = {
        #[a, c, t, g]
    'a': [1, 0, 0, 0],
    'c': [0, 1, 0, 0],
    't': [0, 0, 1, 0],
    'g': [0, 0, 0, 1],
    'r': [1, 0, 0, 1],
    'y': [0, 1, 1, 0], # or u
    'k': [0, 0, 1, 1], # or u
    'm': [1, 1, 0, 0],
    's': [0, 1, 0, 1],
    'w': [1, 0, 1, 0], # or u
    'b': [0, 1, 1, 1], # or u
    'd': [1, 0, 1, 1], # or u
    'h': [1, 1, 1, 0], # or u
    'v': [1, 1, 0, 1],
    'n': [1, 1, 1, 1], # or u
    '-': [0, 0, 0, 0]
}

FASTA_DECODEX =  dict(zip(
    [tuple(e) for e in FASTA_CODEX.values()], 
    FASTA_CODEX.keys()
))
