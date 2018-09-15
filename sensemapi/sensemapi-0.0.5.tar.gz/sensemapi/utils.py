# system modules
import logging
import datetime
import inspect
import iso8601
import json

# internal modules

# external modules

OPENSENSEMAP_DATETIME_FORMAT_UTC = "%Y-%m-%dT%H:%M:%S.000Z"

def str2date(s):
    """
    Convert a string in RFC3339 format to a Python :any:`datetime.datetime`
    object.

    Args:
        s (str) : the string to convert. Needs to be in RFC3339 format.

    Returns:
        datetime.datetime : the converted date
    """
    return iso8601.parse_date(s)

def date2str(d):
    """
    Stringify a :any:`datetime.datetime` object to RFC3339 format

    Args:
        d (datetime.datetime) : the datetime to convert

    Returns:
        str : the converted string
    """
    try:
        utc = d.astimezone(datetime.timezone.utc)
    except ValueError:
        utc = d.replace(tzinfo = datetime.timezone.utc)
    return utc.strftime(OPENSENSEMAP_DATETIME_FORMAT_UTC)

def pretty_json(d): # pragma: no cover
    """
    Pretty-format a JSON dict

    Args:
        d (dict) : the JSON dict

    Returns:
        str : the formatted string
    """
    return json.dumps(d, sort_keys = True, indent = 4)

def location_dict(lat = None, lon = None, height = None):
    """
    Create a location dict from the single values

    Args:
        lat, lon, height (float, optional) : the position

    Returns:
        dict : the location dict

    Raises:
        ValueError : if not enough values are specified
    """
    if lat is not None and lon is not None:
        if height is not None:
            return {"lat":lat, "lng":lon, "height":height}
        else:
            return {"lat":lat, "lng":lon}
    else:
        raise ValueError("At least 'lat' and 'lon' need to be defined")

def simplegetter(fn): # pragma: no cover
    """
    Property getter method decorator for easy getter setup. Getter methods
    decorated with this decorator should return the default value. When the
    property is requested, it is checked whether the internal attribute
    prefixed with ``_`` exists and if so it is returned. If not, it is set
    to the return value of the decorated method and then it is returned.

    Parameters
    ----------

    Returns
    -------

    callable
        The decorated callable
    """
    propname = fn.__name__
    attrname = "_{}".format(propname)
    try:
        inspect.getfullargspec(fn)[0]
    except KeyError:  # pragma: no cover
        raise ValueError(
            "`simplegetter` decorator can only be used for methods that take "
            "the object reference as first argument"
        )

    @property
    def getter(self):
        try:
            return getattr(self, attrname)
        except AttributeError:
            fnval = fn(self)
            setattr(self, attrname, fnval)
        return getattr(self, attrname)

    getter.__doc__ = fn.__doc__
    return getter


def simplesetter(prop, del_on_exceptions=()): # pragma: no cover
    """
    Property setter method decorator for easy setter setup. Setter methods
    decorated with this decorator should take the object reference and the new
    value as argument, modify the value as desired and return it. The return
    value will be stored in the internal attribute prefixed with
    ``_``.

    Parameters
    ----------

    prop : property
        the property
    del_on_exceptions : sequence of BaseException subclasses
        delete the internal attribute if any of these in
        :any:`exceptions` occur

    Returns
    -------

    callable
        The decorated callable
    """
    def simplesetter_decorator(fn):
        propname = fn.__name__
        attrname = "_{}".format(propname)
        try:
            inspect.getfullargspec(fn)[0]
            inspect.getfullargspec(fn)[1]
        except KeyError:  # pragma: no cover
            raise ValueError(
                "`simplegetter` decorator can only be used for methods that "
                "take the object reference as first argument and the new "
                "property value as second argument"
            )

        def setter(self, newval):
            try:
                converted = fn(self, newval)
                setattr(self, attrname, converted)
            except del_on_exceptions:
                try:
                    delattr(self, attrname)
                except AttributeError:
                    pass

        setter.__doc__ = fn.__doc__
        setter = prop.setter(setter)
        return setter

    return simplesetter_decorator
