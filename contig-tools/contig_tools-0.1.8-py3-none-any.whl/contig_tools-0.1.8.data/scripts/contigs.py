#!python
import argparse
import sys as s

from contig_tools.filter_contigs import filter_contig_file

def parse_arguments():
    description = """
    A package to maniuplate and assess contigs arising from de novo assemblies
    """
    # parse all arguments
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter, )
    subparsers = parser.add_subparsers(help='The following commands are available. Type contig_tools <COMMAND> -h for more help on a specific commands', dest='command')

    # The filter command
    filter_parser = subparsers.add_parser('filter', help='Filter contigs based on either length and/or coverage')
    filter_parser.add_argument('-f', '--fasta_file', help='path to SPAdes contig fasta file', required = True, type = str)
    filter_parser.add_argument('-l', '--minimum_contig_length', help='minimum length of a contig to keep', default = 500, type = int)
    filter_parser.add_argument('-c', '--minimum_contig_coverage', help='minimum coverage of a contig to keep', default = 2.0, type = float)

    options = parser.parse_args()
    return options




if __name__ == '__main__':
    options = parse_arguments()
    if options.command == 'filter':
       filter_contig_file(options.fasta_file, options.minimum_contig_length, options.minimum_contig_coverage)