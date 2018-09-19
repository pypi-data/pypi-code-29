# -*- coding: UTF-8 -*-

__author__ = "enrico ziese"
__date__ = "$04.02.2014 13:35:06$"

# Standardmodule:
from urllib import urlencode
import urllib2
from os.path import dirname, join

# Unitracc-Tools:
from visaplan.plone.pdfexport.PDFreactor import PDFreactor
from visaplan.plone.pdfexport.config import pdfreactor_kwargs, LICENSE_DATA

import logging
logger = logging.getLogger('unitracc@@pdfexport')

try:
    from visaplan.plone.tools.cfg import get_debug_active
    debug_active = get_debug_active('export')
except ImportError:
    debug_active = 1
if debug_active:
    DEBUG = logger.info
else:
    DEBUG = logger.debug
logger.info('debug_active ist %r', debug_active)
from pprint import pformat, pprint

import requests


class PDFCreator(object):

    def __init__(self, mydict):
        self.params = mydict
        if debug_active:
            DEBUG('Creating %s, params:\n%s',
                  self.__class__.__name__,
                  pformat(mydict))
        # self.conf = getConfiguration()
        self.reactor = self.createReactor(bool(debug_active))

    def createReactor(self, debug=False):
        # env = self.conf.environment
        return PDFreactor(#env['pdfreactor_host'],
                          #env['pdfreactor_port'],  # default: 9423
                          debug=debug)

    def start(self):
        self.set_key()

        # Setze Cookies
        self.setCookies()

        # setze Base url
        self.reactor.setBaseURL(self.params['base_url'])

        # Enable links in the PDF document.
        self.reactor.setAddLinks(True)
        # Enable bookmarks in the PDF document
        self.reactor.setAddBookmarks(True)
        self.reactor.setCleanupTool(self.reactor.CLEANUP_NONE)
        self.reactor.setLogLevel(self.reactor.LOG_LEVEL_INFO)
        self.reactor.setEncoding('UTF-8')
        self.reactor.setJavaScriptMode(self.reactor.JAVASCRIPT_MODE_ENABLED_NO_LAYOUT)
        self.reactor.addUserScript("""document.body.innerHTML = \
        document.body.innerHTML.replace(/[\\x00-\\x08\\x0B\\x0C\\x0E-\\x1F\\uFFFD]/gi, '')""",
        "",
        True)

        e = None
        pdfcontent = None
        htmlcontent = None
        USE_CONTENT = 1
        try:
            if USE_CONTENT:
                print '#' * 79
                # print dir(self.reactor)
                # print '#' * 79
                cookies = self.params['cookie']
                pprint({'cookies:': cookies,
                        'url': self.params['url'],
                        })
                req = requests.get(self.params['url'], cookies=cookies)
                text = req.text
                print '%d Bytes gelesen:\n%s\n...' % (len(text), text[:1000])
                print '#' * 79
                pdfcontent = self.reactor.renderDocumentFromContent(text)
                print '#' * 79
            else:
                pdfcontent = self.reactor.renderDocumentFromURL(self.params['url'])

        except urllib2.HTTPError as e:
            self.sendMail('failure')
            logger.error("Fehler bei PDF-Erzeugung: %s", str(e))
            logger.exception(e)
        except urllib2.URLError as e:
            self.sendMail('failure')
            logger.error("PDFreactor not available! (%s)", str(e))
            logger.exception(e)
        except Exception as e:
            self.sendMail('failure')
            logger.error("Fehler (%s) bei PDF-Erzeugung: %s",
                    e.__class__.__name__,
                    str(e))
            logger.exception(e)

        finally:
            if pdfcontent is None:
                errtxt = self.reactor.getError()
                logger.error('PDFreactor error: %s', errtxt)
                logtxt = self.reactor.getLog()
                logger.error('PDFreactor error:\n%s', logtxt)
                self.sendMail('failure')
            else:
                self.writePDF(pdfcontent)

    def writePDF(self, content):
        path = self.params['path']
        uid = self.params['brain'].UID
        profile = self.params['export']
        name = uid + "-" + profile + ".pdf"
        f = open(path + name, "w")
        f.write(content)
        f.close()
        self.sendMail('success')

    def sendMail(self, status):
        """
        Auf der URL:object.absolute_url/@@export/sendMail mit params
        """

        # Parameter Dictionary
        params = {'status': status,
                  'etype': 'pdf',
                  }

        params.update(self.params['cookie'])
        data = urlencode(params)

        # URL aufbau
        base_url = self.params['object_url']
        url = "%s/@@export/sendMail" % base_url

        req = urllib2.Request(url, data, {})
        try:
            urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            logger.ERROR("error while send Mail")

    def _fixCookies(self):
        """
        Potentiell unverdauliche Cookies korrigieren
        """
        cookies = self.params['cookie']
        for k, v in cookies.items():
            if '&;' in v:
                if k == 'mjx.menu':
                    cookies[k] = v.replace('&;', ';')
                    logger.warn('Cookie %r:\n%s\n -->\n%s',
                                k, v, cookies[k])
                else:
                    logger.error('Komischer Wert %r fuer unbekanntes Cookie %r!',
                                 v, k)
                    del cookies[k]
                    logger.info('Cookie %r entfernt.', k)

    def setCookies(self, asHeader=False):
        """
        Setzen der Cookies für Authentication des pdfreactors bei Zope
        Cookie=Usercookie
        """
        self._fixCookies()
        for k, v in self.params['cookie'].items():
            self.reactor.setCookie(k, v)

    def set_key(self):
        key = LICENSE_DATA
        if key:
            self.reactor.setLicenseKey(LICENSE_DATA)


if __name__ == "__main__":
    url = 'http://plone4.vbox-therp.sbs-sup.local/akademie/vortraege/auskleidung-mit-oertlich-hergestellten-und-erhaertenden-rohren/html_view?isPDFExport=True&pid=1'
    cookies = {'_ZopeId': '35275626A6haFTtPY6o',
              '__ac': 'dtHC7i58885Ov3AqOXlz/4MpchcgW9oi4/TzdjTJfnA1M2NjZTNmNXRoZXJwIQ==',
              '__utma': '143836146.50691779.1326882381.1371030693.1398168047.662',
              '__utmc': '260597580',
              '__utmz': '260597580.1404289116.499.14.utmcsr=dev-wiki.unitracc.de|utmccn=(referral)|utmcmd=referral|utmcct=/wiki/Mail-ControlPanel',
              'mjx.menu': 'locale:de&;renderer:HTML-CSS',
              'useruid': '88dafad3417290b54727041e1d29a791'}
    urlli = url.split('/')
    base_url = '/'.join(urlli[:3])
    object_url = '/'.join(urlli[:-1])
    params = {'base_url': base_url,
              'cookie': cookies,
              'export': '1',
              'object_url': object_url,
              'path': '/var/zope-instance/plone4-therp/var/pdfs/',
              'url': url,
              }
    pprint(params)
    reactor = PDFCreator(params)
    # reactor.setLogLevel(reactor.LOG_LEVEL_DEBUG)
    print '->'*39
    import pdb
    pdb.set_trace()
    reactor.start()
