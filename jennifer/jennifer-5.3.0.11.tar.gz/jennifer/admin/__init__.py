#!/usr/bin/env python
import sys
from .generate_config import generate_config
from .run import run


def print_help():
    print("""
Usage: jennfier <command> [options]

JENNIFER 5 python agent

Commands:
    generate-config
    version
    run
""")


def main():
    # read command
    if len(sys.argv) < 2:
        print_help()
        exit()

    command = sys.argv[1]
    try:
        if command == 'generate-config':
            generate_config(sys.argv[1:])
            exit(-1)
        elif command == 'version':
            import jennifer
            print('JENNIFER Python(%s)' % jennifer.__version__)
        elif command == 'run':
            run(sys.argv[1:])
        else:
            print_help()
    except (EnvironmentError, FileNotFoundError)as e:
        print("Error: {0}\n\ntype 'jennifer {1} help' for help".format(
            str(e), command
        ))


if __name__ == '__main__':
    main()
    exit(-1)
