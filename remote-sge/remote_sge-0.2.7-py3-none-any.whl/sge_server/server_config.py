from os import getcwd, environ
from os.path import exists, join
import sys

from sge.config_base import ConfigBase, Sections, Settings, Defaults
class ServerSettings(object):
    WORK_ROOT = r'work_root'
    COMPLETED_FILES_ROOT = r'completed_files_root'

STANDARD_WRAPPER = join(sys.prefix, 'bin', 'remote_sge_job_wrapper.sh')
DEV_WRAPPER = join((environ.get('PYTHONPATH') or getcwd()), 'bin', 'remote_sge_job_wrapper.sh')

class ServerConfig(ConfigBase):
    "Server App Configuration"
    def __init__(self, configparser):
        """
        Args:
            configparser (:class:`configobj.ConfigObj`): configuration settings.
        """

        super().__init__(configparser)
        self.qsub_settings = self.__read_qsub_settings(configparser[Sections.QSUB_SETTINGS])
        server_settings = configparser[Sections.SERVER]
        self.work_root = server_settings[ServerSettings.WORK_ROOT]
        self.completed_files_root = server_settings[ServerSettings.COMPLETED_FILES_ROOT]
        self.script_env = configparser[Sections.ENVIRONMENT]
        if exists(STANDARD_WRAPPER):
            self.script_wrapper = STANDARD_WRAPPER
        elif exists(DEV_WRAPPER):
            self.script_wrapper = DEV_WRAPPER
        else:
            raise "Couldn't find script wrapper."

    def __read_qsub_settings(self, parser):
        response = dict(binary_executable=parser.as_bool('binary_executable'),
                        command_shell=parser.get('command_shell'),
                        default_queue=parser.get('default_queue'),
                        exec_in_shell=parser.as_bool('exec_in_shell'),
                        join_stdout_and_stderr=parser.as_bool('join_stdout_and_stderr'),
                        output_path=parser.get('output_path'),
                        parallel_environment=parser.get('parallel_environment'))
        return {k:v for k, v in response.items() if v}
