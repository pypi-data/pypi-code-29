
import re
import os
from subprocess import CalledProcessError, run, PIPE
from pkg_resources import get_distribution
from subprocess import check_output


version_validator = re.compile(
    r"^(\d+!)?(\d+)(\.\d+)+([\.\_\-])?((a(lpha)?|b(eta)?|c|r(c|ev)?|pre(view)?)\d*)?(\.?(post|dev)\d*)?$")
version_re = re.compile('^Version: (.+)$', re.M)


def git_version(dist, attr, value):
    dist.metadata.version = get_git_version(value)


def get_git_version(fallback_value):
    pypigit_version = os.environ.get("PYPIGIT_VERSION", None)
    if pypigit_version:
        return pypigit_version

    with open(os.devnull, 'w') as f_null:
        # Get the current tag using "git describe".
        try:
            version = run('git describe --tags', stdout=PIPE, stderr=f_null, shell=True)
        except CalledProcessError:
            raise RuntimeError('Unable to get version number from git tags')

        if version.returncode == 0:
            version_fixed = version.stdout.decode().splitlines()[0]
            if re.match(version_validator, version_fixed):
                return version_fixed

        # If there is no current tag, try with branch name
        try:
            version = run('git symbolic-ref --short HEAD', stdout=PIPE, stderr=f_null, shell=True)
        except CalledProcessError:
            raise RuntimeError('Unable to get version number from git tags')

        if version.returncode == 0:
            version_fixed = version.stdout.decode().splitlines()[0]
            if re.match(version_validator, version_fixed):
                return version_fixed

    # Extract the version from the PKG-INFO file.
    if os.path.isfile('PKG-INFO'):
        with open('PKG-INFO', "r") as f:
            return version_re.search(f.read()).group(1)

    return fallback_value
