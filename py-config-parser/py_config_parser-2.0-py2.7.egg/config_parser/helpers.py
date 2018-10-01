def boolean_conversion_handler(value):
    """
    Приведение значения к булеву
    """
    if isinstance(value, bool):
        return value

    value = value.lower()
    if value in ('true', 'false'):
        return value == 'true'

    return bool(value)
