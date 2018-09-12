# Filename: cg_base.py
import uuid

from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

DEFAULT_TABLE_ARGS = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_general_ci'}


class CGColumn(Column):
    def __init__(self, *args, **kwargs):
        self.secure = kwargs.pop('secure', False)

        super().__init__(*args, **kwargs)


class LoggedInUser:
    def __init__(self, *args):
        kwargs = args[0]
        self.user_id = kwargs.pop('user_id', None)
        self.session_id = kwargs.pop('session_id', None)
        self.email = kwargs.pop('email', None)
        self.mobile = kwargs.pop('mobile', None)
        self.username = kwargs.pop('username', None)
        self.group_id = kwargs.pop('group_id', None)
        self.menu_permissions = kwargs.pop('menu_permissions', None)
        self.compiled_permissions = kwargs.pop('compiled_permissions', None)
        # self.groups = kwargs.pop('groups', [])

        session_data = kwargs.pop('session_data', {})
        for key in session_data:
            setattr(self, key, session_data[key])

        return


def generatePK():
    return str(uuid.uuid4()).replace("-", "")


class CgBase:
    def initialize(self):
        self.Config = None
        self.DebugDb = False
        self.DbConfig = None
        self.Engine = None
        self.SessionMaker = None

    def init_base(self):
        self.DebugDb = self.Config['Db'].getboolean('DebugDb')
        self.DbConfig = {
            'user': self.Config['Db']['User'],
            'password': self.Config['Db']['Password'],
            'host': self.Config['Db']['Server'],
            'database': self.Config['Db']['Database']
        }

        dbUrl = 'mysql+mysqlconnector://{user}:{password}@{host}/{database}'.format(**self.DbConfig)
        print('DB URL =', dbUrl)
        self.Engine = create_engine(dbUrl, echo=self.DebugDb)
        self.SessionMaker = sessionmaker(bind=self.Engine)

    def CreateSchema(self):
        Base.metadata.create_all(self.Engine)
        return


class Serializer2:

    def serializeRoot(self):
        obj = {}

        for c in inspect(self).attrs.keys():
            val = getattr(self, c)

            # if val.__class__.__module__ == self.__class__.__module__:
            #    continue
            if isinstance(val, InstrumentedList):
                continue
            elif hasattr(val, 'serialize'):
                continue
            elif hasattr(val, '_toJson'):
                obj[c] = val._toJson()
            else:
                obj[c] = val

        return obj

    def serialize(self, originalClass=None, level=0, childAdded=None, rootRels=None, maxLevel=2):
        obj = {}

        if originalClass is None:
            originalClass = self.__class__
        if childAdded is None:
            childAdded = []
        if rootRels is None:
            rootRels = self.__mapper__.relationships._data.keys()

        allKeys = inspect(self).attrs.keys()
        allKeys = sorted(allKeys)

        for c in allKeys:
            val = getattr(self, c)

            if isinstance(val, InstrumentedList):
                continue
            elif hasattr(val, 'serialize'):
                # if val.__class__ != originalClass and level < maxLevel:
                if level < maxLevel:
                    if val.__class__ == originalClass:
                        obj[c] = val.serializeRoot()
                    elif level == 0:
                        childAdded.append(c)
                        obj2 = val.serialize(originalClass, level + 1, childAdded, rootRels, maxLevel)
                        obj[c] = obj2
                    elif c not in childAdded and c not in rootRels:
                        childAdded.append(c)
                        obj2 = val.serialize(originalClass, level + 1, childAdded, rootRels, maxLevel)
                        obj[c] = obj2

            elif hasattr(val, '_toJson'):
                obj[c] = val._toJson()
            else:
                obj[c] = val

        return obj

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


