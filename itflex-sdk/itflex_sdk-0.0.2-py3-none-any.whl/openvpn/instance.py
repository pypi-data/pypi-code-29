from typing import List

from dataclasses import dataclass

from itflex_sdk.common import SdkPage, SdkResp
from itflex_sdk.datetime import str_to_datetime
from itflex_sdk.errors import decode_errors
from itflex_sdk.openvpn.types import (
    CreateInstanceRequest,
    DeleteInstanceRequest,
    GetInstanceRequest,
    GetInstancesPageRequest,
    Instance,
    ReloadInstanceRequest,
    UpdateInstanceRequest,
)
from itflex_sdk.paginate import Pages
from itflex_sdk.requester import HttpMethods, HttpRequest

URL = "/api/openvpn/instances"


@dataclass
class InstanceResp(SdkResp):
    instance: Instance = None


@dataclass
class InstancesPageResp(SdkPage):
    instances: List[Instance] = None


class InstancesPages(Pages):
    resp_cls = InstancesPageResp

    def create_resp(self, status, payload, cursor):
        data = []

        for item in payload["instances"]:
            instance = Instance(
                id=item["id"],
                model_id=item["model_id"],
                ca_id=item["ca_id"],
                name=item["name"],
                description=item["description"],
                country=item["country"],
                province=item["province"],
                city=item["city"],
                organization=item["organization"],
                sector=item["sector"],
                email=item["email"],
                port=item["port"],
                network=item["network"],
                proto=item["proto"],
                dhcp_enabled=item["dhcp_enabled"],
                dhcp_start=item["dhcp_start"],
                dhcp_end=item["dhcp_end"],
                dns_server=item["dns_server"],
                dns_domain=item["dns_domain"],
                push_routes=item["push_routes"],
                routes=item["routes"],
                ldap_auth=item["ldap_auth"],
                remotes=item["remotes"],
                revoked=item["revoked"],
                expired=item["expired"],
                expiry_date=str_to_datetime(item["expiry_date"]),
                created_at=str_to_datetime(item["created_at"]),
                updated_at=str_to_datetime(item["updated_at"]),
            )
            data.append(instance)

        return InstancesPageResp(status=status, instances=data, cursor=cursor)

    def get_items(self, page):
        return page.instances


