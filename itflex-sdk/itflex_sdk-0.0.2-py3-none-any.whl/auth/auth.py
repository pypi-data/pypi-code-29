from itflex_sdk.auth.apikey import (
    create_apikey,
    delete_apikey,
    get_apikey,
    get_apikeys_pages,
    update_apikey,
)
from itflex_sdk.auth.role import (
    create_role,
    delete_role,
    get_role,
    get_roles_pages,
    update_role,
)
from itflex_sdk.auth.scope import get_scopes
from itflex_sdk.auth.user import (
    create_user,
    delete_user,
    get_user,
    get_user_info,
    get_users_pages,
    update_user,
    update_user_info,
)
from itflex_sdk.common import SdkBase


class Auth(SdkBase):
    methods = [
        create_apikey,
        delete_apikey,
        get_apikey,
        get_apikeys_pages,
        update_apikey,
        create_role,
        delete_role,
        get_role,
        get_roles_pages,
        update_role,
        get_scopes,
        create_user,
        delete_user,
        get_user,
        get_user_info,
        get_users_pages,
        update_user,
        update_user_info,
    ]
