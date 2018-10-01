from ..lib.abc import abstractclassmethod

from . import Base


class AbstractExternalIds(Base):
    """"""

    @abstractclassmethod
    def get_baseclass(cls):
        pass
