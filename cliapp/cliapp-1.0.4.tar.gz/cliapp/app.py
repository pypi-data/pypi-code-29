from subprocess import Popen, PIPE, STDOUT

class CliApp:

    def __init__(self):
        pass

    def shell_run(self, cmd, **args):
        p = Popen(cmd, stdout=PIPE,
                stderr=STDOUT, shell=True)
        results = []
        silent = 'silent' in args and args['silent'] == True
        while True:
            line = p.stdout.readline().strip()
            if not line:
                break
            results.append(line)
            if not silent:
                print(line)
        p.communicate()
        return (results, p.returncode)

    def print_helper(self):
        outputs = []
        for f in dir(self):
            if f.startswith('do_'):
                outputs.append(f[3:])
        if len(outputs) > 0:
            print('man, you gotta choose from following: {}'.format(outputs))
        else:
            print('i cannot help you')
        pass

    def print_valid_options(self):
        if 'urls' in dir(self):
            print('valid wheres: {}'.format(self.urls.keys()))
        dos = []
        for f in dir(self):
            if f.startswith('do_'):
                dos.append(f[3:])
        print('valid whats: {}'.format(dos))

    def validate_cmd(self, cmd):
        return 'do_%s' % (cmd) in dir(self)

    def parse_args(self, args):
        d = {}
        for a in args:
            parts = a.split('=', 1)
            if len(parts) > 1:
                d[parts[0]] = parts[1]
        return d

    def run(self, args):
        if len(args) < 1:
            print('dude, you gotta tell me where and what. for example:')
            self.print_valid_options()
            return 1
        cmd = args[0]
        if cmd == 'help':
            self.print_valid_options()
            return 0
        try:
            if not self.validate_cmd(cmd):
                print('you are making things up dude. valid options are:')
                self.print_valid_options()
                return 1
            kwargs = self.parse_args(args[1:])
            getattr(self, 'do_%s' % (cmd))(**kwargs)
        except Exception as e:
            print(e)
            return 1
