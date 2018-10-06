# -*- coding: utf-8 -*-
import click

from sveetoy_cli import __version__


@click.command()
@click.pass_context
def version_command(context):
    """
    Print out version information.
    """
    click.echo("Sveetoy Commandline {}".format(
        __version__,
    ))
