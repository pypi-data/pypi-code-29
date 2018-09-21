class ControllerFileDoesNotExist(Exception):
    pass


class ControllerFileIsInvalid(Exception):
    pass


class RouteDoesNotExist(Exception):
    pass


class ExistRouteIsInvalid(Exception):
    pass


class ViewDoesNotExist(Exception):
    pass


class ExistViewFileIsInvalid(Exception):
    pass


class BadTermUsage(Exception):
    pass
