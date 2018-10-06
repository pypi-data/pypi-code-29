
USER_INPUT_YES = 'y'
USER_INPUT_NO = 'n'


def int_input(msg):
    """
    This methods should be used to request an integer value to the user. This
    method will not return until the user inputs a valid integer value.
    """
    try:
        return int(safe_input(msg), base=10)
    except ValueError:
        print('Input must be a valid integer value')
        int_input(msg)


def yes_or_no_input(msg):
    """
    This methods should be used to request an Yes/No input to the user. This
    method will not return until the user inputs a valid answer.
    """
    full_msg = '{} ({}/{})'.format(msg, USER_INPUT_YES, USER_INPUT_NO)
    answer = safe_input(full_msg).lower()
    while answer not in [USER_INPUT_YES, USER_INPUT_NO]:
        answer = safe_input(full_msg).lower()
    return answer


def safe_input(msg):
    """
    This method extends the system built input() method in order to exit gracefully
    in case of a KeyboardInterrupt signal (ctr+c) being received.
    """
    try:
        return input('{}: '.format(msg))
    except KeyboardInterrupt:
        print('\n\nExiting..')
        raise SystemExit
