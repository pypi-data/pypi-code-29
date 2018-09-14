from sqlalchemy import Table, MetaData, Column, Integer, BigInteger, Text, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

# ==================================================
# Model Name
# ==================================================

# BaseModel = declarative_base()

class Model(BaseModel):

    __tablename__ = "table_name"

    # ==================================================
    # Model Properties
    # ==================================================

    id = Column(BigInteger, primary_key=True)
    type = Column(Text, nullable=False)
    external_id = Column(BigInteger, nullable=True)
    process_state_id = Column(BigInteger, nullable=False)
    process_state_detail = Column(Text, nullable=True)
    process_state_at = Column(DateTime, nullable=False)
    payload = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    # ==================================================
    # Model Functions
    # ==================================================

    # ==================================================
    # Static Functions
    # ==================================================