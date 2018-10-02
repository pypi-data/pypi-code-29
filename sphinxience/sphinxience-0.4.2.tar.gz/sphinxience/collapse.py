# -*- coding: utf-8 -*-
"""
    Collapse directive.

    :copyright: Copyright 2014 by Bram Geron.
    :license: BSD 3-clause.
"""

from docutils import nodes
from docutils.nodes import paragraph, emphasis
import docutils.parsers.rst.directives.admonitions
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.roles import set_classes
from . import latex_is_active, logger, package_dir
from os import path
from sphinx.locale import __
from sphinx.util.fileutil import copy_asset_file


CSS_FILES = [
    "collapse-details-polyfill.css",
]
JS_FILES = [
    "jquery.details.min.js",
    "collapse-details-polyfill.js",
]

" ------- SETUP ------ "

def setup(app):

    # * When rendering a collapse node in HTML, add certain HTML tags, then
    #   render the children.
    # * When rendering a collapse node elsewhere, just render its children.
    html_actions = (visit_collapse_html, depart_collapse_html)
    latex_actions = (visit_collapse_latex, depart_collapse_latex)
    other_actions = (passthrough, passthrough)
    # * When rendering a replacement in HTML, ignore it.
    # * When rendering a replacement elsewhere
    replacement_html_actions = (visit_skipnode, depart_skipnode)
    replacement_other_actions = (visit_skipsiblings, depart_skipsiblings)
    app.add_node(collapse,
        html=html_actions,
        latex=latex_actions, text=other_actions,
        man=other_actions, texinfo=other_actions)
    app.add_node(replacement,
        html=replacement_html_actions,
        latex=replacement_other_actions, text=replacement_other_actions,
        man=replacement_other_actions, texinfo=replacement_other_actions)
    app.add_directive('collapse', CollapseDirective)
    # No directive for replacement, because we only want to create it programmatically.
    app.connect('builder-inited', on_builder_inited)
    app.connect("build-finished", on_build_finished)

    return {
        'version': "0.1",
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

def on_builder_inited(app):
    for css in CSS_FILES:
        app.add_stylesheet(css)
    for js in JS_FILES:
        app.add_javascript(js)

def on_build_finished(app, exc):
    # Copy static files for LaTeX after the rest of the build process is done.

    if exc is None and latex_is_active(app):
        for file in CSS_FILES + JS_FILES:
            src = path.join(package_dir, 'static', file)
            dest = path.join(app.outdir, '_static')
            logger.info(__("Copying file %s into %s" % (src, dest)))
            copy_asset_file(src, dest)

" ------- NODES ------ "

class collapse(nodes.Admonition, nodes.Element):

    pass

class replacement(nodes.General, nodes.Element):
    """A node that serves as a replacement in case we're not writing
    to HTML, in a sense similar to the HTML <noframes> element.

    If we're visiting as HTML, we skip this node.

    If we're visiting otherwise, we visit the children and skip the siblings.
    """

" ------- DIRECTIVES ------ "

class CollapseDirective(directives.admonitions.BaseAdmonition):

    node_class = collapse

    def run(self):

        (node,) = super(CollapseDirective, self).run()

        # Add a replacement node with some text.
        replnode = replacement(node.rawsource,
            paragraph(node.rawsource, "",
                emphasis(node.rawsource, "(Some stuff hidden.)")))
        node.insert(0, replnode)

        return [node]

" ------- VISITOR FUNCTIONS ------ "

def visit_collapse_html(self, node):
    self.body.append(self.starttag(node, 'details'))
    self.body.append(self.starttag(node, 'summary'))
    # self.visit_title(node.title)
    self.body.append("(collapsed)")
    self.body.append("</summary>")
    self.body.append(self.starttag(node, 'div'))

def depart_collapse_html(self, node):
    self.body.append('</div>')
    self.body.append('</details>')

def visit_collapse_latex(self, node):
    self.body.append('\n\n' + r'{\scriptsize ')
    # Replacement text will follow.

def depart_collapse_latex(self, node):
    self.body.append('}\n\n')

def passthrough(self, node): pass

def visit_skipnode(self, node):
    raise nodes.SkipNode
def depart_skipnode(self, node): pass

def visit_skipsiblings(self, node): pass
def depart_skipsiblings(self, node):
    raise nodes.SkipSiblings
