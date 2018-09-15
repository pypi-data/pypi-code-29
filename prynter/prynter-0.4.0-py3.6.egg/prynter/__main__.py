import sys
from . import run, __version__

HELP = """
usage: prynt [options] command
    -h  --help         print this usage and exit
    -v  --version      print version and exit
    -s  --silent       do not print output
"""

OPTIONS_DICT = {
    '--silent': 'silent',
    's': 'silent',

    'h': 'help',
    '--help': 'help',

    '--version': 'version',
    'v': 'version'
}

def get_options(args):
    opts = {}

    for a in args:
        if a[0] != '-':
            continue

        if a.startswith('--'):
            opts[OPTIONS_DICT[a]] = True
        else:
            # a ~ '-xyz'
            for opt in a[1:]:
                opts[OPTIONS_DICT[opt]] = True
    
    return opts

def main():
    if len(sys.argv) < 2:
        print(HELP)
        return

    options = get_options(sys.argv[1:])

    if 'help' in options:
        print(HELP)
        return
    if 'version' in options:
        print(__version__)
        return

    parameters = sys.argv[-1]
    # Separate command in structions
    instructions = parameters.split(';')

    # verbose by default
    run(*instructions, **options)

if __name__ == '__main__':
    main()
