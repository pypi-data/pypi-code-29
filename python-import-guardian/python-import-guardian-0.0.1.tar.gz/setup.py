# Copyright 2018 Graham Binns <graham@outcoded.uk>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""setup.py script for python-import-guardian."""

from distutils.core import setup

setup(
    name="python-import-guardian",
    packages=["importguardian"],
    version="0.0.1",
    description="A static-analysis Python import guardian.",
    author="Graham Binns",
    author_email="graham@outcoded.uk",
    url="https://gitlab.com/gmb/python-import-guardian",
    download_url=(
        "https://gitlab.com/gmb/python-import-guardian/-/archive/master/python-import-guardian-master.tar.gz"),
    keywords=["import", "guardian", "static-analysis"],
    classifiers=[],
    entry_points={
        "console_scripts": [
            "import-guardian = importguardian.importguardian:main",
        ]
    }
)
