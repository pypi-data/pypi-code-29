import os

from flask_security import SQLAlchemySessionUserDatastore
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import config
from eingang.models import *


db_file = os.path.join(os.getcwd(), config['SQLITE_FILE'])
engine = create_engine('sqlite:///' + db_file, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine))

Base.query = db_session.query_property()


def init_db():
    # Import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db().
    import models

    Base.metadata.create_all(bind=engine)

user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
