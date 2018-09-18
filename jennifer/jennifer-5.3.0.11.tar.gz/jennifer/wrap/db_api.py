from jennifer.agent import jennifer_agent
from jennifer.api.proxy import Proxy


def safe(l, idx, default=None):
    try:
        return l[idx]
    except IndexError:
        return default


class CursorProxy(Proxy):
    def __init__(self, obj, host, port, paramstyle, conn):
        Proxy.__init__(self, obj)
        self.set('host', host)
        self.set('port', port)
        self.set('paramstyle', paramstyle)
        self.set('conn', conn)

    def execute(self, *args, **kwargs):
        agent = jennifer_agent()
        transaction = jennifer_agent().current_transaction()
        operation = safe(args, 0) or kwargs.get('operation')
        parameters = safe(args, 1) or kwargs.get('parameters')
        agent.recorder.db_recorder.active(self.conn)
        if transaction is not None and operation is not None:
            transaction.profiler.db_execute(
                self.host, self.port, operation, parameters, self.paramstyle)
        result = None
        try:
            result = self._origin.execute(*args, **kwargs)
        except Exception as e:
            if transaction is not None and operation is not None:
                transaction.profiler.sql_error(e)
                transaction.profiler.end()
            agent.recorder.db_recorder.deactive(self.conn)
            raise e

        if transaction is not None and operation is not None:
            transaction.profiler.end()
        agent.recorder.db_recorder.deactive(self.conn)

        return result

    def record_fetch(self, fetch, size, pass_size=False):
        transaction = jennifer_agent().current_transaction()
        agent = jennifer_agent()
        args = []
        if pass_size:
            args = [size]
        if transaction is None:
            try:
                agent.recorder.db_recorder.active(self.conn)
                ret = fetch(*args)
            except Exception as e:
                agent.recorder.db_recorder.deactive(self.conn)
                raise e
            agent.recorder.db_recorder.deactive(self.conn)
            return ret

        if size == 0:  # it mean fetch all
            size = self._result.num_rows()
        transaction.profiler.db_fetch(size)
        err = None
        try:
            agent.recorder.db_recorder.active(self.conn)
            ret = fetch(*args)
        except Exception as e:
            err = e
        transaction.profiler.end()
        agent.recorder.db_recorder.deactive(self.conn)
        if err is not None:
            raise err
        return ret

    def fetchone(self):
        return self.record_fetch(self._origin.fetchone, 1)

    def fetchmany(self, size=None):
        pass_size = True
        if size is None:
            size = self._origin.arraysize
            pass_size = False
        return self.record_fetch(self._origin.fetchmany, size, pass_size)

    def fetchall(self):
        size = self.rowcount
        return self.record_fetch(self._origin.fetchall, size)


class ConnectionProxy(Proxy):
    def __init__(self, obj, host, port, paramstyle):
        Proxy.__init__(self, obj)
        self.set('host', host)
        self.set('port', port)
        self.set('paramstyle', paramstyle)

    def cursor(self, *args, **kwargs):
        cursor = self._origin.cursor(*args, **kwargs)
        return CursorProxy(cursor, self.host, self.port, self.paramstyle, self)

    def close(self, *args, **kwargs):
        jennifer_agent().recorder.db_recorder.remove_connection(self)
        return self._origin.close(*args, **kwargs)


def register_database(module, connection_info):
    agent = jennifer_agent()
    def wrap_connect(connect):
        def handler(*args, **kwargs):
            host, port, database = connection_info(*args, **kwargs)
            transaction = agent.current_transaction()
            if transaction is not None:
                transaction.profiler.db_open(host, port, database)
            try:
                connection = ConnectionProxy(
                    connect(*args, **kwargs), host, port, module.paramstyle)
            except Exception as e:
                if transaction is not None:
                    transaction.profiler.db_connection_error(e)
                    transaction.profiler.end()
                raise e
            if transaction is not None:
                transaction.profiler.end()
            agent.recorder.db_recorder.add_connection(connection)
            return connection
        return handler
    module.connect = wrap_connect(module.connect)
