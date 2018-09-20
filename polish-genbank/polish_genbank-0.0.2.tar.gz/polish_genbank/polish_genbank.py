#!/usr/bin/python3
import argparse
import sys
import os
import re
from Bio import SeqIO
from Bio.Seq import Seq
import logging


def get_para():
    desc = '''Check for the internal stop codon, then substitute the internal
stop codon with NNN.

By mengguanliang [] genomics.cn, where [] == @. See https://github.com/linzhi2013/polish_genbank

    '''

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--in', dest='infile', metavar='<file>', required=True,
                        help='input genbank file or CDS file (fasta format)')

    parser.add_argument('--format', dest='infile_format', default='gb',
                        choices=['gb', 'fa'],
                        help='the input file format. For fasta file, all sequences are assumed to be forward strand, coding from +1 position [%(default)s]')

    parser.add_argument('--table', default=2, type=int, metavar='<int>',
                        required=False,
                        help='The genetic code table used for translation, for fasta input only [%(default)s]')

    parser.add_argument('--ntNs', dest='NewInternalStopCodonNT',
                        metavar='<str>',
                        required=False,
                        default='NNN',
                        help='the chars used for substituting an internal stop codon in CDS sequence. [%(default)s]')

    parser.add_argument('--aaNs', dest='NewInternalStopCodonAA',
                        metavar='<str>',
                        required=False,
                        default='X',
                        help='the chars used for substituting an internal stop codon in protein sequence. [%(default)s]')

    parser.add_argument('--out', dest='outfile', metavar='<file>',
                        required=True, help='output filename')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()

    return args


def replace_internalStopCodon(seq=None, internalStopCodon_poses=None, NewInternalStopCodonNT='NNN', strand=None):
    seq = list(str(seq))
    NewInternalStopCodonNT = list(NewInternalStopCodonNT)

    if strand > 0:
        for pos in internalStopCodon_poses:
            seq[pos:pos+3] = NewInternalStopCodonNT
    else:
        for pos in internalStopCodon_poses:
            seq[pos-2:pos+1] = NewInternalStopCodonNT

    return ''.join(seq)


def polish_gb(ingb=None, NewInternalStopCodonNT='NNN', NewInternalStopCodonAA='X', logger=None):
    '''
    Replace the internal stop codon with NNNs on Genbank nt sequence,
    and replace the '*' in 'translation' tag (protein sequence) with 'X'

    Return:
        An generator.
        
    Usage:

    >>> records = polish_gb(ingb='in.gb', NewInternalStopCodonNT='NNN',
            NewInternalStopCodonAA='X')
    >>> for rec in records:
    >>>     print(rec.id, rec.seq)

    '''


    for rec in SeqIO.parse(ingb, 'genbank'):
        for fea in rec.features:
            if fea.type == 'CDS':

                gene = ''
                product = ''
                if 'gene' in fea.qualifiers:
                    gene = fea.qualifiers['gene'][0]
                elif 'product' in fea.qualifiers:
                    product = fea.qualifiers['product'][0]
                    gene = product

                start = fea.location.start
                end = fea.location.end
                strand = fea.location.strand  # is a number

                if 'translation' in fea.qualifiers:
                    translation = fea.qualifiers['translation'][0]

                    if '*' in translation:
                        poses = [p for p, val in enumerate(
                            translation) if val == '*']

                        if logger:
                            logger.info('\n{0}, {1} {2}, positions on protein: {3}\n'.format(ingb, rec.id, gene, poses))

                        # the + strand
                        if strand > 0:
                            internalStopCodon_starts = []
                            for pos in poses:
                                nt_pos = start + 3 * pos
                                # nt_pos is the start position of a codon on nt
                                internalStopCodon_starts.append(nt_pos)

                            if logger:
                                logger.info('\n{0}, {1} {2}, positions on NT sequence: {3}\n'.format(ingb, rec.id, gene, internalStopCodon_starts))

                            seq = replace_internalStopCodon(seq=rec.seq,
                                    internalStopCodon_poses=internalStopCodon_starts,
                                    NewInternalStopCodonNT=NewInternalStopCodonNT, strand=strand)
                            if logger:
                                logger.info('\n>{0} {1} {2} {3} protein sequence\n{4}\n'.format(ingb, rec.id, gene, fea.location, translation))

                                logger.info('\n>{0} {1} {2} {3} CDS sequence\n{4}\n'.format(ingb, rec.id, gene, fea.location, rec.seq[start: end]))

                                logger.info('\n>{0} {1} {2} {3} updated CDS sequence\n{4}\n'.format(ingb, rec.id, gene, fea.location, seq[start: end]))

                            # update rec.seq
                            rec.seq = Seq(seq, rec.seq.alphabet)

                        # the - strand
                        else:
                            internalStopCodon_stops = []
                            for pos in poses:
                                nt_pos = end - 3 * pos
                                # nt_pos is the stop position of a codon on nt
                                internalStopCodon_stops.append(nt_pos)

                            if logger:
                                logger.info('\n{0}, {1} {2}, positions on NT sequence: {3}\n'.format(ingb, rec.id, gene, internalStopCodon_starts))


                            seq = replace_internalStopCodon(seq=rec.seq,
                                    internalStopCodon_poses=internalStopCodon_stops,
                                    NewInternalStopCodonNT=NewInternalStopCodonNT, strand=strand)
                            if logger:
                                logger.info('\n>{0} {1} {2} {3} protein sequence\n{4}\n'.format(ingb, rec.id, gene, fea.location, translation))

                                logger.info('\n>{0} {1} {2} {3} CDS sequence\n{4}\n'.format(ingb, rec.id, gene, fea.location, rec.seq[start: end]))

                                logger.info('\n>{0} {1} {2} {3} updated CDS sequence\n{4}\n'.format(ingb, rec.id, gene, fea.location, seq[start: end]))

                            # update rec.seq
                            rec.seq = Seq(seq, rec.seq.alphabet)

                        # finally update the translation
                        fea.qualifiers['translation'][0] = translation.replace(
                            '*', NewInternalStopCodonAA)

        yield rec


