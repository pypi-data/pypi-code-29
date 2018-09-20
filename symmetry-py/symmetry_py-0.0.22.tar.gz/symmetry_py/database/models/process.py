from .base_model import BaseModel

from symmetry_py.util import equinox
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, Column, Integer, BigInteger, Text, DateTime

Base = declarative_base(cls=BaseModel)

# ==================================================
# Process
# ==================================================

class Process(Base):

    # ==================================================
    # Model Properties
    # ==================================================

    __tablename__ = "process"

    pub_id_column = True

    id = Column(BigInteger, primary_key=True)
    pubid = Column(Text, nullable=True)
    type = Column(Text, nullable=False)
    external_id = Column(BigInteger, nullable=True)
    process_state_id = Column(BigInteger, nullable=False)
    process_state_detail = Column(Text, nullable=True)
    process_state_at = Column(DateTime, nullable=False)
    payload = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=equinox.now_db)
    updated_at = Column(DateTime, nullable=True)

    # ==================================================
    # Model Functions
    # ==================================================

    def __repr__(self):
        return f"<Process( " \
               f"id='{self.id}', " \
               f"type='{self.type}', " \
               f"external_id='{self.external_id}', " \
               f"process_state_id={self.process_state_id}, " \
               f"process_state_detail={self.process_state_detail}, " \
               f"process_state_at={self.process_state_at}, " \
               f"payload={self.payload} )>"

    # ==================================================
    # Static Functions
    # ==================================================
