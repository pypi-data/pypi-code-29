import configparser
import os

from manoc.utils.common import config_filename


def get_config():
    config = configparser.ConfigParser()
    config.read(config_filename)
    return config


def save_config(base_url, client_id, client_secret):
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)

    config = configparser.ConfigParser()
    config.read(config_filename)

    if 'common' not in config.sections():
        config['common'] = {}
    config['common']['current_env'] = base_url

    config[base_url] = {}
    config[base_url]['client_id'] = client_id
    config[base_url]['client_secret'] = client_secret

    with open(config_filename, 'w') as configfile:
        config.write(configfile)


def save_tenant(base_url, tenant):
    config = configparser.ConfigParser()
    config.read(config_filename)

    config[base_url]['tenant'] = tenant

    with open(config_filename, 'w') as configfile:
        config.write(configfile)


def save_token(ctx, base_url, access_token, expires_at):
    config = configparser.ConfigParser()
    config.read(config_filename)

    config[base_url]['access_token'] = str(access_token)
    config[base_url]['expires_at'] = str(expires_at)

    with open(config_filename, 'w') as configfile:
        config.write(configfile)


def current_env():
    config = configparser.ConfigParser()
    config.read(config_filename)
    if 'common' in config.sections():
        if 'current_env' in config['common']:
            return config['common']['current_env']


def list_env():
    config = configparser.ConfigParser()
    config.read(config_filename)

    envs = []
    for section in config.sections():
        if section != 'common':
            envs.append(section)
    return envs

