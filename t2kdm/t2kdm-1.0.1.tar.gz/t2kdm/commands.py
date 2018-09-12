"""Module handling the CLI and stand-alone script commands."""

from six import print_
import sh
import shlex
import argparse
import t2kdm
import t2kdm.interactive
import sys
from os import path
import posixpath

all_commands = []

class Command(object):
    """Commands to be used as stand alone scripts and within the CLI.

    Command line arguments are translated to the underlying function's
    positional and keyword arguments. Keyword arguments *must* define a short
    and long version.

    Example:

        ls = Command('ls', t2kdm.interactive.ls, "List contents of a remote logical path.")
        ls.add_argument('remotepath', type=str,
            help="the logical path, e.g. '/nd280'")
        ls.add_argument('-l', '--long', action='store_true',
            help="longer, more detailed output")

    The arguments containing `localpath` or `remotepath` are treated specially.
    These arguments are converted into an absolute path if the `localdir` or
    `remotedir` is specified repectively.
    """

    def __init__(self, name, function, description=""):
        self.name = name
        self.function = function
        # Set prog to command name, iff we are running in the CLI
        if "t2kdm-cli" in sys.argv[0]:
            self.parser = argparse.ArgumentParser(prog=name, description=description)
        else:
            self.parser = argparse.ArgumentParser(description=description)
        self.positional_arguments = []
        self.keyword_arguments = []

    def add_argument(self, *args, **kwargs):
        """Add an argument to the parser and memorize how to pass parsed object to the original function.

        All positional arguments are identified by their first argument *not* starting with a '-'.
        They are passed to the original function as `*args`.

        All keyword arguments are identified by their first argument starting with a '-'.
        Their keys are taken from the second argument minus the leading '--'.
        They are passed to the original function as `**kwargs`.
        """

        if args[0][0] == '-':
            # Keyword argument
            self.keyword_arguments.append(args[1][2:])
        else:
            # Positionsl argument
            self.positional_arguments.append(args[0])

        # Add the arguments to the parser
        self.parser.add_argument(*args, **kwargs)

    def run_from_console(self, **kwargs):
        """Entry point for console scripts.

        Parses command line arguments from sys.argv.
        Prints output on screen.
        Returns error code (0 if successful).
        """

        try:
            ret = self.run(self.parser.parse_args(), **kwargs)
        except t2kdm.backends.BackendException as e:
            print_(e, file=sys.stderr)
            return 1
        except t2kdm.interactive.InteractiveException as e:
            print_(e, file=sys.stderr)
            return 1
        except IOError as e:
            if e.errno == 32:
                # A broken pipe, e.g. from using a command with `head`.
                # Throwing an exception for this looks untidy, so we just return an error code.
                return 1
            else:
                raise

        return ret

    def run_from_cli(self, argstring, _return=False, **kwargs):
        """Run command from command line interface.

        Parses single string into arguments.
        Prints output on screen.
        Returns `False`, unless `_return` is `True`.
        Then it returns the actual return value.
        """

        try:
            args = shlex.split(argstring)
        except ValueError as e: # Catch errors from bad bash syntax
            print_(e)
            return False

        ret = False
        try: # We do *not* want to exit after printing a help message or erroring, so we have to catch that.
            ret = self.run_from_arglist(args, **kwargs)
        except t2kdm.backends.BackendException as e:
            print_(e)
        except t2kdm.interactive.InteractiveException as e:
            print_(e)
        except Exception as e:
            print_(e)
        except SystemExit:
            pass

        if _return:
            return ret
        else:
            return False

    def run_from_arglist(self, arglist, **kwargs):
        """Run command with list of arguments."""
        args = self.parser.parse_args(arglist)
        return self.run(args, **kwargs)

    @staticmethod
    def _condition_argument(name, value, localdir=None, remotedir=None):
        """Apply some processing to the arguments when needed."""

        # Make local paths absolute
        if localdir is not None and 'localpath' in name and not path.isabs(value):
            value = path.normpath(path.join(localdir, value))

        # Make remote paths absolute
        if remotedir is not None and 'remotepath' in name and not posixpath.isabs(value):
            value = posixpath.normpath(posixpath.join(remotedir, value))

        # Special case: remote basename == @
        if 'remotepath' in name:
            # Get all entries in the directory and replace the @ with the (lexigraphically) last one
            dirname, basename = posixpath.split(value)
            if basename == '@':
                entries = [x.name for x in t2kdm.ls(dirname)]
                entries.sort()
                value = posixpath.join(dirname, entries[-1])

        return value

    def run(self, parsed_args, **kwargs):
        """Run the command.

        Takes an parsed arguments object from argparse as input.
        """

        localdir = kwargs.pop('localdir', None)
        remotedir = kwargs.pop('remotedir', None)

        pos_args = []
        for arg in self.positional_arguments:
            value = self._condition_argument(arg, getattr(parsed_args, arg), localdir=localdir, remotedir=remotedir)
            pos_args.append(value)

        key_args = {}
        for arg in self.keyword_arguments:
            value = self._condition_argument(arg, getattr(parsed_args, arg), localdir=localdir, remotedir=remotedir)
            key_args[arg] = value
        key_args.update(kwargs)

        return self(*pos_args, **key_args)

    def __call__(self, *args, **kwargs):
        """Call the underlying function directly."""
        return self.function(*args, **kwargs)

