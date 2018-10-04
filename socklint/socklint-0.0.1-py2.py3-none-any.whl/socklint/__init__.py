from collections import namedtuple
from typing import Sequence, Optional
import secrets

ID_LENGTH = 16

BotGuessItem = namedtuple("BotGuessItem", ["id", "bot"])
ErrorItem = namedtuple(
    "ErrorItem", ["message", "extendedHelper", "sendReport", "reason", "location"])


class ResponseData:
    def __init__(self, **kwargs):
        self.items = kwargs.get("items", tuple())  # type: Sequence[BotGuessItem]
        self.kind = kwargs.get("kind", "")
        self.startIndex = kwargs.get("startIndex", 1)
        self.totalItems = kwargs.get("totalItems", len(self.items))
        self.currentItemCount = kwargs.get("currentItemCount", len(self.items))


class ResponseError:
    def __init__(self, **kwargs):
        if "code" not in kwargs:
            raise ValueError("code field is required and must represent an HTTP status code")

        if "errors" not in kwargs or len(kwargs["errors"]) == 0:
            raise ValueError("Must provide an errors field with ErrorItem objects")

        self.code = kwargs["code"]  # type: int
        self.errors = kwargs["errors"]  # type: Sequence[ErrorItem]
        self.message = self.errors[0].message  # type: str


class Response:
    def __init__(self, **kwargs):
        self.apiVersion = kwargs.get("apiVersion", "1.0")
        self.id = kwargs.get("id", secrets.token_hex(ID_LENGTH))  # type: str
        self.method = kwargs.get("method", "")

        if "data" in kwargs and "error" in kwargs:
            # If we gave both a data field and an error field...
            raise ValueError("Cannot have both error and data fields")
        elif not ("data" in kwargs or "error" in kwargs):
            # Else if we *didn't* give either a data field or an error field...
            raise ValueError("Must have a data field or an error field")
        else:
            self.data = kwargs.get("data", None)  # type: Optional[ResponseData]
            self.error = kwargs.get("error", None)  # type: Optional[ResponseError]
