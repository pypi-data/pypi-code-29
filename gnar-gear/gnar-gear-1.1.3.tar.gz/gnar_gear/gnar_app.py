import fnmatch
import inspect
import logging
import os
import re
import requests
import sys
from datetime import timedelta
from importlib import import_module
from importlib.util import module_from_spec, spec_from_file_location
from pkgutil import get_loader
from threading import Timer
from traceback import format_exc

import boto3
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError, VerifyMismatchError
from bjoern import run
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity
from postgres import Postgres
from json import dumps

from .constants import LOG_FORMAT, LOG_FORMAT_MSEC, PASSWORD_CANNOT_BE_EMPTY, TOKEN_HAS_EXPIRED

log = logging.getLogger(__name__)


class Peer:

    def __init__(self, gnar_app, service):
        self.gnar_app = gnar_app
        env_var = re.sub(r'[^A-Z0-9]', '_', '{}_SERVICE_PORT'.format(service.upper()))
        service_port = os.getenv(env_var) if self.gnar_app.production else self.gnar_app.env(env_var)
        if not service_port:
            raise ValueError('Environment variable "{}" does not exist.'.format(env_var))
        self.root = 'http://{}/'.format(re.sub(r'.+://', '', service_port))

    def parse(self, path, **kwargs):
        url = '{}{}'.format(self.root, path)
        if 'auto_auth' in kwargs:
            kwargs = dict(kwargs)
            identity = get_jwt_identity()
            if identity:
                kwargs.setdefault('headers', {})
                bearer = 'Bearer {}'.format(create_access_token(identity=identity))
                kwargs['headers'] = {'Authorization': bearer, **kwargs['headers']}
            del kwargs['auto_auth']
        return url, kwargs

    def request(self, method, path, **kwargs):
        url, kwargs = self.parse(path, **kwargs)
        return requests.request(method, url, **kwargs)

    def head(self, path, **kwargs):
        url, kwargs = self.parse(path, **kwargs)
        return requests.head(url, **kwargs)

    def get(self, path, params=None, **kwargs):
        url, kwargs = self.parse(path, **kwargs)
        return requests.get(url, params, **kwargs)

    def post(self, path, data=None, json=None, **kwargs):
        url, kwargs = self.parse(path, **kwargs)
        return requests.post(url, data, json, **kwargs)

    def put(self, path, data=None, **kwargs):
        url, kwargs = self.parse(path, **kwargs)
        return requests.put(url, data, **kwargs)

    def patch(self, path, data=None, **kwargs):
        url, kwargs = self.parse(path, **kwargs)
        return requests.patch(url, data, **kwargs)

    def delete(self, path, **kwargs):
        url, kwargs = self.parse(path, **kwargs)
        return requests.delete(url, **kwargs)


class PerpetualTimer:

    thread = None

    def __init__(self, interval_seconds, callback, args):
        self.interval_seconds = interval_seconds
        self.callback = callback
        self.args = args
        self.handle_function()

    def handle_function(self):
        self.callback(*self.args)
        self.thread = Timer(self.interval_seconds, self.handle_function)
        self.thread.daemon = True
        self.thread.start()


