import inspect
import functools

__all__ = ['tail_recurse_optimizer']


class TailRecurseException(BaseException):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_recurse_optimizer(func):
    """
    A decorator for tail recursion optimization.
    Usage example:
    >>> @tail_recurse_optimizer
    ... def fib(i, a=0, b=1):
    ...     if i == 0:
    ...         return a
    ...     else:
    ...         return fib(i - 1, b, a + b)
    >>> fib(1000)
    43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        currentframe = inspect.currentframe()  # sys._current_frames() 也可
        if currentframe.f_back and currentframe.f_back.f_back \
                and currentframe.f_back.f_back.f_code == currentframe.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return func(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    return wrapper
