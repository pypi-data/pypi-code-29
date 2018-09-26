from . import Error

class AdapterNotFoundError(Error):
    def __init__(self, message):
        super().__init__(message)
