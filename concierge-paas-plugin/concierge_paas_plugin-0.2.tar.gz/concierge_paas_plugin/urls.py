from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create_profile', views.create_profile, name="create_profile"),
    url(r'^queryprofile$', views.queryprofile, name="queryprofile"),
]