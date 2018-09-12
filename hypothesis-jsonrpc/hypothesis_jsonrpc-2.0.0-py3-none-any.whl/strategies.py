from typing import Dict, List, Union

import hypothesis.strategies as hs
import hypothesis_json.strategies as js
from hypothesis.searchstrategy import SearchStrategy
from hypothesis_json._utils import validate_bool
from hypothesis_json.errors import InvalidArgument, InvalidArgumentValue
from hypothesis_json.typing import JSON


def requests(
    *, infs: bool = False, nan: bool = False, max_leaves: int = 50
) -> SearchStrategy[JSON]:
    """Strategy to generate random valid JSON-RPC 2.0 requests."""
    return hs.composite(_requests)(infs=infs, nan=nan, max_leaves=max_leaves)


def _ensure_structure(j: JSON) -> Union[List[JSON], Dict[str, JSON]]:
    if not isinstance(j, (list, dict)):
        j = [j]
    return j


def _requests(draw, *, infs, nan, max_leaves):  # type: ignore
    validate_bool(infs)
    validate_bool(nan)
    if not isinstance(max_leaves, int):
        raise InvalidArgument()
    if max_leaves < 0:
        raise InvalidArgumentValue()
    req = draw(
        hs.fixed_dictionaries(
            {
                "jsonrpc": hs.just("2.0"),
                "id": js.primitives(
                    default=False, null=True, integers=True, strings=True
                ),
                "method": js.primitives(default=False, strings=True),
                "params": js.jsons(infs=infs, nan=nan, max_leaves=max_leaves),
            }
        )
    )
    if isinstance(req["id"], int):
        if draw(hs.booleans()):
            req["id"] = float(req["id"])
    elif req["id"] is None:
        del req["id"]
    req["params"] = _ensure_structure(req["params"])
    if not req["params"]:
        if draw(hs.booleans()):
            del req["params"]
    return req


def invalid_requests(
    *, infs: bool = False, nan: bool = False, max_leaves: int = 10
) -> SearchStrategy[JSON]:
    """Strategy to generate invalid JSON-RPC 2.0 requests by mutating valid requests."""
    return hs.composite(_invalid_requests)(
        infs=infs, nan=nan, max_leaves=max_leaves
    )


def _invalid_requests(draw, infs, nan, max_leaves):  # type: ignore
    validate_bool(infs)
    validate_bool(nan)
    if not isinstance(max_leaves, int):
        raise InvalidArgument()
    if max_leaves < 0:
        raise InvalidArgumentValue()
    req = draw(requests(infs=infs, nan=nan, max_leaves=max_leaves))
    omit = object()
    bad = {  # type: ignore
        "jsonrpc": hs.one_of(
            hs.just(omit),
            hs.sampled_from(
                [
                    2,
                    2.0,
                    "2",
                    "2.",
                    "2.00",
                    "02.0",
                    "2,0",
                    "20",
                    " 2.0",
                    "2.0 ",
                    "2 0",
                    "2. 0",
                    "2 .0",
                    ["2.0"],
                    {"2.0": "2.0"},
                ]
            ),
            js.jsons(infs=infs, nan=nan, max_leaves=max_leaves).filter(
                lambda j: j != "2.0"
            ),
        ),
        "id": js.jsons(
            infs=infs,
            nan=nan,
            integers=False,
            strings=False,
            max_leaves=max_leaves,
        ),
        "method": hs.one_of(
            hs.just(omit),
            js.jsons(
                infs=infs, nan=nan, strings=False, max_leaves=max_leaves
            ),
        ),
        "params": js.primitives(infs=infs, nan=nan),
    }
    keys = draw(
        hs.lists(
            hs.sampled_from(sorted(req.keys())),
            min_size=1,
            max_size=len(req),
            unique=True,
        )
    )
    for key in keys:
        req[key] = draw(bad[key])
        if req[key] is omit:
            del req[key]
    return req
