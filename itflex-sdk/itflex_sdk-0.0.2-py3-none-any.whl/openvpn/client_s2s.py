from typing import List

from dataclasses import dataclass

from itflex_sdk.common import SdkPage, SdkResp
from itflex_sdk.datetime import str_to_datetime
from itflex_sdk.errors import decode_errors
from itflex_sdk.openvpn.types import (
    ClientSite2Site,
    ClientSite2SiteConfig,
    CreateClientSite2SiteRequest,
    GetClientSite2SiteConfigRequest,
    GetClientSite2SiteConfigsPageRequest,
    GetClientSite2SiteRequest,
    GetClientsSite2SitePageRequest,
    RevokeClientSite2SiteRequest,
    UpdateClientSite2SiteConfigRequest,
    UpdateClientSite2SiteRequest,
)
from itflex_sdk.paginate import Pages
from itflex_sdk.requester import HttpMethods, HttpRequest

URL = "/api/openvpn/clients/site2site"


@dataclass
class ClientSite2SiteResp(SdkResp):
    client: ClientSite2Site = None


@dataclass
class ClientsSite2SitePageResp(SdkPage):
    clients: List[ClientSite2Site] = None


class ClientsSite2SitePages(Pages):
    resp_cls = ClientsSite2SitePageResp

    def create_resp(self, status, payload, cursor):
        data = []

        for item in payload["clients"]:
            client = ClientSite2Site(
                id=item["id"],
                ca_id=item["ca_id"],
                name=item["name"],
                email=item["email"],
                description=item["description"],
                country=item["country"],
                province=item["province"],
                city=item["city"],
                organization=item["organization"],
                sector=item["sector"],
                expired=item["expired"],
                revoked=item["revoked"],
                expiry_date=str_to_datetime(item["expiry_date"]),
                created_at=str_to_datetime(item["created_at"]),
                updated_at=str_to_datetime(item["updated_at"]),
            )
            data.append(client)

        return ClientsSite2SitePageResp(
            status=status, clients=data, cursor=cursor
        )

    def get_items(self, page):
        return page.clients


@dataclass
class ClientSite2SiteConfigResp(SdkResp):
    config: ClientSite2SiteConfig = None


@dataclass
class ClientsSite2SiteConfigsPageResp(SdkPage):
    configs: List[ClientSite2SiteConfig] = None


class ClientsSite2SiteConfigsPages(Pages):
    resp_cls = ClientsSite2SiteConfigsPageResp

    def create_resp(self, status, payload, cursor):
        data = []

        for item in payload["configs"]:
            config = ClientSite2SiteConfig(
                client_id=item["client_id"],
                instance_id=item["instance_id"],
                static_ip=item["static_ip"],
                push_routes=item["push_routes"],
                iroutes=item["iroutes"],
                push_reset=item["push_reset"],
                extra_conf=item["extra_conf"],
                dns_server=item["dns_server"],
                dns_domain=item["dns_domain"],
                max_routes=item["max_routes"],
                created_at=str_to_datetime(item["created_at"]),
                updated_at=str_to_datetime(item["updated_at"]),
            )
            data.append(config)

        return ClientsSite2SiteConfigsPageResp(
            status=status, configs=data, cursor=cursor
        )

    def get_items(self, page):
        return page.configs


