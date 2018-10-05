"""
ErrorFeed Python Client
===========================
Use this client to integrate ErrorFeed (www.errorfeed.com) into your Python projects.

>>> import ErrorFeed
>>> errorfeed_client = ErrorFeed.ErrorFeedClient(
...     api_token='-- YOUR API TOKEN --',
...     environment='development-experiment', tags=['documentation-test'])
>>> print errorfeed_client
<ErrorFeed.ErrorFeedClient object at 0x10bcfbb90>
>>> try:
...     oops = 1 / 0
... except:
...     errorfeed_client.handle_exception()
...

That's all it takes. The information about the exception, along with platform and machine information, is gathered
up and sent to ErrorFeed.

For WSGI applications, you can use the WSGI Middleware included with this project:

>>> app = ErrorFeedMiddleware(app, errorfeed_client)

Compatibility
=============
This ErrorFeed Python Client is compatible with Python 2.7 and 3.x and ErrorFeed API v1.

License
=======
Copyright 2015-2018 ErrorFeed. All Rights Reserved.

This software is licensed under the Apache License, version 2.0.

See LICENSE for full details.

Getting Help
============
Email support@errorfeed.com with your questions.
"""
import json
import os
import sys

#
# Some sandboxed environments do not have socket
try:
    import socket
except:
    socket = None

#
# Some sandboxed environments do not have platform
try:
    import platform
except:
    platform = None

#
# Python2/3
try:
    from urllib2 import urlopen, Request, HTTPError
except ImportError:
    from urllib.request import urlopen, Request, HTTPError


class ErrorFeedError(ValueError):
    """
    Exception raised when there is an error communicating with backend or generating request for backend.
    """
    pass


