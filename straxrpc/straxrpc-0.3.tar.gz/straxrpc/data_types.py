import numpy as np
import re
from . import straxrpc_pb2
from . import straxrpc_pb2_grpc
# supported types 

simple_types = [
#   name, aliases, columns_class name
    ("int32", ["int16","i4","<i4"], "int32"),
    ("int64", ["<i8","i8"], "int64"),
    ("float32", ["<f4","f4"], "float32"),
    ("float64", ["<f8","f8"], "float64"),
    ("bool", ["boolean"], "bool"),
    ("string", ["str","O","o","object"],  "string"),
]

simple_array_types = [

    ("int32array", ["<i4","i4"], "Int32Array"),
    ("int64array", ["<i8","i8"], "Int64Array"),
    ("float32array", ["<f4","f4"], "Float32Array"),
    ("float64array", ["<f8","f8"], "Float64Array"),
]

class TypeTester:
    def test(self, name):
        raise NotImplementedError

    def cast(self,x):
        return x

class SimpleTester(TypeTester):
    def __init__(self, name, aliases, column_class):
        self.name = name
        self.aliases = aliases
        self.column_class = column_class
    
    def test(self,name):
        if (name.lower() == self.name) or (name in self.aliases):
            return True
        return False

    def cast(self,x):
        if self.name=="string":
            return str(x)
        return x

class SimpleArrayTester(TypeTester):
    def __init__(self, name, aliases, column_class):
        self.name = name
        self.aliases = aliases
        self.column_class = column_class
        self.ms = [re.compile("\('<{}', \(\d*,\)\)".format(alias)) for alias in aliases]

    def test(self, name):
        for m in self.ms:
            res = m.match(name)
            if res:
                return True
        return False

    def cast(self, x):
        return getattr(straxrpc_pb2, self.column_class)(value=x)

type_testers = [SimpleTester(*p) for p in simple_types] + [SimpleArrayTester(*p) for p in simple_array_types]
