from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NlxMiddlewareConfig(AppConfig):
    name = 'nlx_middleware'
    verbose_name = _("NLx middleware")
