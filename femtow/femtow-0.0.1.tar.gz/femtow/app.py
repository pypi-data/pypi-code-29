import configparser
import inspect
import logging

import backlash
import os
import venusian
from routes import Mapper
from webob import Request

from femtow import exceptions
from femtow.decorators import views, view_params

logger = logging.getLogger(__file__)


class Femtow:
    def __init__(self, config, working_dir=None):
        self.config = config
        self.current_request = None
        self.exception_view_registry = {}
        self.route_mapper = Mapper()
        self.view_params = {}
        self.view_registry = {}

        self._scanner = venusian.Scanner(app=self)
        self._working_dir = working_dir

    def __call__(self, environ, start_response):
        self.current_request = request = Request(environ)
        try:
            response = self._build_response(request, environ)
        except Exception as e:
            logger.exception(e)
            response = self._build_exception_response(request, e)

        return response(environ, start_response)

    @classmethod
    def from_config(cls, filename):
        frame_records = inspect.stack()[1]
        working_dir = '/'.join(frame_records[1].split('/')[0:-1])
        config = configparser.ConfigParser({
            key: value.replace('%', '%%')
            for key, value in os.environ.items()
        })
        with open(f'{working_dir}/{filename}') as f:
            config.read_file(f)

        return cls(config, working_dir)

    def with_debugging(self):
        return backlash.DebuggedApplication(
            self, context_injectors=[self._turbogears_backlash_context]
        )

    def scan(self, package):
        self._scanner.scan(view_params, categories=['femtow-view-params'])
        self._scanner.scan(views, categories=['femtow-views'])
        self._scanner.scan(views, categories=['femtow-routes'])

        self._scanner.scan(package, categories=['femtow-view-params'])
        self._scanner.scan(package, categories=['femtow-views'])
        self._scanner.scan(package, categories=['femtow-routes'])

    def _build_response(self, request, environ):
        match_dict = self.route_mapper.match(request.path, environ)
        if not match_dict:
            raise exceptions.HttpNotFound(
                f'No route for path {request.path} configured.'
            )
        view = match_dict.pop('action')
        request.match_dict = match_dict
        return view()

    def _build_exception_response(self, request, exception):
        request.exception = exception
        try:
            return self.exception_view_registry[exception.__class__]()
        except KeyError:
            raise exception

    @staticmethod
    def _turbogears_backlash_context(environ):
        tgl = environ.get('tg.locals')
        return {'request': getattr(tgl, 'request', None)}
