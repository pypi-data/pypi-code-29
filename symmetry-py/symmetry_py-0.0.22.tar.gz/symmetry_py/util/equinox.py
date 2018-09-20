# -------------------------------------------------------------------------
# EQUINOX
# Python time utility helper methods.
# -------------------------------------------------------------------------
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta
from typing import List

DB_DATE_FORMAT = '%Y-%m-%d'
DB_TIME_FORMAT = '%H:%M:%S'
DB_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
POSTGRES_TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


def now(with_microsecond=True)->datetime:

    if with_microsecond:
        return datetime.utcnow()

    return datetime.utcnow().replace(microsecond=0)


def now_db()->datetime:
    return now(with_microsecond=False)


# def to_string_format(dt, format)



def today() -> date:
    return now().date()


def now_timestamp() -> str:
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


def from_param_date(date_str: str) -> date:
    return datetime.strptime(str(date_str), DB_DATE_FORMAT).date()


def from_param_datetime(date_str: str) -> date:
    return datetime.strptime(str(date_str), DB_DATETIME_FORMAT)


def from_postgres_timestamp(timestamp: str) -> datetime:
    return datetime.strptime(str(timestamp), POSTGRES_TIMESTAMP_FORMAT)


def from_time_id_to_time_obj(time_id) -> time:
    """
    Given a `time` stored as an integer, convert it to a time object.
    Eg. time_id -> 2555 (representing time 00:25:55)
    :param time_id:
    :return:
    """
    time_id_padded = str(time_id).zfill(6)
    return datetime.strptime(str(time_id_padded), "%H%M%S").time()

    # ---from_time_id_to_time_obj---


def to_format(dt, format) -> str:
    return dt.strftime(format)


def get_last_n_months(date, n):
    now = date

    n = n - 1

    if n <= 0:
        return [date]

    n_months_ago = now + relativedelta(months=-n)

    cursor = n_months_ago

    month_dates = []

    while cursor <= now:
        month_dates.append(cursor.strftime('%Y-%m'))

        cursor = (cursor + relativedelta(months=+1))

    # Reverse the list in descending order
    return month_dates[::-1]


# CONVERT FROM: str ----
def convert_date_str_to_date(date_str: str) -> date:
    return datetime.strptime(str(date_str), "%Y-%m-%d").date()


def convert_date_str_to_id(date_str: str) -> int:
    return convert_date_to_id(convert_date_str_to_date(date_str))


# CONVERT FROM: id ----
def convert_date_id_to_date(date_id) -> date:
    return datetime.strptime(str(date_id), "%Y%m%d").date()


def convert_date_id_to_str(date_id) -> str:
    date_obj = convert_date_id_to_date(date_id)
    return date_obj.strftime("%Y-%m-%d")


# CONVERT FROM: date ----
def convert_date_to_id(date_obj) -> int:
    return date_obj.year * 10000 + date_obj.month * 100 + date_obj.day


def convert_date_to_str(date_obj) -> str:
    return date_obj.strftime("%Y-%m-%d")


# -------------------------------------------------------------------------
# DATE RANGES
# -------------------------------------------------------------------------

def create_daily_date_ranges(date_from: date, date_to: date) -> List[date]:
    """
    :param date_from: INCLUDED.
    :param date_to: EXCLUDED. The output range does NOT contain this date.
    :return:
    """
    if date_from >= date_to:
        raise ValueError("date_from must be chronologically before date_to.")
    date_range = []
    next_date = date_from
    while next_date < date_to:
        date_range.append(next_date)
        next_date += timedelta(days=1)
    return date_range


def create_monthly_date_ranges(date_from, date_to) -> List[List[date]]:
    date_from = convert_date_id_to_date(date_from)
    date_to = convert_date_id_to_date(date_to)

    if date_from >= date_to:
        raise ValueError("date_from must be chronologically before date_to.")

    curr_month = date_from.month
    date_ranges = []
    curr_date = date(date_from.year, date_from.month, date_from.day)

    while curr_date < date_to:
        if curr_date.month < 12:
            next_month = curr_date.month + 1
            next_year = curr_date.year
        else:
            next_month = 1
            next_year = curr_date.year + 1

        next_date = date(next_year, next_month, 1)
        if next_date > date_to:
            next_date = date_to

        date_ranges.append([curr_date, next_date])
        curr_date = date(next_date.year, next_date.month, next_date.day)

    return date_ranges