from sqlalchemy import Column, Integer, DATE, TIMESTAMP, ForeignKey
from sqlalchemy import Sequence
from sqlalchemy.dialects.oracle import VARCHAR2

from . import connection

FACTOR_TYPE = 'FACTOR'
REFDATA_TYPE = 'REFDATA'


class EQIData(connection.DB_CONNECTION.get_declarative_base()):
    __tablename__ = 'EQI_FACTORS'
    FACTOR_ID_SEQ = Sequence('factor_id_seq')
    id = Column(Integer, FACTOR_ID_SEQ, primary_key=True)
    name = Column(VARCHAR2(127), nullable=False, unique=True)
    path = Column(VARCHAR2(511), nullable=False)
    location = Column(VARCHAR2(31), nullable=False)
    start_date = Column(DATE)
    end_date = Column(DATE)
    ticker_type = Column(VARCHAR2(31))
    owner = Column(VARCHAR2(63), nullable=False)
    description = Column(VARCHAR2(511), nullable=False)
    type = Column(VARCHAR2(31), nullable=False)
    creation_ts = Column(TIMESTAMP)
    last_modified_ts = Column(TIMESTAMP)
    ticker_col_name = Column(VARCHAR2(255))
    date_col_name = Column(VARCHAR2(255))

    def is_s3(self):
        return self.location == 'S3'

    def is_oracle(self):
        return self.location == 'ORACLE'

    def to_list(self):
        return [self.id, self.name, self.description, self.location,
                self.owner, self.last_modified_ts, self.ticker_type]

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'EQI_DATA'
    }


class EQIFactor(EQIData):
    """
    EQIFactor must have the format of:
        - ['date', 'asset'] as index, or ['date', 'asset', 'category'] for
            a categorized factor
        - one single value column
    """
    __mapper_args__ = {
        'polymorphic_identity': 'EQI_FACTORS'
    }


class EQIRefData(EQIData):
    __mapper_args__ = {
        'polymorphic_identity': 'EQI_REF_DATA'
    }


class EQIFactorPerformance(connection.DB_CONNECTION.get_declarative_base()):
    __tablename__ = 'EQI_FACTOR_PERFORMANCE'
    FACTOR_PERFORMANCE_ID_SEQ = Sequence('factor_performance_id_seq')
    id = Column(Integer, FACTOR_PERFORMANCE_ID_SEQ, primary_key=True)
    factor_id = Column(VARCHAR2(127),
                       ForeignKey(EQIFactor.id, ondelete='CASCADE'),
                       nullable=False, unique=True)
    path = Column(VARCHAR2(511), nullable=False)
    location = Column(VARCHAR2(31), nullable=False)
    start_date = Column(DATE)
    end_date = Column(DATE)
    ticker_type = Column(VARCHAR2(31))
    owner = Column(VARCHAR2(63), nullable=False)
    description = Column(VARCHAR2(511), nullable=False)
    type = Column(VARCHAR2(31), nullable=False)
    creation_ts = Column(TIMESTAMP)
    last_modified_ts = Column(TIMESTAMP)
    ticker_col_name = Column(VARCHAR2(255))
    date_col_name = Column(VARCHAR2(255))
