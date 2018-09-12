import os
import sys

import click

from manoc.utils.auth import verify_token
from manoc.utils.context import fill_context

CONTEXT_SETTINGS = dict(auto_envvar_prefix='MANOC')


class Context(object):
    def __init__(self):
        self.verbose = False
        self.access_token = None
        self.expires_at = None


pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))


class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('manoc.commands.cmd_' + name, None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.2.6')
    ctx.exit()


@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True,
              help='Print version information and quit')
@click.option('--verbose', '-v', is_flag=True, help='Make the operation more talkative')
@pass_context
def cli(ctx, verbose):
    ctx.verbose = verbose
    if verbose:
        click.echo('Verbose mode on.')
    fill_context(ctx)
    verify_token(ctx)


