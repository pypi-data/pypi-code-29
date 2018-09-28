import sys
from termcolor import colored

_details = ''

def rd(s):
    return colored(s, 'red')

def gr(s):
    return colored(s, 'green')

def yl(s):
    return colored(s, 'yellow')

def update_details(fn):
    global _details
    _details = fn(_details)

def fail(err):
    assert isinstance(err, str)
    err = rd(err)

    if _details is not None:
        sys.exit(
            _details + '\n\n' + err
        )
    else:
        sys.exit(err)

def report_details():
    if _details is not None:
        print(_details + '\n')

