# Copyright (c) 2018 bluelief.
# This source code is licensed under the MIT license.

import os
import re
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def is_canonical(version):
    return re.match(r'^([1-9]\d*!)?(0|[1-9]\d*)(\.(0|[1-9]\d*))*((a|b|rc)(0|[1-9]\d*))?(\.post(0|[1-9]\d*))?(\.dev(0|[1-9]\d*))?$', version) is not None

def main():
    version = __import__('pkg_init').get_version()
    print(is_canonical(version), version)

if __name__ == '__main__':
    main()
