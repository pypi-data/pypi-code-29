import os.path
import sys

from eingang.models.util import get_class_by_tablename
from sqlalchemy import inspect

from database import db_session, engine


inspector = inspect(engine)

for index, table_name in enumerate(inspector.get_table_names()):
    if index > 0:
        print()
    print(table_name)
    print('-' * len(table_name))
    cls = get_class_by_tablename(table_name)
    for row in db_session.query(cls):
        print(row)

db_session.close()
