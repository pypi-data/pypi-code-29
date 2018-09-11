from functools import partial
from sanic.response import json
from .validate import valida_request_query, MissingQueryException
from .sig import get_signature


def check_return(rv):
    if isinstance(rv, tuple):
        rv, other = rv[0], rv[1]
        if isinstance(other, dict):
            rv_kw = other
        elif isinstance(other, int):
            rv_kw = {"status": other}
        else:
            raise Exception("unaccepted second return value: {}".format(other))
    else:
        rv_kw = {}

    headers = rv_kw.setdefault("headers", {})
    headers.update({"X-Served-By": "sanic", "Access-Control-Allow-Origin": "*"})

    if isinstance(rv, dict):
        if "success" not in rv:
            rv["success"] = True if rv_kw.get("status", 200) < 400 else False

        return json(rv, **rv_kw)
    else:
        return rv


def check_response(fn):
    async def new_fn(req):
        args, kwargs = get_signature(fn)
        # shift the request instance
        args = args[1:]
        # print(args, kwargs)
        try:
            q_args, q_kwargs = valida_request_query(req, *args, **kwargs)
        except MissingQueryException as e:
            rv = (
                {
                    "success": False,
                    "reason": str(e),
                    "type": str(type(e))
                }, 400
            )
            return check_return(rv)

        try:
            rv = await fn(req, *q_args, **q_kwargs)
        except Exception as e:
            rv = (
                {
                    "success": False,
                    "reason": str(e),
                    "type": str(type(e))
                }, 500
            )

        return check_return(rv)

    return new_fn


def add_route(app, url, fn, **kwargs):
    app.route(url, **kwargs)(fn)


def json_route(app, url, fn, **kwargs):
    add_route(app, url, check_response(fn), **kwargs)


def get_json_route(app):
    return partial(json_route, app)
