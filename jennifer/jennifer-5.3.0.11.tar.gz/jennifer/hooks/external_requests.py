from jennifer.agent import jennifer_agent
__hooking_module__ = 'requests'


def wrap_send(origin):
    agent = jennifer_agent()
    def handler(self, request, **kwargs):
        from urllib import parse
        transaction = agent.current_transaction()
        if transaction is not None:
            url = request.url
            o = parse.urlparse(url)
            transaction.profiler.external_call(
                protocol=o.scheme,
                host=o.hostname,
                port=o.port or 80,
                url=url,
                caller='requests.Session.send',
            )
        ret = origin(self, request, **kwargs)
        if transaction is not None:
            message = None
            if ret is not None:
                message='rrequests.Session.send(url=%s,response=%s)' % (
                    url, ret.status_code)
            transaction.profiler.end(message=message)
        return ret
    return handler


def hook(requests):
    requests.Session.send = wrap_send(requests.Session.send)
