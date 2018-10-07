import os
import io
import datetime
from tempfile import NamedTemporaryFile
import pytest
import responses
from findwatt.uploads import UploadSchema, Upload, Uploads
from findwatt.exceptions import APIError, AlreadyExists, MissingInformation


DUMMY_DATA = {
    "id": "dummy-upload",
    "filename": "dummy-file.csv",
    "catalogId": "dummy-catalog",
    "catalogName": "Dummy Catalog",
    "datasetId": "dummy-dataset",
    "sizeUploaded": 26400,
    "size": 26400,
    "mime": "text/csv",
    "startDate": datetime.datetime.utcnow().isoformat(),
    "endDate": datetime.datetime.utcnow().isoformat(),
}


def test_make_upload():
    upload = UploadSchema().load(DUMMY_DATA).data
    assert isinstance(upload, Upload)


def test_to_dict():
    upload = Upload(DUMMY_DATA)
    assert isinstance(upload.to_dict(), dict)


def test_to_json():
    upload = Upload(DUMMY_DATA)
    assert isinstance(upload.to_json(), str)


def test_uploads_properties():
    api_key = "dummy-api-key"
    url = "api.testing.findwatt.com"
    resource = Uploads(api_key, url)
    assert f"Bearer {api_key}" == resource.auth_header
    assert f"{url}/uploads" == resource.url


@responses.activate
def test_create_upload():
    resource = Uploads("dummy-api-key", "http://findwattapi.com")
    responses.add(responses.POST, resource.url, json=DUMMY_DATA, status=201)
    upload = resource.create_upload(
        file_name=DUMMY_DATA["filename"],
        file_size=DUMMY_DATA["size"],
        catalog_id=DUMMY_DATA["catalogId"],
    )
    assert isinstance(upload, Upload)


@responses.activate
def test_create_upload_catalog_already_exists():
    resource = Uploads("dummy-api-key", "http://findwattapi.com")
    responses.add(responses.POST, resource.url, json=DUMMY_DATA, status=422)
    with pytest.raises(AlreadyExists) as err:
        resource.create_upload(
            file_name=DUMMY_DATA["filename"],
            file_size=DUMMY_DATA["size"],
            catalog_id=DUMMY_DATA["catalogId"],
        )
        assert err


@responses.activate
def test_create_upload_failed():
    error_codes = [400, 500, 502]
    for code in error_codes:
        resource = Uploads("dummy-api-key", "http://findwattapi.com")
        responses.add(responses.POST, resource.url, json=DUMMY_DATA, status=code)
        with pytest.raises(APIError) as err:
            resource.create_upload(
                file_name=DUMMY_DATA["filename"],
                file_size=DUMMY_DATA["size"],
                catalog_id=DUMMY_DATA["catalogId"],
            )
            assert err


@responses.activate
def test_upload_chunk():
    resource = Uploads("dummy-api-key", "http://findwattapi.com")
    upload_id = "dummy-upload"
    resp_body = dict(**DUMMY_DATA)
    resp_body["sizeUploaded"] = 13000
    del resp_body["endDate"]
    responses.add(
        responses.PUT,
        os.path.join(resource.url, upload_id),
        json=resp_body,
        status=307,
        headers={"Range": "bytes=0-12999"},
    )
    upload, done = resource.upload_chunk(b"a" * 13000, "0-12999/26400", "dummy-upload")
    assert not done
    assert isinstance(upload, Upload)


@responses.activate
def test_upload_final_chunk():
    resource = Uploads("dummy-api-key", "http://findwattapi.com")
    upload_id = "dummy-upload"
    resp_body = dict(**DUMMY_DATA)
    resp_body["sizeUploaded"] = 26400
    responses.add(
        responses.PUT,
        os.path.join(resource.url, upload_id),
        json=resp_body,
        status=202,
        headers={"Range": "bytes=0-26399/26400"},
    )
    upload, done = resource.upload_chunk(b"a" * 13400, "0-26399/26400", "dummy-upload")
    assert done
    assert isinstance(upload, Upload)


@responses.activate
def test_upload_chunk_failed():
    for error_code in [400, 404, 500, 502]:
        resource = Uploads("dummy-api-key", "http://findwattapi.com")
        upload_id = "dummy-upload"
        resp_body = dict(**DUMMY_DATA)
        responses.add(
            responses.PUT,
            os.path.join(resource.url, upload_id),
            json=resp_body,
            status=error_code,
        )
        with pytest.raises(APIError) as err:
            resource.upload_chunk(b"a" * 13400, "0-26399/26400", "dummy-upload")
            assert err


@responses.activate
def test_upload_fileobj():
    resource = Uploads("dummy-api-key", "http://findwattapi.com")
    upload_id = "dummy-upload"
    fileobj = io.BytesIO(b"a" * 9 * 1024 * 1024)
    upload_creation_resp = dict(**DUMMY_DATA)
    upload_creation_resp["size"] = 9 * 1024 * 1024
    upload_creation_resp["uploadedSize"] = 0
    del upload_creation_resp["endDate"]
    responses.add(responses.POST, resource.url, json=upload_creation_resp, status=201)

    upload_first_chunk = dict(**upload_creation_resp)
    upload_first_chunk["uploadedSize"] = 5 * 1024 * 1024
    responses.add(
        responses.PUT,
        os.path.join(resource.url, upload_id),
        json=upload_first_chunk,
        status=307,
    )

    upload_last_chunk = dict(**upload_creation_resp)
    upload_last_chunk["uploadedSize"] = 4 * 1024 * 1024
    upload_last_chunk["endDate"] = datetime.datetime.utcnow().isoformat()
    responses.add(
        responses.PUT,
        os.path.join(resource.url, upload_id),
        json=upload_last_chunk,
        status=202,
    )

    upload = resource.upload_fileobj(
        fileobj, "dummy-file.csv", catalog_name="Dummy Catalog"
    )
    assert isinstance(upload, Upload)


def test_upload_fileobj_missing_info():
    resource = Uploads("dummy-api-key", "http://findwattapi.com")
    fileobj = io.BytesIO(b"a" * 26400)
    with pytest.raises(MissingInformation) as err:
        resource.upload_fileobj(fileobj, "dummy-file.csv")
        assert err


@responses.activate
def test_upload_fileo():
    resource = Uploads("dummy-api-key", "http://findwattapi.com")
    upload_id = "dummy-upload"
    with NamedTemporaryFile(suffix=".csv", delete=False) as new_file:
        new_file.write(b"a" * 9 * 1024 * 1024)
    filepath = new_file.name
    upload_creation_resp = dict(**DUMMY_DATA)
    upload_creation_resp["size"] = 9 * 1024 * 1024
    upload_creation_resp["uploadedSize"] = 0
    del upload_creation_resp["endDate"]
    responses.add(responses.POST, resource.url, json=upload_creation_resp, status=201)

    upload_first_chunk = dict(**upload_creation_resp)
    upload_first_chunk["uploadedSize"] = 5 * 1024 * 1024
    responses.add(
        responses.PUT,
        os.path.join(resource.url, upload_id),
        json=upload_first_chunk,
        status=307,
    )

    upload_last_chunk = dict(**upload_creation_resp)
    upload_last_chunk["uploadedSize"] = 4 * 1024 * 1024
    upload_last_chunk["endDate"] = datetime.datetime.utcnow().isoformat()
    responses.add(
        responses.PUT,
        os.path.join(resource.url, upload_id),
        json=upload_last_chunk,
        status=202,
    )

    upload = resource.upload_file(filepath, catalog_id="dummy-catalog")
    assert isinstance(upload, Upload)
