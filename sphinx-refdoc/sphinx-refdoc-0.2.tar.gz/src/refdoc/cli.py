# -*- coding: utf-8 -*-
"""
cli interface. Very simple for now.
"""
from __future__ import absolute_import

import click


@click.command()
@click.option('-i', '--input-pkg', metavar='<package_path>', multiple=True)
@click.option('-o',  '--out', metavar='<dst_dir>')
@click.option('--no-index', is_flag=True)
@click.option(
    '-v', '--verbose',
    count=True,
    help="Be verbose. Can specify multiple times for more verbosity."
)
def docs(input_pkg, out, no_index, verbose):
    """ Generate reference documentation for all packages found in src_dir. """
    from . import logic

    logic.generate_docs(input_pkg, out, no_index, verbose)
