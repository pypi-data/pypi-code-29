import grp
import os
import platform
import pwd

python_version = platform.python_version()
PYTHON3 = python_version.startswith('3')


class PermissionsContainer(object):
    def __init__(self, file_obj):
        self._file = file_obj
        self._fp = self._process_permissions()

    def _process_permissions(self):
        return os.stat(self._file)

    @property
    def umask(self):
        """
        File permissions as Unix umask
        """
        return oct(self._fp.st_mode & 0o777)

    @property
    def has_sticky(self):
        """
        Indicates whether file has sticky bit or not
        """
        return self._fp.st_mode & 01000 == 01000

    @property
    def suid(self):
        """
        Indicates whether file has SUID or not
        """
        return self._fp.st_mode & 04000

    @property
    def sgid(self):
        """
        Indicates whether file has SGID or not
        """
        return self._fp.st_mode & 02000

    @property
    def owner(self):
        """
        Information about user that owns the file as pwd.getpwuid outputs it.
        (pw_name,pw_passwd,pw_uid, pw_gid,pw_gecos,pw_dir,pw_shell)
        """
        return pwd.getpwuid(self._fp.st_uid)

    @property
    def group(self):
        """
        Information about group as grp.getgrgid outputs it.
        (gr_name,gr_passwd,gr_gid,gr_mem)
        """
        return grp.getgrgid(self._fp.st_gid)

    @property
    def readable(self):
        """
        Detects whether file could be read by current user
        """
        return os.access(self._file, os.R_OK)

    @property
    def writable(self):
        """
        Detects whether file could be written by current user
        """
        return os.access(self._file, os.W_OK)

    @property
    def executable(self):
        """
        Detects whether file could be executed by current user
        """
        return os.access(self._file, os.EX_OK)


def get_permissions_from(file_obj):
    return PermissionsContainer(file_obj)
