from abc import abstractmethod
from .basis import Basis
from .asserter import Asserter


class Container(Basis, Asserter):

    def __init__(self, agent=None):
        super().__init__()
        self._agent = agent
        self._contents = []

    def agent(self, agent=None):
        if agent:
            self._agent = agent
        return self._agent

    def scenario(self):
        return None if not self.agent() else self.agent().scenario()

    def reactor(self):
        return None if not self.agent() else self.agent().reactor()

    def contents(self, key=None, value=None):
        if key and value:
            self._contents.append((key, value))
        return self._contents
