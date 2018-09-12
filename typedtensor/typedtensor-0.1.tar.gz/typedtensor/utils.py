import inspect
import re
import sys

def verify_package(package,ignored_functions=[]):
    members = inspect.getmembers(package)
    members = filter((lambda m: inspect.isfunction(m[1]) ),members)
    v = []
    for (name,ptr) in members:
        s = inspect.getfullargspec(ptr)
        if ptr.__doc__ == None or \
           ( ptr.__doc__.count('shape_eq') == 0 or \
             ptr.__doc__.count('type_eq') == 0 or \
             ptr.__doc__.count('inout_eq') == 0 ) :
          v.append(name)
    r =  set(v) == set(ignored_functions)
    if not r:
        for i in v:
            print(i)
    return r
