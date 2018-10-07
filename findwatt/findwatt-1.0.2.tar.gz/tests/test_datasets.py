import os
import datetime
import pytest
import responses
from findwatt.datasets import DatasetSchema, Dataset, Datasets
from findwatt.exceptions import DoesNotExist, APIError, NotReady


DUMMY_DATA = {
    "id": "dummy-dataset",
    "catalogId": "dummy-catalog",
    "name": "Dummy Dataset",
    "uploadDate": datetime.datetime.utcnow().isoformat(),
    "totalRows": 65,
}


def test_make_dataset():
    dataset = DatasetSchema().load(DUMMY_DATA).data
    assert isinstance(dataset, Dataset)


def test_to_dict():
    dataset = Dataset(**DUMMY_DATA)
    assert isinstance(dataset.to_dict(), dict)


def test_to_json():
    dataset = Dataset(**DUMMY_DATA)
    assert isinstance(dataset.to_json(), str)


def test_datasets_properties():
    datasets = Datasets("dummy-api-key", "http://api.testing.findwatt.com")
    assert datasets.auth_header == f"Bearer dummy-api-key"
    assert datasets.url == "http://api.testing.findwatt.com/datasets"


@responses.activate
def test_datasets_get():
    datasets = Datasets("dummy-api-key", "http://api.testing.findwatt.com")
    responses.add(
        responses.GET,
        os.path.join(datasets.url, "dummy-dataset"),
        json=DUMMY_DATA,
        status=200,
    )
    dataset = datasets.get("dummy-dataset")
    assert isinstance(dataset, Dataset)


@responses.activate
def test_dataset_get_not_ready():
    datasets = Datasets("dummy-api-key", "http://api.testing.findwatt.com")
    responses.add(
        responses.GET,
        os.path.join(datasets.url, "pending-dataset"),
        json={},
        status=307,
    )
    with pytest.raises(NotReady) as err:
        datasets.get("pending-dataset")
        assert err


@responses.activate
def test_datasets_get_nonexistent():
    dataset_id = "nonexistent-dataset"
    datasets = Datasets("dummy-api-key", "http://api.testing.findwatt.com")
    responses.add(
        responses.GET, os.path.join(datasets.url, dataset_id), json={}, status=404
    )
    with pytest.raises(DoesNotExist) as err:
        dataset = datasets.get(dataset_id)
        assert err


@responses.activate
def test_datasets_get_api_error():
    dataset_id = "dummy-dataset"
    for error_code in [500, 502]:
        datasets = Datasets("dummy-api-key", "http://api.testing.findwat.com")
        responses.add(
            responses.GET,
            os.path.join(datasets.url, dataset_id),
            json={},
            status=error_code,
        )
        with pytest.raises(APIError) as err:
            datasets.get(dataset_id)
            assert err
