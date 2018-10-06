# -*- coding: utf-8 -*-
"""
Try to find all used colors through all given scss/css files

Require:

    pip install colorutils

TODO: * Parse all existing *.scss/*.css files from given directory (instead of SCSS_FILES)
        -> Glob finding
      * When a color name is used more than one time, increment names with "_[+1]" for all other identic names;
        -> A dict to store occurences to a name with each color
      * Procedure to replace hexadecimal, rgb, and rgba colors with their variable name (using their finded name);
        -> Output valid Sass vars but never rewrite searched files, this is out of scope, maybe store color locations (filepath and line) ?
"""
import os, re

from pathlib import Path

from colour import Color


class ColorFinder:
    """
    Color patterns finding in files matching some extensions.
    """
    _DEFAULT_EXTENSIONS = ['scss', 'sass', 'css']

    def __init__(self, extensions=None):
        self.extensions = extensions or self._DEFAULT_EXTENSIONS
        self._reg_hexacode = re.compile(r'#(?:[a-fA-F0-9]{1,6})\b')
        self._reg_rgb = re.compile(r'rgb[a]{0,1}\(([^)]*)\)')

    def get_files(self, path):
        """
        Recursively search for files matching enabled extension from given base
        directory.

        Args:
            path (str): A directory path where to perform recursive search.

        Returns:
            list: List of ``pathlib.Path`` objects for each finded files.
        """
        found_for_extension = []

        for ext in self.extensions:
            found = Path(path).resolve().glob('**/*.{}'.format(ext))
            found_for_extension.extend(found)

        return found_for_extension

    def find_hexacode(self, source):
        """
        Find hexadecimal codes from given sources.

        Args:
            source (str): Source string where to search for codes.

        Returns:
            list: List of found codes. Every code are return in lowercase
                with doubles. Codes are in arbitrary order.
        """
        found = [item.lower() for item in self._reg_hexacode.findall(source)]
        return list(set(found))

    def find_rgb(self, source):
        """
        Find rgb colors from given sources

        Currently not supported until i find how to convert 255 notation to
        float notation (required from 'colour').

        Args:
            source (str): Source string where to search for rgb[a] occurences.

        Returns:
            list: List of found values.
        """
        found = self._reg_rgb.findall(source)

        values = set([])
        for item in found:
            # Rgb with alpha, ignore alpha
            segments = [v.strip() for v in item.split(',')]
            if item.startswith('#'):
                Color(segments[0])
                values.add(segments[0])
            elif len(item) > 3:
                Color(rgb=segments[0:3])
                values.add(",".join(segments[0:3]))
            # Rgb
            elif len(item) > 2:
                Color(rgb=segments[0:3])
                values.add(",".join(segments[0:3]))
            # Hexa with alpha, ignore alpha
            elif len(item) > 1 and item.startswith('#'):
                Color(segments[0])
                values.add(segments[0])
            # Hexa
            # Everything else is assumed to be invalid

        return list(values)

    def read_file(self, path):
        """
        Read given file to find all color occurences.

        Args:
            path (pathlib.Path): Path object to open.

        Returns:
            list: List of finded colors.
        """
        return self.find_hexacode(path.read_text())

    def search(self, path):
        """
        Search through file(s) for every colors

        Args:
            path (pathlib.Path): Path object where to search colors. Either:

                * A directory to recursively search for files ending with one
                  of ``ColorFinder.extensions``.
                * A single file (with any or no extension).

        Returns:
            list: List of finded colors.
        """
        found = set([])

        if path.is_dir():
            for pathobject in self.get_files(path):
                found.update(self.read_file(pathobject))
        elif path.is_file():
            found = set(self.read_file(path))

        return list(found)
