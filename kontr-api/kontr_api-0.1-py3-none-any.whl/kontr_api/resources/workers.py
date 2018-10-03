from kontr_api.resources.default import Default, Defaults
from kontr_api.resources.secrets import Secrets


class Statuses(Defaults):
    def __init__(self, parent):
        super().__init__(parent, instance_klass=Status)

    def url(self):
        return "{self.url}/status"


class Workers(Defaults):
    def __init__(self, parent):
        super().__init__(parent, instance_klass=Worker)


class Status(Default):
    pass


class Worker(Default):
    @property
    def status(self) -> Statuses:
        return Statuses(self)

    @property
    def secrets(self) -> Secrets:
        return Secrets(self)
