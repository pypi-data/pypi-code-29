import pytest

from antaresia import load
from antaresia import exceptions


def test_travis():
    config = load("examples/travis.ppy")
    assert config == {
        "after_success": ["python-codacy-coverage -r coverage.xml"],
        "install": ["pip install tox tox-travis", "pip install codacy-coverage"],
        "language": "python",
        "python": ["3.6"],
        "script": ["tox"],
    }


def test_travis_fail():
    with pytest.raises(exceptions.MyPyFail):
        load("examples/travis.failmypy.ppy")


def test_expression():
    config = load("examples/expression.ppy")
    assert config == ["foo", "bar"]