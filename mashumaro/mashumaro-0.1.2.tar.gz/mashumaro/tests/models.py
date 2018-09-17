from datetime import datetime
from dataclasses import dataclass
from typing import List, Deque, Union, Optional, ChainMap
from collections import deque

from mashumaro.serializer.base.metaprogramming import CodeBuilder


@dataclass
class Inner:
    a: int


@dataclass
class Location:
    # l: Union[str, int]
    l: ChainMap[str, Inner]
    dt: datetime = None
    lat: float = None
    lon: float = None


@dataclass
class OOO:
    a: int = 5
    b: Optional[str] = None


c = CodeBuilder(Inner)
c.add_from_dict()
c.add_to_dict()
c = CodeBuilder(Location)
c.add_from_dict()
c.add_to_dict()

# Compiler(OOO).add_from_dict()

# print(Location.from_dict({'l': [{'a': 1}]}))
# print(Location.from_dict({'l': [1,2,3]}))
loc = Location.from_dict({'l': [{'1': {'a': 1}}]})
print(loc)
print(Location.from_dict(loc.to_dict()))
# print(OOO())

Location.from_dict()