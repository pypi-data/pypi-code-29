from django.apps import apps
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CurrencywareConfig(AppConfig):
    """
    Configuration entry point for the currencyware app
    """
    label = name = 'currencyware'
    verbose_name = _("currencyware app")
