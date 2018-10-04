from ..utils.typecheck import typecheck, NotUpdatable

class IntegerNotPositive(Exception):
    """Integer must be positive"""
    pass

class IntegerNotWholeNumber(Exception):
    """Integer must be whole number"""
    pass

def check_positive_integer(integer):
    if integer < 1:
        raise IntegerNotPositive

def check_whole_number(integer):
    if integer < 0:
        raise IntegerNotWholeNumber

class Stage(object):
    """
    Stage is a representation of a stage in a mongo aggregation.
    It provides some rudimentary typechecking that can be expanded in the future.
    """
    def __init__(self, operation, arguments):
        self._operation, self._arguments = operation, arguments

    def __iter__(self):
        yield '$' + self._operation, self._arguments

    def update(self, stage):
        assert self._operation == stage._operation
        self._arguments.update(stage._arguments)

class AddFields(Stage):
    def __init__(self, fields):
        typecheck(fields, dict)
        super(AddFields, self).__init__('addFields', fields)

class Project(Stage):
    def __init__(self, specifications):
        typecheck(specifications, dict)
        super(Project, self).__init__('project', specifications)

class Sort(Stage):
    def __init__(self, fields):
        typecheck(fields, dict)
        super(Sort, self).__init__('sort', fields)

class Match(Stage):
    def __init__(self, query):
        typecheck(query, dict)
        super(Match, self).__init__('match', query)

class Lookup(Stage):
    def __init__(self, collection_to_join, local_field, foreign_field, output_array_field):
        for attribute in [collection_to_join, local_field, foreign_field, output_array_field]:
            typecheck(attribute, str)

        arguments = {
            'from': collection_to_join,
            'localField': local_field,
            'foreignField': foreign_field,
            'as': output_array_field
        }
        super(Lookup, self).__init__('lookup', arguments)

    def update(self, stage):
        raise NotUpdatable

class Skip(Stage):
    def __init__(self, positive_integer):
        typecheck(positive_integer, int)
        check_whole_number(positive_integer)
        super(Skip, self).__init__('skip', positive_integer)

    def update(self, stage):
        raise NotUpdatable

class Limit(Stage):
    def __init__(self, positive_integer):
        typecheck(positive_integer, int)
        check_positive_integer(positive_integer)
        super(Limit, self).__init__('limit', positive_integer)

    def update(self, stage):
        raise NotUpdatable

