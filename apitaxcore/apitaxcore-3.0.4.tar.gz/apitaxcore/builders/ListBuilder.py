# Builder class for creating headers dynamically
class DictBuilder:
    def __init__(self):
        self.built = []

    def add(self, item):
        self.built.append(item)
        return self

    def get(self):
        return self.built