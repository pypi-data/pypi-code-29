#!/usr/bin/env python3

"""
asciidoc3_postinstall.py 

Copyright (C) 2018 by Berthold Gehrke <berthold.gehrke@gmail.com>

Free use of this software is granted under the terms of the
GNU General Public License Version 2 or higher (GNU GPLv2+).
"""

import os
import re
import shutil
import subprocess
import sys

USERHOMEDIR = os.path.expanduser("~") # e.g. GNU/Linux: USERHOMEDIR = '/home/username'

def main():
    AD3_LOCATION = ''
    try:
        p = subprocess.Popen("pip show asciidoc3", shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, universal_newlines=True, bufsize=-1)
        output = p.communicate()
    except Exception:
        print('error')
    if output:
        output = output[0]
        o = re.split(r'Location: ', output, re.DOTALL)[1]
        o = re.split(r'\nRequires', o, re.DOTALL)[0]
        # sample o
        # '/home/username/.local/lib/python3.5/site-packages', type: <class 'str'>
        AD3_LOCATION = o
    else:
        # no output
        sys.exit(1)

    # symlinks, user home 
    if os.path.exists(USERHOMEDIR + "/.asciidoc3"):
        os.replace(USERHOMEDIR + "/.asciidoc3", USERHOMEDIR + "/.asciidoc3_backup")
    os.symlink(AD3_LOCATION + "/asciidoc3", USERHOMEDIR + "/.asciidoc3")

    if os.path.exists(USERHOMEDIR + "/asciidoc3"):
        os.replace(USERHOMEDIR + "/asciidoc3", USERHOMEDIR + "/asciidoc3_backup")
    os.symlink(AD3_LOCATION + "/asciidoc3", USERHOMEDIR + "/asciidoc3")

    # internal symlinks
    if os.path.exists(AD3_LOCATION + "/asciidoc3/doc/images"):
        os.unlink(AD3_LOCATION + "/asciidoc3/doc/images")
    os.symlink(AD3_LOCATION + "/asciidoc3/images",
               AD3_LOCATION + "/asciidoc3/doc/images")

    if os.path.exists(AD3_LOCATION + "/asciidoc3/filters/graphviz/images"):
        os.unlink(AD3_LOCATION + "/asciidoc3/filters/graphviz/images")
    os.symlink(AD3_LOCATION + "/asciidoc3/images",
               AD3_LOCATION + "/asciidoc3/filters/graphviz/images")

    if os.path.exists(AD3_LOCATION + "/asciidoc3/filters/music/images"):
        os.unlink(AD3_LOCATION + "/asciidoc3/filters/music/images")
    os.symlink(AD3_LOCATION + "/asciidoc3/images",
               AD3_LOCATION + "/asciidoc3/filters/music/images")
      
if __name__ == '__main__':
    main()
