"""AR Dynamics CLI

Usage:
  ardynamics-cli backup [--test|--debug] [--domain=<domain>]
  ardynamics-cli restore [--test|--debug] [--domain=<domain>]
  ardynamics-cli -h | --help
  ardynamics-cli --version

Options:
  -h --help  Show this screen
  --version  Show version

"""
from docopt import docopt
from inspect import getmembers, isclass
from . import __version__ as VERSION


def main():
    import commands
    options = docopt(__doc__, version=VERSION)

    for k, v in options.iteritems():
        if hasattr(commands, k) and v == True:
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()