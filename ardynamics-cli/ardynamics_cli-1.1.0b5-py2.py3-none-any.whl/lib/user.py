import pwd
import os
from subprocess import Popen


class User:
    _username = None

    def __init__(self, username):
        self._username = username

    def create_account(self):
        try:
            pwd.getpwnam(self._username)
        except KeyError:
            print('  - Create account for user ' + self._username)
            Popen(['/sbin/adduser', self._username])

    def set_password(self, password):
        print('  - Set password for user ' + self._username)
        os.system('echo "' + self._username + ':' + password + '" | /sbin/chpasswd')
