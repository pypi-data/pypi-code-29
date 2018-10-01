
import re
import os
from subprocess import CalledProcessError, run, PIPE
from pkg_resources import get_distribution
from subprocess import check_output


version_validator = re.compile(
    r"^(\d+!)?(\d+)(\.\d+)+([\.\_\-])?((a(lpha)?|b(eta)?|c|r(c|ev)?|pre(view)?)\d*)?(\.?(post|dev)\d*)?$")


def git_version(dist, attr, value):
    dist.metadata.version = get_git_version()


def get_git_version():
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

    raise RuntimeError('The working has neither a valid branch or tag')
