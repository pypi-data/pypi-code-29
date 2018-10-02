from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from future.utils import raise_
from future.utils import raise_with_traceback
from future.utils import raise_from
from future.utils import iteritems

from builtins import FileExistsError
#The above future imports helps/ensures that the code is compatible
#with Python 2 and Python 3
#Read more at http://python-future.org/compatible_idioms.html

try:
    import pydevscripts.wingdbstub
except Exception as e:
    print('Failed to load wingdb stub. Wing debugging will not be available')
    print(e)

import os
from pathlib import Path
import shutil

def bump_package_patch_version():
    """
    Updates the VERSION=a.x.y patch version in the setup.py found 
    in the current directory. 
    """
    
    package_dir = os.getcwd()
    setup_filename = Path(package_dir, "setup.py")
    tmp_setup_filename = Path(package_dir, "setup.py.tmp")
    
    setup_file = open(setup_filename, "r+")
    lines = setup_file.readlines()
    
    tmp_setup_file = open(tmp_setup_filename, "w")
    
    for line in lines:
        line = line.strip("\n")
        if line.startswith("VERSION"):
            xyz_version = line.strip("\"").split("=")[1]
            x,y, patch_version = xyz_version.split(".")
            new_patch_versrion = int(patch_version)+1
            new_version_line = "VERSION={}.{}.{}\"".format(x,y,new_patch_versrion)
            line = new_version_line
        #print(line)
        tmp_setup_file.write(line+"\n")
        
    tmp_setup_file.close()
    setup_file.close()
        
    shutil.move(tmp_setup_filename,setup_filename)
        
     

    
    
    