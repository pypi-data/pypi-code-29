from NoobFramework.webob import Request
from NoobFramework.webob import exc

import re

from NoobFramework.router import load_controller
from NoobFramework.regex import regex_utils


class Router(object):
    def __init__(self):
        self.routes = []

    def add_route(self, url, controller, **vars):
        if isinstance(controller, str):
            controller = load_controller.load_controller(controller)

        regex = re.compile(regex_utils.url_to_regex(url))
        self.routes.append((regex, controller, vars))

    def __call__(self, env, start_response):
        req = Request(env)
        for regex, controller, vars in self.routes:
            match = regex.match(req.path_info)
            if match:
                req.urlvars = match.groupdict()
                req.urlvars.update(vars)

                return controller(env, start_response)
        return exc.HTTPNotFound()(env, start_response)
