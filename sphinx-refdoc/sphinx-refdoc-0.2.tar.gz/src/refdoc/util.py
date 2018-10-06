# -*- coding: utf-8 -*-
"""
Various helpers and utilities.
"""
from __future__ import absolute_import

g_verbosity = 0


def gen_ref_file_tree(pkgs):
    """ Generate a nice tree for the reference documentation files.

    :param list<Package> pkgs:
        List of documented packages.
    :return str:
        A tree ready to be printed with fixed-width font.
    """
    lines = []
    pkg_count = len(pkgs)

    for i, pkg in enumerate(pkgs):
        if i < pkg_count - 1:
            prefix = u'|   '
            lines.append(u"├── {}".format(pkg.fullname))
        else:
            prefix = '    '
            lines.append(u"└── {}".format(pkg.fullname))

        mod_count = len(pkg.modules)
        for j, module in enumerate(pkg.modules):
            if j < mod_count - 1:
                lines.append(prefix + u"├── {}".format(module))
            else:
                lines.append(prefix + u"└── {}".format(module))

    return u'\n'.join(lines)


def set_verbosity_level(level):
    """ Set global output verbosity level.

    :param int level:
        Verbosity level. 0 means default, more means more verbose.
    """
    global g_verbosity
    g_verbosity = level


def get_verbosity_level():
    """ Get global output verbosity level.

    :return int:
        Verbosity level. 0 means default, more means more verbose.
    """
    global g_verbosity
    return g_verbosity
