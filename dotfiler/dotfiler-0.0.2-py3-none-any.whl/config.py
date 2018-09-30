# -*- coding: utf-8 -*-
"""Handle configuration files for dot CLI."""

import io
from collections import namedtuple
from pathlib import Path
from typing import Optional, Union

import yaml

from .topic import (
    DEFAULT_ENABLED,
    DEFAULT_INSTALLER,
    DEFAULT_ALIASES,
    DEFAULT_PATHS,
    DEFAULT_ENVS,
    Topic,
)


DEFAULT_DOTFILES_HOME = Path.home() / '.dotfiles'
DEFAULT_DOTFILES_CONFIG = DEFAULT_DOTFILES_HOME / '.dot.yml'
SUPPORTED_VERSIONS = [
    '0.1.0'
]
SUPPORTED_VERSIONS_STR = ', '.join(SUPPORTED_VERSIONS)


class DotfileConfigError(Exception):
    pass


class DotfileConfigValueError(DotfileConfigError):
    pass


class UnsupportedConfigVersionError(DotfileConfigValueError):

    def __init__(self, version: str):
        self.version = version

        msg = f'Unsupported config version {version}. ' \
            f'Supported versions: {SUPPORTED_VERSIONS_STR}'

        super(UnsupportedConfigVersionError, self).__init__(msg)


DotfileConfig = namedtuple('DotfileConfig', [
    'version',
    'dotfiles_home',
    'topics',
])
DotfileConfig.__new__.__defaults__ = (
    '',
    DEFAULT_DOTFILES_HOME,
    [],
)


class DotfileConfigParser(object):

    def parse(self, file_obj: io.IOBase) -> DotfileConfig:
        config = yaml.load(file_obj)

        print('DotfileConfigParser:', config)

        self._validate_version(config)
        self._validate_topics(config)

        return DotfileConfig(
            version=config.get('version'),
            dotfiles_home=Path(
                config.get('dotfiles_home', DEFAULT_DOTFILES_HOME)
            ).expanduser(),
            topics=[Topic(**topic) for topic in config.get('topics', [])],
        )

    @staticmethod
    def _validate_version(config: dict):
        version = config.get('version')
        if not version:
            raise DotfileConfigValueError('Key "version" must be specified.')
        if version not in SUPPORTED_VERSIONS:
            raise UnsupportedConfigVersionError(version)

    @staticmethod
    def _validate_topics(config: dict):
        if 'topics' not in config:
            raise DotfileConfigValueError('Key "topics" must be specified.')

    # @staticmethod
    # def _parse_topic(topic: dict) -> Topic:
    #     return Topic(
    #         name=topic.get('name'),
    #         enabled=topic.get('enabled', True)
    #         initializer=top
    #     )


def get_config(config_path: Optional[Union[Path, str]]) -> DotfileConfig:
    """Return DotfileConfig object after reading config file."""
    print('DEFAULT:', DEFAULT_DOTFILES_HOME, DEFAULT_DOTFILES_CONFIG)
    parser = DotfileConfigParser()

    with Path(config_path).open('r') as fh:
        config = parser.parse(fh)
    return config


def parse_topic(topic: dict) -> Topic:
    """Return Topic after parsing topic dict from config file."""
    return Topic(
        name=topic.get('name'),
        enabled=topic.get('enabled', DEFAULT_ENABLED),
        symlinks=topic.get('symlinks', []),
        installer=topic.get('install', DEFAULT_INSTALLER),
        aliaser=topic.get('aliases', DEFAULT_ALIASES),
        pather=topic.get('paths', DEFAULT_PATHS),
        enver=topic.get('envs', DEFAULT_ENVS),
    )
