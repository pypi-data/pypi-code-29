# -*- coding: utf-8 -*-
# Copyright 2018 NS Solutions Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function, absolute_import, with_statement

import json
import logging
import os.path

import kamonohashi

config_file_path = os.path.expanduser(os.path.join('~', '.kqi', 'config.json'))


def read_file():
    """Read kamonohashi config file. If not exists or invalid, raise Exception.
    :rtype: dict
    """
    require_login = "Log into KAMONOHASHI first to use 'account login' command."

    if os.path.exists(config_file_path):
        logging.info('open config file %s', config_file_path)
        with open(config_file_path) as f:
            logging.info('begin io %s', config_file_path)
            config_file = json.load(f)
            logging.info('end io %s', config_file_path)
        if not {'server', 'token'} <= set(config_file.keys()):
            raise Exception('Invalid configuration file {config_file_path}. {require_login}'
                            .format(config_file_path=config_file_path, require_login=require_login))
        return config_file

    raise Exception('No configuration file {config_file_path}. {require_login}'
                    .format(config_file_path=config_file_path, require_login=require_login))


def try_read_file():
    """Read kamonohashi config file. If not exists, return an empty dictionary.
    :rtype: dict
    """
    try:
        logging.info('open config file %s', config_file_path)
        with open(config_file_path) as f:
            logging.info('begin io %s', config_file_path)
            config_file = json.load(f)
            logging.info('end io %s', config_file_path)
            return config_file
    except (OSError, IOError) as error:
        logging.info('try_read error %s', error)
        return {}


def update_config_file(**kwargs):
    """Update kamonohashi config file."""
    config_file = try_read_file()
    config_file.update(kwargs)
    logging.info('open config file %s', config_file_path)
    with open(config_file_path, 'w') as f:
        logging.info('begin io %s', config_file_path)
        json.dump(config_file, f, indent=4)
        logging.info('end io %s', config_file_path)


def get_api_client():
    """Get kamonohashi.ApiClient.
    :rtype: kamonohashi.ApiClient
    """
    config_file = read_file()
    api_client = create_api_client_base(config_file)
    api_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
    api_client.configuration.api_key['Authorization'] = config_file['token']
    api_client.configuration.host = config_file['server']
    return api_client


def get_api_client_noauth():
    """Get kamonohashi.ApiClient without Authorization.
    :rtype: kamonohashi.ApiClient
    """
    config_file = try_read_file()
    api_client = create_api_client_base(config_file)
    return api_client


def create_api_client_base(config_file):
    """Create kamonohashi.ApiClient and configure base part from config file.
    :param dict config_file:
    :rtype: kamonohashi.ApiClient
    """
    api_client = kamonohashi.ApiClient()
    api_client.rest_client.pool_manager.connection_pool_kw['timeout'] = config_file.get('timeout', 30)
    api_client.rest_client.pool_manager.connection_pool_kw['retries'] = False
    return api_client
