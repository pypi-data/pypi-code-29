"""Premeditated logical Fork class and its standalone mixin functions."""


from .composedfunction import ComposedFunction, resolve_composed_functions


class Fork:
    """
    Premeditated logical fork whose order of path selection is determined on
    instantiation and used to select values on call.

    Initialize
    ==========
    Instantiate the fork with keyword/value pair arguments, in order of
    preference, where the keyword (a.k.a. path) for each `True` value will be
    appended to the list of order preference.

    Call Initialized Instance
    =========================
    Calls to an instantiated fork with keyword/value pair arguments will return
    the value of the first keyword (a.k.a. path) found in the list of path
    order preference made on instantiation. Preferential path's value, before
    returning, will be ran through `resolve_composed_functions` function which
    will recursively replace all `ComposedFunctions` with its return value (see
    `naguine.core.composedfunction`).
    """

    class PathNotAvailable(Exception):
        """
        Raise to indicate a failed attempt to select among paths that are not
        available for the current, instantiated, fork.
        """
        pass

    def __init__(self, **kwargs):
        """
        Creates this fork's list of preferential paths from passed in keyword
        arguments (`kwargs`) whose values are `True` and creates direct access
        to the `ComposedFunction` class through this fork's instance.
        """

        self.__path_preference_order = []
        for path, chosen in kwargs.items():
            if chosen is True:
                self.__path_preference_order.append(path)

        self.ComposedFunction = ComposedFunction

    def __call__(self, **kwargs):
        data = self.__get_preferential_value(kwargs)
        data = resolve_composed_functions(data)

        return data

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.path_preference_order}>'

    def __get_preferential_value(self, paths, index=0):
        """
        Returns the preferential path's value. Preferential path being the
        first keyword (a.k.a. path) found in the path order list created on
        instantiation.
        """

        try:
            value = paths[self.path_preference_order[index]]
        except KeyError:
            value = self.__get_preferential_value(paths, (index + 1))
        except IndexError:
            msg = ('Cannot fork to any of the provided path\'s values. '
                   'Perhaps add a fallback path (set to `True`) in your '
                   'fork\'s instantiation?')
            raise self.PathNotAvailable(msg)

        return value

    @property
    def path_preference_order(self):
        return self.__path_preference_order

    @property
    def most_preferential_path(self):
        return self.path_preference_order[0]