def create_instance(requester, request: CreateInstanceRequest):
    req = HttpRequest(method=HttpMethods.POST, uri=URL, json=request.to_dict())

    resp = requester.execute(req)
    if not resp.success:
        return InstanceResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return InstanceResp(
        status=resp.status,
        instance=Instance(
            id=resp.json["id"],
            model_id=resp.json["model_id"],
            ca_id=resp.json["ca_id"],
            name=resp.json["name"],
            description=resp.json["description"],
            country=resp.json["country"],
            province=resp.json["province"],
            city=resp.json["city"],
            organization=resp.json["organization"],
            sector=resp.json["sector"],
            email=resp.json["email"],
            port=resp.json["port"],
            network=resp.json["network"],
            proto=resp.json["proto"],
            dhcp_enabled=resp.json["dhcp_enabled"],
            dhcp_start=resp.json["dhcp_start"],
            dhcp_end=resp.json["dhcp_end"],
            dns_server=resp.json["dns_server"],
            dns_domain=resp.json["dns_domain"],
            push_routes=resp.json["push_routes"],
            routes=resp.json["routes"],
            ldap_auth=resp.json["ldap_auth"],
            remotes=resp.json["remotes"],
            revoked=resp.json["revoked"],
            expired=resp.json["expired"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def update_instance(requester, request: UpdateInstanceRequest):
    data = {}

    if request.model_id:
        data["model_id"] = request.model_id
    if request.description:
        data["description"] = request.description
    if request.port:
        data["port"] = request.port
    if request.network:
        data["network"] = request.network
    if request.proto:
        data["proto"] = request.proto
    if request.dhcp_enabled is not None:
        data["dhcp_enabled"] = request.dhcp_enabled
    if request.dhcp_start:
        data["dhcp_start"] = request.dhcp_start
    if request.dhcp_end:
        data["dhcp_end"] = request.dhcp_end
    if request.dns_server:
        data["dns_server"] = request.dns_server
    if request.dns_domain:
        data["dns_domain"] = request.dns_domain
    if request.push_routes:
        data["push_routes"] = request.push_routes
    if request.routes:
        data["routes"] = request.routes
    if request.ldap_auth is not None:
        data["ldap_auth"] = request.ldap_auth
    if request.remotes:
        data["remotes"] = request.remotes

    req = HttpRequest(
        method=HttpMethods.PUT, uri=URL + "/" + str(request.id), json=data
    )

    resp = requester.execute(req)

    if not resp.success:
        return InstanceResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return InstanceResp(
        status=resp.status,
        instance=Instance(
            id=resp.json["id"],
            model_id=resp.json["model_id"],
            ca_id=resp.json["ca_id"],
            name=resp.json["name"],
            description=resp.json["description"],
            country=resp.json["country"],
            province=resp.json["province"],
            city=resp.json["city"],
            organization=resp.json["organization"],
            sector=resp.json["sector"],
            email=resp.json["email"],
            port=resp.json["port"],
            network=resp.json["network"],
            proto=resp.json["proto"],
            dhcp_enabled=resp.json["dhcp_enabled"],
            dhcp_start=resp.json["dhcp_start"],
            dhcp_end=resp.json["dhcp_end"],
            dns_server=resp.json["dns_server"],
            dns_domain=resp.json["dns_domain"],
            push_routes=resp.json["push_routes"],
            routes=resp.json["routes"],
            ldap_auth=resp.json["ldap_auth"],
            remotes=resp.json["remotes"],
            revoked=resp.json["revoked"],
            expired=resp.json["expired"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_instances_pages(requester, request: GetInstancesPageRequest):
    cursor = "0"
    size = ""

    if request.cursor:
        cursor = str(request.cursor)

    if request.size:
        size = str(request.size)

    query = {"cursor": cursor, "size": size}
    req = HttpRequest(method=HttpMethods.GET, uri=URL, query=query)

    return InstancesPages(requester, req, cursor)


def get_instance(requester, request: GetInstanceRequest):
    req = HttpRequest(method=HttpMethods.GET, uri=URL + "/" + str(request.id))

    resp = requester.execute(req)
    if not resp.success:
        return InstanceResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return InstanceResp(
        status=resp.status,
        instance=Instance(
            id=resp.json["id"],
            model_id=resp.json["model_id"],
            ca_id=resp.json["ca_id"],
            name=resp.json["name"],
            description=resp.json["description"],
            country=resp.json["country"],
            province=resp.json["province"],
            city=resp.json["city"],
            organization=resp.json["organization"],
            sector=resp.json["sector"],
            email=resp.json["email"],
            port=resp.json["port"],
            network=resp.json["network"],
            proto=resp.json["proto"],
            dhcp_enabled=resp.json["dhcp_enabled"],
            dhcp_start=resp.json["dhcp_start"],
            dhcp_end=resp.json["dhcp_end"],
            dns_server=resp.json["dns_server"],
            dns_domain=resp.json["dns_domain"],
            push_routes=resp.json["push_routes"],
            routes=resp.json["routes"],
            ldap_auth=resp.json["ldap_auth"],
            remotes=resp.json["remotes"],
            revoked=resp.json["revoked"],
            expired=resp.json["expired"],
            expiry_date=str_to_datetime(resp.json["expiry_date"]),
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def delete_instance(requester, request: DeleteInstanceRequest):
    req = HttpRequest(
        method=HttpMethods.DELETE, uri=URL + "/" + str(request.id)
    )
    resp = requester.execute(req)
    if not resp.success:
        return InstanceResp(
            status=resp.status, errors=decode_errors(resp.json)
        )
    return InstanceResp(status=resp.status)


def reload_instance(requester, request: ReloadInstanceRequest):
    url = "{url}/{id}/reload".format(url=URL, id=str(request.id))

    req = HttpRequest(method=HttpMethods.POST, uri=url)
    resp = requester.execute(req)

    if not resp.success:
        return InstanceResp(
            status=resp.status, errors=decode_errors(resp.json)
        )
    return InstanceResp(status=resp.status)
