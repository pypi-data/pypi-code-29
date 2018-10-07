import io
from findwatt import client


class MockUploads:
    upload_file_calls = []
    upload_fileobj_calls = []

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def upload_file(cls, file_path, catalog_id, catalog_name):
        args = {
            "file_path": file_path,
            "catalog_id": catalog_id,
            "catalog_name": catalog_name,
        }
        cls.upload_file_calls.append(args)

    @classmethod
    def upload_fileobj(cls, fileobj, file_name, catalog_id, catalog_name):
        args = {
            "fileobj": fileobj,
            "file_name": file_name,
            "catalog_id": catalog_id,
            "catalog_name": catalog_name,
        }
        cls.upload_fileobj_calls.append(args)


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.orig_uploads = client.Uploads
        client.Uploads = MockUploads

    @classmethod
    def teardown_class(cls):
        client.Uploads = cls.orig_uploads

    def test_upload_file(self):
        fw_client = client.Client(
            "dummy-api-key", api_url="http://api.testing.findwatt.com"
        )

        fw_client.upload_file("dummy_file.txt", "dummy-catalog")
        last_invocation = client.Uploads.upload_file_calls[-1]
        assert last_invocation.get("file_path")
        assert last_invocation.get("catalog_id")

    def test_upload_fileobj(self):
        fw_client = client.Client(
            "dummy-api-key", api_url="http://api.testing.findwatt.com"
        )
        fileobj = io.BytesIO(b"Dummy file content")
        fw_client.upload_fileobj(
            fileobj, "dummy-file.txt", catalog_name="Dummy Catalog"
        )
        last_invocation = client.Uploads.upload_fileobj_calls[-1]
        assert last_invocation.get("fileobj")
        assert last_invocation.get("catalog_name")
