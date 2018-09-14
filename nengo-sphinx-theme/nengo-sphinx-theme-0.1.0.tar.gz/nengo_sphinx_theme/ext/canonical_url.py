from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.epub3 import Epub3Builder


def force_canonical_url(app):
    """Force the canonical URL in multiple ways.

    This gets around several points where the canonical_url override might be
    disregarded or performed out of order.
    """
    options = app.builder.theme_options
    wrong_builder = (
        not isinstance(app.builder, StandaloneHTMLBuilder)
        or isinstance(app.builder, Epub3Builder))
    no_canonical_url_info = ("canonical_url" not in options
                             or "canonical_url_path" not in options)

    if wrong_builder or no_canonical_url_info:
        return

    canonical_url = options["canonical_url"] + options["canonical_url_path"]
    app.env.config.html_context["canonical_url"] = canonical_url
    app.builder.config.html_context["canonical_url"] = canonical_url


def setup(app):
    app.connect("builder-inited", force_canonical_url)
