""" A class to compile the yaml files given two server objects. """

__author__ = "lego_engineer"
__copyright__ = "Copyright 2018, lego_engineer"
__credits__ = ["lego_engineer"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "lego_engineer"
__email__ = "protopeters@gmail.com"
__status__ = "Production"

from yaml import dump as yaml_dump

class DockerComposer:
    """ A class to compile the yaml files given two server objects. """

    def __init__(self, master_server, slave_server=None):
        """
        You must provide at least one server.

        The slave is optional.
        """
        self.master = master_server
        self.slave = slave_server
        self.output_file = 'docker-compose.yml'

    def __call__(self):
        """ Build and write out the docker-compose.yml file. """
        docker_compose_dict = {}
        docker_compose_dict['version'] = "2"
        docker_compose_dict['services'] = {}
        docker_compose_dict['services'].update(self.__build_server_dict(self.master))

        if self.slave is not None:
            docker_compose_dict['services'].update(self.__build_server_dict(self.slave))

        with open(self.output_file, 'w+') as file_obj:
            file_obj.write(yaml_dump(docker_compose_dict, default_flow_style=False))

    @staticmethod
    def __build_server_dict(server):
        """Build a dictionary for a single server.

        :param Server server: The server from which the data is being pulled.
        """
        conatiner_dict = {}
        conatiner_dict['container_name'] = server.container_name
        conatiner_dict['hostname'] = server.container_name
        conatiner_dict['env_file'] = server.env_file_path
        conatiner_dict['ports'] = ["{}:{}/udp".format(server.container_port, server.container_port)]
        conatiner_dict['volumes'] = ["./{}:/var/lib/dsta/cluster".format(server.container_name)]
        conatiner_dict['image'] = 'dstacademy/dontstarvetogether:0.8'
        conatiner_dict['tty'] = 'true'
        conatiner_dict['stdin_open'] = 'true'
        conatiner_dict['command'] = 'dst-server start --update=all'

        server_dict = {}
        server_dict[server.container_name] = conatiner_dict

        return server_dict
