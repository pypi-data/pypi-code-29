#!/usr/bin/python

#-------------------------------------------------------------------------------
# Copyright (C) 2018 Maximilian Stahlberg
#
# This file is part of PICOS Release Scripts.
#
# PICOS Release Scripts are free software: you can redistribute it and/or modify
# them under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PICOS Release Scripts are distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------

import os
from subprocess import check_output

LOCATION = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
VERSION_FILE   = os.path.join(LOCATION, "picos", ".version")

# Version lengthes.
SHORT           = 0
MEDIUM          = 1
MEDIUM_OR_SHORT = 2
LONG            = 3

def repository_is_dirty():
    description = check_output(["git", "describe", "--dirty"]).decode("ascii")
    return "dirty" in description

def _git_describe(tokens = True):
    with open(os.devnull, "w") as DEVNULL:
        gitVer = check_output(["git", "describe", "--long", "--match", "v*"],
            stderr = DEVNULL).decode("ascii").strip()
    return gitVer.split("-") if tokens else gitVer

def verify_version_file(raiseException = True, skipIfNoGit = False):
    with open(VERSION_FILE, "r") as versionFile:
        fileVersion = versionFile.read().strip()

    try:
        gitVersion  = _git_describe()[0].lstrip("v")
    except:
        if skipIfNoGit:
            gitVersion = fileVersion
        else:
            raise

    valid = fileVersion == gitVersion

    if raiseException:
        if not valid:
            raise Exception("File version is {} while git version is {}."
                .format(fileVersion, gitVersion))
    else:
        return valid

def get_base_version():
    """Get the version stored in the version file."""
    verify_version_file(skipIfNoGit = True)

    with open(VERSION_FILE, "r") as versionFile:
        version = versionFile.read().strip()

    return version

def get_commit_count():
    """Get number of commits since the last release."""
    gitVer = _git_describe()

    if len(gitVer) >= 2:
        return int(gitVer[1])
    else:
        raise Exception("Failed to retrieve number of commits since the last release.")

def get_commit_hash():
    gitVer = _git_describe()

    if len(gitVer) >= 3:
        return gitVer[2]
    else:
        raise Exception("Failed to retrieve the commit hash.")

def get_version(length = MEDIUM_OR_SHORT, commitPrefix = ".post", hashPrefix = "+",
        includeZeroCommits = False):
    version = get_base_version()

    if length is not SHORT:
        try:
            commits = get_commit_count()
        except:
            if length is MEDIUM_OR_SHORT:
                commits = 0
            else:
                raise

        if commits != 0 or includeZeroCommits:
            version += "{}{}".format(commitPrefix, commits)

        if length is LONG:
            version += "{}{}".format(hashPrefix, get_commit_hash())

    return version

def get_version_info():
    """Get Python's __version_info__ tuple."""
    return tuple(get_version().split("."))

def bump_version(*parts):
    for number in parts:
        if type(number) is not int:
            raise TypeError("Version number parts must be int.")

    if repository_is_dirty():
        raise Exception("You can only bump version in a non-dirty repository.")

    version = ".".join(["{}".format(x) for x in parts])
    if len(parts) == 2:
        major, minor = parts
        patch = -1
    elif len(parts) == 3:
        major, minor, patch = parts
    else:
        raise Exception("Version format must be MAJOR.MINOR or MAJOR.MINOR.PATCH.")

    oldVersion = get_base_version()
    oldParts = [int(x) for x in oldVersion.split(".")]
    if len(oldParts) == 2:
        oldMajor, oldMinor = oldParts
        oldPatch = -1
    elif len(oldParts) == 3:
        oldMajor, oldMinor, oldPatch = oldParts
    else:
        raise Exception("The old version format is invalid.")

    notNewer = False
    if major < oldMajor:
        notNewer = True
    elif major == oldMajor:
        if minor < oldMinor:
            notNewer = True
        elif minor == oldMinor:
            if patch <= oldPatch:
                notNewer = True
    if notNewer:
        raise Exception("The proposed version of {} is not newer than the "
            "current version of {}.".format(version, oldVersion))

    print("Writing to version file.")
    with open(VERSION_FILE, "tw") as versionFile:
        versionFile.write("{}\n".format(version))

    print("Commiting to git.")
    check_output(["git", "add", VERSION_FILE])
    check_output([
        "git", "commit", "-m", "Bump version to {}.".format(version)])

    print("Creating an annotated git tag.")
    check_output(["git", "tag", "-a", "{}{}".format(VERSION_PREFIX, version),
        "-m", "Release of version {}.".format(version)])

    print("Verifying that version file and git tag version match.")
    verify_version_file()

    print("\nAll set. Execute 'git push --follow-tags' to push the release!")


if __name__ == "__main__":
    import argparse

    def version(str):
        parts = str.lstrip("v").split(".")
        digits = [int(x) for x in parts]
        return tuple(digits)

    parser = argparse.ArgumentParser(description="PICOS version manager.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--test", action="store_true",
        help="verify that file and git versions match")
    group.add_argument("-b", "--bump", metavar="VER", type=version,
        help="bump version to VER = MAJOR.MINOR[.PATCH]")
    group.add_argument("-s", "--short", action="store_true",
        help="print the base version without the commit offset")
    group.add_argument("-m", "--medium", action="store_true",
        help="print the full version with a nonzero commit offset")
    group.add_argument("-f", "--flexible", action="store_true",
        help="like --medium if possible, else like --short (default)")
    group.add_argument("-l", "--long", action="store_true",
        help="print an extended full version with the commit hash")
    group.add_argument("-n", "--commits", action="store_true",
        help="print the number of commits since the last release")
    group.add_argument("-c", "--commit", action="store_true",
        help="print the current commit short hash")
    group.add_argument("--pep", action="store_true",
        help="same as --flexible -o '.post' -a '+'")
    group.add_argument("--aur", action="store_true",
        help="same as --long -z -o '.r' -a '.'")

    parser.add_argument("-z", "--zero-commits", action="store_true",
        default=False, help="include the commit offset even if it is zero")
    parser.add_argument("-p", "--prefix", metavar="STR", type=str,
        default="", help="prefix for the base version")
    parser.add_argument("-o", "--commit-prefix", metavar="STR", type=str,
        default=".post", help="prefix for the number of commits since last release")
    parser.add_argument("-a", "--hash-prefix", metavar="STR", type=str,
        default="+", help="prefix for the commit hash")

    args = parser.parse_args()

    if args.aur:
        args.long = True
        args.commit_prefix = ".r"
        args.hash_prefix = "."
        args.zero_commits = True
    elif args.pep:
        args.flexible = True
        args.commit_prefix = ".post"
        args.hash_prefix = "+"

    version = None
    versionArgs = {
        "commitPrefix": args.commit_prefix,
        "hashPrefix": args.hash_prefix,
        "includeZeroCommits": args.zero_commits
    }

    if args.test:
        verify_version_file()
    elif args.short:
        version = get_version(SHORT, **versionArgs)
    elif args.medium:
        version = get_version(MEDIUM, **versionArgs)
    elif args.long:
        version = get_version(LONG, **versionArgs)
    elif args.commits:
        print(get_commit_count())
    elif args.commit:
        print(get_commit_hash())
    elif args.bump:
        bump_version(*args.bump)
    else: # either args.flexible or none
        version = get_version(MEDIUM_OR_SHORT, **versionArgs)

    if version is not None:
        print(args.prefix + version)

