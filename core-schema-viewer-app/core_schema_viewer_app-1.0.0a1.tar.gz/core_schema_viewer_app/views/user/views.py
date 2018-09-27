""" Schema Viewer app user views
"""
import os
from abc import ABCMeta

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import RedirectView

import core_main_app.utils.decorators as decorators
import core_schema_viewer_app.permissions.rights as rights
from core_main_app.components.template import api as template_api
from core_main_app.utils.file import get_file_http_response
from core_main_app.utils.rendering import render, django_render
from core_schema_viewer_app.settings import BASE_DIR_CORE_SCHEMA_VIEWER_APP
from core_schema_viewer_app.views.user.forms import FormDefaultTemplate


@decorators.permission_required(content_type=rights.schema_viewer_content_type,
                                permission=rights.schema_viewer_access,
                                login_url=reverse_lazy("core_main_app_login"))
def index(request):
    """ Schema views homepage provides the following features :
        - Download a schema as a xsd file
        - Browse a schema by using one of the following views :
            # <oXygen>
            # Tabbed
            # Sandbox

    Args:
        request:

    Returns:

    """

    context = {'form':  FormDefaultTemplate()}
    assets = {
        "js": [
            {
                "path": 'core_schema_viewer_app/user/js/index.js',
                "is_raw": False
            },
        ],
        "css": [
            "core_schema_viewer_app/user/css/index.css",
        ]
    }

    return render(request,
                  "core_schema_viewer_app/user/index.html",
                  context=context,
                  assets=assets)


@decorators.permission_required(content_type=rights.schema_viewer_content_type,
                                permission=rights.schema_viewer_access,
                                login_url=reverse_lazy("core_main_app_login"))
def oxygen_viewer(request, pk):
    """

    Args:
        request:
        pk:

    Returns:

    """
    template = template_api.get(pk)
    file_name_html = template.filename.replace('.xsd', '.html')
    try:
        dir_list = os.listdir(os.path.join(BASE_DIR_CORE_SCHEMA_VIEWER_APP,
                                           'core_schema_viewer_app',
                                           'templates',
                                           'core_schema_viewer_app',
                                           'common',
                                           'oxygen'))
    except OSError, e:
        message = e.strerror
        messages.add_message(request, messages.ERROR, message)
        return redirect(reverse("core_schema_viewer_index"))

    if file_name_html in dir_list:
        return django_render(request, "core_schema_viewer_app/common/oxygen/" + file_name_html)
    else:
        message = "The oxygen documentation file associated to the request template is not available. " \
                  "Please contact your administrator for further information."
        messages.add_message(request, messages.WARNING, message)
        return redirect(reverse("core_schema_viewer_index"))


def download_template(request):
    """ Download template.

    Args:
        request:

    Returns:

    """
    template_id = request.GET.get('template_id', None)
    if template_id:
        template = template_api.get(template_id)
        # return the file
        return get_file_http_response(file_content=template.content,
                                      file_name=template.display_name,
                                      content_type='application/xsd',
                                      extension=".xsd")
    else:
        return redirect(reverse("core_schema_viewer_index"))


class SchemaViewerRedirectView(RedirectView):
    __metaclass__ = ABCMeta

    def get_redirect_url(self, *args, **kwargs):
        # here we receive a template id
        template_id = self.request.GET.get('template_id', None)
        destination_view = self.request.GET.get('destination_view', None)

        if template_id and destination_view:
            destination_url = ""
            if destination_view == "oxygen":
                destination_url = "core_schema_viewer_oxygen_viewer"
            elif destination_view == "tabbed":
                destination_url = "core_schema_viewer_schema_viewer_tabbed"

            # then redirect to the result page core_schema_viewer_schema_viewer_tabbed with /<template_id>/
            return reverse(destination_url, kwargs={"pk": str(template_id)})
        else:
            # messages.add_message(self.request, messages.ERROR, 'The given URL is not valid.')
            return reverse("core_schema_viewer_index")
