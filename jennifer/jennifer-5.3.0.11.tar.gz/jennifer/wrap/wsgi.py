"""Wsgi Agent for Jennifer APM
"""
import os
import sys
import base64
import struct
from jennifer.agent import jennifer_agent
from email.utils import formatdate
import time
try:
    import Cookie as cookies
except ImportError:
    from http import cookies


wmonid_pack = struct.Struct('>Q')

def wrap_wsgi_start_response(origin, set_wmonid, new_wmonid=None):
    def handler(*args, **kwargs):
        if set_wmonid:
            if len(args) == 2:
                expire = formatdate(
                    timeval=time.time() + 31536000,
                    localtime=False,
                    usegmt=True
                )
                set_cookie = 'WMONID=%s; expires=%s; Max-Age=31536000; path=/' % (
                    base64.b64encode(new_wmonid).decode('ascii'), expire)

                args[1].append(('Set-Cookie', str(set_cookie)))

        return origin(*args, **kwargs)
    return handler

def wrap_wsgi_handler(app, wsgi_handler_name):
    agent = jennifer_agent()

    def handler(*args, **kwargs):
        environ = {}
        wmonid = None
        new_wmonid_val = (os.getpid() << 32) + int(time.time())
        new_wmonid = wmonid_pack.pack(new_wmonid_val)
        if len(args) is 3:
            environ = args[1]  # self, environ, start_response
            modargs = [
                args[0],
                args[1],
            ]
            start_response = args[2]
        elif len(args) is 2:
            environ = args[0]  # environ, start_response
            modargs = [
                args[0],
            ]
            start_response = args[1]
        cookie = cookies.SimpleCookie()
        cookie.load(environ.get('HTTP_COOKIE', ''))
        cookie_wmonid = cookie.get('WMONID')
        if cookie_wmonid is None:
            wmonid = new_wmonid_val
        else:
            try:
                wmonid, = wmonid_pack.unpack(
                    base64.b64decode(cookie_wmonid.value))
            except:  # incorrect wmonid
                cookie_wmonid = None
                wmonid = new_wmonid_val
        modargs.append(
            wrap_wsgi_start_response(
                start_response,
                set_wmonid=(cookie_wmonid == None),
                new_wmonid=new_wmonid,
            )
        )

        transaction = agent.start_transaction(
            environ, wmonid, wsgi_handler_name)
        err = None
        try:
            ret = app(*modargs, **kwargs)
        except Exception as e:
            err = e

        end_time = agent.current_time()
        transaction.end(end_time)
        if err is not None:
            raise err
        return ret
    return handler


def wrap_wsgi_app(app, default_wsgi_handler_name='wsgi_handler'):
    return wrap_wsgi_handler(app, default_wsgi_handler_name)
