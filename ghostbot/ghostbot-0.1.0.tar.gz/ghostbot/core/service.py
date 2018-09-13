from abc import abstractmethod


class Service(object):

    @abstractmethod
    def startup(self):
        pass

    def restart(self):
        self.shutdown()
        self.startup()

    @abstractmethod
    def shutdown(self):
        pass
