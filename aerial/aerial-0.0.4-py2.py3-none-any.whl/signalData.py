class SignalData(object):
    """ Object intended to store information about received signals """

    def __init__(self, signum, received=False, frame=None, acknowledged=False):
        self.signum = signum
        self.received = received
        self.frame = frame
        self.acknowledged = acknowledged

    def awk(self):
        """ Acknowledge the signal, this suppresses it in the feed """
        self.acknowledged = True
        return self

    def rec(self, frame):
        """ Receive a the signal, this raises it in the feed """
        self.received = True
        self.acknowledged = False
        self.frame = frame
        return self

    def __bool__(self):
        return self.received and not self.acknowledged

    def __nonzero__(self):
        return self.__bool__()
