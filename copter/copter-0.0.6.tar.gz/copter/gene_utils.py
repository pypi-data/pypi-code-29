# -*- coding: utf-8 -*-


import random
import json
import pkgutil


RANDOM_CODON_USAGE = json.loads(pkgutil.get_data('copter', 'codon_usages/random.json'))


CODON_TO_AMINO_TABLE = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'TGT':'C', 'TGC':'C',
    'GAA':'E', 'GAG':'E',
    'GAT':'D', 'GAC':'D',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'TTT':'F', 'TTC':'F',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'CAT':'H', 'CAC':'H',
    'AAA':'K', 'AAG':'K',
    'TAA':'*', 'TGA':'*', 'TAG':'*',
    'ATG':'M',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAT':'N', 'AAC':'N',
    'CAA':'Q', 'CAG':'Q',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAT':'Y', 'TAC':'Y',
}


def generate_gene(aa_seq):
    return ''.join([amino_to_codon(amino) for amino in aa_seq])


def amino_to_codon(amino, codon_table=RANDOM_CODON_USAGE):
    r = random.random()
    sum = 0
    for codon, prob in codon_table[amino].items():
        sum += prob
        if sum >= r:
            return str(codon)


def codon_to_codon(codon, codon_table=RANDOM_CODON_USAGE):
    amino = CODON_TO_AMINO_TABLE[codon]
    return amino_to_codon(amino, codon_table=codon_table)


def has_ng_sequences(codons, ng_sequences):
    gene = ''.join(codons)
    return True in [ng_seq in gene for ng_seq in ng_sequences]
