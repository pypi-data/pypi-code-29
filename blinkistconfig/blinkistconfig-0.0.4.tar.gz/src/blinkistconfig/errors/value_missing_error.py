from . import Error

class ValueMissingError(Error):
    def __init__(self, message):
        super().__init__(message)
