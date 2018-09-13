from abc import abstractmethod
from .basis import Basis
from .asserter import Asserter


class Reactor(Basis, Asserter):

    def __init__(self, agent=None):
        super().__init__()
        self._agent = agent

    def agent(self, agent=None):
        if agent:
            self._agent = agent
        return self._agent

    def options(self):
        result = None
        if self._agent:
            result = self._agent.options()
        return result

    def scenario(self):
        return None if not self.agent() else self.agent().scenario()

    def container(self):
        return None if not self.agent() else self.agent().container()

    @abstractmethod
    def execute(self):
        pass
