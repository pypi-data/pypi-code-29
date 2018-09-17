__CONSTANT = 7 # this is ignored

import os  # this is ignored

include_config('test.2.py')

def func() -> int:
    return 42

var_1 = __CONSTANT
var_2 = 2
var_3 = func()