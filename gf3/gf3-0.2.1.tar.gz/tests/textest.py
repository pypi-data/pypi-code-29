"""Test scanner and parser of macro talk."""

from unittest import TestCase as BaseTestCase
from doctest import (DocFileSuite, set_unittest_reportflags,
        REPORT_NDIFF, REPORT_ONLY_FIRST_FAILURE)
from glob import glob

import os, sys
sys.path.insert(0,
        os.path.abspath(
            os.path.normpath(
                os.path.join(
                    os.path.basename(__file__), os.pardir))))

from gf import IndentingWriter, push, pop
from gf.go import get_text

test_directory = os.path.abspath(
        os.path.normpath(os.path.dirname(__file__ )))


iw = IndentingWriter()

def show_text():
    global iw
    print(get_text(iw))
    iw = IndentingWriter()


test_functions = dict(
        w=lambda *arguments: iw(*arguments),
        push=lambda *arguments: push(iw, *arguments),
        pop=lambda *arguments: pop(iw, *arguments),
        st=show_text)

suite = DocFileSuite(*glob(os.path.join(test_directory, "*.tst")),
        **dict(module_relative = False, globs=test_functions))


if __name__ == "__main__":
    from unittest import TextTestRunner
    argv = []
    for arg in sys.argv[1:]:
        if arg == "-d":
            set_unittest_reportflags(REPORT_NDIFF)
        elif arg == "-f":
            set_unittest_reportflags(REPORT_ONLY_FIRST_FAILURE)
        else:
            argv.append(arg)
    if argv:
        suite = DocFileSuite(*argv,
                **dict(module_relative=False,
                    globs=test_functions))
    TextTestRunner().run(suite)
