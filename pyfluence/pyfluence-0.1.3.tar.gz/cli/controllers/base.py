import sys
import argparse

from cement.core.controller import CementBaseController, expose


class PyfluenceBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = "Get, change, add, delete content in Confluence on the command line."
        arguments = [
            (['--server'], dict(help="The confluence server")),
            (['--username'], dict(help="Username to login with")),
            (['--password'], dict(help="Password to login with")),
        ]

    @expose(help="base controller default command", hide=True)
    def default(self):
        if self.app.connect_to_confluence():
            self.app.show_app_header()
            print("To use this command, you must specify an action you want to perform.  Use --help to see a list "
                  "of commands and --help for each command to get details about each.  To change configuration you can"
                  "create a .pyfluence file in the current directory or in your home directory and follow the format"
                  "specified in the readme")
        else:
            print("There is no confluence server and credentials configured which is the minimum needed to make "
                  "this command useful.  Checkout the cli readme for more information about configuration")

