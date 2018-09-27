import os
import sys
import getopt
from eroepub.epub_generator.epub_builder import EpubBuilder

def main():
    dirnames = sys.argv[1:]

    for dirname in dirnames:
        # Powershell may add a single '"' to path
        if dirname.endswith('"'):
            dirname = dirname[:-1]

        sub_dirnames = os.walk(dirname).__next__()[1]
        if sub_dirnames:
            # Recursive mode
            for sub_dirname in sub_dirnames:
                full_dirname = os.path.join(dirname, sub_dirname)
                build_from_dirname(full_dirname)
        else:
            # Normal mode
            build_from_dirname(dirname)


def build_from_dirname(dirname):
    abs_dirpath = os.path.abspath(dirname)
    parent_dirpath = os.path.dirname(abs_dirpath)
    b = EpubBuilder(abs_dirpath, parent_dirpath)
    b.build()
