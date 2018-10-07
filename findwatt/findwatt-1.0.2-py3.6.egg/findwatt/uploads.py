"""
This module contains logic to handle requests to the /uploads resource
"""
import os
import io
from typing import Optional, Tuple
import requests
from marshmallow import Schema, fields, post_load
from .exceptions import MissingInformation, AlreadyExists, APIError


class UploadSchema(Schema):
    id = fields.Str()
    filename = fields.Str()
    catalog_id = fields.Str(load_from="catalogId", dump_to="catalogId")
    catalog_name = fields.Str(load_from="catalogName", dump_to="catalogName")
    dataset_id = fields.Str(load_from="datasetId", dump_to="datasetId")
    size = fields.Int()
    size_uploaded = fields.Int(load_from="sizeUpladed", dump_to="sizeUploaded")
    mime = fields.Str()
    start_date = fields.DateTime(load_from="startDate", dump_to="startDate")
    end_date = fields.DateTime(load_from="endDate", dump_to="endDate")

    @post_load
    def make_upload(self, data):
        return Upload(**data)


class Upload(dict):
    def to_dict(self) -> dict:
        schema = UploadSchema()
        return schema.dump(self).data

    def to_json(self) -> str:
        schema = UploadSchema()
        return schema.dumps(self).data


class Uploads:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.auth_header = f"Bearer {self.api_key}"
        self.url = os.path.join(api_url, "uploads")
        self.chunk_size = 5 * 1024 * 1024

    def upload_file(
        self,
        file_path: str,
        catalog_id: Optional[str] = None,
        catalog_name: Optional[str] = None,
    ):
        filename = os.path.basename(file_path)
        with open(file_path, "rb") as f:
            buff = io.BytesIO(f.read())
        return self.upload_fileobj(buff, filename, catalog_id, catalog_name)

    def upload_fileobj(
        self,
        fileobj: io.BytesIO,
        file_name: str,
        catalog_id: Optional[str] = None,
        catalog_name: Optional[str] = None,
    ) -> Optional[Upload]:
        if not catalog_id and not catalog_name:
            msg = "Must provide either catalog_id or catalog_name"
            raise MissingInformation(msg)
        file_size = fileobj.getbuffer().nbytes
        upload = self.create_upload(
            file_name, file_size, catalog_id=catalog_id, catalog_name=catalog_name
        )
        while True:
            initial_byte = fileobj.tell()
            chunk = fileobj.read(self.chunk_size)
            if not chunk:
                break
            final_byte = initial_byte + len(chunk) - 1
            content_range = f"{initial_byte}-{final_byte}/{file_size}"
            upload, done = self.upload_chunk(chunk, content_range, upload["id"])
            if done:
                return upload
        return None

    def create_upload(
        self,
        file_name: str,
        file_size: int,
        catalog_id: Optional[str] = None,
        catalog_name: Optional[str] = None,
    ) -> Optional[Upload]:
        # TODO: Retry 5xx codes
        headers = {"Authorization": self.auth_header}
        payload = {"size": file_size, "filename": file_name}
        if catalog_id:
            payload["catalogId"] = catalog_id
        elif catalog_name:
            payload["catalogName"] = catalog_name
        resp = requests.post(self.url, headers=headers, json=payload)
        if resp.status_code == 201:
            schema = UploadSchema()
            return schema.load(resp.json()).data
        elif resp.status_code == 422:
            msg = f"A Catalog named {catalog_name} already exists"
            raise AlreadyExists(msg)
        raise APIError(resp.status_code)

    def upload_chunk(
        self, chunk: bytes, content_range: str, upload_id: str
    ) -> Tuple[Upload, bool]:
        # TODO: Retry 5xx codes
        url = os.path.join(self.url, upload_id)
        headers = {
            "Content-Type": "application/octect-stream",
            "Content-Range": content_range,
            "Authorization": self.auth_header,
        }
        resp = requests.put(url, headers=headers, data=chunk, allow_redirects=False)
        if resp.status_code in [202, 307]:
            schema = UploadSchema()
            upload = schema.load(resp.json()).data
            if resp.status_code == 202:
                return upload, True
            elif resp.status_code == 307:
                return upload, False
        raise APIError(resp.status_code)
