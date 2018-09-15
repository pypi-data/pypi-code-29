class OpenSenseMapAPIError(Exception):
    """
    Base Exception class raised whenever something is strange
    """
    pass

class OpenSenseMapAPIResponseError(Exception):
    """
    Exception raised when the API responded something strange
    """
    pass

class OpenSenseMapAPIAuthenticationError(OpenSenseMapAPIError):
    """
    Exception raised when the authentication failed
    """
    pass

class OpenSenseMapAPIInvalidCredentialsError(
    OpenSenseMapAPIAuthenticationError):
    """
    Exception raised when the login failed due to invalid credentials
    """
    pass

class OpenSenseMapAPIOutdatedTokenError(OpenSenseMapAPIAuthenticationError):
    """
    Exception raised when a token is outdated
    """
    pass

class OpenSenseMapAPITooManyRequestsError(OpenSenseMapAPIError):
    """
    Exception raised when a client issues too many requests
    """
    pass

class OpenSenseMapAPIPermissionError(OpenSenseMapAPIAuthenticationError):
    """
    Exception raised when the account does not have certain permissions
    """
    pass

class NoClientError(Exception):
    pass

class ConfirmationError(Exception):
    pass
