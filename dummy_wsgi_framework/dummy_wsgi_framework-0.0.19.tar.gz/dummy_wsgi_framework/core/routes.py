#!/usr/bin/python3
import sys
import os
import re
from dummy_wsgi_framework.core.exceptions import (
    ControllerFileDoesNotExist,
    RouteDoesNotExist,
    ExistRouteIsInvalid
)

DEFAULT = '^/$'
ERROR_404 = '^/error_404/$'

base_routes_of_uri_regexps = (
    dict(uri_regexp='^/index/$', controller='index.py'),
    dict(uri_regexp=ERROR_404, controller='error_404.py'),
    dict(uri_regexp=DEFAULT, controller='index.py'),
)


def get_controller_by_uri_regexp(request_uri, app_config):
    try:
        if os.path.exists(os.path.join(app_config.APP_ROOT_DIR, 'routes.py')):
            if app_config.APP_ROOT_DIR not in sys.path:
                sys.path.insert(0, app_config.APP_ROOT_DIR)
            routes_module = __import__("routes")
            if not hasattr(routes_module, 'routes_of_uri_regexps'):
                raise RouteDoesNotExist(
                    'Variable "routes_of_uri_regexps" is not declared '
                    'in file "routes.py" of application "%s"' % app_config.APP_NAME.upper())
            uri_routes_regexps = routes_module.routes_of_uri_regexps
        else:
            uri_routes_regexps = base_routes_of_uri_regexps
    except ImportError:
        raise
    controller = None
    params = dict()
    for uri_route_regexp in uri_routes_regexps:
        p = re.compile(uri_route_regexp.get('uri_regexp'))
        was_found = p.findall(request_uri)
        if isinstance(was_found, list) and len(was_found) == 1:
            if isinstance(was_found[0], str):
                controller = uri_route_regexp.get('controller')
            elif isinstance(was_found[0], tuple):
                controller = uri_route_regexp.get('controller')
                if len(was_found[0]) > 1:
                    for param in was_found[0][1:]:
                        k, v = param.split('=', 1)
                        params[k] = v
            else:
                raise ExistRouteIsInvalid('Exist route does not valid, see route regexp examples')
            break
    if controller is None:
        raise RouteDoesNotExist(
            'All routes of application "%s" are not valid for this uri "%s"' % (
                app_config.APP_NAME, request_uri)
        )
    if not os.path.exists(os.path.join(app_config.APP_CONTROLLERS_DIR, controller)):
        raise ControllerFileDoesNotExist(
            'Declared controller-file "%s" '
            'of application "%s" does not found in directory "%s".' % (
                controller, app_config.APP_NAME, app_config.APP_CONTROLLERS_DIR
            )
        )
    return controller, params
