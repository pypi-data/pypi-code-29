def linear_congruences(x):
    """
    Based on the given Linear congruences
    X1 = AXI + b Mod M
    :param x:
    :return: compute sequence
    """
    # Parameters
    a = 22695477
    b = 1
    m = 2 ** 32

    # Compute the linear sequence, using given formula
    result = ((a * x) + b) % m

    if (m / 2) > result:
        return 1, result
    else:
        return 0, result
