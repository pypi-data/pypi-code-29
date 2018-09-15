import re

__all__ = ['run']

MODULE_RE = re.compile(r'^(\w+)(?=\.)|(?<![.\w])(\w+)(?=\.)')
VAR_RE    = re.compile(r'^(\w+)(?=\s*\=.*)')

def get_modules(s):
    """
    Extracts the module from a given command. E.g.:
        'string.digits' -> 'string'
        'print(3)' -> None
    """ 
    return (x or y for x,y in re.findall(MODULE_RE,s))

def get_var(s):
    search = re.search(VAR_RE, s)
    if search is None:
        return None
    
    return search.group()

def run(*args, **kwargs):
    # get all (unique) modules
    instructions = list(args)

    used = set(get_var(s) for s in instructions)
    modules = set(
        module 
            for mods in map(get_modules,instructions) 
            for module in mods if module not in used
    )

    globs = { module:__import__(module) for module in modules } 

    if not kwargs.get('silent'):
        instructions[-1] = 'print({}, end="")'.format(instructions[-1])

    src = '\n'.join(instructions)
    cmd = compile(src,'cmd','exec')
    exec(cmd,globs)