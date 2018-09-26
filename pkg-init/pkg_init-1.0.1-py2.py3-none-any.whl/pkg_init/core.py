# Copyright (c) 2018 bluelief.
# This source code is licensed under the MIT license.

import sys
import os
from distutils import dir_util


ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "project")

def create_files(directory=None):
    """ Create init files """
    try:
        if directory is None:
            dir_util.copy_tree(ASSET_DIR, os.path.abspath('.'))
        else:
            dir_util.copy_tree(ASSET_DIR, os.path.join(os.path.abspath('.'), directory))
    except Exception as e:
        print(e)
    else:
        print("[*] Compleate create files.")

def main():
    if sys.argv[1]:
        path = sys.argv[1]
    else:
        path = None
    create_files(path)

if __name__ == "__main__":
    main()
