""" Url router for the schema viewer application
"""
from django.conf.urls import url

from core_parser_app.views.common import views as common_parser_views
from core_schema_viewer_app.views.user import views as user_views

urlpatterns = [
    url(r'^$', user_views.index,
        name='core_schema_viewer_index'),
    url(r'^oxygen-viewer/(?P<pk>\w+)$', user_views.oxygen_viewer,
        name='core_schema_viewer_oxygen_viewer'),
    url(r'^download-template$', user_views.download_template,
        name='core_schema_viewer_download_template'),
    url(r'^schema-viewer-redirect$', user_views.SchemaViewerRedirectView.as_view(),
        name='core_schema_viewer_schema_viewer_redirect'),
    url(r'^schema-viewer-tabbed/(?P<pk>\w+)$', common_parser_views.ManageModulesUserView.as_view(
            back_to_previous_url="core_schema_viewer_index",
            read_only=True,
            title="Schema Viewer"
        ),
        name='core_schema_viewer_schema_viewer_tabbed'),
]
