from enum import Enum

from casino_persistent.exceptions.api_errors import ApiError


class Status(Enum):
    RUNNING = 'running'
    CALCULATED = 'calculated'
    ENDED = 'ended'

    @classmethod
    def from_name(cls, name) -> Enum:
        for status in Status:
            print(status.value)
            if status.value == name.lower():
                return status
            raise ApiError(f'{name} is not a valid status name. Status in ({[e.value for e in Status]})')
