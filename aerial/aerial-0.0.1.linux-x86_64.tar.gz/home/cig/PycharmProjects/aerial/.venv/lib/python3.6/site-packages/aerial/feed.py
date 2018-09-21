import signal

from .signalData import SignalData


class Feed(object):
    """ Object intended to raise signals for visibility """

    def __init__(self):
        self.signals = dict()

    def _receiver(self, signum, frame):
        """ Callback that is registered in the signal.signal builtin """
        self.signals[signum].rec(frame)

    def __getitem__(self, item):
        if item not in self.signals:
            signal.signal(item, self._receiver)
            self.signals[item] = SignalData(item)
        return self.signals.__getitem__(item)

    def __bool__(self):
        return any([sig for sig in self.signals.values()])

    def __nonzero__(self):
        return self.__bool__()
