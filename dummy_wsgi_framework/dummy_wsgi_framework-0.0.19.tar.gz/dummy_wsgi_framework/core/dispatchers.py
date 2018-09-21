#!/usr/bin/python3
import os
import sys

dummy_wsgi_framework_module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)
from dummy_wsgi_framework.core.routes import (
    get_controller_by_uri_regexp,
)
from dummy_wsgi_framework.core.exceptions import (
    ControllerFileDoesNotExist,
    ControllerFileIsInvalid,
    RouteDoesNotExist,
    ViewDoesNotExist,
    BadTermUsage,
    ExistViewFileIsInvalid
)
from dummy_wsgi_framework.core.controllers import (
    error404,
    redirect
)


def resolve_name_by_python_file_name(file_name, template_of_name='%s'):
    if file_name.endswith('.py'):
        return template_of_name % os.path.basename(file_name)[:-3]
    raise BadTermUsage('Impossible detect name by file_name "%s".' % file_name)


def get_controller_response(environ, start_response, app_config):
    uri = environ.get('REQUEST_URI')
    if not uri.endswith('/'):
        return redirect.get_response(environ, start_response, app_config, uri + '/')
    try:
        controller_file, kwargs = get_controller_by_uri_regexp(uri, app_config)
        if app_config.APP_CONTROLLERS_DIR not in sys.path:
            sys.path.insert(0, app_config.APP_CONTROLLERS_DIR)
        controller_module = __import__(
            resolve_name_by_python_file_name(controller_file)
        )
        if not hasattr(controller_module, 'get_response'):
            raise ControllerFileIsInvalid(
                'Controller method "get_response" is not declared '
                'in controller-file "%s" of application "%s"' % (controller_file, app_config.APP_NAME))
        return controller_module.get_response(environ, start_response, app_config, **kwargs)
    except RouteDoesNotExist:
        return error404.get_response(
            environ, start_response, app_config,
            message='<b>RouteDoesNotExist:</b> %s' % sys.exc_info()[1]
        )
    except ControllerFileDoesNotExist:
        return error404.get_response(
            environ, start_response, app_config,
            message='<b>ControllerFileDoesNotExist:</b> %s' % sys.exc_info()[1]
        )
    except ViewDoesNotExist:
        return error404.get_response(
            environ, start_response, app_config,
            message='<b>ViewDoesNotExist:</b> %s' % sys.exc_info()[1]
        )
    except BadTermUsage:
        return error404.get_response(
            environ, start_response, app_config,
            message='<b>BadTermUsage:</b> %s' % sys.exc_info()[1]
        )
    except ControllerFileIsInvalid:
        return error404.get_response(
            environ, start_response, app_config,
            message='<b>ControllerFileIsInvalid:</b> %s' % sys.exc_info()[1]
        )
    except ExistViewFileIsInvalid:
        return error404.get_response(
            environ, start_response, app_config,
            message='<b>ExistViewFileIsInvalid:</b> %s' % sys.exc_info()[1]
        )
    except:
        raise


def get_view_response(environ, start_response, app_config, view_file_name, **kwargs):
    if environ or kwargs:
        pass  # Lets ignore PyCharm warning about not usage
    try:
        view_path = os.path.join(app_config.APP_VIEWS_DIR, view_file_name)
        with open(view_path, 'rb') as f:
            response_body = f.read()
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return [response_body]
    except FileNotFoundError:
        raise ViewDoesNotExist(
            'Declared view-file "%s" '
            'of application "%s" does not found in directory "%s".' % (
                view_file_name, app_config.APP_NAME, app_config.APP_VIEWS_DIR
            )
        )


def decorate_loaded_view_function_for_response(decorated_load_view_function):
    def load_view_response(environ, start_response, app_config, view_file_name, **kwargs):
        if environ or kwargs:
            pass  # Lets ignore PyCharm warning about not usage
        try:
            view_path = os.path.join(app_config.APP_VIEWS_DIR, view_file_name)
            response_body = decorated_load_view_function(view_path, **kwargs)
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
            return [response_body]
        except FileNotFoundError:
            raise ViewDoesNotExist(
                'Declared view-file "%s" '
                'of application "%s" does not found in directory "%s".' % (
                    view_file_name, app_config.APP_NAME, app_config.APP_VIEWS_DIR
                )
            )

    return load_view_response


@decorate_loaded_view_function_for_response
def load_view(view_path, **kwargs):
    if kwargs:
        pass  # Lets ignore PyCharm warning about not usage
    with open(view_path, 'rb') as f:
        return f.read()
