
import sys

from kabaret.app.ui import gui


from kabaret.app.actors.flow import Flow
from .flow.custom_home import JosephineHomeRoot


class JosephineGUISession(gui.KabaretStandaloneGUISession):

    def _create_actors(self):
        Flow(self, CustomHomeRootType=JosephineHomeRoot)


if __name__ == '__main__':
    argv = sys.argv[1:]  # get ride of first args wich is script filename
    (
        session_name,
        host, port, cluster_name,
        db_index, password, debug,
        remaining_args
    ) = JosephineGUISession.parse_command_line_args(argv)
    session = JosephineGUISession(session_name=session_name)
    session.cmds.Cluster.connect(host, port, cluster_name, db_index, password)

    session.start()
    session.close()
