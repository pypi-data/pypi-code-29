import os
from jennifer.agent import jennifer_agent
from . import app_flask, \
    app_django, \
    db_pymysql, \
    db_sqlite3, \
    db_mysqlclient, \
    external_urllib, \
    external_requests

HOOK_SUPPORT_LIST = [
    app_flask,
    app_django,
    db_mysqlclient,
    db_pymysql,
    db_sqlite3,
    external_urllib,
    external_requests,
]


def is_module_exist(module):
    try:
        return __import__(module)
    except ImportError:
        return False


def wrap_open(origin):
    agent = jennifer_agent()

    def handler(file, mode='r', *args, **kwargs):
        transaction = agent.current_transaction()
        if transaction is not None:
            transaction.profiler.file_opened(
                name=os.path.abspath(os.path.join(os.getcwd(), file)),
                mode=mode
            )
        return origin(file, mode, *args, **kwargs)
    return handler


def wrap_connect(connect):
    import socket
    agent = jennifer_agent()

    def handler(self, address):
        transaction = agent.current_transaction()
        ret = connect(self, address)
        if self.family != socket.AF_INET:
            return ret
        if transaction is not None:
            raddr = self.getpeername()
            laddr = self.getsockname()
            transaction.profiler.socket_opened(
                host=raddr[0],
                port=raddr[1],
                local=laddr[1],
            )
        return ret
    return handler


def hook_builtins():
    import socket
    __builtins__['open'] = wrap_open(__builtins__['open'])
    socket.socket.connect = wrap_connect(socket.socket.connect)


def hooking():
    for m in HOOK_SUPPORT_LIST:
        module = is_module_exist(m.__hooking_module__)
        if module is not False:
            m.hook(module)
    hook_builtins()
