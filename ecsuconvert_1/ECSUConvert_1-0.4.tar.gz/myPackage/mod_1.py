#!/usr/bin/python
from pathlib import Path


def read_file(filename):
    '''Reads in a file.

    Args:
        filename: holds a user input value for the name of an existing file.

    Returns:
        read_lines: a list of the lines read in from a file.
        filename: desired file name for the new file.

    '''
    read_lines = []

    try:
        with open(filename) as f:
            read_lines = f.readlines()
            read_lines = [x.strip() for x in read_lines]
        return read_lines, filename
    except Exception as e:
        if e is IOError:
            print 'File does not exist.'
        return 1


def write_file(filename, converted_list):
    '''Writes converted list to new file.

    Args:
        filename: name of new written file.
        converted_list: list of converted string from original file.

    '''
    if_exist = Path(filename)
    if if_exist.is_file():
        f = open(filename + "(1).txt", "w+")
        index = 0
        while index < len(converted_list):
            for val in converted_list[index]:
                f.write(val)
            f.write('\n')
            index += 1
    else:
        f = open(filename + ".txt", "w+")
        index = 0
        while index < len(converted_list):
            for val in converted_list[index]:
                f.write(val)
            f.write('\n')
            index += 1
    return 0


