# -*- coding:utf-8 -*-
# create_time: 2018/9/4 10:25
__author__ = 'brad'

from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("endpoints", views.EndpointViewSet)
router.register("counters", views.CounterViewSet)
router.register("tags", views.TagViewSet)

urlpatterns = [
    url(r'^g/', include(router.urls)),
]
