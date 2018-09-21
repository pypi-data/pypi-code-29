"""
import typing
"""

class PInput:
    """creates a parsable input class
    example:
    >>> import inputlib
    >>>
    >>> def foo():
    ...     print("bar :)")
    ...
    >>>
    >>> inp = inputlib.PInput()
    >>> inp.add_keyword("foo", foo)
    >>>
    >>> inp.ask()
    ::>>> foo
    bar :)
    >>>

    error example: (cotd from prev code...)
    >>> inp.ask()
    ::>>> fooi
    bad keyword: fooi
    retry

    available keywords:
    foo
    ::>>> foo
    bar :)
    >>>

    changing the input starting chars example (cotd..):
    >>> ainp = inputlib.PInput("#> ")
    >>> ainp.add_keyword("bar", foo)
    >>>
    >>> ainp.ask()
    #> bar
    bar :)
    >>>
    """
    def __init__(self, foretext="::>>> "):
        """initializes the pInput class
           see class help for an example
        """
        self.functions = {}
        self.foretext = foretext
        self.answer = None

    def add_keyword(self,
                    keyword: str,
                    keyword_callback: typing.Callable = None,
                    callback_args: tuple = (),
                    callback_kwargs: dict = {}):
        """adds a matchable keyword to be used when the ask function
           called
           see module help for an example
           """
        self.functions[keyword] = (keyword_callback,
                                   callback_args,
                                   callback_kwargs)

    def ask(self):
        """asks for an argument
           see module class for an example
        """
        kw = input(self.foretext)

        # fallback in case the keyword does not exist
        fallbackdef = (self.fallback, (kw), {})

        function, args, kwargs = self.functions.get(kw,
                                                    fallbackdef)
        return function(*args, **kwargs)

    def fallback(self, kw):
        """fallback in case ask does not return anything"""
        print(f"bad keyword: {kw}")
        print(f"retry")
        print()
        print(f"available keywords:")
        for keyword in self.functions:
            print(keyword)

        self.ask()


def get_confirmation():
    """
    returns True if the user type in yes, False if the user types in No
    """
    inp = PInput("#> ")

    def yes():
        return True

    def no():
        return False

    inp.add_keyword("yes", yes)
    inp.add_keyword("no", no)
    return inp.ask()
