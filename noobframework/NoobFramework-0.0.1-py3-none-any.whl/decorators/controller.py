from NoobFramework.webob import Request, Response
from NoobFramework.webob import exc


def controller(func):
    def replacement(env, start_response):
        req = Request(env)
        try:
            resp = func(req, **req.urlvars)
        except exc.HTTPException as e:
            resp = e

        if isinstance(resp, str):
            resp = Response(body=resp)

        return resp(env, start_response)
    return replacement
