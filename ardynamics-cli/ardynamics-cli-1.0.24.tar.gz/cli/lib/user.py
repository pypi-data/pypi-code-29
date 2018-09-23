import grp
import pwd
import os
from subprocess import Popen


class User:
    _username = None

    def __init__(self, username):
        self._username = username

    def create_account(self):
        group_added = False
        try:
            grp.getgrnam(self._username)
        except KeyError:
            print('  - Create group for user ' + self._username)
            Popen(['/sbin/groupadd', self._username])
            group_added = True
        try:
            pwd.getpwnam(self._username)
        except KeyError:
            print('  - Create account for user ' + self._username)
            Popen(['/sbin/adduser', self._username])
            if group_added:
                Popen(['/sbin/usermod', '-g', self._username, self._username])

    def set_password(self, password):
        print('  - Set password for user ' + self._username)
        os.system('echo "' + self._username + ':' + password + '" | /sbin/chpasswd')
