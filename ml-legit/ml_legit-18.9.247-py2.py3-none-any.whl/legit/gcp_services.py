# -*- coding: utf8 -*-
try:
    # noinspection PyPep8Naming
    import ConfigParser as configparser
except ImportError:
    # noinspection PyUnresolvedReferences
    import configparser

import json

import os
import requests
from requests.adapters import HTTPAdapter
import warnings
from missinglink.core.exceptions import NonRetryException


warnings.filterwarnings("ignore", "Your application has authenticated using end user credentials")


class GooglePackagesMissing(NonRetryException):
    pass


class GoogleAuthError(NonRetryException):
    pass


class GCPServices(object):
    CLOUD_SDK_CONFIG_DIR = 'CLOUDSDK_CONFIG'
    _CONFIG_DIRECTORY = 'gcloud'
    _CREDENTIALS_FILENAME = 'application_default_credentials.json'
    _WINDOWS_CONFIG_ROOT_ENV_VAR = 'APPDATA'
    _AUTHORIZED_USER_TYPE = 'authorized_user'
    _SERVICE_ACCOUNT_TYPE = 'service_account'
    _DEFAULT_CONFIG_FILE = 'config_default'
    _DEFAULT_CONFIG_PATH = 'configurations'
    _VALID_TYPES = (_AUTHORIZED_USER_TYPE, _SERVICE_ACCOUNT_TYPE)

    def __init__(self):
        pass

    @classmethod
    def _setup_session(cls, session):
        a = HTTPAdapter(pool_maxsize=50)
        b = HTTPAdapter(pool_maxsize=50)
        session.mount('http://', a)
        session.mount('https://', b)

    @classmethod
    def get_config_path(cls):
        # If the path is explicitly set, return that.
        try:
            return os.environ[cls.CLOUD_SDK_CONFIG_DIR]
        except KeyError:
            pass

        # Non-windows systems store this at ~/.config/gcloud
        if os.name != 'nt':
            return os.path.join(os.path.expanduser('~'), '.config', cls._CONFIG_DIRECTORY)
        # Windows systems store config at %APPDATA%\gcloud
        else:
            try:
                return os.path.join(os.environ[cls._WINDOWS_CONFIG_ROOT_ENV_VAR], cls._CONFIG_DIRECTORY)
            except KeyError:
                # This should never happen unless someone is really
                # messing with things, but we'll cover the case anyway.
                drive = os.environ.get('SystemDrive', 'C:')
                return os.path.join(drive, '\\', cls._CONFIG_DIRECTORY)

    @classmethod
    def get_application_default_credentials_path(cls):
        config_path = cls.get_config_path()
        return os.path.join(config_path, cls._CREDENTIALS_FILENAME)

    @classmethod
    def get_default_config_path(cls):
        config_path = cls.get_config_path()
        return os.path.join(config_path, cls._DEFAULT_CONFIG_PATH, cls._DEFAULT_CONFIG_FILE)

    @classmethod
    def get_default_project_id(cls):
        def _get_project_id_from_path():
            default_config = cls.get_default_config_path()
            config = configparser.ConfigParser()
            config.read(default_config)
            try:
                return config.get('core', 'project')
            except (configparser.NoOptionError, configparser.NoSectionError):
                return None

        def _get_project_id_from_gae():
            try:
                from google.appengine.api import app_identity
            except ImportError:
                app_identity = None

            if app_identity is None:
                return None

            return app_identity.get_application_id()

        for project_id_method in (_get_project_id_from_gae, _get_project_id_from_path):
            project_id = project_id_method()
            if project_id is None:
                continue

            return project_id

    @classmethod
    def _get_gcloud_auth_session(cls, credentials=None):
        try:
            import google.auth.transport.requests
        except ImportError:
            raise GooglePackagesMissing()

        if credentials is None:
            credentials = cls.gcp_default_credentials()

            if credentials is None:
                raise GoogleAuthError()

        # noinspection PyUnresolvedReferences
        auth_method_session = google.auth.transport.requests.AuthorizedSession(credentials)
        cls._setup_session(auth_method_session)

        return auth_method_session, credentials

    @classmethod
    def gcp_default_credentials(cls):
        try:
            import google.auth.exceptions
            from google.oauth2 import service_account, credentials as google_credentials
        except ImportError:
            raise GooglePackagesMissing()

        def _get_gae_credentials():
            """Gets Google App Engine App Identity credentials and project ID."""
            from google.auth import app_engine

            try:
                gae_credentials = app_engine.Credentials()
                return gae_credentials
            except EnvironmentError:
                return None

        def _get_credentials_from_files():
            filename = cls.get_application_default_credentials_path()
            try:
                with open(filename) as file_obj:
                    info = json.load(file_obj)
                    credential_type = info.get('type')
            except (IOError, OSError):
                return None

            if credential_type == cls._AUTHORIZED_USER_TYPE:
                file_credentials = google_credentials.Credentials.from_authorized_user_info(info)
            elif credential_type == cls._SERVICE_ACCOUNT_TYPE:
                file_credentials = service_account.Credentials.from_service_account_info(info)
            else:
                # noinspection PyUnresolvedReferences
                raise google.auth.exceptions.DefaultCredentialsError(
                    'The file {file} does not have a valid type. '
                    'Type is {type}, expected one of {valid_types}.'.format(
                        file=filename, type=credential_type, valid_types=cls._VALID_TYPES))

            return file_credentials

        for credentials_method in (_get_gae_credentials, _get_credentials_from_files):
            credentials = credentials_method()

            if credentials is None:
                continue

            return credentials

    @classmethod
    def get_auth_session(cls, auth_method, credentials):
        if auth_method == 'gcloud':
            return cls._get_gcloud_auth_session(credentials)[0]

        thread_session = requests.Session()
        cls._setup_session(thread_session)

        return thread_session

    @classmethod
    def gcs_service(cls, credentials=None):
        try:
            from google.cloud import storage
        except ImportError:
            raise GooglePackagesMissing()

        auth_method_session, credentials = cls._get_gcloud_auth_session(credentials)

        params = {
            '_http': auth_method_session
        }

        if credentials is not None:
            params['credentials'] = credentials

        project = cls.get_default_project_id()
        if project is not None:
            params['project'] = project

        return storage.Client(**params)
