"""
Handle conversions of MacOS installed media
"""

import os
import plistlib
import sys

from subprocess import Popen


class InstallerError(Exception):
    pass


class MacOSInstallerApp(object):
    """
    Class for MacOS installer app downloaded from app store
    """

    def __init__(self, path):
        self.path = os.path.expandvars(os.path.expanduser(path))
        self.__parse_version__()

    def __str__(self):
        return '{} (installer {})'.format(self.name, self.version)

    def __parse_version__(self):
        """
        Parse installer verison from .app version.info
        """
        version_file = os.path.join(self.path, 'Contents/Info.plist')
        if not os.path.isfile(version_file):
            raise InstallerError('No such file: {}'.format(version_file))

        try:
            data = plistlib.load(open(version_file, 'rb'))
        except Exception as e:
            raise InstallerError('Error parsing {}: {}'.format(version_file, e))

        try:
            self.version = data['CFBundleShortVersionString']
        except KeyError:
            raise InstallerError('Error looking CFBundleShortVersionString from {}'.format(version_file))

        try:
            self.volume_name = data['CFBundleDisplayName']
            self.name = data['CFBundleDisplayName'].replace('Install macOS ', '')
        except KeyError:
            raise InstallerError('Error looking CFBundleDisplayName from {}'.format(version_file))

    def convert_to_dvd(self, filename, mountpoint=None):
        """
        Convert installer to DVD image

        This is currently specific to High Sierra.

        Most likely would work with others but has not been tested.
        """

        if mountpoint is None:
            mountpoint = '/Volumes/installer_convert'

        if self.name == 'High Sierra':
            convert_command = os.path.join(
                self.path,
                'Contents/Resources/createinstallmedia'
            )
            if not os.access(convert_command, os.X_OK):
                raise InstallerError('No such executable: {}'.format(convert_command))

            # Create image file with SPUD format and HFS+J filesystem
            cmd = (
                'hdiutil',
                'create',
                '-size', '8G',
                '-layout', 'SPUD',
                '-fs', 'HFS+J',
                '-o', filename,
            )
            p = Popen(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
            p.wait()
            # Attach image file
            cmd = (
                'hdiutil',
                'attach',
                '-noverify',
                '-mountpoint', mountpoint,
                '{}.dmg'.format(filename),
            )
            p = Popen(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
            p.wait()

            # Use converter command to create installable DVD image. This must be run with sudo
            cmd = (
                'sudo',
                convert_command,
                '--nointeraction',
                '--applicationpath', self.path,
                '--volume', mountpoint,
            )
            p = Popen(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
            p.wait()

            # Detach volume. After conversion it is named like the installer volume
            cmd = ('hdiutil', 'detach', '/Volumes/Install macOS High Sierra')
            p = Popen(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
            p.wait()

            # Convert image to UDTO format
            cmd = (
                'hdiutil',
                'convert',
                '-format', 'UDTO',
                '-o', filename,
                '{}.dmg'.format(filename),
            )
            p = Popen(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
            p.wait()

            # Rename file to remove the extra .cdr added by hdiutil
            os.rename('{}.cdr'.format(filename), filename)

            # Remove the temporary dmg file
            os.unlink('{}.dmg'.format(filename))

        else:
            raise InstallerError('Conversion of {} installer not yet supported'.format(self.name))
