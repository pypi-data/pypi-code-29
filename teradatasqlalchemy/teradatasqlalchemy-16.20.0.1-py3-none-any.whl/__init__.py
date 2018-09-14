# Copyright 2018 by Teradata Corporation. All rights reserved.

from .types import TIME, TIMESTAMP, DECIMAL, CHAR, VARCHAR, CLOB, BYTEINT

from sqlalchemy.sql.sqltypes import (Integer, Interval, SmallInteger,\
                                     BigInteger, Float, Boolean,\
                                     Text, Unicode, UnicodeText,\
                                     DATE)

from . import vernumber

__version__ = vernumber.sVersionNumber

__all__ = (Integer, SmallInteger, BigInteger, Float, Text, Unicode,
           UnicodeText, Interval, Boolean,
           DATE, TIME, TIMESTAMP, DECIMAL,
           CHAR, VARCHAR, CLOB, BYTEINT)

import teradatasql