ls = Command('ls', t2kdm.interactive.ls, "List contents of a remote logical path.")
ls.add_argument('remotepath', type=str, nargs='?', default='',
    help="the remote logical path, e.g. '/nd280'")
ls.add_argument('-l', '--long', action='store_true',
    help="longer, more detailed output")
ls.add_argument('-d', '--directory', action='store_true',
    help="list directory entries instead of contents")
all_commands.append(ls)

replicas = Command('replicas', t2kdm.interactive.replicas, "List replicas of a remote logical path.")
replicas.add_argument('remotepath', type=str, nargs='?', default='',
    help="the remote logical path, e.g. '/nd280/file.txt'")
replicas.add_argument('-c', '--checksum', action='store_true',
    help="display checksums of all replicas")
replicas.add_argument('-s', '--state', action='store_true',
    help="display the state of all replicas, e.g. 'ONLINE'")
replicas.add_argument('-n', '--name', action='store_true',
    help="display the name of the storage element")
all_commands.append(replicas)

check = Command('check', t2kdm.interactive.check, "Check the replicas of a given file/directory.")
check.add_argument('remotepath', type=str,
    help="the remote logical path, e.g. '/nd280'")
check.add_argument('-r', '--recursive', nargs='?', metavar="REGEX", default=False, const=True,
    help="recursively check all files and subdirectories [that match REGEX] of a directory")
check.add_argument('-q', '--quiet', action='store_true',
    help="do not print problematic files to screen")
check.add_argument('-v', '--verbose', action='store_true',
    help="print status messages to the screen")
check.add_argument('-l', '--list', metavar='FILENAME',
    help="save a list of failed files to FILENAME")
check.add_argument('-c', '--checksum', action='store_true',
    help="check whether the checksums of all replicas is identical, takes longer than just the se tests")
check.add_argument('-s', '--se', action='append', default=[],
    help="report replication status to the given storage element, can be used multiple times")
all_commands.append(check)

replicate = Command('replicate', t2kdm.interactive.replicate, "Replicate file to a storage element.")
replicate.add_argument('remotepath', type=str,
    help="the remote logical path, e.g. '/nd280/file.txt'")
replicate.add_argument('destination', type=str,
    help="the destination storage element by name, e.g. 'UKI-SOUTHGRID-RALPP-disk', or by host, e.g. 't2ksrm.nd280.org'")
replicate.add_argument('-r', '--recursive', nargs='?', metavar="REGEX", default=False, const=True,
    help="recursively replicate all files and subdirectories [that match REGEX] of a directory")
replicate.add_argument('-l', '--list', metavar='FILENAME',
    help="save a list of failed files to FILENAME")
replicate.add_argument('-s', '--source', type=str, default=None,
    help="the source storage element by name, e.g. 'UKI-SOUTHGRID-RALPP-disk', or by host, e.g. 't2ksrm.nd280.org'. If no source is provided, the replica closest to the destination is chosen")
