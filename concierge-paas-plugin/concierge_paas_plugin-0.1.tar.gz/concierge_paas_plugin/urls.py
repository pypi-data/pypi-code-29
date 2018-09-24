from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_profile', views.create_profile, name="create_profile"),
    url(r'^queryprofile$', views.queryprofile, name="queryprofile"),
]