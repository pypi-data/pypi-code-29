import os

from .version import version as __version__

assert __version__

__copyright__ = "2018 Applied Brain Research"
current_dir = os.path.abspath(os.path.dirname(__file__))


def setup(app):
    app.add_html_theme(
        "nengo_sphinx_theme", os.path.join(current_dir, "theme")
    )
