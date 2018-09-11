# encoding: utf-8

import threading
import logging_helper
from furl import furl
from ssl import SSLSocket
from networkutil.addressing import get_my_addresses

logging = logging_helper.setup_logging()


class Shared(object):

    def __init__(self,
                 request,
                 uri=None):

        self._request = request

        self.client_address = request.client_address

        # Save the request parameters
        self._uri = furl()
        self.request_headers = request.headers
        self.request_uri = uri if uri is not None else u'://{host}{path}'.format(host=self.request_headers[u'Host'],
                                                                                 path=request.path)

    # Properties
    @property
    def _request_address(self):
        return self.request_uri.host

    @property
    def _addressed_to_self(self):
        return self._request_address in get_my_addresses()
        # TODO: Add ability to configure & check server aliases

    @property
    def request_uri(self):
        return self._uri

    @request_uri.setter
    def request_uri(self, value):

        self._uri = furl(value)

        # Ensure a scheme is set!
        if not self._uri.scheme:
            self._uri.scheme = u'https' if isinstance(self._request.connection, SSLSocket) else u'http'

        logging_helper.LogLines(self._uri.asdict(),
                                level=logging_helper.DEBUG)

    @property
    def thread(self):
        thread = threading.currentThread().name
        return thread if thread else u'?'

    # Log message formatters
    def prefix_message(self,
                       msg):
        return u'{proto} {type} [{port}] ({thread}): {msg}'.format(proto=self.request_uri.scheme.upper(),
                                                                   type=self._request.command.upper(),
                                                                   port=self._request.server.port,
                                                                   thread=self.thread,
                                                                   msg=msg)

    def _get_debug_separator(self,
                             section):
        return self.prefix_message(u'=========================== '
                                   u'{section} '
                                   u'==========================='.format(section=section))

    # Error processing
    def _log_error(self,
                   err,
                   log_msg=u'Something went wrong',
                   exception=True):

        # Log the error
        logging.error(self.prefix_message(u'{msg}: {err}'.format(msg=log_msg,
                                                                 err=err)))

        if exception:
            logging.exception(self.prefix_message(err))
