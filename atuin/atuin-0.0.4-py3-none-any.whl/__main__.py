import logging
from atuin.commands import parser
from atuin.commands import *

__LOG_LEVEL = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}


def main():

    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        logging.getLogger().setLevel(__LOG_LEVEL[min(2, args.verbose)])
        args.func(args)


if __name__ == '__main__':
    main()
