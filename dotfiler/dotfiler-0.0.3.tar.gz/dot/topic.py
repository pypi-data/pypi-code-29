# -*- coding: utf-8 -*-


from collections import namedtuple


DEFAULT_ENABLED = True
DEFAULT_INSTALLER = 'install.zsh'
DEFAULT_ALIASES = 'aliases.zsh'
DEFAULT_PATHS = 'paths.zsh'
DEFAULT_ENVS = 'envs.zsh'


Topic = namedtuple('Topic', [
    'name',
    'enabled',
    'symlinks',
    'installer',
    'aliaser',
    'pather',
    'enver',
])
Topic.__new__.__defaults__ = (
    '',                 # name
    DEFAULT_ENABLED,    # enabled
    [],                 # symlinks
    DEFAULT_INSTALLER,  # installer
    DEFAULT_ALIASES,    # aliaser
    DEFAULT_PATHS,      # pather
    DEFAULT_ENVS,       # enver
)
