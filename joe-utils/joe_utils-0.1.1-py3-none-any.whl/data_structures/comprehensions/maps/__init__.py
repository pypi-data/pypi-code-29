"""Map Comprehensions"""


def inverse_filter_dict(dictionary, keys):
    """Filter a dictionary by any keys not given.

    Args:
        dictionary (dict): Dictionary.
        keys (iterable): Iterable containing data type(s) for valid dict key.

    Return:
        dict: Filtered dictionary.
    """
    return {key: val for key, val in dictionary.items() if key not in keys}


def ne_dict(dictionary):
    """Prune dictionary of empty key-value pairs.

    Aliases: pruned()
    """
    return {k: v for k, v in dictionary.items() if v}


def pruned(dictionary):
    """Prune dictionary of empty key-value pairs.

    Alias of ne_dict().
    """
    return ne_dict(dictionary)


def prune_by_n_required_children(dictionary, n=1):
    """Return with only key value pairs that meet required n children."""
    return {key: val for key, val in dictionary.items() if len(val) >= n}
