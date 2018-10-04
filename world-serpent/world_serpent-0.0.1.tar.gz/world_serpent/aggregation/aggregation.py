from .stage import Stage, AddFields, Project, Lookup, Skip, Limit, Sort, Match
from ..utils.typecheck import typecheck, NotUpdatable


class Aggregation(object):
    """
    Aggregation is a representation of a Mongo Aggregation. It provides a set
    of methods that allows you to easily construct aggregations using the Stage
    class. It is iterable and will cast Stage as a dict while iterating.
    This allows one to cast it as a list and pass it to pymongo's aggregate function.
    i.e.:
        class MyAggregation(Aggregation):
            pass
        my_aggregation = MyAggregation()
        db.collection.aggregate(list(my_aggregation))
    """

    def __init__(self):
        self._stages = []

    def __iter__(self):
        for item in self._stages:
            yield dict(item)

    def add_field(self, field, expression):
        return self.add_fields({ field: expression })

    def add_fields(self, fields):
        return self.__append(AddFields(fields))

    def project(self, specifications):
        return self.__append(Project(specifications))

    def lookup(self, collection_to_join, local_field, foreign_field, output_array_field):
        return self.__append(Lookup(collection_to_join, local_field, foreign_field, output_array_field))

    def skip(self, integer):
        return self.__append(Skip(integer))

    def limit(self, integer):
        return self.__append(Limit(integer))

    def sort(self, field, sort_order):
        sort_order = self.__convert_sort_order(sort_order)
        return self.sorts({ field: sort_order })

    def sorts(self, fields):
        return self.__append(Sort(fields))

    def match(self, query):
        return self.__append(Match(query))

    @property
    def last(self):
        try:
            return self._stages[-1]
        except IndexError:
            return None

    def __append(self, stage):
        """
        Checks that the appended stage is a non-empty dict.
        Could in the future provide syntax validation for aggregations
        """
        typecheck(stage, Stage)
        if type(self.last) is type(stage):
            try:
                self.last.update(stage)
                return self
            except NotUpdatable:
                pass

        self._stages.append(stage)
        return self

    def __convert_sort_order(self, sort_order):
        typecheck(sort_order, str, int)
        if sort_order == 'desc':
            return -1
        elif sort_order == 'asc':
            return 1
        elif sort_order in [1, -1]:
            return sort_order
        else:
            raise InvalidSortOrder

class InvalidSortOrder(Exception):
    """sort order must be 'desc', 'asc' 1, or -1"""
    pass

