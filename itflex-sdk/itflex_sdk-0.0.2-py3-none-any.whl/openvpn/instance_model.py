from typing import List

from dataclasses import dataclass

from itflex_sdk.common import SdkPage, SdkResp
from itflex_sdk.datetime import str_to_datetime
from itflex_sdk.errors import decode_errors
from itflex_sdk.openvpn.types import (
    CreateInstanceModelRequest,
    DeleteInstanceModelRequest,
    GetInstanceModelRequest,
    GetInstancesModelsPageRequest,
    InstanceModel,
    UpdateInstanceModelRequest,
)
from itflex_sdk.paginate import Pages
from itflex_sdk.requester import HttpMethods, HttpRequest

URL = "/api/openvpn/instances/models"


@dataclass
class InstanceModelResp(SdkResp):
    instance_model: InstanceModel = None


@dataclass
class InstancesModelsPageResp(SdkPage):
    instances_models: List[InstanceModel] = None


class InstancesModelsPages(Pages):
    resp_cls = InstancesModelsPageResp

    def create_resp(self, status, payload, cursor):
        data = []

        for item in payload["instances_models"]:
            instance_model = InstanceModel(
                id=item["id"],
                name=item["name"],
                template=item["template"],
                created_at=str_to_datetime(item["created_at"]),
                updated_at=str_to_datetime(item["updated_at"]),
            )
            data.append(instance_model)

        return InstancesModelsPageResp(
            status=status, instances_models=data, cursor=cursor
        )

    def get_items(self, page):
        return page.instances_models


def create_instance_model(requester, request: CreateInstanceModelRequest):
    req = HttpRequest(method=HttpMethods.POST, uri=URL, json=request.to_dict())

    resp = requester.execute(req)
    if not resp.success:
        return InstanceModelResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return InstanceModelResp(
        status=resp.status,
        instance_model=InstanceModel(
            id=resp.json["id"],
            name=resp.json["name"],
            template=resp.json["template"],
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def update_instance_model(requester, request: UpdateInstanceModelRequest):
    data = {}

    if request.name:
        data["name"] = request.name

    if request.template:
        data["template"] = request.template

    req = HttpRequest(
        method=HttpMethods.PUT, uri=URL + "/" + str(request.id), json=data
    )

    resp = requester.execute(req)

    if not resp.success:
        return InstanceModelResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return InstanceModelResp(
        status=resp.status,
        instance_model=InstanceModel(
            id=resp.json["id"],
            name=resp.json["name"],
            template=resp.json["template"],
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_instances_models_pages(
    requester, request: GetInstancesModelsPageRequest
):
    cursor = "0"
    size = ""

    if request.cursor:
        cursor = str(request.cursor)

    if request.size:
        size = str(request.size)

    query = {"cursor": cursor, "size": size}
    req = HttpRequest(method=HttpMethods.GET, uri=URL, query=query)

    return InstancesModelsPages(requester, req, cursor)


def get_instance_model(requester, request: GetInstanceModelRequest):
    req = HttpRequest(method=HttpMethods.GET, uri=URL + "/" + str(request.id))

    resp = requester.execute(req)
    if not resp.success:
        return InstanceModelResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return InstanceModelResp(
        status=resp.status,
        instance_model=InstanceModel(
            id=resp.json["id"],
            name=resp.json["name"],
            template=resp.json["template"],
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_default_instance_model(requester):
    req = HttpRequest(method=HttpMethods.GET, uri=URL + "/default")

    resp = requester.execute(req)
    if not resp.success:
        return InstanceModelResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    return InstanceModelResp(
        status=resp.status,
        instance_model=InstanceModel(
            name=resp.json["name"], template=resp.json["template"]
        ),
    )


def delete_instance_model(requester, request: DeleteInstanceModelRequest):
    req = HttpRequest(
        method=HttpMethods.DELETE, uri=URL + "/" + str(request.id)
    )
    resp = requester.execute(req)
    if not resp.success:
        return InstanceModelResp(
            status=resp.status, errors=decode_errors(resp.json)
        )
    return InstanceModelResp(status=resp.status)
