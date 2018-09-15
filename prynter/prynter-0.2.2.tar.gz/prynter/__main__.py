import sys
from . import run

def main():
    if len(sys.argv) < 2:
        # show help
        print('Help')
        return

    parameters = sys.argv[-1]
    # Separate command in structions
    instructions = parameters.split(';')

    # verbose by default
    options = {'-v': True}
    run(*instructions, **options)

if __name__ == '__main__':
    main()
