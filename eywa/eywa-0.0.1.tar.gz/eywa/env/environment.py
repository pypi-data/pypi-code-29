from ..graph import Signal, Node, Graph
import sys

py3 = sys.version_info[0] == 3

if py3:
    raw_input = input

_cursor = '==> '
def _printer(x):
    print(_cursor + str(x))

class Environment(object):

    def __init__(self):
        self.output_hooks = set([_printer])
        self.graphs = []

    def input(self, x):
        tokens = x.split()
        if tokens[0] == 'env':
            cmd = x.strip()[3:].strip()
            self.execute(cmd)
        else:
            try:
                exec(x, globals())
            except Exception as e:
                self.output(e)

    def output(self, x):
        for output_hook in self.output_hooks:
            output_hook(x)

    def execute(self, x):
        self.output('cmd: ' + x)

    def text(self, message):
        if not hasattr(self, 'main'):
            if not self.graphs:
                raise Exception('No graph has been added to the environment.')
            if len(self.graphs) > 1:
                raise Exception('Multiple graphs have been added to the environment; but main graph has not been set.')
            self.main = self.graph[0]
        self.main(Signal(message))

    def cli(self):
        print('-------- Welcome to EYWA CLI --------')
        user_id = raw_input('Enter User ID (press Enter to use default User ID \'admin\'):')
        if not user_id:
            user_id = 'admin'
        print('Welcome ' + user_id + '. Type \'exit\' to exit the CLI.' )
        while(True):
            inp = raw_input(_cursor)
            if inp.strip() == 'exit':
                break
            else:
                self.input(inp)
