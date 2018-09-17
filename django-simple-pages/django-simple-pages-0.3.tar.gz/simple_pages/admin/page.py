"""Admin classes for the simple_pages.models.page.Page model."""

from django import forms
from django.contrib.admin import register, ModelAdmin
from django.utils.translation import ugettext_lazy as _

from ..models import Page
from ..widgets import CodeMirrorTextarea


class PageAddForm(forms.ModelForm):
    """Form to change an existing Page."""

    class Meta:
        """Meta class definition."""

        model = Page
        fields = (
            "title",
            "access_url",
        )


class PageChangeForm(forms.ModelForm):
    """Form to change an existing Page."""

    class Meta:
        """Meta class definition."""

        model = Page
        exclude = (
            "created",
            "modified",
        )

    def __init__(self, *args, **kwargs):
        """Ensure the content field is using the CodeMirrorTextarea widget."""
        super(PageChangeForm, self).__init__(*args, **kwargs)
        self.fields["content"].widget = CodeMirrorTextarea(mode="htmlmixed")


@register(Page)
class PageModelAdmin(ModelAdmin):
    """ModelAdmin for simple_pages.models.Page."""

    list_display = (
        "id",
        "title",
        "access_url",
        "is_redirect",
        "enabled",
        "created",
    )
    list_filter = (
        "created",
        "modified",
        "enabled",
    )
    ordering = (
        "access_url",
    )
    search_fields = (
        "title",
        "access_url",
        "redirect_url",
    )
    readonly_fields = (
        "created",
        "modified",
    )

    def add_view(self, request, form_url="", extra_context=None):
        """Render the admin's add view."""
        self.form = PageAddForm
        self.fieldsets = (
            (_("Page content"), {
                "fields": (
                    "title",
                    "access_url",
                )
            }),
        )
        return super(PageModelAdmin, self).add_view(
            request=request,
            form_url=form_url,
            extra_context=extra_context
        )

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """Render the admin's change view."""
        self.form = PageChangeForm
        self.fieldsets = (
            (_("Page content"), {
                "fields": (
                    "title",
                    "access_url",
                    "content",
                )
            }),
            (_("Advanced"), {
                "fields": (
                    "enabled",
                    "redirect_url",
                    "template_name",
                ),
            }),
            (_("Readonly fields"), {
                "classes": ("collapse", ),
                "fields": (
                    "created",
                    "modified",
                ),
            }),
        )
        return super(PageModelAdmin, self).change_view(
            request=request,
            object_id=object_id,
            form_url=form_url,
            extra_context=extra_context
        )

    def is_redirect(self, obj):
        """Return True if the input object is a redirect Page."""
        return obj.is_redirect
    is_redirect.boolean = True
