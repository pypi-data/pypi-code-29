import click

from manoc.utils.config import list_env


@click.command()
def cli():
    """List registered environments"""
    for env in list_env():
        click.echo(env)

