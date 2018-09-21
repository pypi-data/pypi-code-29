import json as jsonlib

import pytest

from mocket.plugins.httpretty import HTTPretty

from simpl_client import GamesAPIClient


SIMPL_GAMES_URL = 'http://dummy.org'
SIMPL_GAMES_AUTH = ('user', 'user')


@pytest.fixture
def simpl_url():
    return SIMPL_GAMES_URL


@pytest.fixture
def simpl_auth():
    return SIMPL_GAMES_AUTH


@pytest.fixture
def games_client(simpl_url, simpl_auth):
    return GamesAPIClient(url=simpl_url, auth=simpl_auth)


@pytest.fixture
def register_json(simpl_url):
    def fn(method, url, json=None, **kwargs):
        if json is not None:
            body = jsonlib.dumps(json)
        else:
            body = ''
        kwargs.setdefault('content-type', 'application/json')
        kwargs.setdefault('match_querystring', True)
        return HTTPretty.register_uri(method, simpl_url + url, body, **kwargs)
    return fn