class GnarApp:

    has_error = False
    queue_urls = {}
    sqs_client = None

    def __init__(
            self,
            name,
            production,
            port,
            env_prefix='GNAR',
            log_level=None,
            blueprint_modules=None,
            no_db=False,
            no_jwt=False,
            sqs=None):

        self.name = name
        self.display_name = name.title().replace('_', '')
        self.production = production
        self.port = port
        self.env_prefix = env_prefix
        self.log_level = log_level
        self.blueprint_modules = blueprint_modules
        self.no_db = no_db
        self.no_jwt = no_jwt
        self.sqs = sqs
        self.external = requests

        if self.production or os.environ.get('WERKZEUG_RUN_MAIN'):
            self.configure_logger()

    def env(self, name, default=None):
        env_var = '{}_{}'.format(self.env_prefix, name).upper()
        value = os.getenv(env_var, default)
        if value is None:
            raise ValueError('Environment variable "{}" does not exist.'.format(env_var))
        return value

    def check_password_hash(self, hash, password):
        try:
            return self.argon2.verify(hash, password)
        except (VerificationError, VerifyMismatchError):
            return False

    def generate_password_hash(self, password):
        if not password:
            raise ValueError(PASSWORD_CANNOT_BE_EMPTY)
        return self.argon2.hash(password)

    def get_ses_client(self):
        return boto3.client(
            'ses',
            region_name=self.env('SES_REGION_NAME'),
            aws_access_key_id=self.env('SES_ACCESS_KEY_ID'),
            aws_secret_access_key=self.env('SES_SECRET_ACCESS_KEY'))

    def get_sqs_client(self):
        if not self.sqs_client:
            self.sqs_client = boto3.client(
                'sqs',
                region_name=self.env('SQS_REGION_NAME'),
                aws_access_key_id=self.env('SQS_ACCESS_KEY_ID'),
                aws_secret_access_key=self.env('SQS_SECRET_ACCESS_KEY'))
        return self.sqs_client

    def get_sqs_queue_url(self, queue_name):
        queue_url = self.queue_urls.get(queue_name)
        if not queue_url:
            sqs_client = self.get_sqs_client()
            queue_url = sqs_client.get_queue_url(QueueName='gnar-queue')['QueueUrl']
            self.queue_urls[queue_name] = queue_url
        return queue_url

    def peer(self, service):
        return Peer(self, service)

    def send_sqs_message(self,
                         queue_name,
                         message_body,
                         delay_seconds=None,
                         message_attributes=None,
                         message_deduplication_id=None,
                         message_group_id=None):
        sqs_client = self.get_sqs_client()
        kwargs = {k: v for k, v in {'DelaySeconds': delay_seconds,
                                    'MessageAttributes': message_attributes,
                                    'MessageDeduplicationId': message_deduplication_id,
                                    'MessageGroupId': message_group_id}.items() if v is not None}

        return sqs_client.send_message(QueueUrl=self.get_sqs_queue_url(queue_name), MessageBody=message_body, **kwargs)

    def receive_sqs_messages(self, queue_url, callback, kwargs):
        sqs_client = self.get_sqs_client()
        while True:
            messages = sqs_client.receive_message(QueueUrl=queue_url, **kwargs)
            if 'Messages' not in messages:
                break
            for message in messages['Messages']:
                if callback(message) is not False:
                    sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])

    def preconfig(self):
        pass

    def configure_flask(self):
        self.flask = Flask(self.name)
        self.flask.env = 'production' if self.production else 'development'

    def configure_logger(self):
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(self.env('LOG_FORMAT', LOG_FORMAT))
        formatter.default_msec_format = self.env('LOG_FORMAT_MSEC', LOG_FORMAT_MSEC)
        ch.setFormatter(formatter)
        root = logging.getLogger()
        root.addHandler(ch)
        logging.getLogger('boto').setLevel(logging.WARNING)
        project_env = '{}_LOG_LEVEL'.format(self.name.upper())
        default_log_level = self.env('LOG_LEVEL', 'INFO')
        log_level = self.log_level or self.env(project_env, default_log_level)
        root.setLevel(log_level)

        log.info('Logging at {}'.format(log_level))

    def configure_argon2(self):
        kwarg_list = ['time_cost', 'memory_cost', 'parallelism', 'hash_len', 'salt_len', 'encoding']
        kwargs = {key: self.env('{}_{}'.format('argon2', key), '') for key in kwarg_list}
        kwargs = {key: val for key, val in kwargs.items() if val}
        self.argon2 = PasswordHasher(**kwargs)
        log.info('Argon2 PasswordHasher instantiated with {}'.format(kwargs if kwargs else 'defaults'))

    def configure_database(self):
        if not self.no_db:
            endpoint = self.env('PG_ENDPOINT')
            database = self.env('PG_DATABASE')
            username = self.env('PG_USERNAME')
            password = self.env('PG_PASSWORD')
            self.db = Postgres('host={} dbname={} user={} password={}'.format(endpoint, database, username, password))
            log.info('Database connected at {}/{}@{}'.format(endpoint, database, username))

    def attach_instance(self):
        main = import_module('{}.app.main'.format(self.name))
        main.app = self

    def configure_blueprints(self):
        app_root = os.path.dirname(get_loader(self.name).path)

        def get_module(module_path):
            module_name = '{}{}'.format(self.name, re.sub(r'[\/]', '.', module_path[len(app_root):-3]))
            spec = spec_from_file_location(module_name, module_path)
            module = module_from_spec(spec)
            return module_name, spec, module

        def register_exception_files(e):
            filename = getattr(e, 'filename', '')
            if filename:
                module_name, _, module = get_module(filename)
                if module_name not in sys.modules:  # pragma: no cover
                    sys.modules[module_name] = module
            for frame in inspect.trace():
                if frame.filename.startswith(app_root):
                    module_name, _, module = get_module(frame.filename)
                    if module_name not in sys.modules:
                        sys.modules[module_name] = module

        if self.blueprint_modules:
            blueprint_modules = \
                self.blueprint_modules if isinstance(self.blueprint_modules, list) else [self.blueprint_modules]
            for blueprint_module in blueprint_modules:
                template = '{}.app.{}' if '.' in blueprint_module else '{}.app.{}.apis'
                module_name = template.format(self.name, blueprint_module)
                if self.production:
                    blueprint = import_module(module_name).blueprint
                else:
                    try:
                        blueprint = import_module(module_name).blueprint
                    except Exception as e:
                        module_path = '{}.py'.format(os.path.join(app_root, *module_name.split('.')[1:]))
                        module_name, spec, module = get_module(module_path)
                        sys.modules[module_name] = module
                        register_exception_files(e)
                        log.error(format_exc())
                        self.has_error = True
                        continue
                self.flask.register_blueprint(blueprint)
                log.info('Listening on {}'.format(blueprint.url_prefix))
        else:
            for root, dirnames, filenames in os.walk(os.path.join(app_root, 'app')):
                for filename in fnmatch.filter(filenames, '*.py'):
                    module_name, spec, module = get_module(os.path.join(root, filename))
                    if self.production:
                        spec.loader.exec_module(module)
                    else:
                        try:
                            spec.loader.exec_module(module)
                        except Exception as e:
                            sys.modules[module_name] = module
                            register_exception_files(e)
                            log.error(format_exc())
                            self.has_error = True
                            continue
                    if hasattr(module, 'blueprint'):
                        self.flask.register_blueprint(module.blueprint)
                        log.info('Listening on {}'.format(module.blueprint.url_prefix))

    def configure_errorhandler(self):
        @self.flask.errorhandler(Exception)
        def error_handler(exp):
            error = '{} API Error'.format(self.display_name)
            traceback = '{}:\n{}'.format(error, format_exc())
            log.error(traceback)
            return jsonify({'error': error, 'traceback': traceback})

    def configure_jwt(self):
        if not self.no_jwt:
            jwt_secret_key = self.env('JWT_SECRET_KEY')
            self.flask.config['JWT_SECRET_KEY'] = jwt_secret_key

            exp_minutes = self.env('JWT_ACCESS_TOKEN_EXPIRES_MINUTES', '')
            exp_minutes = int(exp_minutes) if exp_minutes.isdigit() else 15
            self.flask.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=exp_minutes)

            self.jwt = JWTManager(self.flask)

            def error_message(msg):
                return jsonify({'error': msg})

            @self.jwt.expired_token_loader
            def expired_token_callback():
                return error_message(TOKEN_HAS_EXPIRED)

            @self.jwt.invalid_token_loader
            def invalid_token_callback(msg):
                return error_message(msg)

            @self.jwt.unauthorized_loader
            def unauthorized_callback(msg):
                return error_message(msg)

            log.info('JWT configured, tokens expire in {} minutes'.format(exp_minutes))

    def configure_sqs_polls(self):
        if self.sqs:
            sqs_queues = self.sqs if isinstance(self.sqs, list) else [self.sqs]
            for sqs_queue in sqs_queues:
                for key in ['queue_name', 'callback']:
                    if key not in sqs_queue:
                        raise ValueError('"{}" missing in {}'.format(key, dumps(sqs_queue)))
                queue_url = self.get_sqs_queue_url(sqs_queue['queue_name'])
                callback = sqs_queue['callback']

                def g(key, default=None): return sqs_queue.get(key, default)
                interval_seconds = g('interval_seconds', 60)
                kwargs = {k: v for k, v in {'AttributeNames': g('attribute_names'),
                                            'MaxNumberOfMessages': g('max_number_of_messages'),
                                            'MessageAttributeNames': g('message_attribute_names'),
                                            'ReceiveRequestAttemptId': g('receive_request_attempt_id'),
                                            'VisibilityTimeout': g('visibility_timeout'),
                                            'WaitTimeSeconds': g('wait_time_seconds')}.items()
                          if v is not None}

                log.info('Polling SQS queue {} every {} seconds'.format(sqs_queue['queue_name'], interval_seconds))
                PerpetualTimer(interval_seconds, self.receive_sqs_messages, [queue_url, callback, kwargs])

    def configure_after_request(self):
        @self.flask.after_request
        def after_request(response):
            if not self.production:
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT'
                response.headers['Access-Control-Allow-Headers'] = 'Authorization'
                response.headers['Access-Control-Expose-Headers'] = 'Authorization'
            if not self.no_jwt:
                identity = get_jwt_identity()
                if identity:
                    response.headers['Authorization'] = 'Bearer {}'.format(create_access_token(identity=identity))
            return response

    def postconfig(self):
        pass

    def run(self):

        if self.production or os.environ.get('WERKZEUG_RUN_MAIN'):

            self.preconfig()

        self.configure_flask()

        if self.production or os.environ.get('WERKZEUG_RUN_MAIN'):

            self.configure_argon2()

            self.configure_database()

            self.attach_instance()

            self.configure_blueprints()

            self.configure_errorhandler()

            self.configure_jwt()

            self.configure_after_request()

            self.configure_sqs_polls()

            self.postconfig()

            if not self.has_error:
                log.info('Gnar-{}{} is up'.format(self.display_name, '' if self.production else ' development server'))

        if self.production:
            run(self.flask, '', self.port)
        else:
            self.flask.run('', self.port, debug=True)
