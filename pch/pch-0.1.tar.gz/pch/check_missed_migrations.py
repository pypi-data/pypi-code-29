import argparse
import os

from pch.utils import cmd_output, RexList


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('directories', nargs='*', help="")

    args = parser.parse_args(argv)
    dirs = args.directories
    ret = 0

    if not dirs:
        dirs = [os.curdir]
    dirs = list(map(os.path.realpath, dirs))

    for target in dirs:
        migration_dirs = list(filter(None, cmd_output("find", target,
                                    "-type", "d",
                                    "-name", "migrations").split("\n")))
        output = cmd_output("git", "ls-files", "--others", "--exclude-standard", *migration_dirs)
        if output:
            ret = 1
            print(output)

    return ret


if __name__ == '__main__':
    exit(main())
