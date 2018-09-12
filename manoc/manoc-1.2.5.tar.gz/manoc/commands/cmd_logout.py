import sys

import click

from manoc.cli import pass_context


@click.command('logout')
@pass_context
def cli(ctx):
    """Command on logout"""
    click.echo('Logout successful')
    sys.exit(1)
