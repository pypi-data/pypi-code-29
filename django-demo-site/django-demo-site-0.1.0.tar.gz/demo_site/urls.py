# -*- coding: utf-8 -*-
from django.urls import path

from demo_site.views import demo_site_index

app_name = 'demo_site'

urlpatterns = [
    path('', demo_site_index, name='index'),
]
