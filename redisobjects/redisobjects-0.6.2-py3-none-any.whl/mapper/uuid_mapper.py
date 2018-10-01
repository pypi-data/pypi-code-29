from .string_mapper import StringMapper
from redisobjects.serializer import UUIDSerializer

class UUIDMapper(StringMapper):
    def __init__(self):
        StringMapper.__init__(self, UUIDSerializer())
