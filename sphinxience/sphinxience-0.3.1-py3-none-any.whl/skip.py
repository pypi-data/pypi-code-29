r"""
Skip directive. Adds a bit of vertical space.

Usage:

    .. skip:: big

This adds a \bigskip  in the LaTeX, and a vertical space in the HTML. For HTML
standards, the space is not very big.

It is not possible to give a custom skip size. But of course, you can make
your own tweaks to this file of Sphinxience. Maybe even send in a pull request
if you think it will be popular!

The current skip sizes are as follows:

-   ``para``: Paragraph break in LaTeX (two newlines), nothing in HTML.

-   ``paramed``: Paragraph break + ``\medskip`` in LaTeX, nothing in HTML.

-   ``big``: Paragraph break + ``\bigskip`` in LaTeX, a similar amount in HTML.

-   ``xxlarge``: An absurdly large skip in both LaTeX and HTML. Can be useful for
    visually separating parts of your notes.

-   ``forceabovedisplaysmallskip``: When used between a paragraph and display
    math, forcibly turns a ``\abovedisplayskip`` into a
    ``\abovedisplayshortskip``.

Note that the Sphinx LaTeX writer does already insert paragraph breaks between
paragraphs. It does not insert paragraph breaks in certain other situations,
like a math display following a paragraph, or a paragraph following a math
display. So the combination (paragraph + math display + paragraph) will come
out in LaTeX as one paragraph, as if you wrote
``paragraph1\[math\]paragraph2``.
"""

from docutils import nodes
from docutils.parsers.rst import Directive
import docutils.parsers.rst.directives as directives
from sphinx.errors import SphinxError

def setup(app):
    app.add_node(skip,
                 html=(visit_skip_html, depart_skip_html),
                 latex=(visit_skip_tex, depart_skip_tex))
    app.add_directive('skip', SkipDirective)

    return {
        'version': "0.1",
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

class skip(nodes.General, nodes.Element):
    pass

class SkipError(SphinxError):
    pass

class SkipDirective(Directive):
    
    has_content = True

    option_spec = {}

    def run(self):
        if self.content.data == []:
            raise self.error("missing skip size")
        elif not isinstance(self.content.data, list) or len(self.content.data) != 1:
            raise self.error("skip size decl not recognised: " + repr(self.content.data))

        size = self.content.data[0]

        if size in ALLOWEDSIZES:
            return [skip(size=size)]
        else:
            raise self.error("skip size not recognised: " + repr(size))

ALLOWEDSIZES = ['para', 'paramed', 'big', 'xxlarge', 'forceabovedisplaysmallskip']

def visit_skip_tex(self, node):
    if node['size'] == 'para':
        self.body.append("\n\n")
    elif node['size'] == 'paramed':
        self.body.append("\n\n\\medskip\n\n")
    elif node['size'] == 'big':
        self.body.append("\n\n\\bigskip\n\n")
    elif node['size'] == 'xxlarge':
        self.body.append("\n\n\\vfill\n\n")
    elif node['size'] == 'forceabovedisplaysmallskip':
        self.body.append(r'\vspace{\abovedisplayshortskip}\vspace{-\abovedisplayskip}')
    else:
        raise SkipError("cannot render skip size %r to latex"
            % (node['size'],))

def depart_skip_tex(self, node):
    pass

def visit_skip_html(self, node):
    if node['size'] in ['para', 'paramed', 'forceabovedisplaysmallskip']:
        pass # not necessary in HTML
    elif node['size'] in ['big', 'xxlarge']:

        self.body.append(
            self.starttag(node, 'div', **{'class': 'sphinxience-skip-%s' % (node['size'],)}))
        self.body.append("</div>")

    else:
        raise SkipError("cannot render skip size %s to HTML"
            % (node['size'],))


def depart_skip_html(self, node):
    pass
