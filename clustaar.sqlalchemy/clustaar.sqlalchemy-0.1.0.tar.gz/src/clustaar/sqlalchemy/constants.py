import re


# Used in the Table class to detect & convert Sort Unary Expressions (-field1, +field2))
SQLALCHEMY_SORT_SYNTAX_RE = re.compile(r"(\+|\-)([\w\.]+)")
