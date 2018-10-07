# coding: utf-8

from time import time

from pony.orm import Required, Optional, Set, LongStr

from . import ClientMixin, AuthorizationCodeMixin


__all__ = ['OAuth2ClientMixin', 'OAuth2AuthorizationCodeMixin']


class OAuth2ClientMixin(ClientMixin):
    pass


class OAuth2AuthorizationCodeMixin(AuthorizationCodeMixin):
    code = Required(str, 120, unique=True)
    client_id = Optional(str, 48)
    redirect_uri = Optional(LongStr)
    response_type = Optional(LongStr)
    scope = Optional(LongStr)
    auth_time = Required(default=time)
