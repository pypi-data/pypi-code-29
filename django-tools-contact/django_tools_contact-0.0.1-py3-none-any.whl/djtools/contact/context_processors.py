from django.conf import settings


def settings_context(request):
    return {
        'DJTOOLS_CONTACT_GMAPS_APIKEY': settings.DJTOOLS_CONTACT_GMAPS_APIKEY
    }
