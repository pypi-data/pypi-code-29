#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Yaml parser
-----------

Yaml parsing and setup.

"""

import os
from collections import Mapping
from functools import partial

import yaml


class YamlConstructor:
    """
    Collection of custom Yaml constructor.
    """
    @staticmethod
    def simple_join(loader, node):
        """
        Yaml join list of string on empty string.
        usage: !join [param, ...]

        :param obj loader: PyYaml Loader.
        :param obj node: Pyyaml node.
        :return: joined string.
        """
        seq = loader.construct_sequence(node)
        return ''.join(seq)

    @staticmethod
    def string_join(loader, node):
        """
        Yaml join list of string by given string as first param.
        usage: !string_join [param, ...]

        :param obj loader: PyYaml Loader.
        :param obj node: Pyyaml node.
        :return: joined string.
        """
        seq = loader.construct_sequence(node)
        return seq[0].join(seq[1:])

    @staticmethod
    def yaml_getter(loader, node, *, data):
        """
        Constructor to get data from dictionary.

        :param obj loader: PyYaml Loader.
        :param obj node: Pyyaml node.
        :param dict directory: project directory path.
        :return: value at given key.
        """
        key = loader.construct_sequence(node)[0]
        return data.get(key)


class YamlParser:
    """
    Parse yaml file using custom constructor with two level of settings
    prod and dev, dev inherite from prod and override it.

    :param bool debug: bool to setup prod or dev settings.
    :param str prod_block: yaml block name for production settings, default: prod.
    :param str dev_block: yaml block name for development settings, default: dev.
    :param dict directory: project directory path, default: {}.
    """
    custom_constructors = {
        '!join': YamlConstructor.simple_join,
        '!string_join': YamlConstructor.string_join,
    }

    def __init__(self, debug, *, prod_block='prod', dev_block='dev', custom_constructors=None):
        self.prod_block = prod_block
        self.dev_block = dev_block
        self.debug = debug
        self.custom_constructors.update(custom_constructors or {})
        self.add_custom_constructors(self.custom_constructors)

    def add_custom_constructors(self, custom_constructors):
        """
        Add custom constructors to yaml.

        :param dict custom_constructors: custom constructors to add as key: tag, value: func.
        """
        [yaml.add_constructor(tag, func) for tag, func in custom_constructors.items()]
        return self

    def add_getter_constructor(self, name, data):
        """
        Set a yaml constructor to get data from other yaml.

        :param str name: name of the getter.
        :param dict data: data dictionary to get from.
        """
        yaml.add_constructor(
            name, partial(YamlConstructor.yaml_getter, data=data)
        )
        return self

    def _update(self, source, update_dict):
        """
        Update nested mapping entity.

        :param dict source: source directory.
        :param dict update_dict: dict info to update.
        :return: data updated.
        """
        if isinstance(update_dict, Mapping):
            for k, v in update_dict.items():
                if isinstance(v, Mapping):
                    source[k] = self._update(source.get(k, {}), v)
                else:
                    source[k] = v
            return source
        return update_dict

    def parse(self, yaml_to_dict, yaml_dir_path):
        """
        Extract .yml conf files into info dict.

        :param dict yaml_to_dict: dict to map yaml file with variable.
        :param str yaml_dir_path: path directory for all yaml files.
        """
        for yml, info_dict in yaml_to_dict.items():
            with open(os.path.join(yaml_dir_path, yml), "r") as ymlfile:
                config = yaml.load(ymlfile)

            for section, value in config[self.prod_block].items():
                info_dict[section] = value
                if self.debug is True and config.get(self.dev_block):
                    info_dict[section] = self._update(
                        info_dict[section],
                        config[self.dev_block].get(section, value)
                    )
        return self
