import uuid
from django.core.cache import cache
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
try:
    from singular_api.client import Client
    from singular_api.exceptions import SessionMismatchException
except ModuleNotFoundError:
    from .client import Client
    from .exceptions import SessionMismatchException


def get_client_id():
    return settings.CLIENT_ID


def get_client_secret():
    return settings.CLIENT_SECRET


def build_full_url(request, url):
    hostname = request.META['HTTP_HOST']
    debug = getattr(settings, 'DEBUG', True)
    connection_protocol = getattr(settings, 'CONNECTION_PROTOCOL', 'https')
    if debug:
        hostname = settings.DOMAIN
    return '{}://{}{}'.format(connection_protocol, hostname, url)


def init_singular(request):
    """
    init_singular endpoint is called from singular center when user wants to use this connector,
    works only with django
    :param request:
    :return django redirect obj:
    """

    callback_uri = request.GET.get('callback')
    state = uuid.uuid4()
    cache.set(state, callback_uri, timeout=60)
    redirect_uri = build_full_url(request, reverse('register_user_singular'))

    client = Client()
    scopes = ['all']  # TODO replace with proper scopes
    url = client.get_authorization_url(get_client_id(),
                                       redirect_uri,
                                       state,
                                       scopes)

    return redirect(url)


def register_user(request):
    """
    register_user_singular endpoint is called from singular after redirect in
    init_singular.
    :param request:
    :return token, refresh_token:

    """
    code = request.GET.get('code')
    state = request.GET.get('state')

    original_callback = cache.get(state)
    if original_callback is None:
        raise SessionMismatchException

    redirect_uri = build_full_url(request, reverse('register_user_singular'))

    client = Client()
    token, refresh_token = client.register_user(get_client_id(),
                                                get_client_secret(),
                                                code,
                                                redirect_uri)
