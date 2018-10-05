#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys

from . import entries, meta


logger = logging.getLogger(__name__)


def build_parser():
    prog = os.path.basename(sys.argv[0])
    if prog not in ("pyclean", "pyclean.py"):
        prog = "pyclean"
    parser = argparse.ArgumentParser(prog=prog)

    parser.add_argument(
        "entries", nargs="+", metavar="DIR_OR_FILE",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose",
        action="store_true", help="be verbose",
    )
    parser.add_argument(
        "--version", action="version",
        version="%(prog)s, version {}".format(meta.__version__),
    )

    return parser


def parse_args(argv):
    parser = build_parser()
    options = parser.parse_args(argv)
    return options


def setup_logging(options):
    if options.verbose:
        logging.root.setLevel(logging.DEBUG)
        form = "%(levelname).1s: %(module)s:%(lineno)d: %(message)s"
    else:
        logging.root.setLevel(logging.INFO)
        form = "%(message)s"
    logging.basicConfig(format=form)


def main(argv=None):
    options = parse_args(argv)
    setup_logging(options)
    if options.verbose:
        logger.debug("options: %s", options.__dict__)
    entries.clean(options.entries)


if __name__ == '__main__':
    main()
