import sys
from . import run

HELP = """
    options:

"""

OPTIONS = {
    '-s': 'silent'
    '-o': ''
}

def main():
    if len(sys.argv) < 2:
        print(HELP)
        return

    options = {}
    for a in sys.argv[1:-1]:
        options[OPTIONS[a]] = True

    if ''

    parameters = sys.argv[-1]
    # Separate command in structions
    instructions = parameters.split(';')

    # verbose by default
    
    run(*instructions, **options)

if __name__ == '__main__':
    main()
