"""Models representing Page objects."""

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):
    """Represents a Page that can be accessed via it's URL."""

    class Meta:
        """Meta class definition."""

        verbose_name = _("page")
        verbose_name_plural = _("pages")

    title = models.CharField(
        verbose_name=_("title"),
        max_length=255,
        help_text=_("The title of this Page."),
    )
    access_url = models.CharField(
        verbose_name=_("access URL"),
        max_length=255,
        unique=True,
        help_text=_("The URL at which this Page can be accessed. "
                    "eg: /terms-and-conditions/"),
    )
    redirect_url = models.CharField(
        verbose_name=_("redirect URL"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The URL to redirect to when this Page is accessed."),
    )
    content = models.TextField(
        verbose_name=_("content"),
        blank=True,
        null=True,
        help_text=_("The content to be displayed in the body of this Page."),
    )
    template_name = models.CharField(
        verbose_name=_("template name"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("The name of the template to use when rendering this "
                    "page. If blank or invalid, the simple_pages/default.html "
                    "template will be used."),
    )
    enabled = models.BooleanField(
        verbose_name=_("Enabled"),
        default=True,
        blank=True,
        help_text=_("If unchecked, this model is disabled."),
    )
    created = models.DateTimeField(
        verbose_name=_("Created date/time"),
        auto_now_add=True,
        help_text=_("The date and time on which this model instance was first "
                    "created."),
    )
    modified = models.DateTimeField(
        verbose_name=_("Modified date/time"),
        auto_now=True,
        help_text=_("The date and time on which this model instance was last "
                    "modified."),
    )

    def __str__(self):
        """Return a string representation for this object."""
        if self.redirect_url:
            return "{access_url} -> {redirect_url}".format(
                access_url=self.access_url, redirect_url=self.redirect_url)
        else:
            return "{access_url}".format(access_url=self.access_url)

    @property
    def is_redirect(self):
        """Return True if a redirect_url is set."""
        return bool(self.redirect_url)

    def get_absolute_url(self):
        """Get the URL to this page (used in the 'View on site' link)."""
        return self.access_url

    def clean(self):
        """Perform per-object validation."""
        if not self.access_url.startswith("/"):
            raise ValidationError(
                message=_("The access_url must start with a '/'."))

        if self.template_name and self.template_name.startswith("/"):
            raise ValidationError(
                message=_("The template_name must not start with a '/'."))
