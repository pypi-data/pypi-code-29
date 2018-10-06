# -*- coding: utf-8 -*-
import logging

from pathlib import Path

import click

from sveetoy_cli.colors.finder import ColorFinder
from sveetoy_cli.colors.naming import ColorNames


@click.command('colors', short_help='Search for colors to name them.')
@click.argument('source', type=click.Path(exists=True), required=True)
@click.option('-t', '--to', type=click.File(mode='w'))
@click.pass_context
def colors_command(context, source, to):
    """
    Search for colors from files and return named colors.

    Files are found from 'SOURCE' argument that can be either a single filepath
    or a directory where to search recursively for Sass and CSS files.

    Optionnal 'TO' argument is file path where to write results.
    """
    logger = logging.getLogger("sveetoy")

    logger.info("Search files for colors")

    finder = ColorFinder()
    colors = finder.search(Path(source))

    namer = ColorNames()
    namer.load()

    results = namer.batch_names(colors)

    if not results:
        logger.warning("Unable to find any color from source(s)")
    else:
        click.echo(namer.as_json(results, fp=to))
