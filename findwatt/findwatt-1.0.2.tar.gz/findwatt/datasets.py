"""
This module should handle operations related to the Dataset resource
"""
import os
from typing import Optional
from marshmallow import Schema, fields, post_load
import requests
from .exceptions import DoesNotExist, APIError, NotReady


class DatasetSchema(Schema):
    id = fields.Str()
    catalog_id = fields.Str(load_from="catalogId", dump_to="catalogId")
    name = fields.Str()
    url = fields.Str()
    upload_date = fields.DateTime(load_from="uploadDate", dump_to="uploadDate")
    total_rows = fields.Int(load_from="totalRows", dump_to="totalRows")

    @post_load
    def make_dataset(self, data):
        return Dataset(**data)


class Dataset(dict):
    def to_json(self) -> str:
        schema = DatasetSchema()
        return schema.dumps(self).data

    def to_dict(self) -> dict:
        schema = DatasetSchema()
        return schema.dump(self).data


class Datasets:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.auth_header = f"Bearer {self.api_key}"
        self.url = os.path.join(api_url, "datasets")

    def get(self, id: str) -> Optional[Dataset]:
        # TODO: Retry 5xx codes
        headers = {"Authorization": self.auth_header}
        url = os.path.join(self.url, id)
        resp = requests.get(url, headers=headers, allow_redirects=False)
        if resp.status_code == 200:
            schema = DatasetSchema()
            return schema.load(resp.json()).data
        if resp.status_code == 404:
            msg = f"Dataset with ID {id}"
            raise DoesNotExist(msg)
        if resp.status_code == 307:
            try_in = resp.headers.get("Retry-After", 15)
            msg = f"Try again in {try_in} seconds"
            raise NotReady(msg)
        raise APIError(resp.status_code)
