import pytest


def test_secure_view_requires_auth(app):
    app.get('/secure', status=403)


def test_login(app):
    r = app.get('/login')
    token = str(r.json_body['token'])  # Must be str on all Python versions
    r = app.get('/secure', headers={'X-Token': token})
    assert r.unicode_body == 'OK'
