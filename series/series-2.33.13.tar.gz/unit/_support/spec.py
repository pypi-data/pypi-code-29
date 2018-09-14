from amino.test.spec_spec import Spec as SpecBase

from golgi.test.spec import SpecConfigConcern


class Spec(SpecConfigConcern, SpecBase):

    def setup(self, **kw) -> None:
        SpecConfigConcern.setup(self, **kw)
        SpecBase.setup(self)

__all__ = ('Spec',)
