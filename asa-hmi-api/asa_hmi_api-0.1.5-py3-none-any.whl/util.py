

class AsaHmiException(IOError):
    """Base class for related exceptions."""

SerialNotOpenException = AsaHmiException("SerialNotOpen")
