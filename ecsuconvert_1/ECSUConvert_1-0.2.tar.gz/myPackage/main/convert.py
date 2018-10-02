#!/usr/bin/python
import sys
from myPackage.mod_1 import read_file, write_file
from myPackage.mod_2 import string_opp


def main():
    '''Convert all characters in a file to their inverse case (upper or lower case).

    '''
    if len(sys.argv) != 3:
        print 'python convert.py [input file] [output file]'
        exit(1)

    file_list, filename = read_file(sys.argv[1])
    converted_list = string_opp(file_list)
    write_file(sys.argv[2], converted_list)


if __name__ == '__main__':
    main()
