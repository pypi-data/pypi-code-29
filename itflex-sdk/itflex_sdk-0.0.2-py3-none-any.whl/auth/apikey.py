from typing import List

from dataclasses import dataclass

from itflex_sdk.auth.types import (
    Apikey,
    CreateApikeyRequest,
    DeleteApikeyRequest,
    GetApikeyRequest,
    GetApikeysPageRequest,
    Role,
    UpdateApikeyRequest,
)
from itflex_sdk.common import SdkPage, SdkResp
from itflex_sdk.datetime import str_to_datetime
from itflex_sdk.errors import decode_errors
from itflex_sdk.paginate import Pages
from itflex_sdk.requester import HttpMethods, HttpRequest

URL = "/api/3rdparty/apikeys"


@dataclass
class ApikeyResp(SdkResp):
    apikey: Apikey = None


@dataclass
class ApikeysPageResp(SdkPage):
    apikeys: List[Apikey] = None


class ApikeysPages(Pages):
    resp_cls = ApikeysPageResp

    def create_resp(self, status, payload, cursor):
        data = []
        for item in payload["apikeys"]:

            roles = []
            for role in item["roles"]:
                roles.append(Role(id=role["id"], name=role["name"]))

            apikey = Apikey(
                id=item["id"],
                name=item["name"],
                token=item["token"],
                superuser=item["superuser"],
                roles=roles,
                created_at=str_to_datetime(item["created_at"]),
                updated_at=str_to_datetime(item["updated_at"]),
            )
            data.append(apikey)

        return ApikeysPageResp(status=status, apikeys=data, cursor=cursor)

    def get_items(self, page):
        return page.apikeys


def create_apikey(requester, request: CreateApikeyRequest):
    req = HttpRequest(method=HttpMethods.POST, uri=URL, json=request.to_dict())

    resp = requester.execute(req)
    if not resp.success:
        return ApikeyResp(status=resp.status, errors=decode_errors(resp.json))

    roles = []
    for role in resp.json["roles"]:
        roles.append(Role(id=role["id"], name=role["name"]))

    return ApikeyResp(
        status=resp.status,
        apikey=Apikey(
            id=resp.json["id"],
            name=resp.json["name"],
            token=resp.json["token"],
            superuser=resp.json["superuser"],
            roles=roles,
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def update_apikey(requester, request: UpdateApikeyRequest):
    data = {}
    if request.name:
        data["name"] = request.name

    if request.superuser is not None:
        data["superuser"] = request.superuser

    if request.roles is not None:
        data["roles"] = request.roles

    req = HttpRequest(
        method=HttpMethods.PUT, uri=URL + "/" + str(request.id), json=data
    )

    resp = requester.execute(req)

    if not resp.success:
        return ApikeyResp(status=resp.status, errors=decode_errors(resp.json))

    roles = []
    for role in resp.json["roles"]:
        roles.append(Role(id=role["id"], name=role["name"]))

    return ApikeyResp(
        status=resp.status,
        apikey=Apikey(
            id=resp.json["id"],
            name=resp.json["name"],
            token=resp.json["token"],
            superuser=resp.json["superuser"],
            roles=roles,
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_apikeys_pages(requester, request: GetApikeysPageRequest):
    cursor = "0"
    size = ""

    if request.cursor:
        cursor = str(request.cursor)

    if request.size:
        size = str(request.size)

    query = {"cursor": cursor, "size": size}
    req = HttpRequest(method=HttpMethods.GET, uri=URL, query=query)

    return ApikeysPages(requester, req, cursor)


def get_apikey(requester, request: GetApikeyRequest):

    req = HttpRequest(method=HttpMethods.GET, uri=URL + "/" + str(request.id))

    resp = requester.execute(req)
    if not resp.success:
        return ApikeyResp(status=resp.status, errors=decode_errors(resp.json))

    roles = []
    for role in resp.json["roles"]:
        roles.append(Role(id=role["id"], name=role["name"]))

    return ApikeyResp(
        status=resp.status,
        apikey=Apikey(
            id=resp.json["id"],
            name=resp.json["name"],
            token=resp.json["token"],
            superuser=resp.json["superuser"],
            roles=roles,
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def delete_apikey(requester, request: DeleteApikeyRequest):
    req = HttpRequest(
        method=HttpMethods.DELETE, uri=URL + "/" + str(request.id)
    )
    resp = requester.execute(req)
    if not resp.success:
        return ApikeyResp(status=resp.status, errors=decode_errors(resp.json))
    return ApikeyResp(status=resp.status)
