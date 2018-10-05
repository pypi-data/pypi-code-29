from itflex_sdk.common import SdkPage
from itflex_sdk.errors import decode_errors


class Pages:
    resp_cls = None

    def __init__(self, requester, request, cursor=None):
        self.requester = requester
        self.request = request
        self.current_cursor = cursor
        self.previous_cursor = None
        self.next_cursor = None
        self.first = True

    def create_resp(self, status, payload, cursor) -> SdkPage:
        raise NotImplementedError

    def get_items(self, page):
        raise NotImplementedError

    def has_next(self) -> bool:
        return bool(self.next_cursor)

    def has_previous(self) -> bool:
        return bool(self.previous_cursor)

    def _get_page(self, cursor) -> SdkPage:
        self.request.query["cursor"] = cursor
        resp = self.requester.execute(self.request)

        if not resp.success:
            return self.resp_cls(
                status=resp.status,
                errors=decode_errors(resp.json),
                cursor=cursor,
            )

        self.current_cursor = resp.json["cursor"]["current"]
        self.next_cursor = resp.json["cursor"]["next"]
        self.previous_cursor = resp.json["cursor"]["previous"]
        self.first = False

        return self.create_resp(
            status=resp.status,
            payload=resp.json,
            cursor=int(self.current_cursor),
        )

    def next(self) -> SdkPage:
        cursor = self.next_cursor
        if self.first:
            cursor = self.current_cursor

        if not self.first and cursor is None:
            return

        return self._get_page(cursor)

    def previous(self) -> SdkPage:
        if self.previous_cursor is None:
            return

        return self._get_page(self.previous_cursor)

    def __iter__(self):
        page = self.next()

        while page:
            items = self.get_items(page)

            for item in items:
                yield item

            page = self.next()
