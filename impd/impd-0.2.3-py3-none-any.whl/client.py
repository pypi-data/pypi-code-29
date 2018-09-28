from mpd import MPDClient, base


class AttemptFailure(Exception):
    pass


class Client(MPDClient):

    _host = None
    _port = None

    def connect(self, host, port, attempt_count=10):
        self._host = host
        self._port = port
        self._attempt_count = attempt_count
        super().connect(host, port)

    def _attempt(self, call, errors, *args, **kwargs):
        try:
            result = call(*args, **kwargs)
        except errors as e:
            return (None, AttemptFailure)
        return result

    def currentsong(self):
        errors = (base.ConnectionError, base.ProtocolError, BrokenPipeError)
        for i in range(self._attempt_count):
            result = self._attempt(super().currentsong, errors)
            if result == (None, AttemptFailure):
                super().connect(self._host, self._port)
            else:
                return result
        return {}

    def pause(self, *args, **kwargs):
        errors = (base.ConnectionError, base.ProtocolError, BrokenPipeError)
        for i in range(self._attempt_count):
            result = self._attempt(super().pause, errors, *args, **kwargs)
            if result == (None, AttemptFailure):
                super().connect(self._host, self._port)
            else:
                return result
        return {}

    def next(self):
        errors = (base.ConnectionError, base.ProtocolError, BrokenPipeError)
        for i in range(self._attempt_count):
            result = self._attempt(super().next, errors)
            if result == (None, AttemptFailure):
                super().connect(self._host, self._port)
            else:
                return result
        return {}

    def previous(self):
        errors = (base.ConnectionError, base.ProtocolError, BrokenPipeError)
        result = self._attempt(super().previous, errors)
        if result == (None, AttemptFailure):
            super().connect(self._host, self._port)
            return {}
        return result

    def play(self, *args, **kwargs):
        errors = (base.ConnectionError, base.ProtocolError, BrokenPipeError)
        for i in range(self._attempt_count):
            result = self._attempt(super().play, errors, *args, **kwargs)
            if result == (None, AttemptFailure):
                super().connect(self._host, self._port)
            else:
                return result
        return {}

    def playlistinfo(self):
        errors = (base.ConnectionError, base.ProtocolError, BrokenPipeError)
        result = self._attempt(super().playlistinfo, errors)
        if result == (None, AttemptFailure):
            super().connect(self._host, self._port)
            return {}
        return result
