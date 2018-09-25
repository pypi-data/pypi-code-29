from mock import patch
import pytest
import pygass as pya
from pygass import constants as st


pya.ANALYTICS_URL = "https://www.google-analytics.com/debug/collect"
st.ANALYTICS_CODE = "UA-10000000-1"
CLIENT_ID = 1337


def valid_state(response):
    return response["hitParsingResult"][-1]["valid"]


def valid_url(response):
    return response["hitParsingResult"][-1]["hit"]


def valid_message(response):
    return response["parserMessage"][-1]["description"]


def test_pageview():
    result = pya.track_pageview(CLIENT_ID, "/test/client/pageview")
    assert valid_state(result) is True
    assert valid_message(result) == "Found 1 hit in the request."
    assert valid_url(
        result
    ) == "/debug/collect?v=1&tid=UA-10000000-1&cid=1337&t=pageview&dp=%2Ftest%2Fclient%2Fpageview"


def test_event():
    result = pya.track_event(CLIENT_ID, action="start", category="click")
    assert valid_message(result) == "Found 1 hit in the request."
    assert valid_state(result) is True
    assert valid_url(
        result
    ) == "/debug/collect?v=1&tid=UA-10000000-1&cid=1337&t=event&ec=click&ea=start"


def test_transaction():
    result = pya.track_transaction(CLIENT_ID, transaction_id=1)
    print(result)
    assert valid_message(result) == "Found 1 hit in the request."
    assert valid_state(result) is True
    assert valid_url(
        result
    ) == "/debug/collect?v=1&tid=UA-10000000-1&cid=1337&t=event&ti=1"


def test_item():
    result = pya.track_item(CLIENT_ID, transaction_id=1, name="item 1")
    assert valid_message(result) == "Found 1 hit in the request."
    assert valid_state(result) is True
    assert valid_url(
        result
    ) == "/debug/collect?v=1&tid=UA-10000000-1&cid=1337&t=item&ti=1&in=item+1&iq=1"


def test_social():
    result = pya.track_social(
        CLIENT_ID, action="like", network="facebook", target="/home"
    )
    assert valid_message(result) == "Found 1 hit in the request."
    assert valid_state(result) is True
    assert valid_url(
        result
    ) == "/debug/collect?v=1&tid=UA-10000000-1&cid=1337&t=social&sa=like&sn=facebook&st=%2Fhome"
