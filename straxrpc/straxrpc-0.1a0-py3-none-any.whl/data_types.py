import numpy as np
import re


simple_types = [
#   name, aliases, columns_class name
    ("int32", ["int16","i4","<i4"], "Int32Array"),
    ("int64", ["<i8","i8"], "Int64Array"),
    ("float32", ["<f4","f4"], "Float32Array"),
    ("float64", ["<f8","f8"], "Float64Array"),
    ("bool", ["boolean"], "BoolArray"),
    ("string", ["str","O","o","object"],  "StringArray"),
]

simple_array_types = [

    ("int32array", ["<i4","i4"], "Int32ArrayArray"),
    ("int64array", ["<i8","i8"], "Int64ArrayArray"),
    ("float32array", ["<f4","f4"], "Float32ArrayArray"),
    ("float64array", ["<f8","f8"], "Float64ArrayArray"),
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
        if self.name=='string':
            return x.astype('str')
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

type_testers = [SimpleTester(*p) for p in simple_types] + [SimpleArrayTester(*p) for p in simple_array_types]
