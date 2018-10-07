# -*- coding: utf-8 -*-
"""
The actual documentation generation happens here.
"""
from __future__ import absolute_import, unicode_literals

# stdlib imports
import os
import os.path

# 3rd party imports
from . import rst
from . import util
from .objects import Package
from .toctree import Toctree


def generate_docs(pkg_paths, out_dir, gen_index=False, verbose=None, **kw):
    """ Generate documentation for the given package list. """
    del kw    # Exists For compatibility with future versions.

    pkgs = [Package.create(p) for p in pkg_paths]

    if verbose is not None:
        util.set_verbosity_level(verbose)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if gen_index:
        with open(os.path.join(out_dir, 'index.rst'), 'w') as fp:
            fp.write(generate_root_index_rst(pkgs))

    for pkg in pkgs:
        generate_pkg_docs(pkg, out_dir)


def generate_root_index_rst(packages):
    """ Generate root package index file. """
    toc = Toctree()
    for pkg in packages:
        toc.add(os.path.join(pkg.name + '/index.rst'))

    src = [
        rst.title('Reference documentation'),
        '',
        '.. ref_toc_inclusion_marker',
        '',
        str(toc)
    ]

    return '\n'.join(src)


def generate_pkg_docs(pkg, out_dir):
    """ Generate documentation for the given package in the given out_dir. """
    pkg.collect_children()
    pkg_path = os.path.join(out_dir, pkg.name)

    if not os.path.exists(pkg_path):
        os.makedirs(pkg_path)

    # Generate the package documentation
    with open(os.path.join(pkg_path, 'index.rst'), 'w') as fp:
        fp.write(pkg.to_rst())

    # Generate documentation for all the children
    for child in pkg.children:
        if child.type == 'package':
            generate_pkg_docs(child, pkg_path)
        elif child.type == 'module':
            generate_module_docs(child, pkg_path)
        else:
            print("Unknown child type '{}'".format(child.type))


def generate_module_docs(module, out_dir):
    """ Generate documentation for the given module in the given out_dir. """
    with open(os.path.join(out_dir, module.name + '.rst'), 'w') as fp:
        fp.write(module.to_rst())
