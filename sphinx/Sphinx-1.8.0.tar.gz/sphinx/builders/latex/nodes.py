# -*- coding: utf-8 -*-
"""
    sphinx.builders.latex.nodes
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Additional nodes for LaTeX writer.

    :copyright: Copyright 2007-2018 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes


class captioned_literal_block(nodes.container):
    """A node for a container of literal_block having a caption."""
    pass


class footnotemark(nodes.Inline, nodes.Referential, nodes.TextElement):
    """A node represents ``\footnotemark``."""
    pass


class footnotetext(nodes.General, nodes.BackLinkable, nodes.Element,
                   nodes.Labeled, nodes.Targetable):
    """A node represents ``\footnotetext``."""


class math_reference(nodes.Inline, nodes.Referential, nodes.TextElement):
    """A node for a reference for equation."""
    pass


class thebibliography(nodes.container):
    """A node for wrapping bibliographies."""
    pass
