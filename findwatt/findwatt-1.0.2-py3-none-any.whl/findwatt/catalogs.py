"""
This module should handle operations related to the Catalog resource
"""
import os
from urllib.parse import quote
from typing import Optional
from marshmallow import Schema, fields, post_load
import requests
from .exceptions import DoesNotExist, APIError


class CatalogSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    creation_date = fields.Str(load_from="creationDate", dump_to="creationDate")
    active_versions = fields.Int(load_from="activeVersions", dump_to="activeVersions")

    @post_load
    def make_catalog(self, data):
        return Catalog(**data)


class Catalog(dict):
    def to_json(self) -> str:
        schema = CatalogSchema()
        return schema.dumps(self).data

    def to_dict(self) -> dict:
        schema = CatalogSchema()
        return schema.dump(self).data


class Catalogs:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.auth_header = f"Bearer {self.api_key}"
        self.url = os.path.join(api_url, "catalogs")

    def get(self, id: str) -> Optional[Catalog]:
        # TODO: Retry 5xx codes
        headers = {"Authorization": self.auth_header}
        url = os.path.join(self.url, id)
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            schema = CatalogSchema()
            # TODO: Handle marshaling errors
            return schema.load(resp.json()).data
        if resp.status_code == 404:
            msg = f"Catalog with ID {id} does not exist"
            raise DoesNotExist(msg)
        raise APIError(resp.status_code)

    def search(self, name: str = "", limit: int = 0, offset: int = 0):
        # TODO: Retry 5xx codes
        headers = {"Authorization": self.auth_header}
        query = f"name={quote(name.strip())}&limit={limit}&offset={offset}"
        url = f"{self.url}?{query}"
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            schema = CatalogSchema(many=True)
            data = schema.load(resp.json())
            # TODO: Handle marshaling errors
            return data.data
        raise APIError(resp.status_code)
