# -*- coding: utf-8 -*-
import io
import json
import logging

from pathlib import Path

import click

from sveetoy_cli.export import export_html, export_sass, export_python


@click.command('export', short_help='Export JSON to some formats.')
@click.argument('source', type=click.Path(exists=True), required=True)
@click.option('-f', '--format', metavar='STRING',
              type=click.Choice(['html', 'sass', 'python']),
              help="Export format, either 'html' or 'sass'",
              required=True)
@click.option('-t', '--to', type=click.File(mode='w'))
@click.pass_context
def export_command(context, source, format, to):
    """
    From given JSON file (dumped from ``colors`` command) export to some
    formats.

    Available formats:

    \b
    - 'html' build a HTML snippet with inline styles to make a palette preview;
    - 'sass' build a Sass file with variable for each color (color name is the
      variable name and hexadecimal code as value).
    - 'python' build a Python tuple of named colors;
    """
    logger = logging.getLogger("sveetoy")

    logger.info("Opening JSON dump")
    palette = json.load(io.open(source))

    if format == 'html':
        output = export_html(palette)
    elif format == 'sass':
        output = export_sass(palette)
    elif format == 'python':
        output = export_python(palette)

    if to:
        to.write(output)
        logger.info("Writed to {}".format(to.name))
    else:
        click.echo(output)
