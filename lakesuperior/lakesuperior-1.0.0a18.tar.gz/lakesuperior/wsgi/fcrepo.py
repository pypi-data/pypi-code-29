#!/usr/bin/env python

from gunicorn.app.base import BaseApplication

class WsgiApp(BaseApplication):

    def __init__(self, app, options={}):
        self.options = options
        self.application = app
        super(WsgiApp, self).__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def run():
    from lakesuperior import wsgi
    from lakesuperior.server import fcrepo
    options = {opn: getattr(wsgi, opn) for opn in wsgi.__all__}
    print('WSGI Options: {}'.format(options))
    WsgiApp(fcrepo, options).run()


if __name__ == '__main__':
    run()

