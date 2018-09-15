from sqlalchemy import Table, MetaData, Column, Integer, BigInteger, Text, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import date
from sqlalchemy.ext.declarative import declared_attr

# ==================================================
# Base Model 
# ==================================================

class BaseModel(object):

    # ==================================================
    # Properties
    # ==================================================

    # The descendand class should set this property to
    # `True` if the model has a `pub_id` column.
    pub_id_column = False

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # ==================================================
    # Model Functions
    # ==================================================

    def has_pubid_column(self):
        return self.pub_id_column == True

