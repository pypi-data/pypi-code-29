from django.conf.urls import url
from .views import AsyncView


urlpatterns = [
    url(
        r'^(?P<app>[\w]+)/(?P<view>[\w]+)\.html$',
        AsyncView.as_view(),
        {
            'format': 'html'
        },
        name='async_view_html'
    ),
    url(
        r'^(?P<app>[\w]+)/(?P<view>[\w]+)\.js$',
        AsyncView.as_view(),
        {
            'format': 'js'
        },
        name='async_view_js'
    )
]
