from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^upload_pic/$', views.upload_pic, name='upload_pic'),
    re_path(r'^crop_pic/$', views.crop_pic, name='crop_pic'),
]
