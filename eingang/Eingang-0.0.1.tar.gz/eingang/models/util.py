from sqlalchemy.ext.declarative import declarative_base

from . import Base


def get_class_by_tablename(tablename):
    for c in Base._decl_class_registry.values():
        try:
            if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
                return c
        except AttributeError:
            pass
