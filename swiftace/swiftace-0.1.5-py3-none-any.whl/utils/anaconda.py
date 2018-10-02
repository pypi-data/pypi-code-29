"""Anaconda related utilities"""
import os
import yaml
import logging
import tempfile
from swiftace.utils.api import upload_conda_env, download_conda_env


class CondaError(Exception):
    """Error class for Anaconda-related exceptions"""
    pass


def get_conda_bin():
    """Get the path to the Anaconda binary"""
    conda_bin = os.popen('echo $CONDA_EXE').read().strip()
    if conda_bin == '':
        if os.popen('conda --version').read().strip() == '':
            raise CondaError(
                'Anaconda binary not found. Please make sure the "conda" command is in your system PATH or the environment variable $CONDA_EXE points to the anaconda binary')
        else:
            conda_bin = 'conda'
    logging.info(f'Anaconda binary: {conda_bin}')
    return conda_bin


def get_conda_env_name():
    """Get the name of the active conda environment"""
    env_name = os.popen('echo $CONDA_DEFAULT_ENV').read().strip()
    if env_name == '':
        env_name = 'base'
    logging.info(f'Anaconda environment: {env_name}')
    return env_name


def read_conda_env():
    """Read the anaconda environment into a YAML object"""
    command = f'{get_conda_bin()} env export -n {get_conda_env_name()}'
    stream = os.popen(command).read()
    if stream == '':
        raise CondaError(
            f'Failed to read Anaconda environment using command: "{command}""')
    return stream


def save_conda_env():
    """Read and save the Anaconda environment"""
    return upload_conda_env(read_conda_env(), get_conda_env_name())


def parse_conda_env(stream):
    """Parse conda environment details"""
    try:
        yml_data = yaml.load(stream)
        return yml_data
    except yaml.YAMLError as e:
        raise CondaError('Failed to parse Anaconda environment') from e


def update_conda_env(fname, env_name):
    """Create or update a conda environment"""
    command = f'{get_conda_bin()} env update -n {env_name} -f {fname}'
    print(command)
    out = os.system(command)
    if out != 0:
        raise CondaError('Failed to update conda environment!')


def load_conda_env(env_id, name):
    """Download and update an anaconda environment from server"""
    data = download_conda_env(env_id)
    fname = f'{env_id}.yml'
    env_file = open(fname, 'wb')
    env_file.write(data)
    env_file.close()
    update_conda_env(fname, name)
