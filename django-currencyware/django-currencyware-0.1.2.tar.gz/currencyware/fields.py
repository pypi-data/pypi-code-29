from django.contrib.db import models

from . import defaults as defs


class CurrencyField(models.CharField):
    """ Custom Currency Filed """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 3)
        kwargs.setdefault('choices', defs.ALL_CURRENCY_CODES)
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"
