import os
import logging

# Setup logging
logger = logging.getLogger(__name__)


def normalize_path(path: str) -> str:
    """
    Method to expand and return an absolute
    path from a normal path.

    :param path: The path to normalize.
    :type path: str
    :returns: The absolute path.
    :rtype: str
    """
    logger.debug("Normalizing path: {}".format(path))
    exp_path = os.path.expanduser(path)
    abs_path = os.path.abspath(exp_path)
    logger.debug("Normalized path: {}".format(abs_path))
    return abs_path


def check_file(path: str) -> str:
    """
    Method to normalize the path of a file and
    check if the file exists and is a file.

    :param path: The file path to check.
    :type path: str
    :returns: The absolute path of a file.
    :rtype: str
    :raises: FileNotFoundError
    """
    logger.debug("Checking file: {}".format(path))
    file_path = normalize_path(path)
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        logger.error("File '{}' not found, raising exception".format(
            file_path))
        raise FileNotFoundError
    logger.debug("File '{}' found, returning path".format(file_path))
    return file_path


def get_section(plugin: str, title: str) -> str:
    """
    Construct the configuration section

    :param plugin: The plugin name.
    :type plugin: str
    :param title: The title seperated by `:` in the configuration file.
    :type title: str
    :returns: The configuration section to pull from the configuration
                file.
    :rtype: str
    """
    return ':'.join([plugin, title])
