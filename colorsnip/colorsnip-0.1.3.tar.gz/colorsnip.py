"""
Colorsnip is provided under the MIT License:

Copyright (c) 2018, Joachim Jablon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Usage: colorsnip [{filename,-}, ...]
Reads all provided files, syntax highlight them and copy that
to your MacOS clipboard
"""

import platform
import sys

import pygments
import pygments.lexers
import pygments.formatters

def main():
    filename = sys.argv[1]
    colorsnip(filename)

def copy(text, html, rtf):
    if platform.system() == "Darwin":
        copy_richxerox(text, html, rtf)
    else:
        copy_klembox(text, html)

def copy_richxerox(text, html, rtf):
    import richxerox
    richxerox.copy(text, html=html, rtf=rtf)

def copy_klembox(text, html):
    import klembox
    klembord.set_with_rich_text(text, html)


def colorsnip(filename):

    if filename == "-":
        contents = sys.stdin.read()
        lexer = pygments.lexers.guess_lexer_for_filename(
            filename, contents)
    else:
        with open(filename) as fh:
            contents = fh.read()
        lexer = pygments.lexers.get_lexer_for_filename(filename)

    html_formatter = pygments.formatters.get_formatter_by_name(
        "html",
        style="monokai")
    rtf_formatter = pygments.formatters.get_formatter_by_name(
        "rtf",
        style="monokai",
        fontface="Menlo",
        fontsize=60)
    html = pygments.highlight(
        code=contents,
        lexer=lexer,
        formatter=html_formatter)
    rtf = pygments.highlight(
        code=contents,
        lexer=lexer,
        formatter=rtf_formatter)

    copy(text=contents, html=html, rtf=rtf)


if __name__ == '__main__':
    main()
