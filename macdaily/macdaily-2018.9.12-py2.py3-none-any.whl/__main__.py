# -*- coding: utf-8 -*-


import argparse
import datetime
import os
import pathlib
import platform
import sys

from macdaily.daily_archive import archive
from macdaily.daily_bundle import bundle
from macdaily.daily_config import parse, config, launch
from macdaily.daily_dependency import dependency
from macdaily.daily_logging import logging
from macdaily.daily_postinstall import postinstall
from macdaily.daily_reinstall import reinstall
from macdaily.daily_uninstall import uninstall
from macdaily.daily_update import update
from macdaily.daily_utility import beholder


# change working directory
os.chdir(os.path.dirname(__file__))


# version string
__version__ = '2018.09.12'


# today
today = datetime.datetime.today()


# error handling class
class UnsupoortedOS(RuntimeError):
    def __init__(self, *args, **kwargs):
        sys.tracebacklimit = 0
        super().__init__(*args, **kwargs)


def get_parser():
    parser = argparse.ArgumentParser(prog='jsupdate', description=(
                    'Package Day-Care Manager'
                ), usage=(
                    'macdaily [-h] command '
                ))
    parser.add_argument('-V', '--version', action='version', version=__version__)

    group = parser.add_argument_group(
                    'Commands',
                    'macdaily provides a friendly CLI workflow for the '
                    'administrator of macOS to manipulate packages '
                )
    group.add_argument('command', choices=[
                            'update', 'up', 'upgrade',                      # update
                            'uninstall', 'remove', 'rm', 'r', 'un',         # uninstall
                            'reinstall', 're',                              # reinstall
                            'postinstall', 'post', 'ps',                    # postinstall
                            'dependency', 'deps', 'dp',                     # dependency
                            'logging', 'log',                               # logging
                            'launch', 'init',                               # launch
                            'config', 'cfg',                                # config
                            'archive',                                      # archive
                            'bundle',                                       # bundle
                        ], help=argparse.SUPPRESS)

    return parser


@beholder
def main():
    if platform.system() != 'Darwin':
        raise UnsupoortedOS('macdaily: script runs only on macOS')

    cfgdct = parse()
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:2])
    logdate = datetime.date.strftime(today, '%y%m%d')
    logtime = datetime.date.strftime(today, '%H%M%S')

    argv = sys.argv[2:]
    command = args.command.lower()
    if command in ('update', 'up', 'upgrade',):
        update(argv, cfgdct, logdate=logdate, logtime=logtime, today=today)
    elif command in ('uninstall', 'remove', 'rm', 'r', 'un',):
        uninstall(argv, cfgdct, logdate=logdate, logtime=logtime, today=today)
    elif command in ('reinstall', 're',):
        reinstall(argv, cfgdct, logdate=logdate, logtime=logtime, today=today)
    elif command in ('postinstall', 'post', 'ps',):
        postinstall(argv, cfgdct, logdate=logdate, logtime=logtime, today=today)
    elif command in ('dependency', 'deps', 'dp',):
        dependency(argv, cfgdct, logdate=logdate, logtime=logtime, today=today)
    elif command in ('logging', 'log',):
        logging(argv, cfgdct, logdate=logdate, logtime=logtime, today=today)
    elif command in ('launch', 'init',):
        launch(cfgdct)
    elif command in ('config', 'cfg',):
        config()
    elif command in ('archive',):
        archive(cfgdct, logdate=logdate, today=today)
    elif command in ('bundle',):
        bundle(argv, cfgdct, logdate=logdate, logtime=logtime, today=today)
    else:
        parser.print_help()


if __name__ == '__main__':
    sys.exit(main())
