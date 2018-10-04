class TypeMisMatch(ValueError):
    def __init__(self, value, *expected):
        actual = type(value).__name__
        expected_names = ", ".join(x.__name__ for x in expected)
        super(TypeMisMatch, self).__init__("expected {}; got {} ({})".format(expected_names, value, actual))

class NotUpdatable(Exception):
    """The stage is not updatable"""
    pass

def typecheck(value, *types):
    for t in types:
        if isinstance(value, t):
            return True
    raise TypeMisMatch(value, types)

