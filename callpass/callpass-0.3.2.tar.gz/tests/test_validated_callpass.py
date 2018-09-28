import pytest
from callpass import ValidatedCallpass, InvalidLicense, MalformedCallsign


def test_malformed_callsign():
    with pytest.raises(MalformedCallsign):
        ValidatedCallpass("AAAAAA")


def test_invalid_licence():
    with pytest.raises(InvalidLicense):
        ValidatedCallpass("AB3DEF")
