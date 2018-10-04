from django.conf.urls import *


urlpatterns = patterns(
    "csefemerideak.views",
    url(
        r"^hamarkada-(?P<hamarkada_slug>(\d+))$",
        "hamarkada_index",
        name="csefemerideak_hamarkada_index",
    ),
    url(
        r"^eguna-(?P<hila_slug>(\d+))-(?P<eguna_slug>(\d+))$",
        "eguna_index",
        name="csefemerideak_eguna_index",
    ),
    url(r"^bilaketa$", "search_index", name="csefemerideak_search_index"),
)

