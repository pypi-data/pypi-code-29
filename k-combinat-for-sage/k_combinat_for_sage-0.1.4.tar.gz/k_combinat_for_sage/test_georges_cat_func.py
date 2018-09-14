#!/usr/bin/env sage
# use `sage --python -m pdb test_all.py` for the debugger
# A place to test my functions
from __future__ import print_function
import time

from sage.all import *
print('Sage loaded.  Now loading local modules...')
from testing import *
from all import *
from strong_marked_tableau import __go_to_ribbon_head
from shorthands import *
start_time = time.time()
print('Modules loaded.  Testing...')


















# ALL DONE!
print('Testing completed successfully!', end='')
end_time = time.time()
elapsed_time = end_time - start_time
print(' Elapsed time = {}'.format(elapsed_time))
