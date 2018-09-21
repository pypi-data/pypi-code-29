# -*- coding: utf-8 -*-

import setuptools
import re

with open("README.txt", "r") as fh:
    long_description = fh.read()
long_description = re.sub('^[.][.] role:: rem[(]comment[)]', '', long_description)
long_description = re.sub(':rem:`[^`]*`(\\\\ )?', '', long_description)

with open(".version", "r") as fh:
    version = fh.read().strip()

setuptools.setup(
    name="snappets",
    version=version,
    author='Wolfgang Scherer',
    author_email="wolfgang.scherer@gmx.de",
    description="Snippets in Python",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://bitbucket.org/wolfmanx/snappets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)

# :ide-menu: Emacs IDE Menu - Buffer @BUFFER@
# . M-x `eIDE-menu' ()(eIDE-menu "z")

# :ide: COMPILE: Run with python3 --test
# . (progn (save-buffer) (compile (concat "python3 ./" (file-name-nondirectory (buffer-file-name)) "  --test")))

# :ide: COMPILE: Run with python3 w/o args
# . (progn (save-buffer) (compile (concat "python3 ./" (file-name-nondirectory (buffer-file-name)) " ")))

# :ide: COMPILE: Run with --test
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --test")))

# :ide: COMPILE: Run w/o args
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " ")))

# :ide: COMPILE: Run with sdist --manifest-only
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " sdist --manifest-only")))

# :ide: COMPILE: Run with sdist
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " sdist")))

# :ide: +-#+
# . Compile ()

#
# Local Variables:
# mode: python
# comment-start: "#"
# comment-start-skip: "#+"
# comment-column: 0
# truncate-lines: t
# End:
