# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# python imports
import logging

# 3rd. libraries imports
from appconf import AppConf

# django imports
from django.conf import settings  # noqa

logger = logging.getLogger(__name__)


class AuthUuidConfig(AppConf):
    # JWT Config
    JWT_VERIFY_EXPIRATION = False
    JWT_VERIFY = True
    JWT_LEEWAY = 0
    JWT_AUDIENCE = None
    JWT_ISSUER = None
    JWT_ALGORITHM = 'HS256'
    JWT_AUTH = {
        'JWT_DECODE_HANDLER': 'auth_uuid.helper_jwt.jwt_decode_handler',
        'JWT_PAYLOAD_GET_USERNAME_HANDLER': 'auth_uuid.helper_jwt..jwt_get_username_from_payload_handler'
    }

    LOGGER_NAME = 'simple_user'

    class Meta:
        prefix = 'auth'
        required = ['JWT_SECRET_KEY', 'URL_VALIDATE_USER_UUID']
