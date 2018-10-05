from typing import List

from dataclasses import dataclass

from itflex_sdk.auth.types import (
    CreateRoleRequest,
    DeleteRoleRequest,
    GetRoleRequest,
    GetRolesPageRequest,
    Role,
    Scope,
    UpdateRoleRequest,
)
from itflex_sdk.common import SdkPage, SdkResp
from itflex_sdk.datetime import str_to_datetime
from itflex_sdk.errors import decode_errors
from itflex_sdk.paginate import Pages
from itflex_sdk.requester import HttpMethods, HttpRequest

URL = "/api/roles"


@dataclass
class RoleResp(SdkResp):
    role: Role = None


@dataclass
class RolesPageResp(SdkPage):
    roles: List[Role] = None


class RolesPages(Pages):
    resp_cls = RolesPageResp

    def create_resp(self, status, payload, cursor) -> SdkPage:
        data = []
        for item in payload["roles"]:

            scopes = []
            for scope in item.get("scopes", []):
                scopes.append(
                    Scope(
                        name=scope["name"],
                        read=scope["read"],
                        write=scope["write"],
                    )
                )

            role = Role(
                id=item["id"],
                name=item["name"],
                scopes=scopes,
                created_at=str_to_datetime(item["created_at"]),
                updated_at=str_to_datetime(item["updated_at"]),
            )
            data.append(role)

        return RolesPageResp(status=status, roles=data, cursor=cursor)

    def get_items(self, page):
        return page.roles


def create_role(requester, request: CreateRoleRequest):
    req = HttpRequest(method=HttpMethods.POST, uri=URL, json=request.to_dict())

    resp = requester.execute(req)
    if not resp.success:
        return RoleResp(status=resp.status, errors=decode_errors(resp.json))

    scopes = []
    for scope in resp.json["scopes"]:
        scopes.append(
            Scope(name=scope["name"], read=scope["read"], write=scope["write"])
        )

    return RoleResp(
        status=resp.status,
        role=Role(
            id=resp.json["id"],
            name=resp.json["name"],
            scopes=scopes,
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def update_role(requester, request: UpdateRoleRequest):
    data = {}
    if request.name:
        data["name"] = request.name

    if request.scopes:
        scopes = []

        for scope in request.scopes:
            scopes.append(scope.to_dict())

        data["scopes"] = scopes

    req = HttpRequest(
        method=HttpMethods.PUT, uri=URL + "/" + str(request.id), json=data
    )

    resp = requester.execute(req)

    if not resp.success:
        return RoleResp(status=resp.status, errors=decode_errors(resp.json))

    scopes = []
    for scope in resp.json["scopes"]:
        scopes.append(
            Scope(name=scope["name"], read=scope["read"], write=scope["write"])
        )

    return RoleResp(
        status=resp.status,
        role=Role(
            id=resp.json["id"],
            name=resp.json["name"],
            scopes=scopes,
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_roles_pages(requester, request: GetRolesPageRequest):
    cursor = "0"
    size = ""

    if request.cursor:
        cursor = str(request.cursor)

    if request.size:
        size = str(request.size)

    query = {"cursor": cursor, "size": size}
    req = HttpRequest(method=HttpMethods.GET, uri=URL, query=query)

    return RolesPages(requester, req, cursor)


def get_role(requester, request: GetRoleRequest):
    req = HttpRequest(method=HttpMethods.GET, uri=URL + "/" + str(request.id))

    resp = requester.execute(req)
    if not resp.success:
        return RoleResp(status=resp.status, errors=decode_errors(resp.json))

    scopes = []
    for scope in resp.json["scopes"]:
        scopes.append(
            Scope(name=scope["name"], read=scope["read"], write=scope["write"])
        )

    return RoleResp(
        status=resp.status,
        role=Role(
            id=resp.json["id"],
            name=resp.json["name"],
            scopes=scopes,
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def delete_role(requester, request: DeleteRoleRequest):
    req = HttpRequest(
        method=HttpMethods.DELETE, uri=URL + "/" + str(request.id)
    )
    resp = requester.execute(req)
    if not resp.success:
        return RoleResp(status=resp.status, errors=decode_errors(resp.json))
    return RoleResp(status=resp.status)
