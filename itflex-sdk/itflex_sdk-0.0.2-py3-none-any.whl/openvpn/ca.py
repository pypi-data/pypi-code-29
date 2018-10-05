from typing import List

from dataclasses import dataclass

from itflex_sdk.common import SdkPage, SdkResp
from itflex_sdk.datetime import str_to_datetime
from itflex_sdk.errors import decode_errors
from itflex_sdk.openvpn.types import (
    Ca,
    CreateCaRequest,
    DeleteCaRequest,
    GetCaRequest,
    GetCasPageRequest,
    UpdateCaRequest,
)
from itflex_sdk.paginate import Pages
from itflex_sdk.requester import HttpMethods, HttpRequest

URL = "/api/openvpn/cas"


@dataclass
class CaResp(SdkResp):
    ca: Ca = None


@dataclass
class CasPageResp(SdkPage):
    cas: List[Ca] = None


class CasPages(Pages):
    resp_cls = CasPageResp

    def create_resp(self, status, payload, cursor):
        data = []

        for item in payload["cas"]:
            ca = Ca(
                id=item["id"],
                name=item["name"],
                description=item["description"],
                country=item["country"],
                province=item["province"],
                city=item["city"],
                organization=item["organization"],
                sector=item["sector"],
                email=item["email"],
                expiry_date=str_to_datetime(item["expiry_date"]),
                created_at=str_to_datetime(item["created_at"]),
                updated_at=str_to_datetime(item["updated_at"]),
            )
            data.append(ca)

        return CasPageResp(status=status, cas=data, cursor=cursor)

    def get_items(self, page):
        return page.cas


def create_ca(requester, request: CreateCaRequest):
    req = HttpRequest(method=HttpMethods.POST, uri=URL, json=request.to_dict())

    resp = requester.execute(req)
    if not resp.success:
        return CaResp(status=resp.status, errors=decode_errors(resp.json))

    return CaResp(
        status=resp.status,
        ca=Ca(
            id=resp.json["id"],
            name=resp.json["name"],
            description=resp.json["description"],
            country=resp.json["country"],
            province=resp.json["province"],
            city=resp.json["city"],
            organization=resp.json["organization"],
            sector=resp.json["sector"],
            email=resp.json["email"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def update_ca(requester, request: UpdateCaRequest):
    data = {}

    if request.description:
        data["description"] = request.description

    req = HttpRequest(
        method=HttpMethods.PUT, uri=URL + "/" + str(request.id), json=data
    )

    resp = requester.execute(req)

    if not resp.success:
        return CaResp(status=resp.status, errors=decode_errors(resp.json))

    return CaResp(
        status=resp.status,
        ca=Ca(
            id=resp.json["id"],
            name=resp.json["name"],
            description=resp.json["description"],
            country=resp.json["country"],
            province=resp.json["province"],
            city=resp.json["city"],
            organization=resp.json["organization"],
            sector=resp.json["sector"],
            email=resp.json["email"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_cas_pages(requester, request: GetCasPageRequest):
    cursor = "0"
    size = ""

    if request.cursor:
        cursor = str(request.cursor)

    if request.size:
        size = str(request.size)

    query = {"cursor": cursor, "size": size}
    req = HttpRequest(method=HttpMethods.GET, uri=URL, query=query)

    return CasPages(requester, req, cursor)


def get_ca(requester, request: GetCaRequest):
    req = HttpRequest(method=HttpMethods.GET, uri=URL + "/" + str(request.id))

    resp = requester.execute(req)
    if not resp.success:
        return CaResp(status=resp.status, errors=decode_errors(resp.json))

    return CaResp(
        status=resp.status,
        ca=Ca(
            id=resp.json["id"],
            name=resp.json["name"],
            description=resp.json["description"],
            country=resp.json["country"],
            province=resp.json["province"],
            city=resp.json["city"],
            organization=resp.json["organization"],
            sector=resp.json["sector"],
            email=resp.json["email"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def delete_ca(requester, request: DeleteCaRequest):
    req = HttpRequest(
        method=HttpMethods.DELETE, uri=URL + "/" + str(request.id)
    )
    resp = requester.execute(req)
    if not resp.success:
        return CaResp(status=resp.status, errors=decode_errors(resp.json))
    return CaResp(status=resp.status)
