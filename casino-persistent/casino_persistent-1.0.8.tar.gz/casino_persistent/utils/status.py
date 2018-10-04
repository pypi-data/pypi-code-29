import logging
from enum import Enum


class Status(Enum):
    RUNNING = 'running'
    CALCULATING = 'calculating'
    PENDING = 'pending'
    SUCCESS = 'success'
    FAILED = 'failed'
    ENDING = 'ending'
    ENDED = 'ended'

    @classmethod
    def from_name(cls, name) -> Enum:
        for status in Status:
            print(status.value)
            if status.value == name.lower():
                return status
        logging.debug(f'{name} is not a valid status name. Status in ({[e.value for e in Status]})')