def polish_fasta(infasta=None, NewInternalStopCodonNT='NNN', table=2, logger=None):
    '''
    Replace the internal stop codon with NNNs.

    The infasta file is assumed to be CDS sequences, and coding from +1
    position.

    Return:
        An generator.

    Usage:

    >>> records = polish_fasta(infasta='myfile', NewInternalStopCodonNT='NNN', table=2)
    >>> for rec in records:
    >>>     print(rec.id, rec.seq)


    '''

    for rec in SeqIO.parse(ingb, 'fasta'):
        end = len(rec) / 3
        translation = str(rec.seq[:end].translate(table=table))
        # remove the last terminal stop codon (if any)
        translation = re.sub(r'*$', '', translation)

        if '*' in translation:
            poses = [p for p, val in enumerate(
                translation) if val == '*']

            if logger:
                logger.info('{0} {1}: positions on protein: {2}'.format(infasta, rec.id, poses))

            internalStopCodon_starts = []
            for pos in poses:
                nt_pos = start + 3 * pos
                # nt_pos is the start position of a codon on nt
                internalStopCodon_starts.append(nt_pos)

            if logger:
                logger.info('{0} {1}: positions on NT sequence: {1}'.format(infasta, rec.id, internalStopCodon_starts))

            seq = replace_internalStopCodon(seq=rec.seq,
                    internalStopCodon_poses=internalStopCodon_starts,
                    NewInternalStopCodonNT=NewInternalStopCodonNT,
                    strand=1)

            if logger:
                logger.info('{0} {1} protein sequence:\n{2}'.format(infasta, rec.id, translation))
                logger.info('{0} {1} CDS sequence:\n{2}'.format(infasta, rec.id, rec.seq))
                logger.info('{0} {1} updated CDS sequence:\n{2}'.format(infasta, rec.id, seq))

            # update rec.seq
            rec.seq = Seq(seq, rec.seq.alphabet)

        yield rec


def main():
    args = get_para()

    # 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) # must be DEBUG, then 'ch' below works.

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


    infor_file = os.path.basename(sys.argv[0]) + '.infor'
    #if os.path.exists(infor_file):
    #    os.remove(infor_file)

    fh = logging.FileHandler(infor_file)
    fh.setLevel(logging.INFO) # INFO level goes to the log file
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING) # only WARNING level will output on screen
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # 'application' code
    #logger.debug('debug message')
    #logger.info('info message')
    #logger.warn('warn message')
    #logger.error('error message')
    #logger.critical('critical message')


    logger.info(args)

    fhout = open(args.outfile, 'w')

    if args.infile_format == 'fa':
        records = polish_fasta(infasta=args.infile,
                            NewInternalStopCodonNT=args.NewInternalStopCodonNT,
                            table=args.table, logger=logger)
        for rec in records:
            SeqIO.write(rec, fhout, args.infile_format)

    else:
        records = polish_gb(ingb=args.infile,
                            NewInternalStopCodonNT=args.NewInternalStopCodonNT,
                            NewInternalStopCodonAA=args.NewInternalStopCodonAA,
                            logger=logger)
        for rec in records:
            SeqIO.write(rec, fhout, args.infile_format)

    fhout.close()


if __name__ == '__main__':
    main()
