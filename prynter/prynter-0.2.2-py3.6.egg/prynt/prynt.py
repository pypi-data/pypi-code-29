#!/usr/bin/env python3

import sys
import re

module_re = re.compile(r'^(\w+)(?=\.)|(?<![.\w])(\w+)(?=\.)')

def get_modules(s):
    """
    Extracts the module from a given command. E.g.:
        'string.digits' -> 'string'
        'print(3)' -> None
    """
    return [x or y for x,y in re.findall(module_re,s)]

def main():
    if len(sys.argv) == 2:
        parameter = sys.argv[1]
        options = set()
    else:
        parameter = sys.argv[1]
        options = set(sys.argv[1:-1])
    # Separate command in structions
    instructions = parameter.split(';')

    # get all (unique) modules
    modules = set(module for mods in map(get_modules,instructions) for module in mods)

    globs = { module:__import__(module) for module in modules } 

    if '-s' not in options:
        # verbose by default
        instructions[-1] = 'print({})'.format(instructions[-1])

    src = ';'.join(instructions)
    cmd = compile(src,'cmd','exec')
    exec(cmd,globs)

if __name__ == '__main__':
    main()