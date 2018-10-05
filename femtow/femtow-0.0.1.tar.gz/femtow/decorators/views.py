import inspect
import traceback

import venusian
from webob import Response

from femtow import exceptions
from femtow.decorators import renderers, routes


def view(*, renderer=renderers.json_renderer):
    def decorator(view_func):
        def callback(scanner, name, ob):
            params = [
                scanner.app.view_params[p]
                for p in inspect.signature(view_func).parameters
            ]

            def wrapper():
                response = Response()
                evaluated_params = [p(scanner.app) for p in params]
                view_results = view_func(*evaluated_params)
                if isinstance(view_results, Response):
                    return view_results
                renderer(view_results, response)
                return response

            scanner.app.view_registry[view_func] = wrapper

        venusian.attach(view_func, callback, 'femtow-views')
        return view_func

    return decorator


def view_param(view_func):
    def callback(scanner, name, ob):
        scanner.app.view_params[name] = view_func

    venusian.attach(view_func, callback, 'femtow-view-params')
    return view_func


@routes.exception_route(exception=exceptions.HttpNotFound)
@view(renderer=renderers.http_exception_renderer(status=404))
def http_not_found():
    return {'tb': [], 'msg': 'HTTP Not Found'}


@routes.exception_route(exception=Exception)
@view(renderer=renderers.http_exception_renderer(status=500))
def http_internal_server_error(request):
    tb = traceback.format_tb(request.exception.__traceback__)
    return {'tb': tb, 'msg': 'Internal Server Error'}

