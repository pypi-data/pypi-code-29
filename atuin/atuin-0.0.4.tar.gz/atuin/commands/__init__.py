import argparse
import atuin

parser = argparse.ArgumentParser(description=None)
parser.add_argument('--version', action='version', version=atuin.__version__)
parser.add_argument('-v', '--verbose', action='count', default=2)
subparsers = parser.add_subparsers(metavar='command', dest="subcommand")


def subcommand(args=[], help=None, name=None, parent=subparsers):
    """Decorator for wrapping argparse capabilities"""
    def decorator(func):
        nonlocal name
        if name is None:
            name = func.__name__.replace('_', '-')
        parser = parent.add_parser(name, help=help, description=func.__doc__)

        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)

    return decorator


def argument(*name_or_flags, **kwargs):
    """Helper function to satisfy argparse.ArgumentParser.add_argument()'s
    input argument syntax"""
    return (list(name_or_flags), kwargs)


__all__ = ['base']
