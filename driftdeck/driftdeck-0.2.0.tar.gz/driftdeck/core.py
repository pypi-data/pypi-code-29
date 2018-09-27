import os
import webbrowser
from io import open

from docopt import docopt
from markdown import markdown

from driftdeck.httpd import ThreadedHTTPServer
from driftdeck import __version__ as ver, __doc__ as doc


def convert(md: str, slide: int, total: int) -> str:
    """

    :param md: the markdown of one slide
    :param slide: number of the slide
    :param total: total number of slides
    :return:
    """
    html = '<html><head><link rel="stylesheet" href="style.css" /></head><body>'
    html += markdown(md, extensions=['markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.nl2br',
                                     'markdown.extensions.sane_lists',
                                     'markdown.extensions.smarty'])
    html += '<ul>'
    if slide > 1:
        html += '<li><a href="/%d">prev</a></li>' % (slide - 1)
    html += '<li>%d</li>' % slide
    if slide < total:
        html += '<li><a href="/%d">next</a></li>' % (slide + 1)
    html += '</ul><script>'
    html += '''
    window.addEventListener("keydown", function (event) {
        if (event.defaultPrevented) {
            return;
        }
        switch (event.key) {
            case "ArrowLeft":
                window.location.replace("/%d");
                break;
            case "ArrowRight":
                window.location.replace("/%d");
                break;
            default:
                return;
        }
        event.preventDefault();
    }, true);
    ''' % (slide - 1 if slide > 1 else 1,
           slide + 1 if slide < total else total)
    html += '</script></body></html>'

    return html


def start():
    args = docopt(doc, version='Drift Deck v%s' % ver)

    if args['--css'] and os.path.isfile(args['--css']):
        with open(args['--css'], 'r') as fd:
            custom_css = fd.read()
    else:
        custom_css = None

    markupfile = os.path.expanduser(args['<slides.md>'])
    with open(markupfile, 'r') as fd:
        mdslides = fd.read().split('---\n')

    htmlslides = []
    for i, slide in enumerate(mdslides, start=1):
        htmlslides.append(convert(slide, int(i), len(mdslides)))
    del mdslides

    with ThreadedHTTPServer(slides=htmlslides, css=custom_css) as s:
        webbrowser.open('http://localhost:%d/1' % s.server.server_port)
        input('Running presentation, press <Enter> to quit...')
