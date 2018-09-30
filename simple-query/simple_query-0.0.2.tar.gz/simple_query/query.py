class Query:

    def __init__(self, data):
        self.data = [item for item in data]

    def all(self):
        return self.data

    def filter(self, field, operator, value):
        criteria = Criteria(field, operator, value)
        return Query(filter(criteria.includes, self.data))


class Criteria:

    def __init__(self, field, operator, value):
        self.field_for = Field(field).get_for
        self.matches = Matcher(operator, value).matches

    def includes(self, item):
        return self.matches(self.field_for(item))


class Matcher:

    def __init__(self, operator, value):
        self.value = value
        self.operator = operator

    def matches(self, target_value):
        return self.operator(target_value, self.value)


class Field:

    def __init__(self, field):
        self.field = field

    def get_for(self, item):
        return getattr(item, self.field)
