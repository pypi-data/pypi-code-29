import calendar
from datetime import datetime, timedelta
from email.utils import formatdate, parsedate

from cachecontrol.heuristics import BaseHeuristic


class OneHourHeuristic(BaseHeuristic):
    def update_headers(self, response):
        date = parsedate(response.headers["date"])
        expires = datetime(*date[:6]) + timedelta(hours=1)
        return {
            "expires": formatdate(calendar.timegm(expires.timetuple())),
            "cache-control": "public",
        }

    def warning(self, _):
        msg = "Automatically cached! Response is Stale."
        return '110 - "%s"' % msg
