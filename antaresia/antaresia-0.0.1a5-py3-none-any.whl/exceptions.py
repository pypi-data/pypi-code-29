class AnataresiaException(Exception): pass

class MyPyFail(AnataresiaException):
    def __str__(self):
        # TODO improve
        return "Failed MyPy Check."