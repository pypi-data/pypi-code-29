from apitaxcore.builders.DictBuilder import DictBuilder


class Catalog(DictBuilder):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.built = {self.name: {}}

    def add(self, item):
        super().add({self.name: item})
