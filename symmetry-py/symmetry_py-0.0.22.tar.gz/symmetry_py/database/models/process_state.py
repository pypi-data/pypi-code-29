from .base_model import BaseModel

from sqlalchemy import Table, MetaData, Column, Integer, BigInteger, Text, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base(cls=BaseModel)

# ==================================================
# Process State
# ==================================================

class ProcessState(Base):

    # ==================================================
    # Constants
    # ==================================================

    CODE_PENDING = 'PENDING'
    CODE_IN_PROGRESS = 'IN_PROGRESS'
    CODE_PAUSED = 'PAUSED'
    CODE_CANCELLED = 'CANCELLED'
    CODE_COMPLETED = 'COMPLETED'
    CODE_FAILED = 'FAILED'

    # ==================================================
    # Model Properties
    # ==================================================

    __tablename__ = "process_state"

    pub_id_column = True

    id = Column(BigInteger, primary_key=True)
    pubid = Column(Text, nullable=True)
    code = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    # ==================================================
    # Model Functions
    # ==================================================

    def __repr__(self):
        return f"<ProcessState( " \
               f"id='{self.id}', " \
               f"pub_id='{self.pubid}', " \
               f"code={self.code}, " \
               f"description={self.description} )>"

    # ==================================================
    # Static Functions
    # ==================================================
