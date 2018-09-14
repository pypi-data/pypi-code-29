import argparse

from .__about__ import __version__

def main():
    parser = argparse.ArgumentParser(description='axju')
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
    args = parser.parse_args()
    parser.print_help()


if __name__ == '__main__':
    main()
