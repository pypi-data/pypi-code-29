__version__ = '0.11.0'


class FondueError(Exception):
    """ Base exception from which all others inherit. """
    pass


class PeeringError(FondueError):
    pass

class ConnectionReset(FondueError):
    pass