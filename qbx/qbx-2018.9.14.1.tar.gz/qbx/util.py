import sys

from docopt import docopt as docoptinit


def must_success(func, *args, **kwargs):
    if 'timeout' not in kwargs:
        kwargs['timeout'] = 5
    try:
        r = func(*args, **kwargs)
    except Exception as e:
        print('force exit, statuscode != 200', type(e))
        sys.exit(1)
    if r.status_code >= 300:
        print(r, r.text)
        print('force exit, statuscode != 200')
        sys.exit(1)
    return r


def docopt(doc, argv):
    return docoptinit(doc, argv=argv)
