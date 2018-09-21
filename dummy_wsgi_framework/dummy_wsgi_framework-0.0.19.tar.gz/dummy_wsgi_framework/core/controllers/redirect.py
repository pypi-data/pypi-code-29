#!/usr/bin/python3
def get_response(environ, start_response, app_config, location):
    if environ and app_config:
        pass  # Lets ignore not usage PyCharm
    start_response('301 Moved Permanently', [('Location', location)])
    return b''
