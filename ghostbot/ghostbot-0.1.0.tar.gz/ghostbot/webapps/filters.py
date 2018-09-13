def filter_numeric(amount):
    result = amount
    if isinstance(amount, int):
        result = "{:,d}".format(amount)
    elif isinstance(amount, float):
        result = "{:,.2f}".format(amount)
    return result
