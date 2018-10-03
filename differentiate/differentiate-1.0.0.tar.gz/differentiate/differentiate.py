def differentiate(x, y):
    """
    Retrieve a unique of list of elements that do not exist in both x and y.
    Capable of parsing one-dimensional (flat) and two-dimensional (lists of lists) lists.

    :param x: list #1
    :param y: list #2
    :return: list of unique values
    """
    # Validate both lists, confirm either are empty
    if len(x) == 0 and len(y) > 0:
        return y  # All y values are unique if x is empty
    elif len(y) == 0 and len(x) > 0:
        return x  # All x values are unique if y is empty

    # Get the input type to convert back to before return
    try:
        input_type = type(x[0])
    except IndexError:
        input_type = type(y[0])

    # Dealing with a 2D dataset (list of lists)
    try:
        # Immutable and Unique - Convert list of tuples into set of tuples
        first_set = set(map(tuple, x))
        secnd_set = set(map(tuple, y))

    # Dealing with a 1D dataset (list of items)
    except TypeError:
        # Unique values only
        first_set = set(x)
        secnd_set = set(y)

    # Determine which list is longest
    longest = first_set if len(first_set) > len(secnd_set) else secnd_set
    shortest = secnd_set if len(first_set) > len(secnd_set) else first_set

    # Generate set of non-shared values and return list of values in original type
    return [input_type(i) for i in {i for i in longest if i not in shortest}]