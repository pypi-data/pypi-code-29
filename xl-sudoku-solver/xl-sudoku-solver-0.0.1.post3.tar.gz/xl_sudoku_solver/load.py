import os
import sys

from .exceptions import FormatError


def from_string(txt):
    """Create a list structure from a special format of string.

    Args:
        txt: a string, 9 lines, 'x' represents blank cell that needs to fill. An example here:
            xx31x8xxx
            xx2xxx7xx
            8xx63xxxx
            xx4x568xx
            xxx2x9xxx
            xx538x2xx
            xxxx91xx3
            xx9xxx4xx
            xxx8x79xx
    
    Returns:
        A 2d list object.
    """
    if txt is None or txt == '':
        raise FormatError('Nothing passed in')
    if not isinstance(txt, str):
        raise FormatError('Expect a string value')
    table = list(filter(lambda x: False if x == '' else True, txt.splitlines()))
    if len(table) != 9:
        raise FormatError('Row number is {} which is not equal to 9'.format(len(table)))
    for i,row in enumerate(table):
        try:
            table[i] = list(map(lambda x: None if x == 0 else x,
                map(int, row.strip().replace(' ', '').replace('x', '0'))))
            if len(table[i]) < 9:
                raise FormatError('Col-{} has cells less than 9'.format(i+1))
            elif len(table[i]) > 9:
                raise FormatError('Col-{} has cells more than 9'.format(i+1))
        except ValueError as e:
            msg = e.args[0]
            idx_start = msg.index('\'')
            idx_end = msg.rindex('\'')
            raise FormatError('Row-{} has an error when parsing, {} is not an number'.format(i+1,
                msg[idx_start:idx_end+1]))
    return table

def from_file(filename):
    """Create a list structure from a special format of file.

    Args:
        filename: in which the formated string is located.
    
    Returns:
        A 2d list object.
    """
    with open(filename, 'r') as f:
        return from_string(f.read())

def from_input():
    """Create a list structure from input.

    Returns:
        A 2d list object.
    """
    # insert a white line means input is over
    return from_string(''.join(line for line in iter(sys.stdin.readline, '\n')))
