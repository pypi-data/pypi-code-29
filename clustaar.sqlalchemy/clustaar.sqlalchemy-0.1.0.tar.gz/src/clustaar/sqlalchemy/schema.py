from sqlalchemy import Table

class Schema:
    """ Use in table object for make logic """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, metadata: 'Metadata') -> Table:
        return Table(*[*self.args[:1], metadata, *self.args[1:]], **self.kwargs)
