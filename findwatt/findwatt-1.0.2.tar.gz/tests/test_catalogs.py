import os
import datetime
import pytest
import responses
from findwatt.catalogs import Catalog, Catalogs, CatalogSchema
from findwatt.exceptions import DoesNotExist, APIError


DUMMY_DATA = {
    "id": "dummy-catalog",
    "name": "Dummy Catalog",
    "creationDate": datetime.datetime.utcnow().isoformat(),
    "activeVersions": 2,
}


def test_make_catalog():
    catalog = CatalogSchema().load(DUMMY_DATA).data
    assert isinstance(catalog, Catalog)


def test_to_json():
    catalog = CatalogSchema().load(DUMMY_DATA).data
    assert isinstance(catalog.to_json(), str)


def test_to_dict():
    catalog = CatalogSchema().load(DUMMY_DATA).data
    assert isinstance(catalog.to_dict(), dict)


def test_catalogs_properties():
    api_key = "dummy-api-key"
    url = "https://api.testing.findwatt.com"
    catalogs = Catalogs(api_key, url)
    assert catalogs.auth_header == f"Bearer {api_key}"
    assert catalogs.url == os.path.join(url, "catalogs")


@responses.activate
def test_catalogs_get():
    catalogs = Catalogs("dummy-api-key", "http://api.testing.findwatt.com")
    responses.add(
        responses.GET,
        os.path.join(catalogs.url, "dummy-catalog"),
        json=DUMMY_DATA,
        status=200,
    )
    catalog = catalogs.get("dummy-catalog")
    assert isinstance(catalog, Catalog)


@responses.activate
def test_get_nonexistent_catalog():
    catalogs = Catalogs("dummy-api-key", "http://api.testing.findwatt.com")
    responses.add(
        responses.GET,
        os.path.join(catalogs.url, "nonexistent-catalog"),
        json={"message": "Does not exist"},
        status=404,
    )
    with pytest.raises(DoesNotExist) as err:
        catalogs.get("nonexistent-catalog")
        assert err


@responses.activate
def test_get_catalog_failed():
    for error_code in [500, 502]:
        catalogs = Catalogs("dummy-api-key", "http://api.testing.findwatt.com")
        responses.add(
            responses.GET,
            os.path.join(catalogs.url, "dummy-catalog"),
            json={},
            status=error_code,
        )
        with pytest.raises(APIError) as err:
            catalogs.get("dummy-catalog")
            assert err


@responses.activate
def test_catalogs_list():
    resource = Catalogs("dummy-api-key", "http://api.testing.findwatt.com")
    responses.add(
        responses.GET, resource.url, json=[DUMMY_DATA, DUMMY_DATA], status=200
    )
    catalogs = resource.search()
    assert isinstance(catalogs, list)
    assert all(isinstance(elem, Catalog) for elem in catalogs)


@responses.activate
def test_catalogs_filter():
    resource = Catalogs("dummy-api-key", "http://api.testing.findwatt.com")
    mocked_url = f"{resource.url}?name=Dummy%20Catalog&limit=0&offset=0"
    print(f"MOCKED_URL: {mocked_url}")
    responses.add(responses.GET, mocked_url, json=[DUMMY_DATA], status=200)
    catalogs = resource.search(name="Dummy Catalog")
    assert isinstance(catalogs, list)
    assert all(isinstance(elem, Catalog) for elem in catalogs)


@responses.activate
def test_list_catalogs_error():
    for error_code in [500, 502]:
        resource = Catalogs("dummy-api-key", "http://api.testing.findwatt.com")
        responses.add(responses.GET, resource.url, json={}, status=error_code)
        with pytest.raises(APIError) as err:
            resource.search()
            assert err
