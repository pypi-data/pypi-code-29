"""
This module is responsible for turning your cardinal inputs into their ordinal representations
"""


class NonOrdinalizableException(Exception):
    """
    Should be raised when the input cannot be turned into an ordinal
    """
    pass


def ordinalize(cardinal):
    """
    Ordinalizes the input number. If a non-integer input is give, exception is raised.
    :param cardinal: an integer is expected
    :raise: NonOrdinalizableException if input is not an integer
    :return: The ordinal string for the given cardinal number
    """
    if is_not_a_non_negative_integer(cardinal) and is_not_a_non_negative_numeric_string(cardinal):
        raise NonOrdinalizableException("{} is not a non-negative int".format(cardinal))

    cardinal = str(cardinal)
    if cardinal.endswith("1") and not cardinal.endswith("11"):
        cardinal += "st"
    elif cardinal.endswith("2") and not cardinal.endswith("12"):
        cardinal += "nd"
    elif cardinal.endswith("3") and not cardinal.endswith("13"):
        cardinal += "rd"
    else:
        cardinal += "th"

    return cardinal


def is_not_a_non_negative_integer(candidate):
    return not isinstance(candidate, int) or candidate < 0


def is_not_a_non_negative_numeric_string(candidate):
    return not (isinstance(candidate, str) and candidate.isdigit())
