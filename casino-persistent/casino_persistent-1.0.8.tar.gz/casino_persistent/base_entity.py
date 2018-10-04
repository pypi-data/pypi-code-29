from uuid import uuid4

from sqlalchemy import Column, Boolean, BigInteger
from sqlalchemy_utils import UUIDType

from casino_persistent.utils import get_epochtime_ms


class BaseEntity(object):
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    created_at = Column(BigInteger, default=get_epochtime_ms())
    updated_at = Column(BigInteger, default=get_epochtime_ms(), onupdate=get_epochtime_ms())
    active = Column(Boolean, default=True)
