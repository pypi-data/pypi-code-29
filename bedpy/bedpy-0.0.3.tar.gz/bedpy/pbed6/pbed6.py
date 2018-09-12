from .base import BASE

class PBED6(BASE):
    def depad(self):
        from ..bed6 import BED6
        return BED6(*[
            self.chromosome,
            self.original_start,
            self.original_stop,
            self.name,
            self.score,
            self.strand
        ])
