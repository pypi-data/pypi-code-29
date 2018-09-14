# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set
# to its containing dir.

import nengo_sphinx_theme

extensions = [
    "sphinx.ext.autodoc",
    'sphinx.ext.githubpages',
    "sphinx.ext.todo",
    "nengo_sphinx_theme",
    "nengo_sphinx_theme.ext.canonical_url",
]


# -- sphinx
nitpicky = True
exclude_patterns = ["_build", "**/.ipynb_checkpoints"]
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
project = u"Nengo Sphinx theme"
authors = u"Applied Brain Research"
copyright = nengo_sphinx_theme.__copyright__
version = ".".join(nengo_sphinx_theme.__version__.split(".")[:2])
release = nengo_sphinx_theme.__version__

# -- sphinx.ext.todo
todo_include_todos = True

# -- Options for HTML output --------------------------------------------------

pygments_style = "sphinx"
templates_path = ["_templates"]
html_static_path = ["_static"]

html_title = "Nengo Sphinx theme v{}".format(release)
html_theme = "nengo_sphinx_theme"
html_sidebars = {"**": ["sidebar.html", "sourcelink.html"]}
html_last_updated_fmt = ""  # Suppress "Last updated on:" timestamp
html_theme_options = {
    "hidesidebar": "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    "navbar_class": "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    "navbar_fixed_top": "false",

    "globaltoc_includehidden": "true",

    "canonical_url_path": "",
    "canonical_url": "https://www.nengo.ai/",
}

# -- Options for LaTeX output -------------------------------------------------

latex_documents = [
    # (source start file, target, title, author, documentclass [howto/manual])
    ("index", "nengo-sphinx-theme.tex", html_title, authors, "manual"),
]

# -- Options for manual page output -------------------------------------------

man_pages = [
    # (source start file, name, description, authors, manual section).
    ("index", "nengo-sphinx-theme", html_title, [authors], 1)
]