def create_client_site2site(requester, request: CreateClientSite2SiteRequest):
    req = HttpRequest(method=HttpMethods.POST, uri=URL, json=request.to_dict())

    resp = requester.execute(req)
    if not resp.success:
        return ClientSite2SiteResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return ClientSite2SiteResp(
        status=resp.status,
        client=ClientSite2Site(
            id=resp.json["id"],
            ca_id=resp.json["ca_id"],
            name=resp.json["name"],
            email=resp.json["email"],
            description=resp.json["description"],
            country=resp.json["country"],
            province=resp.json["province"],
            city=resp.json["city"],
            organization=resp.json["organization"],
            sector=resp.json["sector"],
            expired=resp.json["expired"],
            revoked=resp.json["revoked"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def update_client_site2site(requester, request: UpdateClientSite2SiteRequest):
    data = {}

    if request.description:
        data["description"] = request.description

    req = HttpRequest(
        method=HttpMethods.PUT, uri=URL + "/" + str(request.id), json=data
    )

    resp = requester.execute(req)

    if not resp.success:
        return ClientSite2SiteResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return ClientSite2SiteResp(
        status=resp.status,
        client=ClientSite2Site(
            id=resp.json["id"],
            ca_id=resp.json["ca_id"],
            name=resp.json["name"],
            email=resp.json["email"],
            description=resp.json["description"],
            country=resp.json["country"],
            province=resp.json["province"],
            city=resp.json["city"],
            organization=resp.json["organization"],
            sector=resp.json["sector"],
            expired=resp.json["expired"],
            revoked=resp.json["revoked"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_clients_site2site_pages(
    requester, request: GetClientsSite2SitePageRequest
):
    cursor = "0"
    query = {}

    if request.cursor:
        query["cursor"] = str(request.cursor)
        cursor = query["cursor"]

    if request.size:
        query["size"] = str(request.size)

    if request.name:
        query["name"] = request.name

    if request.instance_id:
        query["instance_id"] = str(request.instance_id)

    if request.ca_id:
        query["ca_id"] = str(request.ca_id)

    if request.status:
        query["status"] = request.status

    req = HttpRequest(method=HttpMethods.GET, uri=URL, query=query)

    return ClientsSite2SitePages(requester, req, cursor)


def get_client_site2site(requester, request: GetClientSite2SiteRequest):
    req = HttpRequest(method=HttpMethods.GET, uri=URL + "/" + str(request.id))

    resp = requester.execute(req)
    if not resp.success:
        return ClientSite2SiteResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return ClientSite2SiteResp(
        status=resp.status,
        client=ClientSite2Site(
            id=resp.json["id"],
            ca_id=resp.json["ca_id"],
            name=resp.json["name"],
            email=resp.json["email"],
            description=resp.json["description"],
            country=resp.json["country"],
            province=resp.json["province"],
            city=resp.json["city"],
            organization=resp.json["organization"],
            sector=resp.json["sector"],
            expired=resp.json["expired"],
            revoked=resp.json["revoked"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def revoke_client_site2site(requester, request: RevokeClientSite2SiteRequest):
    req = HttpRequest(
        method=HttpMethods.DELETE, uri=URL + "/" + str(request.id)
    )
    resp = requester.execute(req)
    if not resp.success:
        return ClientSite2SiteResp(
            status=resp.status, errors=decode_errors(resp.json)
        )
    return ClientSite2SiteResp(status=resp.status)


def update_client_site2site_config(
    requester, request: UpdateClientSite2SiteConfigRequest
):
    data = {}

    if request.static_ip is not None:
        data["static_ip"] = request.static_ip

    if request.push_routes is not None:
        data["push_routes"] = request.push_routes

    if request.iroutes is not None:
        data["iroutes"] = request.iroutes

    if request.push_reset is not None:
        data["push_reset"] = request.push_reset

    if request.extra_conf is not None:
        data["extra_conf"] = request.extra_conf

    if request.dns_domain is not None:
        data["dns_domain"] = request.dns_domain

    if request.dns_server is not None:
        data["dns_server"] = request.dns_server

    if request.max_routes is not None:
        data["max_routes"] = request.max_routes

    req = HttpRequest(
        method=HttpMethods.PUT,
        uri=URL
        + "/"
        + str(request.client_id)
        + "/configs/"
        + str(request.instance_id),
        json=data,
    )

    resp = requester.execute(req)
    if not resp.success:
        return ClientSite2SiteConfigResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return ClientSite2SiteConfigResp(
        status=resp.status,
        config=ClientSite2SiteConfig(
            client_id=resp.json["client_id"],
            instance_id=resp.json["instance_id"],
            static_ip=resp.json["static_ip"],
            push_routes=resp.json["push_routes"],
            iroutes=resp.json["iroutes"],
            push_reset=resp.json["push_reset"],
            extra_conf=resp.json["extra_conf"],
            dns_server=resp.json["dns_server"],
            dns_domain=resp.json["dns_domain"],
            max_routes=resp.json["max_routes"],
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_client_site2site_config(
    requester, request: GetClientSite2SiteConfigRequest
):
    req = HttpRequest(
        method=HttpMethods.GET,
        uri=URL
        + "/"
        + str(request.client_id)
        + "/configs/"
        + str(request.instance_id),
    )

    resp = requester.execute(req)
    if not resp.success:
        return ClientSite2SiteConfigResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return ClientSite2SiteConfigResp(
        status=resp.status,
        config=ClientSite2SiteConfig(
            client_id=resp.json["client_id"],
            instance_id=resp.json["instance_id"],
            static_ip=resp.json["static_ip"],
            push_routes=resp.json["push_routes"],
            iroutes=resp.json["iroutes"],
            push_reset=resp.json["push_reset"],
            extra_conf=resp.json["extra_conf"],
            dns_server=resp.json["dns_server"],
            dns_domain=resp.json["dns_domain"],
            max_routes=resp.json["max_routes"],
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_client_site2site_configs_pages(
    requester, request: GetClientSite2SiteConfigsPageRequest
):
    cursor = "0"
    query = {}

    if request.cursor:
        query["cursor"] = str(request.cursor)
        cursor = query["cursor"]

    if request.size:
        query["size"] = str(request.size)

    req = HttpRequest(
        method=HttpMethods.GET,
        uri=URL + "/" + str(request.client_id) + "/configs",
        query=query,
    )

    return ClientsSite2SiteConfigsPages(requester, req, cursor)
