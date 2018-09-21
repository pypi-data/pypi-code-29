from .feed import Feed

feed = None


def received(signal_id, awk=True):
    """
    This method checks if the provided signal has been received,
    and returns a Boolean.

    The first call per signal_id will start up a listener for that signal.
    All calls after that check the state of that listener.

    :param Integer signal_id: The signal to check.
        It is recommended to pull these from the signals builtin.
    :param Boolean awk: Optional, defaults to True.
        True will acknowledge the signal, so that the same signal does not
        cause this return True twice for the same signal.
        False skips this step.
    :return Boolean: True if the signal has been received.  Else False.
    """
    global feed
    if feed is None:
        feed = Feed()
    if not feed[signal_id]:
        return False
    if awk:
        feed[signal_id].awk()
    return True
