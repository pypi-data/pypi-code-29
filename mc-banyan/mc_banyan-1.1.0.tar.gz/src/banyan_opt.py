from optparse import OptionParser
import sys
from .debug import simple as debug_simple

opt_configs = [
{
    "short": "p",
    "long": "projectname",
    "dest": "projectname",
    "help": "the project name"
},
    {
        "short": "c",
        "long": "cfg",
        "dest": "cfg",
        "help": "the banyan configuration file name",
        "default": "banyan"
    },
    {
        "short": "u",
        "long": "giturl",
        "dest": "giturl",
        "help": "git url for the project",
        "default": None
    },
    {
        "short": "t",
        "long": "tag",
        "dest": "tag",
        "help": "tag of the project",
        "default": "v1.0.0"
    }
]
def get_options(sys_args = None):

    def configure_parser(parser):
        def add_opt(opt):
            parser.add_option("-"+opt["short"], \
                              "--" + opt["long"], \
                              dest=opt["dest"] if "dest" in opt else None, \
                              help=opt["help"] if "help" in opt else None, \
                              default = opt["default"] if "default" in opt else None)

        [add_opt(opt) for opt in opt_configs]
        
        (options, args) = parser.parse_args(debug_simple(sys_args or sys.argv, "original args"))

        class dumy:
            def __init__(self):
                self.projectname = options.projectname
                self.cfg = options.cfg
                self.command = args[1]
                self.giturl = options.giturl
                self.tag = options.tag
                
        return dumy()

    return configure_parser(OptionParser())
