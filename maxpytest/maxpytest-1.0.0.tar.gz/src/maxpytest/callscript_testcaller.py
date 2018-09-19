#!/usr/bin/env python2
from __future__ import print_function
import os
import sys
import subprocess as sp
try:
    import pytest
except ImportError:
    pass

# class MaxpytestPlugin(object):
#     def __init__(self, args):
#         self.args = args
#         print('MaxPytestPlugin.args:', args)

#     def pytest_sessionfinish(self):
#         print('--------pytest_sessionfinish()--------------')
#         print('--------------------------------------------')

#     def pytest_cmdline_parse(self, pluginmanager, args):
#         """return initialized config object, parsing the specified args.
#         """
#         print('------pytest_cmdline_parse()----------------')
#         print(pluginmanager)
#         print(args)
#         print('--------------------------------------------')

#     def pytest_load_initial_conftests(self, early_config, parser, args):
#         """implements the loading of initial conftest files ahead of command line option parsing.
#         """
#         print('------pytest_load_initial_conftests()-------')
#         print(early_config)
#         print(parser)
#         print(parser.parse_known_and_unknown_args())
#         print(args)
#         print('--------------------------------------------')

#     def pytest_cmdline_main(self, config):
#         """called for performing the main command line action. The default implementation will invoke the configure hooks and runtest_mainloop.
#         """
#         print('------pytest_cmdline_main()-----------------')
#         print(config)
#         print('--------------------------------------------')

def _get_venv_path(cwd):
    """Returns pipenv virtual environment's site-packages path."""
    proc = sp.Popen(r'pipenv --venv', cwd=cwd, stdout=sp.PIPE, shell=True)
    venvpath = proc.communicate()[0].rstrip()
    if not os.path.exists(venvpath):
        raise RuntimeError('No pipenv installation found at: {0}'.format(cwd))
    return venvpath

def add_venv_sitepkgs(cwd):
    """Add site-packages directory from target's virtual environment to 3ds Max Python sys.path.
    
    :param cwd: root directory path for an installed Python virtual environment
    :type cwd: str
    """
    venv = _get_venv_path(cwd)
    sitepkgs = os.path.join(venv, r'Lib', r'site-packages')
    sitepkgs_escaped = sitepkgs.replace('\\', r'\\')
    sys.path.insert(0, sitepkgs)

def patch_isatty():
    """Add a mocked method to handle pytest expectations in 3ds Max. More:
    https://cbuelter.wordpress.com/2014/10/21/running-pytest-inside-3ds-max/
    """
    def _isatty(*args, **kwargs):
        return False
    sys.stdout.isatty = _isatty

def get_pytest(cwd):
    try:
        import pytest
    except ImportError:
        pass

    add_venv_sitepkgs(cwd)

    if 'pytest' not in globals():
        # Attempt pytest import with venv site-pkgs added to sys.path
        try:
            import pytest
        except ImportError as e:
            msg = '- Update packages with \'pipenv update\' from {0}'
            raise ImportError(str(e).rstrip(), msg.format(cwd))
    return pytest

def prep_environment(cwd):
    patch_isatty()
    os.chdir(cwd)

def get_args(pytestargs):
    """Add arg to turn off capturing of filedescriptors
    """
    #TODO Replace with plugin hook
    return pytestargs + [r"--capture=sys"]

def call_tests(cwd, pytestargs):
    pytest = get_pytest(cwd)
    prep_environment(cwd)
    args = get_args(pytestargs)

    try:
        pytest.main(args)
    except Exception as e:
        print(e, 'Pytest args:', args)
        raise e
    