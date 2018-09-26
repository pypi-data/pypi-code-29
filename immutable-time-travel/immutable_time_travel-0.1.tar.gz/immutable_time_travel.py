"""Immutable, interactive computation in Python.

Reversible with time-travel.
"""

import copy
import sys
import traceback

# History of immutable namespaces over time
namespaces = [{}]

# Allow the user to jump in time
class TimeTravel(Exception):
    pass

def time_travel(n):
    global namespaces
    namespaces = namespaces[0:n+1]
    raise TimeTravel()

while True:
    
    # Prompt the user to type code
    code = input("\n>>> ")
    if not code:
        continue

    # Each block of code is run in a copy of the last namespace
    namespace = copy.deepcopy(namespaces[-1])
    
    # Run the user's code with basic exception handling
    try:
        exec(code, globals(), namespace)
    except SystemExit:
        raise
    except TimeTravel:
        pass
    except:
        traceback.print_exception(*sys.exc_info())
    else:
        # Append current namespace to namespace history
        namespaces.append(namespace)

    for i, ns in enumerate(namespaces):
        print('namespace[{}] : {}'.format(i, ns))


