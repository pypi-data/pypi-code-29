"""
Main entrance to commandline actions
"""
import click

from sveetoy_cli.cli.version import version_command
from sveetoy_cli.cli.colors import colors_command
from sveetoy_cli.cli.export import export_command
from sveetoy_cli.cli.schemes import schemes_command
from sveetoy_cli.logs import init_logger


# Help alias on '-h' argument
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# Default logger conf
SVEETOY_LOGGER_CONF = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', None)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', type=click.IntRange(min=0, max=5), default=4,
              metavar='INTEGER',
              help="An integer between 0 and 5, where '0' make a totaly "
              "silent output and '5' set level to DEBUG (the most verbose "
              "level). Default to '4' (Info level).")
@click.pass_context
def cli_frontend(ctx, verbose):
    """
    Sveetoy Commandline
    """
    printout = True
    if verbose == 0:
        verbose = 1
        printout = False

    # Verbosity is the inverse of logging levels
    levels = [item for item in SVEETOY_LOGGER_CONF]
    levels.reverse()
    # Init the logger config
    root_logger = init_logger(levels[verbose], printout=printout)

    # Init the default context that will be passed to commands
    ctx.obj = {
        'verbosity': verbose,
        'logger': root_logger,
    }


# Attach commands methods to the main grouper
cli_frontend.add_command(colors_command, name="colors")
cli_frontend.add_command(export_command, name="export")
cli_frontend.add_command(schemes_command, name="schemes")
cli_frontend.add_command(version_command, name="version")
