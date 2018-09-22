#!/usr/bin/env python2.7
import argparse
import os
import re
import sys

from prename import prename

renames = []


def _colourise(s, colour):
    """Print a message in the colour with the given ANSI number"""
    print ('\x1b[%dm' % colour) + s + '\x1b[0m'


def _error(s):
    _colourise(s, 31)


def _debug(s):
    _colourise(s, 36)


def _clean_filename(s):
    """
    Attempts to clean the filename prior to matching for rename, to avoid
    the patterns getting confused over things like strings of numbers referring
    to year or encoding.

    Just strip out runs of numbers which don't seem to be relevant to season /
    episode numbers and return the result.
    """
    s = re.sub('[0-9]{4,}', '', s)  # Probably a year
    s = re.sub('x[0-9]{3,4}', '', s)  # Probably an encoding (eg. x640)
    s = re.sub('[0-9]{3,}p', '', s)  # Very likely an encoding (eg. 1080p)
    return s


def smart_rename(dir, recursive=False, verbose=False, season_hint=None):
    """
    Rename media files in the given directory to the Sxx Exx syntax
    """
    _regexes = [
        '^.*[Ss]([0-9]{2})[\s\-\.]*[eE]([0-9]{2}).*\.([a-z0-9]+)$',
        '^.*[^0-9]([0-9]{1,2})[x\.]([0-9]{1,2}).*\.([a-z0-9]+)$',
        '^.*[\s\-\.]([1-9])([0-9]{2}).*\.([a-z0-9]+)$',
        # Anime pattern - no season info
        '^.* - ()([0-9]{1,2}) .*\.([a-z0-9]+)$'
    ]

    # Compile the regexes
    regexes = [re.compile(r) for r in _regexes]

    dirs, files = prename.sort_dir(os.listdir(dir))

    if recursive:
        for subdir in dirs:
            smart_rename(subdir, verbose=verbose)

    for file in files:
        for regex in regexes:
            cleaned = _clean_filename(file)
            match = regex.match(file)
            if not match:
                continue

            if verbose:
                if cleaned != file:
                    _debug('File %s cleaned to %s' % (file, cleaned))
                _debug('File %s matched %s' % (file, regex.pattern))

            # Use the regex to attempt to extract info from the filename
            season = match.group(1) or season_hint
            episode = match.group(2)
            ext = match.group(3)

            if not season:
                continue

            if len(season) == 1:
                season = '0' + season

            if len(episode) == 1:
                episode = '0' + episode

            dest = 'S%s E%s.%s' % (season, episode, ext)

            # No need to check other patterns; we've found one
            renames.append((dir, file, dest))
            break


def validate_renames():
    """Do a sanity check, testing for duplicate destinations"""
    mappings = {}
    error = False

    for _, file, dest in renames:
        if dest in mappings:
            _error(
                'Both %s and %s look like %s!\x1b[0m' % (
                    file, mappings[dest], dest
                )
            )
            error = True

        mappings[dest] = file

    if error:
        _error('You will need to resolve the above error(s).')
        sys.exit(1)


def commit_renames(force=False):
    """
    Commit the rename list
    """
    if not force:
        print 'The following files will be renamed:'

        for dir, file, dest in renames:
            print '%s \x1b[1;33m-->\x1b[0m %s' % (file, dest)

        if raw_input('Is this OK? (y/N) ') != 'y':
            return

    for dir, file, dest in renames:
        os.rename(os.path.join(dir, file), os.path.join(dir, dest))


def main():
    parser = argparse.ArgumentParser('Smart renamer')
    parser.add_argument('directory')
    parser.add_argument(
        '-r', '-R', '--recursive', action='store_true', dest='recursive'
    )
    parser.add_argument(
        '-s', '--season-hint', dest='season_hint', type=str,
        help='Provide a season for patterns which do not find one (e.g. anime)'
    )
    parser.add_argument('-f', '--force', action='store_true', dest='force')
    parser.add_argument('-v', '--verbose', action='store_true', dest='verbose')

    args = parser.parse_args()

    smart_rename(
        args.directory, args.recursive, args.verbose, args.season_hint
    )
    validate_renames()
    commit_renames(args.force)


if __name__ == '__main__':
    main()
