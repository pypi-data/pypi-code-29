#!/usr/bin/python

'''IO operations.

'''

import os

__author__ = "Mitchell Sheep"
__version__ = "0.1"


def inputs(filename, root):

    '''Read a plain text into a list of string, each string is a line of the file.

    Args:
        filename (str): the name of the input file.

    Returns:
        list: a list of strings.

    Raises:
        IOError, if the file cannot be opened.

    '''

    hold = []
    fil = open(os.path.join(root, filename), "r")
    lines = fil.readlines()
    for xss in lines:
        hold.append(xss)
    fil.close()
    return hold

def output(one, two, root, name):
    '''Write a list of strings to a file.

    Args:
        a,b (list): a list of strings.
        name (str): output file name.

    Raises:
        IOError, if the output file cannot be created.

    '''
    if os.path.isfile(os.path.join(root, name)):
        print "The file {} aready exists.".format(name)
    else:
        fil = open(os.path.join(root, name), "w+")
        for i in one:
            fil.write(i)
        for j in two:
            fil.write(j)
        fil.close()


def main():
    '''
    DO NOthing
    '''
    pass

if __name__ == "__main__":
    main()
