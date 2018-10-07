__version__ = '0.11.1'


class FondueError(Exception):
    """ Base exception from which all others inherit. """
    pass


class PeeringError(FondueError):
    pass

class ConnectionReset(FondueError):
    pass