class Error(Exception):
    pass


class InputError(Error):
    def __init__(self,  msg):
        """
        :type msg: str
        """
        self.msg = msg
