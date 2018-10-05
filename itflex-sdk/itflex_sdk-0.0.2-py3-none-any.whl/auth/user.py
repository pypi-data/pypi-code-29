from typing import List

from dataclasses import dataclass

from itflex_sdk.auth.types import (
    CreateUserRequest,
    DeleteUserRequest,
    GetUserRequest,
    GetUsersPageRequest,
    Role,
    Scope,
    UpdateUserInfoRequest,
    UpdateUserRequest,
    User,
    UserInfo,
)
from itflex_sdk.common import SdkPage, SdkResp
from itflex_sdk.datetime import str_to_datetime
from itflex_sdk.errors import decode_errors
from itflex_sdk.paginate import Pages
from itflex_sdk.requester import HttpMethods, HttpRequest

URL = "/api/users"
URL_USER_INFO = "/api/user/info"


@dataclass
class UserResp(SdkResp):
    user: User = None


@dataclass
class UserInfoResp(SdkResp):
    user: UserInfo = None


@dataclass
class UsersPageResp(SdkPage):
    users: List[User] = None


class UsersPages(Pages):
    resp_cls = UsersPageResp

    def create_resp(self, status, payload, cursor):
        data = []
        for item in payload["users"]:

            roles = []
            for role in item["roles"]:
                roles.append(Role(id=role["id"], name=role["name"]))

            user = User(
                id=item["id"],
                username=item["username"],
                email=item["email"],
                fullname=item["fullname"],
                superuser=item["superuser"],
                roles=roles,
                created_at=str_to_datetime(item["created_at"]),
                updated_at=str_to_datetime(item["updated_at"]),
            )
            data.append(user)

        return UsersPageResp(status=status, users=data, cursor=cursor)

    def get_items(self, page):
        return page.users


def create_user(requester, request: CreateUserRequest):
    req = HttpRequest(method=HttpMethods.POST, uri=URL, json=request.to_dict())

    resp = requester.execute(req)
    if not resp.success:
        return UserResp(status=resp.status, errors=decode_errors(resp.json))

    roles = []
    for role in resp.json["roles"]:
        roles.append(Role(id=role["id"], name=role["name"]))

    return UserResp(
        status=resp.status,
        user=User(
            id=resp.json["id"],
            username=resp.json["username"],
            email=resp.json["email"],
            fullname=resp.json["fullname"],
            superuser=resp.json["superuser"],
            roles=roles,
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def update_user(requester, request: UpdateUserRequest):

    data = {}
    if request.fullname:
        data["fullname"] = request.fullname

    if request.email:
        data["email"] = request.email

    if request.password:
        data["password"] = request.password

    if request.superuser is not None:
        data["superuser"] = request.superuser

    if request.roles is not None:
        data["roles"] = request.roles

    req = HttpRequest(
        method=HttpMethods.PUT, uri=URL + "/" + str(request.id), json=data
    )

    resp = requester.execute(req)

    if not resp.success:
        return UserResp(status=resp.status, errors=decode_errors(resp.json))

    roles = []
    for role in resp.json["roles"]:
        roles.append(Role(id=role["id"], name=role["name"]))

    return UserResp(
        status=resp.status,
        user=User(
            id=resp.json["id"],
            username=resp.json["username"],
            email=resp.json["email"],
            fullname=resp.json["fullname"],
            superuser=resp.json["superuser"],
            roles=roles,
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def update_user_info(requester, request: UpdateUserInfoRequest):
    data = {}
    if request.fullname:
        data["fullname"] = request.fullname

    if request.email:
        data["email"] = request.email

    if request.password:
        data["current_password"] = request.current_password

    if request.password:
        data["password"] = request.password

    req = HttpRequest(method=HttpMethods.PUT, uri=URL_USER_INFO, json=data)

    resp = requester.execute(req)

    if not resp.success:
        return UserResp(status=resp.status, errors=decode_errors(resp.json))

    roles = []
    for role in resp.json["roles"]:
        roles.append(Role(id=role["id"], name=role["name"]))

    return UserResp(
        status=resp.status,
        user=User(
            id=resp.json["id"],
            username=resp.json["username"],
            email=resp.json["email"],
            fullname=resp.json["fullname"],
            superuser=resp.json["superuser"],
            roles=roles,
        ),
    )


def get_users_pages(requester, request: GetUsersPageRequest):
    cursor = "0"
    size = ""

    if request.cursor:
        cursor = str(request.cursor)

    if request.size:
        size = str(request.size)

    query = {"cursor": cursor, "size": size}
    req = HttpRequest(method=HttpMethods.GET, uri=URL, query=query)

    return UsersPages(requester, req, cursor)


def get_user(requester, request: GetUserRequest):

    req = HttpRequest(method=HttpMethods.GET, uri=URL + "/" + str(request.id))

    resp = requester.execute(req)
    if not resp.success:
        return UserResp(status=resp.status, errors=decode_errors(resp.json))

    roles = []
    for role in resp.json["roles"]:
        roles.append(Role(id=role["id"], name=role["name"]))

    return UserResp(
        status=resp.status,
        user=User(
            id=resp.json["id"],
            username=resp.json["username"],
            email=resp.json["email"],
            fullname=resp.json["fullname"],
            superuser=resp.json["superuser"],
            roles=roles,
            created_at=str_to_datetime(resp.json["created_at"]),
            updated_at=str_to_datetime(resp.json["updated_at"]),
        ),
    )


def get_user_info(requester):

    req = HttpRequest(method=HttpMethods.GET, uri=URL_USER_INFO)

    resp = requester.execute(req)
    if not resp.success:
        return UserInfoResp(
            status=resp.status, errors=decode_errors(resp.json)
        )

    scopes = []
    for scope in resp.json["scopes"]:
        scopes.append(
            Scope(name=scope["name"], read=scope["read"], write=scope["write"])
        )

    return UserInfoResp(
        status=resp.status,
        user=UserInfo(
            username=resp.json["username"],
            email=resp.json["email"],
            fullname=resp.json["fullname"],
            superuser=resp.json["superuser"],
            owner_type=resp.json["owner_type"],
            scopes=scopes,
        ),
    )


def delete_user(requester, request: DeleteUserRequest):
    req = HttpRequest(
        method=HttpMethods.DELETE, uri=URL + "/" + str(request.id)
    )
    resp = requester.execute(req)
    if not resp.success:
        return UserResp(status=resp.status, errors=decode_errors(resp.json))
    return UserResp(status=resp.status)
