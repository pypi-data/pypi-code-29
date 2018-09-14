import json

from flask import Blueprint

from diku_tools.diku_tools.calendars import Calendar
from ..tools import get_user

bp = Blueprint('calendar', __name__)


@bp.route("/calendar/today")
def calendar_today():
    user = get_user()
    calendar = Calendar(user["username"])
    today = calendar.get_day(2018, 9, 13)
    events = []
    for event in today:
        events.append(event.to_dict())
    return json.dumps(events)
