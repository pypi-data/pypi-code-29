# -*- coding: utf-8 -*-
import io
import json
import logging

from pathlib import Path

import click

from sveetoy_cli.schemes import export_sass_schemes


@click.command('schemes', short_help='Build color scheme variables.')
@click.argument('source', type=click.Path(exists=True), required=True)
@click.option('-t', '--to', type=click.File(mode='w'))
@click.pass_context
def schemes_command(context, source, to):
    """
    From given Sass file, create Sass variables for Color schemes.
    """
    logger = logging.getLogger("sveetoy")

    logger.info("Opening Sass file")
    palette = io.open(source).read()

    output = export_sass_schemes(palette)

    if to:
        to.write(output)
        logger.info("Writed to {}".format(to.name))
    else:
        click.echo(output)
