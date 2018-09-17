from .events import EventsStream
from .transactions import TransactionsStream

AVAILABLE_STREAMS = [
    EventsStream,
    TransactionsStream
]
