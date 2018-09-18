import logging

from influxdb import InfluxDBClient

logger = logging.getLogger('pyinfluxdb')


class InfluxClient(InfluxDBClient):
    def __init__(self,
                 host='localhost',
                 port=8086,
                 username='root',
                 password='root',
                 database=None,
                 **kwargs
                 ):
        super().__init__(host, port, username, password, database, timeout=10, **kwargs)
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__database = database
        self.__kwargs = kwargs

        self._database_list = self.get_list_database()
        logger.debug(self._database_list)

    def connect_to_database(self, name):
        return Database(host=self.__host,
                        port=self.__port,
                        username=self.__username,
                        password=self.__password,
                        database=name,
                        **self.__kwargs
                        )

    def __getattr__(self, name):
        """Get a collection of this database by name.

        Raises InvalidName if an invalid collection name is used.

        :Parameters:
          - `name`: the name of the collection to get
        """
        if name.startswith('_'):
            raise AttributeError(
                "Database has no attribute %r. To access the %s"
                " collection, use database[%r]." % (name, name, name))
        return self.__getitem__(name)

    def __getitem__(self, name):
        """Get a database by name.

        Raises :class:`~pymongo.errors.InvalidName` if an invalid
        database name is used.

        :Parameters:
          - `name`: the name of the database to get
        """
        if {'name': name} not in self._database_list:
            self.create_database(name)
        return self.connect_to_database(name)


class Database(InfluxDBClient):
    def __init__(self,
                 host='localhost',
                 port=8086,
                 username='root',
                 password='root',
                 database=None,
                 **kwargs
                 ):
        super().__init__(host, port, username, password, database, timeout=10, **kwargs)
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__database = database
        self.__kwargs = kwargs
        self._measurements_list = self.get_list_measurements()
        logger.debug(self._measurements_list)
        pass

    def get_measurement(self, name):
        return Measurement(self, name)

    def __getattr__(self, name):
        """Get a collection of this database by name.

        Raises InvalidName if an invalid collection name is used.

        :Parameters:
          - `name`: the name of the collection to get
        """
        if name.startswith('_'):
            raise AttributeError(
                "Database has no attribute %r. To access the %s"
                " collection, use database[%r]." % (name, name, name))
        return self.__getitem__(name)

    def __getitem__(self, name):
        """Get a database by name.

        Raises :class:`~pymongo.errors.InvalidName` if an invalid
        database name is used.

        :Parameters:
          - `name`: the name of the database to get
        """
        return self.get_measurement(name)


class Measurement(object):
    FIND_ONE_BASE = 'SELECT * FROM {condition} ORDER BY time DESC LIMIT 1;'
    FIND_BASE = 'SELECT * FROM {condition} ORDER BY time DESC;'
    key_words = ['name', 'key']

    def __init__(self, database, name):
        if not isinstance(name, str):
            raise TypeError("name must be an instance "
                            "of %s" % (str.__name__,))

        if not name or ".." in name:
            raise Exception("collection names cannot be empty")
        if "$" in name and not (name.startswith("oplog.$main") or
                                name.startswith("$cmd")):
            raise Exception("collection names must not "
                            "contain '$': %r" % name)
        if name[0] == "." or name[-1] == ".":
            raise Exception("collection names must not start "
                            "or end with '.': %r" % name)
        if "\x00" in name:
            raise Exception("collection names must not contain the "
                            "null character")

        self.__database = database
        self.__name = name

    def find_one(self, filter):
        for k in filter.keys():
            if k in self.key_words:
                raise Exception('key {} is keyword'.format(k))
        kwargs_str_list = ["{} = '{}'".format(k, v) for k, v in filter.items()]
        condition = '{measurement}'.format(measurement=self.__name)
        if kwargs_str_list:
            kwargs_str = ' AND '.join(kwargs_str_list)
            condition += ' WHERE {where}'.format(where=kwargs_str)
        sql_str = self.FIND_ONE_BASE.format(condition=condition)
        logger.debug(sql_str)
        rs = self.__database.query(sql_str)
        if rs is None:
            return None
        points = list(rs.get_points(measurement=self.__name))
        if not points:
            return None
        point = points[0]
        return point

    def find(self, filter):
        for k in filter.keys():
            if k in self.key_words:
                raise Exception('key {} is keyword'.format(k))
        kwargs_str_list = ["{} = '{}'".format(k, v) for k, v in filter.items()]
        condition = '{measurement}'.format(measurement=self.__name)
        if kwargs_str_list:
            kwargs_str = ' AND '.join(kwargs_str_list)
            condition += ' WHERE {where}'.format(where=kwargs_str)
        sql_str = self.FIND_BASE.format(condition=condition)
        logger.debug(sql_str)
        rs = self.__database.query(sql_str)
        if rs is None:
            return None
        points = list(rs.get_points(measurement=self.__name))
        if not points:
            return []
        return points

    def insert_one(self, tags, fields):
        point = dict(
            fields=fields,
            tags=tags,
            measurement=self.__name
        )

        return self.__database.write_points([point])
