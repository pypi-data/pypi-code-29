#! /usr/bin/python
"""
codegenerator
"""

import os

import generator


def main(argv):
    """TODO: Docstring for main.

    :arg1: TODO
    :returns: TODO

    """
    if len(argv) < 2:
        print('ERROR : Too less arguments : askelerator TEMPLATE [ARGS]')
        return 1

    template_dir = argv[0] + "templates/"
    template_path = template_dir + argv[1]
    if not os.path.isdir(template_path):
        print('ERROR : Unknown template : ' + argv[1])
        return 1

    gen = generator.Generator(template_path, os.path.abspath('.'))

    gen.prepare_specs()
    gen.list_files()
    gen.check_files()
    gen.build_skel()

    return 0


if __name__ == "__main__":
    import sys
    main(sys.argv)
