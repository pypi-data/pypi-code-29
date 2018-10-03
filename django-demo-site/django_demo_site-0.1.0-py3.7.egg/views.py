from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _


from .models import (AccessToken, DemoSiteSettings)
from django.conf import settings


if not hasattr(settings, 'DEMO_SITE_ACCESS_TOKEN_REQUIRED'):
    raise Exception("demo-site added to INSTALLED_APPS, but DEMO_SITE_ACCESS_TOKEN_REQUIRED not set in settings.py.")

atr = getattr(settings, 'DEMO_SITE_ACCESS_TOKEN_REQUIRED')
if not atr:
    if not hasattr(settings, 'DEMO_SITE_DEFAULT_URL'):
        raise Exception("demo-site added to INSTALLED_APPS, but DEMO_SITE_DEFAULT_URL not set in settings.py.")


def demo_site_index(request):
    """

    :param request:
    :return:
    """
    msg = None
    if request.POST:
        access_token = request.POST.get('used_token')
        if not access_token:
            msg = _('Enter an access token to continue.')
        else:
            status, success_url = AccessToken.is_valid(access_token)
            if status:
                return redirect(success_url)
            msg = _('Access token is not valid.')

    return render(request, 'demo_site/index.html', {'msg': msg, 'demo_site': DemoSiteSettings.current_settings()})
