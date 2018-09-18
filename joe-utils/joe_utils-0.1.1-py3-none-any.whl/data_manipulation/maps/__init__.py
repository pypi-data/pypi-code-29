"""Data Manipulation - Maps"""


def set_and_true(key, _dict):
    """Is key in dict and value True?

    Args:
        key (str): Key to lookup in dictionary.
        _dict (dict): The dictionary.

    Returns:
        bool: Is key in dict and value True?
    """
    return key in _dict and _dict[key] is True
