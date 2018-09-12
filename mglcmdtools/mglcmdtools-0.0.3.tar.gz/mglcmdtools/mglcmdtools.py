#!/usr/bin/env python3
import subprocess
import sys
import os
import time
import re


def rm_and_mkdir(directory, force=False):
    '''
    create the `directory`.

    If it already exists, when `force=True`, will forcely delete the `directory` and recreate it, otherwise, do nothing and return `None`.

    '''

    if os.path.exists(directory):
        if force:
            cmd = 'rm -rf {0}'.format(directory)
            subprocess.check_output(cmd, shell=True)
        else:
            print(directory, 'already exists!', file=sys.stderr)
            return None

    os.mkdir(directory)

    return directory


def runcmd(command, verbose=False):
    '''
    Run `command`. if `verbose`, print time, and command content to stdout.

    '''
    try:
        if verbose:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                         time.localtime(time.time()))
            print(current_time, "\n", command, "\n", sep="", flush=True)
        subprocess.check_output(command, shell=True)

    except Exception as e:
        print(e, file=sys.stderr)
        raise RuntimeError(
            "Error occured when running command:\n{0}".format(command))

    return command


def longStrings_not_match_shortStrings(Long_strings, Short_strings, reverse=False):
    '''
    Long_strings: the long element list, e.g., ['AABB', 'CCDD', 'EEFF']
    Short_strings: the short element list, e.g., ['AA', 'EE']

    Excluding the elements of Long_strings whose substring is element of Short_strings.

    In the example above, the return is ['CCDD'].

    If reverse=True, the return will be ['AABB', 'EEFF'].

    Return: A list if the result contains one or more elements, or None if no element found.
    '''

    res = []
    for long_string in Long_strings:
        in_SS = any(
            short_string in long_string for short_string in Short_strings)
        if not in_SS and not reverse:
            res.append(long_string)
        elif in_SS and reverse:
            res.append(long_string)

    if len(res) == 0:
        return False

    return res


def read_fastaLike(file, startswith='>', maxrecords=-1):
    '''
    Every time return one record using the 'yield' function,
    the return record is a list, containing the 'seqid' line,
    and 'sequence' lines.

    By default, the 'seqid' line starts with '>',while the 'sequence'
    lines don't. Change this behavior with 'startswith' option.

    Usage:
    >>>records = read_fastaLike('myFastaLikefile')
    >>>for rec in records:
    >>>    print('seqid:', rec[0])
    >>>    print('first seq line:', rec[1])

    '''

    with open(file, 'r') as fh:
        firstline = True
        count = 0
        rec = []
        for i in fh:
            i = i.rstrip()
            if i.startswith(startswith):
                if firstline:
                    firstline = False
                else:
                    yield rec

                count += 1
                if (maxrecords > 0) and (count > maxrecords):
                    raise StopIteration

                rec = []
                rec.append(i)

            else:
                rec.append(i)

        yield rec

        raise StopIteration


def read_fastaLike2(file, seqid_pattern='^>', maxrecords=-1):
    '''
    Every time return one record using the 'yield' function,
    the return record is a list, containing the 'seqid' line,
    and 'sequence' lines.

    By default, the 'seqid' line has regular pattern '^>',while the 'sequence'
    lines don't. Change this behavior with 'seqid_pattern' option.

    Usage:
    >>>records = read_fastaLike2('myFastaLikefile')
    >>>for rec in records:
    >>>    print('seqid:', rec[0])
    >>>    print('first seq line:', rec[1])

    '''

    with open(file, 'r') as fh:
        firstline = True
        count = 0
        rec = []
        for i in fh:
            i = i.rstrip()
            if re.search(seqid_pattern, i):
                if firstline:
                    firstline = False
                else:
                    yield rec

                count += 1
                if (maxrecords > 0) and (count > maxrecords):
                    raise StopIteration

                rec = []
                rec.append(i)

            else:
                rec.append(i)

        yield rec

        raise StopIteration
