from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.staticfiles.templatetags.staticfiles import static

from landing_page.models import LandingPage


def generate_response(request, slug=None):
    """

    :param request:
    :param slug:
    :return:
    """
    page = slug and get_object_or_404(LandingPage, slug=slug) or LandingPage.objects.first()
    if not page:
        return render(request, 'landing_page/not_finished.html', {})

    layout_folder_name = page.layout.folder_name
    context = {'page': page, 'static_folder': static('landing_page/layouts/%s' % layout_folder_name)}
    return render(request, 'landing_page/layouts/%s/index.html' % layout_folder_name, context)


def by_slug(request, slug):
    """

    :param request:
    :param slug:
    :return:
    """
    return generate_response(request, slug)


def default(request):
    """

    :param request:
    :param slug:
    :return:
    """
    return generate_response(request)
