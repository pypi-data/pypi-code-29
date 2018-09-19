# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 18.

@author: jason96
'''
import sys
from sputil.base import VERSION


usage = '''
usage: cmd <subcommand>
Splunk command-line utility.
Type 'cmd --version' to see the program version.

Most subcommands take file and/or directory arguments, recursing
on the directories.  If no arguments are supplied to such a
command, it recurses on the current directory (inclusive) by default.

Available subcommands:
   index : index test "/tmp/test.txt"
   search : search test "index=test"

For additional information, see https://github.com/gamjapower/splunk-util
'''


def main():
    if len(sys.argv) == 1:
        print usage
    elif len(sys.argv) == 2:
        # subcommand
        if sys.argv[1] == '--version':
            print VERSION
        elif sys.argv[1] == 'help':
            print usage
        elif sys.argv[1] == 'index':
            if len(sys.argv) == 2:
                print usage


if __name__ == '__main__':
    main()
