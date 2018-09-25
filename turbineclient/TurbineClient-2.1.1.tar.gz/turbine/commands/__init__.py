#!/usr/bin/env python
##########################################################################
# $Id: __init__.py 10089 2016-02-29 19:46:07Z aaelbashandy $
# Joshua R. Boverhof, LBNL
# See LICENSE.md for copyright notice!
#
#   $Author: aaelbashandy $
#   $Date: 2016-02-29 11:46:07 -0800 (Mon, 29 Feb 2016) $
#   $Rev: 10089 $
#
###########################################################################
import urllib2,csv,sys,os,ssl,httplib,socket
import json
import optparse
import sys
from ConfigParser import ConfigParser
import logging as _log
import logging.config as _loggingconfig
from turbine.utility import states
from ntlm import HTTPNtlmAuthHandler


_opener = None

def handler_http_error(func):
    """
    """
    log = _log.getLogger('%s.handler_http_error' %(__name__))
    def _exit_on_http_error(*args, **kw):
        try:
            r = func(*args, **kw)
        except urllib2.HTTPError,ex:
            log.error("%s" %ex)
            if getattr(ex, 'read', None):
                log.error("%s" %ex.read())
            sys.exit(1)
        return r
    return _exit_on_http_error


def _print_page(page, out=sys.stdout):
    print >>out, page

def _print_numbered_lines(data, out=sys.stdout):
    for i in xrange(len(data)):
        print >>out, '%d) %s' %(i,data[i])

def _print_as_json(data, out=sys.stdout):
    print >>out, json.dumps(data)

""" Internal methods
"""

def _open_config(filename=None):
    """ _open_config:  Reads the config parser file, initializes logging.
    After this call can use logging.
    """
    if getattr(_open_config, 'cp', None): return _open_config.cache_cp
    if filename is None:
        filename = os.environ.get("TURBINE_CONFIG")

    if filename is None:
        raise RuntimeError, "Provide Configuration as command-line argument or using environment variable 'TURBINE_CONFIG'"
    cp = ConfigParser();
    cp.optionxform = str
    cp.read(filename)
    _open_config.cache_cp = cp
    _setup_logging(cp)
    return cp

def getFromConfigWithDefaults(cp, section, var, default):
    try:
        return cp.get(section, var)
    except:
        return default

def _make_url(url, **query):
    _log.getLogger(__name__).debug(query)
    url += '?'
    for k,v in query.items():
        if url.endswith('?'):
            url += '%s=%s' %(k,v)
            continue
        url += '&%s=%s' %(k,v)
    return url

def _urlopen(url, data=None):
    """ HTTP 401 responses are handled by the chain, and the request is retried with credentials.
    However the response to this is not checked, so errors will not be thrown.  This function
    simply checks to see if there was an HTTPError, and throws one.
    """
    result = urllib2.urlopen(url, data)
    if not (200 <= result.code < 300):
        raise urllib2.HTTPError(result.url, result.code, result.msg, result.headers, result.fp)
    return result

def _do_get(url):
    d = _urlopen(url)
    g = d.geturl()
    _log.getLogger(__name__).info('HTTP GET(%d) %s: %s', d.getcode(),d.msg, g)
    content = d.read()
    _log.getLogger(__name__).debug("HTTP RESPONSE: \n%s", content)
    return content


def _setup_logging(cp):
    """ Function will configure the logger only ONCE
    """
    if getattr(_setup_logging, 'done', False): return
    assert isinstance(cp, ConfigParser)
    try:
        fileConfig = cp.get('Logging', 'fileConfig')
        _loggingconfig.fileConfig(fileConfig)
    except Exception,ex:
        _log.basicConfig(\
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=_log.ERROR
            )

    l = _log.getLogger(__name__)
    l.debug('Setup Logging Done')
    _setup_logging.done = True


class MyHTTPNtlmAuthHandler(HTTPNtlmAuthHandler.HTTPNtlmAuthHandler):

    def http_error_401(self, req, fp, code, msg, headers):
        response = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler.http_error_401(self, req, fp, code, msg, headers)
        # NOTE: problem with how 401 errors are retried, don't utilize the 'chain'
        handler = urllib2.HTTPErrorProcessor()
        handler.parent = self.parent
        tmp = handler.http_response(req, response)
        if tmp:
            return tmp
        return response

class TurbineHTTPDefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
    def http_error_default(self, req, fp, code, msg, hdrs):
        msg += '\n%s' %fp.read()
        raise urllib2.HTTPDefaultErrorHandler.http_error_default(self, req, fp, code, msg, hdrs)


