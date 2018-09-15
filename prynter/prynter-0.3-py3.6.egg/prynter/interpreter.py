import re

__all__ = ['run']

MODULE_RE = re.compile(r'^(\w+)(?=\.)|(?<![.\w])(\w+)(?=\.)')

def get_modules(s):
    """
    Extracts the module from a given command. E.g.:
        'string.digits' -> 'string'
        'print(3)' -> None
    """
    return [x or y for x,y in re.findall(MODULE_RE,s)]

def run(*args, silent=False):
    # get all (unique) modules
    instructions = list(args)
    modules = set(module for mods in map(get_modules,instructions) for module in mods)

    globs = { module:__import__(module) for module in modules } 

    if not silent:
        instructions[-1] = 'print({})'.format(instructions[-1])

    src = ';'.join(instructions)
    cmd = compile(src,'cmd','exec')
    exec(cmd,globs)