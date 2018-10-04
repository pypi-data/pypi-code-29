#!/usr/bin/python

'''Operations on the string list.

'''
__author__ = "Mitchell Sheep"
__version__ = "0.1"


def upper(fil):
    '''Convert strings to upper case.

    Args:
        a (list): a list of strings.

    Returns:
        list: a list of strings, in which all strings are upper case.
    '''
    out = []
    for i in fil:
        line = i.upper()
        out.append(line)
    return out

def lower(fil):
    '''Convert strings to lower case.

    Args:
        l (list): a list of strings.

    Returns:
        list: a list of strings, in which all strings are lower case.

    '''
    out = []
    for i in fil:
        line = i.lower()
        out.append(line)
    return out


def main():
    '''
    Do Nothing
    '''
    pass

if __name__ == '__main__':
    main()