class _HTTPSConnection(httplib.HTTPSConnection):
    """ Verify the server certificate with trusted CA certificates
    """
    ca_certs = None
    cert_reqs = ssl.CERT_NONE
    @classmethod
    def setup_verify(cls, cp):
        section = 'Security'
        option = 'TrustedCertificateAuthorities'
        if not cp.has_option(section, option):
            _log.getLogger(__name__).debug('No Configuration ["%s","%s"]: Verify Off'
                                           %(section,option))
            return
        cls.ca_certs = cp.get(section, option)
        if cls.ca_certs is None:
            _log.getLogger(__name__).debug('Configuration ["%s","%s"] is None: Verify Off'
                                           %(section,option))
        elif not os.path.isfile(cls.ca_certs):
            _log.getLogger(__name__).error('Configuration ["%s","%s"] value must be a file'
                                           %(section,option))
            sys.exit(1)
        else:
            _log.getLogger(__name__).debug('Configuration ["%s","%s"] verify server certificate'
                                           %(section,option))
            cls.cert_reqs = ssl.CERT_REQUIRED

    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        if getattr(self, '_tunnel_host', None) is not None:
            self.sock = sock
            self._tunnel()
        self.sock = ssl.wrap_socket(sock,
                                    self.key_file,
                                    self.cert_file,
                                    cert_reqs=_HTTPSConnection.cert_reqs,
                                    ca_certs=_HTTPSConnection.ca_certs)


class _VerifyServer_HTTPSHandler(urllib2.HTTPSHandler):
    """ server certificate verification, must subclass HTTPSConnection to override
    """
    def https_open(self, req):
        _log.getLogger(__name__).debug("HTTPS OPEN")
        return self.do_open(_HTTPSConnection, req)

    https_request = urllib2.AbstractHTTPHandler.do_request_

class _AmazonRemappedHTTPBasicAuthHandler(urllib2.AbstractBasicAuthHandler, urllib2.BaseHandler):

    auth_header = 'Authorization'

    def http_error_401(self, req, fp, code, msg, headers):
        url = req.get_full_url()
        response = self.http_error_auth_reqed('x-amzn-Remapped-WWW-Authenticate',
                                              url, req, headers)
        return response

class _AmazonHTTPBasicCustomAuthHandler(urllib2.AbstractBasicAuthHandler, urllib2.BaseHandler):
    """ No www-authenticate header is included when "Authorized" Header is missing
    from request never invoke API Gateway Custom Authorizer.
    """
    auth_header = 'Authorization'

    def http_error_401(self, req, fp, code, msg, headers):
        url = req.get_full_url()
        realm = "FOQUS"
        #response = self.http_error_auth_reqed('x-amzn-Remapped-WWW-Authenticate',
        #                                      url, req, headers)
        #return response
        host = url
        return self.retry_http_basic_auth(host, req, realm)


def _setup(cp, url, realm=None):
    """_setup initializes the password manager and logging configuration.  Must call this
    function before logging.   Initializes server certificate verification.
    """
    global _opener
    assert isinstance(cp, ConfigParser)
    _setup_logging(cp)

    if _setup.passman is None:
        _setup.passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    elif _setup.passman.find_user_password(realm, url) != (None,None):
        _log.getLogger(__name__).debug('passman "%s" password already registered' %url)
        return

    _log.getLogger(__name__).debug('passman "%s" password NOT registered' %url)
    section = 'Authentication'
    username = cp.get(section, 'username', raw=True)
    password = cp.get(section, 'password', raw=True)

    #if url.startswith('https') and (not username or not password):
    #    sys.exit('HTTPS: Requires HTTP Basic Authentication, Provide both username and password')
    #if url.startswith('http://') and username and password:
    #    sys.exit('HTTP:  HTTP Basic Authentication requires HTTPS to be secure')

    #if not username or not password:
    #    sys.exit('Provide both username and password')

    passman = _setup.passman

    _log.getLogger(__name__).debug('%s', username)
    passman.add_password(realm, url, username, password)

    if _opener is not None:
        return

    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    #auth_NTLM = MyHTTPNtlmAuthHandler(passman)

    handlers = [urllib2.ProxyHandler, urllib2.UnknownHandler, urllib2.HTTPHandler,
                TurbineHTTPDefaultErrorHandler, urllib2.HTTPRedirectHandler,
                urllib2.FTPHandler, urllib2.FileHandler,
                urllib2.HTTPErrorProcessor]

    if url.startswith('https'):
        handlers.append(_VerifyServer_HTTPSHandler)
        _HTTPSConnection.setup_verify(cp)
        handlers.append(authhandler)
        #handlers.append(auth_NTLM)
    elif username and password:
        handlers.append(authhandler)

    # Amazon Remapped x-amzn-Remapped-WWW-Authenticate
    #handlers.append(_AmazonRemappedHTTPBasicAuthHandler(passman))

    handlers.append(_AmazonHTTPBasicCustomAuthHandler(passman))


    _opener = urllib2.build_opener(*handlers)
    urllib2.install_opener(_opener)
    return cp
_setup.passman = None


"""
"""
def add_options(op):
    """
    """
    assert(isinstance(op, optparse.OptionParser))

    # Paging
    op.add_option("-p", "--page", type="int",
                  action="store", dest="page", default=0,
                  help="page number")
    op.add_option("-r", "--rpp", type="int",
                  action="store", dest="rpp", default=1000,
                  help="results per page")
    op.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="verbose output")

def add_session_option(op):
    op.add_option("-s", "--session",
                  action="store", dest="session", default=None,
                  help="session identifier (guid)")

