# -*- coding: utf-8 -*-


class ResultError(Exception):
    """
    Invocation error
    """

    def __init__(self, name, code, msg):
        super().__init__()
        self.name = name
        self.code = code
        self.msg = msg

    def __str__(self):
        return '{}({}), {}'.format(self.name, self.code, self.msg)
