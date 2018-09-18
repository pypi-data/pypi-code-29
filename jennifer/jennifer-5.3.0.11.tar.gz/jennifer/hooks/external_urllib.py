from jennifer.agent import jennifer_agent
__hooking_module__ = 'urllib'


def wrap_urlopen(urlopen):
    agent = jennifer_agent()
    def handler(*args, **kwargs):  # TODO: is safe in Python2?
        from urllib import parse
        from urllib.request import Request
        from http.client import HTTPResponse
        transaction = agent.current_transaction()
        url = kwargs.get('url') or args[0]
        if isinstance(url, Request):
            url = url.full_url
        if transaction is not None:
            o = parse.urlparse(url)
            transaction.profiler.external_call(
                protocol=o.scheme,
                host=o.hostname,
                port=o.port or 80,
                url=url,
                caller='urllib.request.urlopen',
            )
        ret = urlopen(*args, **kwargs)
        if isinstance(ret, HTTPResponse):
            v = ret.version
            version = 'HTTP/1.1'
            if v is 10:
                version  = 'HTTP/1.0'
            transaction.profiler.end(
                message='uurllib.request.urlopen(url=%s,response=%s,%s)' % (
                    url, version, ret.status)
            )
        else:
            transaction.profiler.end()
        return ret
    return handler


def hook(urllib):
    import urllib.request
    urllib.request.urlopen = wrap_urlopen(urllib.request.urlopen)