class ErrorFeedClient(object):
    """
    Client to send exceptions to ErrorFeed. See in particular the handle_exception method, which can be called
    within an except block. See also the send_error method, which at a lower level generates an appropriate payload
    for the ErrorFeed API.
    """
    USER_AGENT = 'ERRORFEED PYTHON CLIENT'

    def __init__(self, api_token, environment, tags=None,
                 endpoint="https://report.errorfeed.com/api/2.0/insert"):
        """

        :param account_token: Your account token, as supplied by ErrorFeed
        :param project_token: Your project token, as supplied by ErrorFeed
        :param environment: The environment of the project (eg, "production", "devel", etc)
        :param tags: Any tags you want associated with *all* errors sent using this client.
        :param endpoint: API endpoint. Defaults to ErrorFeed backend.
        """
        self.api_token = api_token
        self.endpoint = endpoint
        self.environment = environment
        if tags:
            assert isinstance(tags, list) or isinstance(tags, tuple), 'Tags must be a sequence. It is %r' % (tags,)
            self.tags = tags
        else:
            self.tags = []

    @staticmethod
    def _serialize_object(obj):
        """
        When the state of an exception includes something that we can't pickle, show something useful instead.
        """
        try:
            return repr(obj)
        except:
            return '<Cannot Be Serialized>'

    def handle_exception(self, exc_info=None, context=None, tags=None, return_feedback_urls=False,
                         dry_run=False):
        """
        Call this method from within a try/except clause to generate a call to ErrorFeed.

        :param exc_info: Return value of sys.exc_info(). If you pass None, handle_exception will call sys.exc_info() itself
        :param context: Dictionary of state information associated with the error. This could be form data, cookie data, whatnot. NOTE: sys and machine are added to this dictionary if they are not already included.
        :param tags: Any string tags you want associated with the exception report.
        :param return_feedback_urls: If True, ErrorFeed will return feedback URLs you can present to the user for extra debugging information.
        :param dry_run: If True, method will not actively send in error information to API. Instead, it will return a request object and payload. Used in unittests.

        """
        if not exc_info:
            exc_info = sys.exc_info()
        if exc_info is None:
            raise ErrorFeedError("handle_exception called outside of exception handler")

        (etype, value, tb) = exc_info
        try:
            msg = value.args[0]
        except:
            msg = repr(value)

        if tags is None:
            tags = []

        if not isinstance(tags, list):
            tags = [tags]

        limit = None

        new_tb = []
        n = 0

        while tb is not None and (limit is None or n < limit):
            f = tb.tb_frame
            lineno = tb.tb_lineno
            co = f.f_code
            filename = co.co_filename
            name = co.co_name
            tb = tb.tb_next
            n = n + 1

            new_tb.append({'line': lineno, 'file': filename, 'method': name})

        if context is None:
            context = {}

        if 'sys' not in context:
            try:
                context['sys'] = self._get_sys_info()
            except Exception as e:
                context['sys'] = '<Unable to get sys: %r>' % e
        if 'machine' not in context:
            try:
                context['machine'] = self._get_machine_info()
            except Exception as e:
                context['machine'] = '<Unable to get machine: %e>' % e

        # The joy of Unicode
        if sys.version_info.major > 2:
            error_type = str(etype.__name__)
            error_message = str(value)
        else:
            # noinspection PyUnresolvedReferences
            error_type = unicode(etype.__name__)
            # noinspection PyUnresolvedReferences
            error_message = unicode(value)

        send_error_args = dict(error=error_type,
                               message=error_message,
                               traceback=new_tb,
                               environment=self.environment,
                               context=context,
                               tags=self.tags + tags,
                               return_feedback_urls=return_feedback_urls)
        if dry_run:
            return send_error_args
        else:
            return self.send_error(**send_error_args)

    def _get_sys_info(self):
        sys_info = {
            'version': sys.version,
            'version_info': sys.version_info,
            'path': sys.path,
            'platform': sys.platform
        }
        return sys_info

    def _get_machine_info(self):
        machine = {}
        if socket:
            try:
                machine['hostname'] = socket.gethostname()
            except Exception as e:
                machine['hostname'] = '<Could not determine: %r>' % (e,)
        else:
            machine['hostname'] = "<socket module not available>"
        machine['environ'] = dict(os.environ)
        if platform:
            machine['platform'] = platform.uname()
            machine['node'] = platform.node()
            machine['libc_ver'] = platform.libc_ver()
            machine['version'] = platform.version()
            machine['dist'] = platform.dist()
        return machine

    def send_error(self, error, message, traceback, environment, context, tags=None,
                   return_feedback_urls=False):
        """
        Sends error payload to ErrorFeed API, returning a parsed JSON response. (Parsed as in,
        converted into Python dict/list objects)

        :param error: Type of error generated. (Eg, "TypeError")
        :param message: Message of error generated (Eg, "cannot concatenate 'str' and 'int' objects")
        :param traceback: List of dictionaries. Each dictionary should contain, "line", "method", and "module" keys.
        :param environment: Environment the error occurred in (eg, "devel")_
        :param context: State of the application when the error happened. Could contain form data, cookies, etc.
        :param tags: Arbitrary tags you want associated with the error. list.
        :param return_feedback_urls: If True, return payload will offer URLs to send users to collect additional feedback for debugging.
        :return: Parsed return value from ErrorFeed API
        """

        (request, payload) = self._generate_request(environment, error, message, return_feedback_urls,
                                                    context, tags, traceback)

        try:
            response = urlopen(request)
        except HTTPError as e:
            if e.code == 400:
                raise ErrorFeedError(e.read())
            else:
                raise

        if sys.version_info.major > 2:
            text_response = response.read().decode(response.headers.get_content_charset() or 'utf8')
        else:
            encoding = response.headers.get('content-type', '').split('charset=')[-1].strip()
            if encoding:
                text_response = response.read().decode('utf8', 'replace')
            else:
                text_response = response.read().decode(encoding)

        return json.loads(text_response)

    def _generate_request(self, environment, error, message, return_feedback_urls, context, tags, traceback):
        file = None
        line = None
        if traceback:
            file = traceback[0]['file']
            line = traceback[0]['line']

        payload = json.dumps(dict(
            api_token=self.api_token,
            return_feedback_urls=return_feedback_urls,
            exceptions=[dict(
                error=error,
                message=message,

                language='python',
                runtime=sys.version,

                file=file,
                line=line,
                machine=context.get('machine', {}).get('node', None),

                environment=environment,
                traceback=traceback,
                context=context,
                tags=tags or []
            )]
        ), default=self._serialize_object)
        request = Request(self.endpoint, data=payload.encode('utf8'), headers={
            'Accept-Charset': 'utf-8',
            "Content-Type": "application/x-www-form-urlencoded ; charset=UTF-8",
            'User-Agent': self.USER_AGENT})
        return (request, payload)


class ErrorFeedMiddleware(object):
    """
    ErrorFeed middleware client. As easy as this:

    >>> client = ErrorFeedClient(...)
    >>> app = ErrorFeedMiddleware(app, client)
    """
    def __init__(self, app, client):
        """
        :param app: WSGI application object
        :param client: Instance of ErrorFeed
        """
        self.app = app

        self.client = client

    def __call__(self, environ, start_response):
        result = None

        try:
            result = self.app(environ, start_response)
        except Exception:
            self.client.handle_exception(context={'wsgi_environ': environ})
            raise

        try:
            if result is not None:
                for i in result:
                    yield i
        except Exception:
            self.client.handle_exception(context={'wsgi_environ': environ})
            raise

        finally:
            if hasattr(result, 'close'):
                result.close()
