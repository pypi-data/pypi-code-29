from datetime import datetime

class DateTimeSerializer:
    def serialize(self, dt):
        return dt.timestamp()

    def deserialize(self, value):
        return datetime.fromtimestamp(value)
