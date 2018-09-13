from datetime import datetime, date
import time


class TimeoutException(Exception):
    pass


class Timer(object):

    def __init__(self, seconds):
        self.timeout = time.time() + seconds
        self.split = None

    @classmethod
    def now(cls):
        return time.time()

    def start(self):
        pass

    def split(self):
        pass

    def stop(self):
        pass


class Datetime(object):
    DATE = "%Y-%m-%d"
    DATETIME = "%Y-%m-%d %H:%M:%S"
    TIMESTAMP = "%Y%m%d_%H%M%S"

    @classmethod
    def today(cls, to_string=False, date_separator=None):
        result = date.today()
        if to_string:
            date_format = cls.DATE
            if date_separator:
                date_format = date_format.replace("-", date_separator)
            result = result.strftime(date_format)
        return result

    @classmethod
    def now(cls, to_string=False, date_separator=None):
        result = datetime.now()
        if to_string:
            datetime_format = cls.DATETIME
            if date_separator:
                datetime_format = datetime_format.replace("-", date_separator)
            result = result.strftime(datetime_format)
        return result

    @classmethod
    def timestamp(cls, to_string=False):
        result = datetime.now()
        if to_string:
            result = result.strftime(cls.TIMESTAMP)
        return result

    @classmethod
    def parse(cls, data, data_format):
        return datetime.strptime(data, data_format)
