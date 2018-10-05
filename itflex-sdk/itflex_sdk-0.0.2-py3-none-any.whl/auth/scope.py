from dataclasses import dataclass

from itflex_sdk.common import SdkResp
from itflex_sdk.errors import decode_errors
from itflex_sdk.requester import HttpMethods, HttpRequest

URL = "/api/scopes"


@dataclass
class ScopesResp(SdkResp):
    scopes: list = None


def get_scopes(requester):
    req = HttpRequest(method=HttpMethods.GET, uri=URL)

    resp = requester.execute(req)
    if not resp.success:
        return ScopesResp(status=resp.status, errors=decode_errors(resp.json))

    return ScopesResp(status=resp.status, scopes=resp.json["scopes"])
