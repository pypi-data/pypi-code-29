from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from csefemerideak.models import Efemeridea

from datetime import date, timedelta
from django.db.models import Min, Max


def _text_to_fulltext_search(t):
    """ """
    return "+%s*" % t.replace(" ", "* +")


def _get_archive():
    """ """
    h = {}
    h["hamarkadak"] = []
    efemerideak = Efemeridea.objects.filter(is_public=True).aggregate(
        Min("date"), Max("date")
    )
    h_aurrena = efemerideak["date__min"].year // 10
    h_azkena = efemerideak["date__max"].year // 10
    for hamarkada in range(h_aurrena, h_azkena + 1):
        h2 = {}
        h2["hamarkada"] = hamarkada * 10
        h2["kopurua"] = Efemeridea.objects.filter(
            is_public=True, hamarkada=hamarkada * 10
        ).count()
        if h2["kopurua"]:
            h["hamarkadak"].append(h2)
    h["egunak"] = []
    # bisiestoa
    e_aurrena = date(2012, 1, 1)
    e_azkena = date(2013, 1, 1)
    for d in range(0, (e_azkena - e_aurrena).days):
        e = e_aurrena + timedelta(days=d)
        h2 = {}
        h2["eguna"] = e.day
        h2["hila"] = e.month
        h2["kopurua"] = Efemeridea.objects.filter(
            is_public=True, hila=e.month, eguna=e.day
        ).count()
        h["egunak"].append(h2)
    return h


def index(request):
    h = {}
    h["archive"] = _get_archive()
    h["efemerideak"] = Efemeridea.objects.filter(is_public=True).order_by("-date")
    return render(request, "csefemerideak/index.html", h)


def eguna_index(request, hila_slug, eguna_slug):
    h = {}
    h["archive"] = _get_archive()
    h["title"] = "Eguna: %s-%s" % (hila_slug, eguna_slug)
    h["efemerideak"] = Efemeridea.objects.filter(
        is_public=True, hila=hila_slug, eguna=eguna_slug
    ).order_by("-date")
    return render(request, "csefemerideak/index_filtered.html", h)


def hamarkada_index(request, hamarkada_slug):
    h = {}
    h["archive"] = _get_archive()
    h["title"] = "Hamarkada: %s" % (hamarkada_slug)
    h["efemerideak"] = Efemeridea.objects.filter(
        is_public=True, hamarkada=hamarkada_slug
    ).order_by("-date")
    return render(request, "csefemerideak/index_filtered.html", h)


def search_index(request):
    """ """
    h = {}
    h["archive"] = _get_archive()
    bilatutakoa = request.GET.get("bilatutakoa", "")
    if request.method == "GET" and bilatutakoa:
        h["bilatutakoa"] = bilatutakoa
        t = _text_to_fulltext_search(bilatutakoa)
        h["efemerideak"] = Efemeridea.objects.filter(
            is_public=True, text__search=t
        ).order_by("-date")
        h["kopurua"] = len(h["efemerideak"])
        h["bilaketa_egin_da"] = True
    else:
        h["bilatutakoa"] = ""
        h["bilaketa_egin_da"] = False

    return render(request, "csefemerideak/index_searched.html", h)

