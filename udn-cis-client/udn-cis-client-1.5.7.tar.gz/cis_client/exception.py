import json


class OptionException(Exception):
    pass


class UploadConflictException(Exception):
    def __init__(self, destination_path):
        self.message = "Conflict. File {} exists on remote server.".format(destination_path)


class AsperaExecutableNotFound(Exception):
    message = "Aspera executable 'ascp' is not found. Please add path to 'ascp' into PATH environment variable."


class AsperaUploadFailed(Exception):
    def __init__(self, return_code):
        self.message = "'ascp' returned non successful code {}.".format(return_code)


class HttpClientError(Exception):
    def __init__(self, response, message, reason, **kwargs):
        self.response = response
        for key, value in kwargs.items():
            if type(value) is dict:
                kwargs[key] = json.dumps(value, sort_keys=True)
        self.message = "{} {}".format(message.format(**kwargs), reason)
