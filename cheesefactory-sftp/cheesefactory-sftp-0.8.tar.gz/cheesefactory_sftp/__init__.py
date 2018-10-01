# __init__.py
__authors__ = ["tsalazar"]
__version__ = "0.3"

# v0.1 (tsalazar) -- Stand-alone SFTP package, split from cheesefactory package.
# v0.2 (tsalazar) -- 2018/08/18 Removed misplaced __connect() in __init__()
# v0.3 (tsalazar) -- 2018/08/22 Converted to dataframe.  Updated docstrings.
# v0.4 (tsalazar) -- 2018/09/29 Added regex to filter out files during walktree()
# v0.5 (tsalazar) -- 2018/10/01 Added callback for directory during walktree()


import logging
import pysftp
import pysftp.exceptions
import paramiko.ssh_exception
import re
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class SFTP:
    """Methods for interacting with an SFTP server.

    host: SFTP server hostname or IP.
    port: SFTP server port.
    username: SFTP server account username.
    password: SFTP server account password.
    """

    host: str = '127.0.0.1'
    port: str = '22'
    username: str = None
    password: str = None

    def __post_init__(self):

        self.__logger = logging.getLogger(__name__)
        self.__local_directory = '/'  # Default local directory for transferred files.
        self._remote_directory = '/'  # Default remote directory to get files from.
        self._new_file_count = 0  # Counter to determine total number of new files received.
        self._existing_file_count = 0  # Counter to determine total number of files not transferred.
        self._ignore_regex = None  # String regex used to ignore files when performing walktree()

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None          # Accept unknown hostkeys

        # Establish SFTP connection
        try:
            self.__sftp_connection = pysftp.Connection(
                self.host,
                port=int(self.port),
                username=self.username,
                password=self.password,
                cnopts=cnopts
            )

        except (pysftp.exceptions.ConnectionException, paramiko.ssh_exception.SSHException) as error:
            print(f'Connection Exception: ', str(error))
            exit(1)
        except pysftp.exceptions.CredentialException as error:
            print('Credential Exception: ', str(error))
            exit(1)
        except pysftp.exceptions.HostKeysException as error:
            print('Host Keys Exception: ', str(error))
            exit(1)

        self.__logger.info(f'SFTP connection established to: {self.host}')

    @property
    def status(self):
        if self.__sftp_connection.exists('/etc/hosts'):
            return f'Connected to {self.username}@{self.host}:{self.port}{self._remote_directory}'
        else:
            return 'Not connected.'

    def get(self, filename: str=None, local_directory: str='/', remote_directory: str='/'):
        """Download a file from an SFTP server.

        :param filename: The name of the file to download.
        :param local_directory: The local directory to download the file into.
        :param remote_directory: Remote SFTP directory.
        """

        try:
            with self.__sftp_connection.cd(remote_directory):
                self.__sftp_connection.get(
                    filename,
                    localpath=f'{local_directory}/{filename}'
                )
            self.__logger.info(f'File retrieved: {remote_directory}/{filename} to {local_directory}.')

        except ValueError:
            self.__logger.critical(f'Problem encountered when retrieving file: {remote_directory}/{filename}')
            exit(1)

    def put(self, filename: str=None, confirm: bool=True, remote_directory: str='/'):
        """Upload a file to an SFTP server.

        :param filename: The name of the file to upload.
        :param confirm: Confirm that the transfer was successful using stat().
        :param remote_directory: Remote SFTP directory.
        """

        try:
            with self.__sftp_connection.cd(remote_directory):
                self.__sftp_connection.put(
                    filename,
                    confirm=confirm
                )
            self.__logger.info(f'File put: {remote_directory}/{filename}')

        except ValueError:
            self.__logger.critical('Problem encountered when uploading file.')
            exit(1)

    def get_new_files(self, remote_directory: str='/', local_directory: str='/', recursive: bool=True,
                      ignore_regex: str=None):
        """Get all unretrieved files from remote SFTP directory

        :param remote_directory: Remote SFTP directory.
        :param local_directory: Local directory to copy the files to.
        :param recursive: Recursively search for new files.
        :param ignore_regex: A regex string used to filter out unwanted files and paths.
        """

        self._ignore_regex = ignore_regex
        self.__sftp_connection.cd(remote_directory)

        # Create the local directory if it does not exist
        Path(local_directory).mkdir(
            parents=True,
            exist_ok=True
        )

        self.__logger.info(f'Retrieving new files from remote directory: {str(remote_directory)}')
        self.__sftp_connection.walktree(
            remote_directory,
            self.__is_this_a_new_file,  # file
            self.__is_this_a_new_file,  # directory
            self.__is_this_a_new_file,  # unknown
            recursive
        )
        self.__logger.info(f'{str(self._new_file_count)} files retrieved')
        self.__logger.info(f'{str(self._existing_file_count)} files already existed.  Skipped.')

    def __is_this_a_new_file(self, filename: str):
        """Test to see if the current file has been retrieved yet.

        :param filename:  File to test for.
        """
        local_file: Path = Path(self.__local_directory, Path(filename).name)

        if os.path.isdir(str(Path(self._remote_directory, filename))):
            self.__logger.debug(f'Directory ignored: {filename} (regex: {self._ignore_regex})')
        elif re.match(self._ignore_regex, filename):
            self.__logger.debug(f'Remote file ignored: {filename} (regex: {self._ignore_regex})')
        elif local_file.exists():
            self.__logger.debug(f'File exists: {str(local_file)} -- Skipping.')
            self._existing_file_count += 1
        else:
            self.__logger.debug(f'File not found: {str(local_file)} -- Transferring.')
            self.get(
                filename=filename,
                local_directory=self.__local_directory,
                remote_directory=self._remote_directory
            )
            self._new_file_count += 1

    def close(self):
        """Close a connection to an SFTP server."""

        try:
            self.__sftp_connection.close()
        except ConnectionError:
            self.__logger.critical('Problem closing connection.')
            exit(1)
