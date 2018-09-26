from si.client import Client
import pytest


def test_url():
    client = Client("access_token", url="http://localhost:8080")
    assert client._url == "http://localhost:8080"

def test_default_url():
    client = Client("access_token")
    assert client._url == "https://app.trademark-ai.com/_api"

def test_access_token():
    client = Client("access_token")
    assert client._access_token == "access_token"
    assert client._session.headers['Authorization'] == "apiKey access_token"

def test_access_token_change():
    client = Client("access_token")
    client.set_auth("access_token1")
    assert client._access_token == "access_token1"
    assert client._session.headers['Authorization'] == "apiKey access_token1"

def test_trademark_exists():
    client = Client("access_token")
    assert client.trademark 