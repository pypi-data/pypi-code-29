# -*- coding: utf-8 -*-
"""
Export Sass color schemes
"""
import io


def export_sass_schemes(palette):
    """
    From given Sass variables, build color schemes.

    Arguments:
        palette (string): Sass variables for colors.

    Returns:
        string: Sass variable for color schemes.
    """
    colors = []
    output = []

    for item in palette.splitlines():
        if item:
            name, code = item.split(':')
            name, code = name.strip(), code.strip()
            name = name[1:]
            if code.endswith(';'):
                code = code[:-1]

            #print(name,code)
            colors.append((name, code))

    # Text color palette init
    text_palette = io.StringIO()
    text_palette.write(u'$sv-color-text-palette: (\n')

    # Scheme color init
    model_schemes = io.StringIO()

    # Text color palette init
    scheme_palette = io.StringIO()
    scheme_palette.write(u'$sv-colors-schemes: (\n')

    #
    for name,code in colors:
        text_palette.write(u'    {}: ${},\n'.format(name, name))
        scheme_palette.write(u'    {}: ${}-color-scheme,\n'.format(name, name))
        model_schemes.write(u'${}-color-scheme: (\n    background: ${},\n);\n\n'.format(name, name))

    # Text color palette output
    text_palette.write(u');\n\n')
    text_palette_content = text_palette.getvalue()
    text_palette.close()
    output.append(text_palette_content)

    # Color scheme models output
    model_schemes_content = model_schemes.getvalue()
    model_schemes.close()
    output.append(model_schemes_content)

    # Color scheme palette output
    scheme_palette.write(u');\n\n')
    scheme_palette_content = scheme_palette.getvalue()
    scheme_palette.close()
    output.append(scheme_palette_content)

    return "\n".join(output)


def export_python_schemes(palette):
    """
    From given Sass variables, build color schemes

    Arguments:
        palette (string): Sass variables for colors.

    Returns:
        string: Sass variable for color schemes.
    """
    colors = []
    output = []

    for item in palette.splitlines():
        if item:
            name, code = item.split(':')
            name, code = name.strip(), code.strip()
            name = name[1:]
            if code.endswith(';'):
                code = code[:-1]

            #print(name,code)
            colors.append((name, code))

    # Text color palette init
    text_palette = io.StringIO()
    text_palette.write(u'$sv-color-text-palette: (\n')


    # Scheme color init
    model_schemes = io.StringIO()


    # Text color palette init
    scheme_palette = io.StringIO()
    scheme_palette.write(u'$sv-colors-schemes: (\n')


    # Color palette as Python list
    python_palette = io.StringIO()
    python_palette.write(u'colors = [\n')


    #
    for name,code in colors:
        text_palette.write(u'    {}: ${},\n'.format(name, name))
        python_palette.write(u"    '{}',\n".format(name))
        scheme_palette.write(u'    {}: ${}-color-scheme,\n'.format(name, name))
        model_schemes.write(u'${}-color-scheme: (\n    background: ${},\n);\n\n'.format(name, name))


    # Text color palette output
    text_palette.write(u');\n\n')
    text_palette_content = text_palette.getvalue()
    text_palette.close()
    output.append(text_palette_content)


    # Color scheme models output
    model_schemes_content = model_schemes.getvalue()
    model_schemes.close()
    output.append(model_schemes_content)


    # Color scheme palette output
    scheme_palette.write(u');\n\n')
    scheme_palette_content = scheme_palette.getvalue()
    scheme_palette.close()
    output.append(scheme_palette_content)


    # Python color palette
    python_palette.write(u']\n\n')
    python_palette_content = python_palette.getvalue()
    python_palette.close()
    output.append(python_palette_content)

    return "\n".join(output)
