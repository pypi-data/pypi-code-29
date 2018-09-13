class Scenario(object):

    def __init__(self, data):
        self._data = data

    def data(self, data=None):
        if data:
            self._data = data
        return self._data
