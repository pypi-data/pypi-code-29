import inspect


def get_classname(o):
    """ Returns the classname of an object r a class

    :param o:
    :return:
    """
    if inspect.isclass(o):
        target = o
    elif callable(o):
        target = o
    else:
        target = o.__class__
    try:
        return target.__qualname__
    except AttributeError:  # pragma: no cover
        return target.__name__


def fqn(o):
    """Returns the fully qualified class name of an object or a class

    :param o: object or class
    :return: class name

    >>> import django_db_logging
    >>> fqn('str')
    Traceback (most recent call last):
    ...
    ValueError: Invalid argument `str`
    >>> class A(object):
    ...     def method(self):
    ...         pass
    >>> str(fqn(A))
    'django_db_logging.utils.A'

    >>> str(fqn(A()))
    'django_db_logging.utils.A'

    >>> str(fqn(A.method))
    'django_db_logging.utils.A.method'

    >>> str(fqn(django_db_logging))
    'django_db_logging'


    """
    parts = []
    if hasattr(o, '__module__'):
        parts.append(o.__module__)
        parts.append(get_classname(o))
    elif inspect.ismodule(o):
        return o.__name__
    if not parts:
        raise ValueError("Invalid argument `%s`" % o)
    return ".".join(parts)
