#!/usr/bin/env python3
import argparse
import logging
from .config import read_config
from .plugins import load_plugins
from .logger import setup_logging

from . import __version__

# Setup logging
logger = logging.getLogger(__name__)


def main() -> None:
    """
    Main method.
    """
    parser = argument_parse()
    args = parser.parse_args()
    verbosity_level = verbosity(args.verbose)
    setup_logging(args.logger, verbosity_level)
    logger.info("Reading the rundeck-resources configuration")
    config = read_config(args.config)
    logger.info("Loading importer plugins")
    input_plugins = load_plugins(config, 'Importers')
    logger.info("Loading exporter plugins")
    output_plugins = load_plugins(config, 'Exporters')

    logger.info("Initializing input interfaces")
    logger.debug("Input plugins: {}".format(input_plugins))
    input_interfaces = initialize_interfaces(config, input_plugins)
    logger.info("Initializing output interfaces")
    logger.debug("Output plugins: {}".format(output_plugins))
    output_interfaces = initialize_interfaces(config, output_plugins)

    logger.info("Importing nodes resources from input plugins")
    logger.debug("Input interfaces: {}".format(input_interfaces))
    nodes = import_resources(input_interfaces)
    logger.info("Exporting nodes resources using output plugins")
    logger.debug("Output interfaces: {}".format(output_interfaces))
    export_resources(output_interfaces, nodes)


def initialize_interfaces(config: dict, plugins: dict) -> dict:
    """
    Method to initialize the interfaces with the configuration.

    :param config: The configuration file content.
    :type config: dict
    :param plugins: The list of loaded plugins.
    :type plugins: dict
    :returns: The list of loaded plugins initialized.
    :rtype: dict
    """
    interfaces = []
    for interface in plugins.values():
        interfaces.append(
            interface['plugin'](interface['title'],
                                config))
    return interfaces


def import_resources(interfaces: list) -> dict:
    """
    Method to get all resources from the *input* interfaces.

    :param interfaces: The list of initialized input interfaces.
    :type interfaces: list
    :returns: The resources returned by the input interfaces.
    :rtype: dict
    """
    resources = {}
    for interface in interfaces:
        resources.update(interface.import_resources())
    return resources


def export_resources(interfaces: list, resources: dict) -> None:
    """
    Method to export the resources using the *output* interfaces.

    :param interfaces: The list of initialized output interfaces.
    :type interfaces: list
    :param resources: The resources provided by the input interfaces.
    :type resources: dict
    """
    for interface in interfaces:
        interface.export_resources(resources)


def argument_parse() -> argparse.ArgumentParser:
    """
    Method to extract the arguments from the command line.

    :returns: The argument parser.
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description="Generates rundeck resources "
                    "file from different API sources.")

    parser.add_argument(
        'config', type=str,
        help='Configuration file.')
    parser.add_argument(
        '-v', '--verbose', action='count',
        help='Verbosity level to use.')
    parser.add_argument(
        '-l', '--logger', type=str,
        help='The logger YAML configuration file.')
    parser.add_argument(
        '-V', '--version', action='version',
        version='%(prog)s {}'.format(__version__),
        help='Prints version.')
    return parser


def verbosity(verbose: int):
    """
    Method to set the verbosity.

    :param verbose: The verbosity set by user.
    :type verbose: int
    :returns: The verbosity level.
    :rtype: int
    """
    if verbose == 0 or verbose is None:
        return logging.ERROR
    elif verbose == 1:
        return logging.INFO
    elif verbose > 1:
        return logging.DEBUG
