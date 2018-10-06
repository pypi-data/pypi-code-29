# -*- coding: utf-8 -*-
"""
Export dumped JSON named colors to some formats
"""
import io
import json


def export_html(palette):
    """
    Return a HTML string for a palette preview

    Arguments:
        palette (dict): Dictionnary of named colors (as dumped in JSON from
            ``colors`` command)

    Returns:
        string: HTML preview.
    """
    # HTML color palette
    html_palette = io.StringIO()
    html_palette.write('<div class="palette" style="display: flex; flex-direction: row; flex-wrap: wrap;">\n')

    for original_code, values in sorted(palette.items(), key=lambda x:x[1]):
        name, from_color = values
        html_palette.write('  <div class="item" style="flex: 1 0 20%; max-width: 20%; padding: 0.5rem;">\n')
        html_palette.write('    <div class="color" style="background-color: {}; width: 100%; height: 3rem;"></div>\n'.format(original_code))
        html_palette.write('    <p class="code" style="">{}</p>\n'.format(original_code))
        html_palette.write('    <p class="name" style="">{}</p>\n'.format(name))
        html_palette.write('  </div>\n')

    html_palette.write('</div>\n')

    output = html_palette.getvalue()

    html_palette.close()

    return output


def export_sass(palette):
    """
    Return a string of Sass variable for every colors.

    Arguments:
        palette (dict): Dictionnary of named colors (as dumped in JSON from
            ``colors`` command)

    Returns:
        string: Sass variables.
    """
    # Sass color palette variable
    sass_palette = io.StringIO()

    for original_code, values in sorted(palette.items(), key=lambda x:x[1]):
        name, from_color = values
        sass_palette.write('${}: {};\n'.format(name, original_code))

    output = sass_palette.getvalue()

    sass_palette.close()

    return output


def export_python(palette):
    """
    Return a string of a Python tuple of every named colors.

    Arguments:
        palette (dict): Dictionnary of named colors (as dumped in JSON from
            ``colors`` command)

    Returns:
        string: Python tuple.
    """
    # Open Python tuple
    python_palette = io.StringIO()
    python_palette.write(u'colors = (\n')

    for original_code, values in sorted(palette.items(), key=lambda x:x[1]):
        name, from_color = values
        python_palette.write("    ('{}', '{}'),\n".format(name, original_code))

    # Close Python tuple
    python_palette.write(u')\n\n')

    output = python_palette.getvalue()

    python_palette.close()

    return output
