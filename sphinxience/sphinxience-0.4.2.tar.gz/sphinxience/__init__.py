__version_tuple__ = (0, 4, 2)
__version__ = '.'.join(map(str, __version_tuple__))
__version_date_latex__ = "2018/10/01" # in LaTeX format

__all__ = []

import logging, os.path
from os import path
from sphinx.locale import __
from sphinx.util.fileutil import copy_asset_file

SUBMODULES = [
    "collapse",
    "skip",
]

ASSET_FILES = [
    "sphinxience-article.cls_t",
    "sphinxience.sty_t",
]

package_dir = path.abspath(path.dirname(__file__))
logger = logging.getLogger(__name__)

def latex_is_active(app):
    return app.builder.format == 'latex'

def update_context(app, pagename, templatename, context, doctree):
    context["sphinxience_version"] = __version__

def on_build_finished(app, exc):
    # Copy static files for LaTeX after the rest of the build process is done.

    if exc is None and latex_is_active(app):
        context = dict(
            sphinxience_version = __version__,
            sphinxience_version_date_latex = __version_date_latex__
        )

        src = path.join(package_dir, 'templates')
        for asset_file in ASSET_FILES:
            src_path = path.join(src, asset_file)
            logger.info(__("Copying file %s into %s" % (src_path, app.outdir)))
            copy_asset_file(src_path, app.outdir, context=context)

def setup(app):
    app.require_sphinx('1.7')

    app.add_html_theme('sphinxience',
        os.path.abspath(os.path.dirname(__file__)))

    app.connect("html-page-context", update_context)
    app.connect("build-finished", on_build_finished)

    for submodule in SUBMODULES:
        app.setup_extension("sphinxience.{}".format(submodule))

    return {'version': __version__, "parallel_read_safe": True}