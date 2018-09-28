from itertools import cycle


class Callpass(object):

    callsign: str
    callpass: int

    def __init__(self, callsign: str) -> None:
        self.callsign = callsign
        self.callpass = self._generate_callpass(self.bare_callsign)

    @property
    def bare_callsign(self) -> str:
        return self.callsign.upper().split("-")[0]

    @staticmethod
    def _generate_callpass(callsign: str) -> int:
        callpass = 0x73e2  # seed value, non-negotiable
        last = 0x7fff  # shift value, non-negotiable
        loop_switch = cycle([True, False])

        for switch, char in zip(loop_switch, callsign):
            callpass = callpass ^ (ord(char) << 8 if switch else ord(char))

        return int(callpass & last)

    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}(callsign="{self.callsign}")'

    def __str__(self) -> str:
        return "{:05}".format(self.callpass)

    def __int__(self) -> int:
        return self.callpass

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return str(self) == other
        elif isinstance(other, (Callpass, int)):
            return int(self) == int(other)
        return NotImplemented

    def __ne__(self, other) -> bool:
        return not (self == other)
