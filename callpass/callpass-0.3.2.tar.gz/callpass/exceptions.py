class Callsign(Exception):
    pass


class MalformedCallsign(Callsign):
    pass


class License(Exception):
    pass


class InvalidLicense(License):
    pass


class ExpiredLicense(License):
    pass


class Server(Exception):
    pass


class ServerUpdating(Server):
    pass


class ServerStatus(Server):
    pass
