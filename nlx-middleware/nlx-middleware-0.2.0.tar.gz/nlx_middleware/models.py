from django.db import models
from django.utils.translation import ugettext_lazy as _

from .settings import app_settings


class NLxService(models.Model):
    """
    Define a service registered with NLx.

    Note: there is a pending feature request on NLx
    (https://gitlab.com/commonground/nlx/issues/316) where we'd like to fetch
    the service config from the directory.

    TODO: validators
    """
    organisation = models.SlugField(_("organisation"))
    service = models.SlugField(_("service"))
    address = models.URLField(
        _("address"), max_length=255,
        help_text=_("Network-address where this service is provided. Must be the canonical URL."),
        unique=True
    )

    class Meta:
        verbose_name = _("NLx service")
        verbose_name_plural = _("NLx services")
        unique_together = ('organisation', 'service')

    def __str__(self):
        return _("{org}/{service} -> {address}").format(
            org=self.organisation,
            service=self.service,
            address=self.address
        )

    @property
    def outway_address(self) -> str:
        return f'{app_settings.outway_address}/{self.organisation}/{self.service}'
