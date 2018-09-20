import argparse
import os
from pathlib import Path

from pch.utils import RexList


def is_key(line):
    return line and not line.startswith('#')


def split(line):
    return line.split('=')[0]


def get_keys(text, ignored):
    lines = text.strip().splitlines()
    is_valid = lambda x: is_key(x) and x not in ignored
    return set(map(split, sorted(filter(is_valid, lines))))


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help="")
    parser.add_argument('-e', '--envfile', default='.env', help=".env file to check")
    parser.add_argument('-t', '--template', default='env.tpl', help="template file")
    parser.add_argument('-i', '--ignore', action='append', help="regular expression of entries to ignore")

    args = parser.parse_args(argv)

    if os.path.isfile(args.envfile):
        c1 = Path(args.envfile).read_text()
        c2 = Path(args.template).read_text()
        ignored = RexList(args.ignore or [])
        k1 = get_keys(c1, ignored)
        k2 = get_keys(c2, ignored)

        missing = k1 - k2
        aliens = k2 - k1
        if missing or aliens:
            print("Template `{}` does not match `{}` file".format(args.template, args.envfile))
            if missing:
                print("  Missing entries:", ", ".join(missing))

            if aliens:
                print("  Unknown entries:", ", ".join(missing))

            return 1

    return 1
