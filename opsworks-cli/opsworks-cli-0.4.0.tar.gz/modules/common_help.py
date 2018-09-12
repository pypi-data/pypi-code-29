#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

import sys
import getopt
from common_functions import usage


def common_help():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', [
            'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(0)
        else:
            usage()
            sys.exit(0)