def add_json_option(op):
    """
    """
    op.add_option("-j", "--json",
                  action="store_true", dest="json", default=False,
                  help="print results as json to stdout")


def delete_page(configFile, section, **kw):
    """ HTTP DELETE
    """
    url = configFile.get(section, 'url')
    _setup(configFile, url)
    subr = kw.get('subresource')
    if subr is not None:
        url += subr
    request = urllib2.Request(url, data=None)
    request.get_method = lambda: 'DELETE'
    _log.getLogger(__name__).debug("DELETE URL: %s", url)
    p = _opener.open(request)
    return p.read()

def put_page(configFile, section, data, **kw):
    """
    data -- data to PUT
    """
    url = configFile.get(section, 'url')
    return _put_page_by_url(url, configFile, section, data, **kw)

def _put_page_by_url(url, configFile, section, data, content_type='application/octet-stream', **kw):
    """
    data -- data to PUT
    """
    _setup(configFile, url)
    subr = kw.get('subresource')
    if subr is not None:
        url += subr
    request = urllib2.Request(url, data=data)
    request.add_header('Content-Type', content_type)

    request.get_method = lambda: 'PUT'
    try:
        d = _opener.open(request)
    except urllib2.HTTPError, ex:
        _log.getLogger(__name__).debug("HTTPError: " + str(ex.__dict__))
        _log.getLogger(__name__).debug("HTTPError: " + str(ex.readline()))
        raise

    _log.getLogger(__name__).info("HTTP PUT(%d): %s", d.code, url)
    _log.getLogger(__name__).debug("Content-Type: %s", content_type)
    _log.getLogger(__name__).debug("BODY:\n%s", data)
    content = d.read()
    _log.getLogger(__name__).debug("HTTP RESPONSE: \n%s", content)
    return content

def post_page_by_url(url, configFile, section, data, **kw):
    """
    data -- data to POST
    """
    _setup(configFile, url)
    subr = kw.get('subresource')
    if subr is not None:
        url += subr
    d = _urlopen(url, data)
    _log.getLogger(__name__).info("HTTP POST(%d): %s", d.code, url)
    _log.getLogger(__name__).debug("BODY:\n%s", data)
    content = d.read()
    _log.getLogger(__name__).debug("HTTP RESPONSE: \n%s", content)
    return content

def post_page(configFile, section, data, **kw):
    """
    data -- data to POST
    """
    url = configFile.get(section, 'url')
    return post_page_by_url(url, configFile, section, data, **kw)

def get_page_by_url(url, configFile, **extra_query):
    _setup(configFile, url)
    query = {}
    for k,v in extra_query.items():
        if k == 'subresource' and v:
            url += v
        elif callable(v): query[k] = v()
        else: query[k] = v

    page_url = _make_url(url, **query)
    _log.getLogger(__name__).debug('retrieving job metadata: %s', page_url)
    return _do_get(page_url)

def get_page(configFile, section, **extra_query):
    url = configFile.get(section, 'url')
    return get_page_by_url(url, configFile, **extra_query)

#Returns a URL with the subresource tacked on and a complete set of query parameters
def standardizeOptions(url, options, **extra_query):
    query = {}
    for k,v in extra_query.items():
        if k == 'subresource' and v:
            url += v
        elif callable(v): query[k] = v()
        else: query[k] = v

    query['rpp'] = options.rpp
    query['page'] = options.page

    if options.verbose:
        query['verbose'] = options.verbose

    return (url, query)

def get_paging_by_url(url, configFile, section, query):
    """ If page>0, returns a list with a single string representing the response
    If page=0, gets all contents by automatically paging and
    returns a list of strings representing all the queries
    """
    _setup(configFile, url)

    allResults = []

    # page == 0 will automatically collect all the results
    # page > 0 will request a specific page, and only return those results
    if query["page"] == 0:
        query["page"] = 1
        #query["page"] == 1 is just to get us past the first iteration
        #if we got fewer than the requested results per page, we must have run out all the results
        isNext = False
        while query["page"] == 1 or isNext:
            page_url = _make_url(url, **query)
            _log.getLogger(__name__).debug('retrieving job metadata: %s', page_url)
            thisResults = _do_get(page_url)
            allResults.append(thisResults)
            query["page"] += 1
            isNext = len(thisResults) > 4096  #Fix, how do I actually tell when I have all the data?

    elif query["page"] >= 1:
        page_url = _make_url(url, **query)
        _log.getLogger(__name__).debug('retrieving job metadata: %s', page_url)
        allResults.append(_do_get(page_url))
    else:
        _log.getLogger(__name__).debug('ignore page query parameter: ' + query["page"])

    return allResults

def get_paging(configFile, section, options, **extra_query):
    """
    Returns a list, each item is the result of a query
    """
    url = configFile.get(section, 'url')
    (url, query) = standardizeOptions(url, options, **extra_query)
    return get_paging_by_url(url, configFile, section, query)


def load_pages_json(pages):
    data = []
    for l in pages:
        data += json.loads(l)
    return data
