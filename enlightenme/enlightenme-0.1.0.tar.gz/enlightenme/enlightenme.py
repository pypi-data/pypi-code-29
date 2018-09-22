import click

from enlightenme.commands.source_command import SourceCommand
from enlightenme.news.news_formatters import NewsFormatter

ENLIGHTENME_HELP = "collect news/updates from your favorite tech channels"


@click.group(name="enlightenme",
             help=ENLIGHTENME_HELP,
             invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context):
    if not ctx.invoked_subcommand:
        click.echo("""
Welcome to Enlighten Me!
------------------------
%s

See enlightenme --help for more details.""" % ENLIGHTENME_HELP)


@cli.group(cls=SourceCommand, help=SourceCommand.help)
@click.option('--format', '-f', default=NewsFormatter.DEFAULT_FORMAT,
              type=click.Choice(NewsFormatter.FORMAT_OPTIONS),
              help="Displays news in a format")
@click.option('--output', '-o', required=False,
              help="Write to FILE instead of stdout")
@click.option('--keywords', '-k', required=False,
              help="Topics or Keywords that interest you (e.g. python,golang)")
@click.pass_context
def source(ctx: click.Context, format: str = None,
           output: str = None, keywords: str = None):
    pass
