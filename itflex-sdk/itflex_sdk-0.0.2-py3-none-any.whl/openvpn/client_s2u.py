from typing import List

from dataclasses import dataclass

from itflex_sdk.common import SdkPage, SdkResp
from itflex_sdk.datetime import str_to_datetime
from itflex_sdk.errors import decode_errors
from itflex_sdk.openvpn.types import (
    ClientSite2User,
    CreateClientSite2UserRequest,
    GetClientSite2UserRequest,
    GetClientsSite2UserPageRequest,
    RevokeClientSite2UserRequest,
    UpdateClientSite2UserRequest,
)
from itflex_sdk.paginate import Pages
from itflex_sdk.requester import HttpMethods, HttpRequest

URL = "/api/openvpn/clients/site2user"


@dataclass
class ClientSite2UserResp(SdkResp):
    client: ClientSite2User = None


@dataclass
class ClientsSite2UserPageResp(SdkPage):
    clients: List[ClientSite2User] = None


class ClientsSite2UserPages(Pages):
    resp_cls = ClientsSite2UserPageResp

    def create_resp(self, status, payload, cursor):
        data = []

        for item in payload["clients"]:
            client = ClientSite2User(
                id=item["id"],
                ca_id=item["ca_id"],
                instance_id=item["instance_id"],
                name=item["name"],
                email=item["email"],
                description=item["description"],
                ip=item["ip"],
                push_routes=item["push_routes"],
                revoked=item["revoked"],
                expired=item["expired"],
                expiry_date=str_to_datetime(item["expiry_date"]),
                created_at=str_to_datetime(item["created_at"]),
                updated_at=str_to_datetime(item["updated_at"]),
            )
            data.append(client)

        return ClientsSite2UserPageResp(
            status=status, clients=data, cursor=cursor
        )

    def get_items(self, page):
        return page.clients


def create_client_site2user(requester, request: CreateClientSite2UserRequest):
    req = HttpRequest(method=HttpMethods.POST, uri=URL, json=request.to_dict())

    resp = requester.execute(req)
    if not resp.success:
        return ClientSite2UserResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return ClientSite2UserResp(
        status=resp.status,
        client=ClientSite2User(
            id=resp.json["id"],
            ca_id=resp.json["ca_id"],
            instance_id=resp.json["instance_id"],
            name=resp.json["name"],
            email=resp.json["email"],
            description=resp.json["description"],
            ip=resp.json["ip"],
            push_routes=resp.json["push_routes"],
            revoked=resp.json["revoked"],
            expired=resp.json["expired"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def update_client_site2user(requester, request: UpdateClientSite2UserRequest):
    data = {}

    if request.description:
        data["description"] = request.description
    if request.ip:
        data["ip"] = request.ip
    if request.push_routes:
        data["push_routes"] = request.push_routes

    req = HttpRequest(
        method=HttpMethods.PUT, uri=URL + "/" + str(request.id), json=data
    )

    resp = requester.execute(req)

    if not resp.success:
        return ClientSite2UserResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return ClientSite2UserResp(
        status=resp.status,
        client=ClientSite2User(
            id=resp.json["id"],
            ca_id=resp.json["ca_id"],
            instance_id=resp.json["instance_id"],
            name=resp.json["name"],
            email=resp.json["email"],
            description=resp.json["description"],
            ip=resp.json["ip"],
            push_routes=resp.json["push_routes"],
            revoked=resp.json["revoked"],
            expired=resp.json["expired"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_clients_site2user_pages(
    requester, request: GetClientsSite2UserPageRequest
):
    cursor = "0"
    size = ""

    if request.cursor:
        cursor = str(request.cursor)

    if request.size:
        size = str(request.size)

    query = {"cursor": cursor, "size": size}
    req = HttpRequest(method=HttpMethods.GET, uri=URL, query=query)

    return ClientsSite2UserPages(requester, req, cursor)


def get_client_site2user(requester, request: GetClientSite2UserRequest):
    req = HttpRequest(method=HttpMethods.GET, uri=URL + "/" + str(request.id))

    resp = requester.execute(req)
    if not resp.success:
        return ClientSite2UserResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return ClientSite2UserResp(
        status=resp.status,
        client=ClientSite2User(
            id=resp.json["id"],
            ca_id=resp.json["ca_id"],
            instance_id=resp.json["instance_id"],
            name=resp.json["name"],
            email=resp.json["email"],
            description=resp.json["description"],
            ip=resp.json["ip"],
            push_routes=resp.json["push_routes"],
            revoked=resp.json["revoked"],
            expired=resp.json["expired"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def revoke_client_site2user(requester, request: RevokeClientSite2UserRequest):
    req = HttpRequest(
        method=HttpMethods.DELETE, uri=URL + "/" + str(request.id)
    )
    resp = requester.execute(req)

    if not resp.success:
        return ClientSite2UserResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return ClientSite2UserResp(status=resp.status)
