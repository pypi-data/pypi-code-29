from .serializations import parse


class DotNetBinaryParser:

    def __init__(self, binary: bytes):
        self.user_email = None
        self.obj = parse(bytearray(binary))

    def get_user_email(self):
        email = self._parse_dict(self.obj)
        return email if email else ''

    def _parse_dict(self, d):
        for k, v in d.items():
            if isinstance(v, dict):
                self._parse_dict(v)
            else:
                if isinstance(v, list) or isinstance(v, tuple):
                    self._parse_list(v)

            if self.user_email is not None:
                return self.user_email

    def _parse_list(self, l):
        found = False
        for e in l:
            if found:
                return self.parse_email(e)
            if isinstance(e, list) or isinstance(e, tuple):
                self._parse_list(e)
            elif isinstance(e, dict):
                self._parse_dict(e)
            elif isinstance(e, str) and e == '<Email>k__BackingField : String':
                found = True

    def parse_email(self, t: tuple):
        self.user_email = t[1]['Value']
