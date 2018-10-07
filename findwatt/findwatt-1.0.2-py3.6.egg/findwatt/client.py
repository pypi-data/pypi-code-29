"""
Client for FindWAtt's API
"""
import io
from typing import Optional
from .uploads import Uploads
from .catalogs import Catalogs
from .datasets import Datasets


class Client:
    def __init__(self, api_key: str, api_url: str = "https://api.findwatt.com/v1/"):
        self.api_key = api_key
        self.auth_header = f"Bearer {self.api_key}"
        self.api_url = api_url
        self.uploads = Uploads(api_key, api_url)
        self.catalogs = Catalogs(api_key, api_url)
        self.datasets = Datasets(api_key, api_url)

    def upload_file(
        self,
        file_path: str,
        catalog_id: Optional[str] = None,
        catalog_name: Optional[str] = None,
    ):
        return self.uploads.upload_file(
            file_path, catalog_id=catalog_id, catalog_name=catalog_name
        )

    def upload_fileobj(
        self,
        fileobj: io.BytesIO,
        file_name: str,
        catalog_id: Optional[str] = None,
        catalog_name: Optional[str] = None,
    ):
        return self.uploads.upload_fileobj(
            fileobj, file_name, catalog_id=catalog_id, catalog_name=catalog_name
        )
