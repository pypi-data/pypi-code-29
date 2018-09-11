# -*- coding: utf-8 -*-
try:
    from django.urls import get_resolver
except ImportError:
    from django.core.urlresolvers import get_resolver

from django import http
from django_js_reverse import core


def _urls_js(fn, type):
    def view(request):
        default_urlresolver = get_resolver(getattr(request, 'urlconf', None))
        return http.HttpResponse(fn(default_urlresolver), content_type=type)

    return view

urls_js = _urls_js(core.generate_js, 'application/javascript');
urls_json = _urls_js(core.generate_json, 'application/json');
