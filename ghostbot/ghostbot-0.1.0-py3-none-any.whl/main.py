from docopt import docopt
from ghostbot import GhostbotProfile, Scaffolds
from ghostbot.dashboard import Dashboard
from ghostbot.diagnose import Diagnose
from ghostbot.inspector import Inspector
from ghostbot.scheduler import Scheduler
from ghostbot.wizard import Wizard


__product__ = "ghostbot"
__version__ = GhostbotProfile.version_info()
__doc__ = """
Usage:
    {me} -h | --help
    {me} -v | --version
    {me} doctor
    {me} update
    {me} wizard (project|agent|container|reactor) [(-d [<directory>])] <name>
    {me} list [<expression>]
    {me} append <project_name> <full_path>
    {me} remove <signature>
    {me} run <signature> [<options>]
    {me} inspector [<options>]
    {me} scheduler (append|remove) <task>
    {me} dashboard (status|start|restart|stop) [<options>]

Command:
    doctor      self diagnose
    update      update selenium drivers
    wizard      create specified object
    list        show the managed project
    append      append project to the ghostbot repository
    remove      remove project from the ghostbot repository
    run         launch specified project
    inspector   inspector via the web-browser
    scheduler   scheduler via the web-browser
    dashboard   dashboard via the web-browser
""".format(me=__product__)


class Ghostbot(object):

    def __init__(self):
        self.repository = {}
        self.diagnose = Diagnose()
        self.inspector = Inspector()
        self.scheduler = Scheduler()
        self.wizard = Wizard()
        self.dashboard = Dashboard()

    def execute(self):
        args = docopt(__doc__)
        if args["-v"] or args["--version"]:
            self._version()
        elif args["-h"] or args["--help"]:
            self._help()
        elif args["doctor"]:
            self._doctor()
        elif args["update"]:
            self._update()
        elif args["wizard"]:
            if args["-d"] and args["<directory>"]:
                directory = args["<directory>"]
            else:
                directory = None
            if args["project"]:
                self._wizard(Scaffolds.PROJECT, args["<name>"], directory)
            elif args["agent"]:
                self._wizard(Scaffolds.AGENT, args["<name>"], directory)
            elif args["container"]:
                self._wizard(Scaffolds.CONTAINER, args["<name>"], directory)
            elif args["reactor"]:
                self._wizard(Scaffolds.REACTOR, args["<name>"], directory)
        elif args["inspector"]:
            self._inspector()
        elif args["append"]:
            self._append()
        elif args["remove"]:
            self._remove()
        elif args["list"]:
            self._list(args["<expression>"])
        elif args["run"]:
            self._run(args["<project_name>"], args["<options>"])
        elif args["dashboard"]:
            command = "status"
            self._dashboard(command, args["<options>"])
        else:
            # TODO useless due to docopt behaviour
            self._help()

    @staticmethod
    def _version():
        print("ghostbot version={}".format(GhostbotProfile.version()))

    @staticmethod
    def _help():
        # TODO show detail message
        print("this is a help")

    def _doctor(self):
        self.diagnose.execute("check")

    def _update(self):
        self.diagnose.execute("update")

    def _wizard(self, target, name, directory=None):
        self.wizard.execute(target, name, directory)

    def _inspector(self, options):
        self.inspector.execute(options)

    def _append(self, name, path):
        if name not in self.repository:
            self.repository[name] = path
            # TODO persistent
        else:
            # TODO show error message
            pass

    def _remove(self, expression):
        # TODO support regexp and call _list()
        if expression in self.repository:
            # TODO remove after confirmation
            # del(self.repository[name])
            # TODO save to database
            pass
        else:
            # TODO show error message
            pass

    def _list(self, expression=None):
        for name, path in self.repository.items():
            if expression is not None:
                # TODO save to database
                pass
            else:
                # TODO formatting
                print("{} {}".format(name, path))

    def _run(self, name, options):
        self.run.execute(name, options)

    def _dashboard(self, command, options):
        self.dashboard.execute(command, options)


if __name__ == "__main__":
    try:
        ghostbot = Ghostbot()
        ghostbot.execute()
    except Exception as e:
        print("exception occurred: {}".format(e.args))
        exit(-1)
