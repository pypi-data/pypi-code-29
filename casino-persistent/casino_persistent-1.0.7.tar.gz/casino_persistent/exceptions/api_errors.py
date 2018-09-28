class ApiError(Exception):
    def __init__(self, arg):
        self.error = arg
        self.args = {arg}
