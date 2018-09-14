from .base_model import BaseModel

import datetime
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, Column, Integer, BigInteger, Text, DateTime

from symmetry_py.util import equinox

Base = declarative_base(cls=BaseModel)

# ==================================================
# Process Log
# ==================================================

class ProcessLog(Base):

    # ==================================================
    # Constants
    # ==================================================

    TYPE_INFO = "INFO"
    TYPE_WARNING = "WARNING"
    TYPE_ERROR = "ERROR"

    # ==================================================
    # Model Properties
    # ==================================================

    __tablename__ = "process_log"

    pub_id_column = True

    id = Column(BigInteger, primary_key=True)
    pubid = Column(Text, nullable=True)
    process_id = Column(BigInteger, nullable=False)
    process_state_id = Column(BigInteger, nullable=False)
    type = Column(Text, nullable=False)
    message = Column(Text, nullable=True)
    message_detail = Column(Text, nullable=True)
    payload = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=equinox.now_db)
    updated_at = Column(DateTime, nullable=True)

    # ==================================================
    # Model Functions
    # ==================================================

    def __repr__(self):
        return f"<ProcessLog( " \
               f"id='{self.id}', " \
               f"type='{self.type}', " \
               f"process_id={self.process_id}, " \
               f"process_state_id={self.process_state_id}, " \
               f"message={self.message}, " \
               f"message_detail={self.message_detail}, " \
               f"created_at={self.created_at}, " \
               f"payload={self.payload} )>"

    # ==================================================
    # Static Functions
    # ==================================================

    @staticmethod
    def make_log_entry(
            process_id,
            state_id,
            log_level=None,
            message=None,
            message_detail=None,
            payload=None
        ):
        
        process_log = ProcessLog()

        if log_level is None:
            log_level = ProcessLog.TYPE_INFO

        process_log.type = log_level

        process_log.process_id = process_id
        process_log.process_state_id = state_id
        process_log.message = message
        process_log.message_detail = message_detail
        process_log.payload = payload

        return process_log