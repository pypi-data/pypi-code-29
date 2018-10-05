
import json
import sys,os
import configparser
from cement.core.foundation import CementApp
from munch import munchify

cli_root = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(cli_root)
sys.path.append(root)
sys.path.append(cli_root)

from controllers import PyfluenceBaseController, SearchController, LabelController, ContentController
from pyfluence import Confluence


class PyfluenceApp(CementApp):
    """The Cement top level application object

    Arguments:
        CementApp {CementApp} -- The base class
    """
    class Meta:
        label = 'pyfluence'
        hooks = {}
        exit_on_close = True
        base_controller = PyfluenceBaseController
        handlers = [
            SearchController,
            LabelController,
            ContentController
        ]

    def __init__(self, *args, **kwargs):
        self.conf_server = None
        self.conf_username = None
        self.conf_password = None
        self.confluence = None
        super(PyfluenceApp, self).__init__(*args, **kwargs)

    def read_config_file(self):
        config = configparser.ConfigParser()
        try:
            config.read('.pyfluence')
            connection = config['connection']
            if connection:
                self.conf_server = connection['server']
                self.conf_username = connection['username']
                self.conf_password = connection['password']

        except configparser.Error as e:
            print ("There was a problem with the found config file: %s" % e.message)

    def ensure_connection(self):
        self.connect_to_confluence() or self.close(1)

    def get_connection_info(self):

        self.read_config_file()

        # override with command line argument (if there)

        if self.pargs.server:
            self.conf_server = self.pargs.server

        if self.pargs.username:
            self.conf_username = self.pargs.username

        if self.pargs.password:
            self.conf_password = self.pargs.username

        if self.conf_server and self.conf_username and self.conf_password:
            return True

        return False

    def connect_to_confluence(self):
        if self.get_connection_info():
            self.confluence = Confluence(host=self.conf_server,
                                         username=self.conf_username,password=self.conf_password)
            return True
        else:
            return False

    def get_stdin_as_object(self):
        val = self.get_stdin_as_string()
        try:
            if val:
                return munchify(json.loads(val))
        except json.JSONDecodeError as e:
            print("Invalid JSON encountered on stdin: {msg}".format(msg=e.msg))
            self.close(1)

    def show_app_header(self):
        print("Pyfluence CLI")
        print("Connecting to {server} as {user}".format(server=self.conf_server,user=self.conf_username))
        print("--------------")

    def get_content_ids(self):
        """
        Pulls content IDs either from the content_id argument or looks in stdin to see if there is JSON
        formatted as search results from which content IDs can be pulled.
        :return: Returns a list of content IDs
        """
        content_ids = []
        if not self.pargs.content_id:
            ob = self.get_stdin_as_object()
            if ob:
                try:
                    for content in ob.results:
                        content_ids.append(content.content.id)
                except KeyError:
                    print("stdin is valid JSON but does not appear to conform to Confluence REST API results.")
                    self.close(1)
            else:
                print("You must either specify a content_id parameter or pass search results in stdin")
        else:
            content_ids.append(self.pargs.content_id)

        return content_ids

    @staticmethod
    def get_stdin_as_string():
        """
        Gets anything in stdin pipe as a string. If nothing there it will return None
        :return: Returns either a string or None (if nothing found)
        """
        if not sys.stdin.isatty():
            return "".join(sys.stdin.readlines())
        else:
            return None

