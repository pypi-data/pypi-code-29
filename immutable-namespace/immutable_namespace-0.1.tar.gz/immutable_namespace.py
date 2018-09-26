"""Immutable, interactive computation in Python.
"""

import copy
import sys
import traceback

# History of immutable namespaces over time
namespaces = [{}]

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
    except:
        traceback.print_exception(*sys.exc_info())
    else:
        # Append current namespace to namespace history
        namespaces.append(namespace)

    for i, ns in enumerate(namespaces):
        print('namespace[{}] : {}'.format(i, ns))


