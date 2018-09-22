from cmd import Cmd

from clint.textui import colored

from midpoint_cli.mpclient import MidpointClient


class MidpointClientPrompt(Cmd):
    intro = 'Welcome to Midpoint client ! Type ? for a list of commands'

    def __init__(self, client: MidpointClient):
        Cmd.__init__(self)
        self.client = client
        self.prompt = colored.green('midpoint') + '> '

    def can_exit(self):
        return True

    def do_EOF(self, inp):
        print()
        return self.do_exit(inp)

    def do_exit(self, inp):
        return True

    def help_exit(self):
        print('Exit the shell')
