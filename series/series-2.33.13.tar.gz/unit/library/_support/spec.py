from unit._support.spec import Spec as SpecBase


class Spec(SpecBase):

    def setup(self, *a, configs=['series.library'], **kw):
        super().setup(*a, configs=configs, **kw)

__all__ = ['Spec']
