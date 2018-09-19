import twisted.protocols.amp


class PrintError(Exception):
    pass


class Print(twisted.protocols.amp.Command):
    arguments = [
        (b'text', twisted.protocols.amp.Unicode()),
    ]

    response = [
        (b'success', twisted.protocols.amp.Boolean()),
    ]

    errors = {
        PrintError: b'print-error',
    }


class Commands(twisted.protocols.amp.CommandLocator):
    @Print.responder
    def print(self, text):
        print('printing: {}'.format(repr(text)))

        return {'success': True}
