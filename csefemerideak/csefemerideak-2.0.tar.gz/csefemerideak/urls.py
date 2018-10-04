from django.conf.urls import *
from csefemerideak import views

urlpatterns = [
    url(
        r"^hamarkada-(?P<hamarkada_slug>(\d+))$",
        views.hamarkada_index,
        name="csefemerideak_hamarkada_index",
    ),
    url(
        r"^eguna-(?P<hila_slug>(\d+))-(?P<eguna_slug>(\d+))$",
        views.eguna_index,
        name="csefemerideak_eguna_index",
    ),
    url(r"^bilaketa$", views.search_index, name="csefemerideak_search_index"),
]