replicate.add_argument('-t', '--tape', action='store_true',
    help="accept tape storage elements when choosing the closest one")
replicate.add_argument('-v', '--verbose', action='store_true',
    help="print status messages to the screen")
replicate.add_argument('-x', '--bringonline', action='store_true',
    help="do not wait for tape replicas to come online (EXPERT OPTION)")
all_commands.append(replicate)

get = Command('get', t2kdm.interactive.get, "Download file from grid.")
get.add_argument('remotepath', type=str,
    help="the remote logical path, e.g. '/nd280/file.txt'")
get.add_argument('localpath', type=str, nargs='?', default='./',
    help="the local path, e.g. `./`")
get.add_argument('-f', '--force', action='store_true',
    help="overwrite local files if necessary")
get.add_argument('-r', '--recursive', nargs='?', metavar="REGEX", default=False, const=True,
    help="recursively get all files and subdirectories [that match REGEX] of a directory")
get.add_argument('-l', '--list', metavar='FILENAME',
    help="save a list of failed files to FILENAME")
get.add_argument('-s', '--source', type=str, default=None,
    help="the source storage element by name, e.g. 'UKI-SOUTHGRID-RALPP-disk', or by host, e.g. 't2ksrm.nd280.org'. If no source is provided, the replica closest to the destination is chosen")
get.add_argument('-t', '--tape', action='store_true',
    help="accept tape storage elements when choosing the closest one")
get.add_argument('-v', '--verbose', action='store_true',
    help="print status messages to the screen")
get.add_argument('-x', '--bringonline', action='store_true',
    help="do not wait for tape replicas to come online (EXPERT OPTION)")
all_commands.append(get)

put = Command('put', t2kdm.interactive.put, "Upload file to the grid.")
put.add_argument('localpath', type=str, nargs='?', default='./',
    help="the file to be uploaded")
put.add_argument('remotepath', type=str,
    help="the remote logical path, e.g. '/nd280/file.txt'")
put.add_argument('-d', '--destination', type=str, default=None,
    help="the destination storage element by name, e.g. 'UKI-SOUTHGRID-RALPP-disk', or by host, e.g. 't2ksrm.nd280.org'. If no destination is provided, the closest one is chosen")
put.add_argument('-t', '--tape', action='store_true',
    help="accept tape storage elements when choosing the closest one")
all_commands.append(put)

SEs = Command('SEs', t2kdm.interactive.print_storage_elements, "Print all available storage elements on screen.")
all_commands.append(SEs)

remove = Command('remove', t2kdm.interactive.remove, "Remove file replica from a storage element, if it is not the last one.")
remove.add_argument('remotepath', type=str,
    help="the remote logical path, e.g. '/nd280/file.txt'")
remove.add_argument('destination', type=str,
    help="the destination storage element by name, e.g. 'UKI-SOUTHGRID-RALPP-disk', or by host, e.g. 't2ksrm.nd280.org'")
remove.add_argument('-f', '--final', action='store_true',
    help="do not refuse to remove the last replica of the file, USE WITH CARE!")
remove.add_argument('-r', '--recursive', nargs='?', metavar="REGEX", default=False, const=True,
    help="recursively remove all files and subdirectories [that match REGEX] of a directory")
remove.add_argument('-l', '--list', metavar='FILENAME',
    help="save a list of failed files to FILENAME")
remove.add_argument('-v', '--verbose', action='store_true',
    help="print status messages to the screen")
remove.add_argument('-x', '--unregister',
    help="unregister only, do NOT try to delete the actual replica (EXPERT OPTION)")
all_commands.append(remove)

fix = Command('fix', t2kdm.interactive.fix, "Try to fix some common issues with a file.")
fix.add_argument('remotepath', type=str,
    help="the remote logical path, e.g. '/nd280/file.txt'")
fix.add_argument('-v', '--verbose', action='store_true',
    help="print status messages to the screen")
fix.add_argument('-r', '--recursive', nargs='?', metavar="REGEX", default=False, const=True,
    help="recursively remove all files and subdirectories [that match REGEX] of a directory")
fix.add_argument('-l', '--list', metavar='FILENAME',
    help="save a list of failed files to FILENAME")
all_commands.append(fix)
