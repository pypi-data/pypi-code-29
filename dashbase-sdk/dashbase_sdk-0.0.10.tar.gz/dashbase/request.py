import time
from schematics.models import Model
from schematics.types.base import LongType, StringType, BooleanType, BaseType
from schematics.types.compound import ListType, ModelType, DictType


class Request(Model):
    startTimeInMillis = LongType(serialize_when_none=False)
    endTimeInMillis = LongType(serialize_when_none=False)
    endGlobalId = LongType(serialize_when_none=False)
    startGlobalId = LongType(serialize_when_none=False)
    numResults = LongType(default=10)
    tableNames = ListType(StringType, default=["*"])
    excludeTableNames = ListType(StringType, default=[])
    query = DictType(BaseType, serialize_when_none=False)
    aggregations = DictType(BaseType, serialize_when_none=False)
    fields = ListType(StringType, default=[])
    useApproximation = BooleanType(default=False)
    ctx = StringType(serialize_when_none=False)
    fetchSchema = BooleanType(default=False)
    timeoutMillis = LongType(default=0x7fffffff)
    disableHighlight = BooleanType(default=False)
    startId = StringType(serialize_when_none=False)
    endId = StringType(serialize_when_none=False)
    debugMode = LongType(serialize_when_none=False)

    def set_query(self, query=None):
        if not query:
            query = "*"
        self.query = {"queryType": "string", "queryStr": query}
