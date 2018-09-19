# -*- coding: UTF-8 -*- äöü

__author__ = "enrico ziese"
__date__ = "$04.02.2014 13:35:06$"

# siehe neues Modul ../../tools/pdf/creator.py

# Standardmodule:
from urllib import urlencode
import urllib2
from os.path import dirname, join

# Plone/Zope/Dayta:
from App.config import getConfiguration

# Unitracc-Tools:
from visaplan.plone.pdfexport.PDFreactor import PDFreactor
from visaplan.plone.pdfexport.config import pdfreactor_kwargs, LICENSE_DATA
from visaplan.plone.pdfexport.utils import ApiFilter, acceptable_method_name

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.debug import pp, log_or_trace
from visaplan.tools.dicts import updated
logger, debug_active, DEBUG = getLogSupport(default='2')
logger.info('debug_active ist %r', debug_active)
from pprint import pformat

lot_kwargs = {'logger': logger,
              'debug_level': debug_active,
              }

import requests

class PDFCreator(object):
    """
    Für jeden PDF-Export wird ein PDFCreator-Objekt erzeugt
    """

    def __init__(self, mydict):
        self.params = mydict
        if debug_active:
            DEBUG('Creating %s, params:\n%s',
                  self.__class__.__name__,
                  pformat(mydict))
        self.conf = getConfiguration()
        if debug_active:
            pp({'self.conf': self.conf})
        self.reactor = self.createReactor(bool(debug_active))

    def createReactor(self, debug=None):
        kwargs = dict(pdfreactor_kwargs)
        if debug is not None:
            kwargs['debug'] = debug
        return PDFreactor(**kwargs)

    def doApiCalls(self):
        """
        Interpretiere die Liste der API-Aufrufe und führe sie aus.

        Änderungen der PDFreactor-Defaults:
        - setAddLinks(True)
          PDFreactor-Default wäre setAddLinks(False).
          Der PDFreactor differenziert nicht zwischen lokalen (die für
          Querverweise benötigt werden, insbesondere aus Verzeichnissen)
          und externen Hyperlinks.
          Der API-Aufruf wird beim Parsen abgefangen (skip_this-Methode)
          und der Wert im transform-Browser verwendet, um ggf. dort
          die Hyperlinks zu entfernen - dann aber nur die externen.
        - setJavaScriptMode(JAVASCRIPT_MODE_ENABLED)
          Wir benötigen Javascript-Unterstützung, um die in PDFreactor 7 noch
          nicht behobenen Layout-Fehler zu umgehen
        """
        if 0 and 'fix whitespace':
            calls_after = ("addUserScript('"
                    "document.body.innerHTML = "
                    "document.body.innerHTML.replace(/[\\x00-\\x08\\x0B\\x0C"
                                                    "\\x0E-\\x1F\\uFFFD]/gi,"
                                                    ' "")'
                    "', '', True);\n")
        else:
            calls_after = ''
        calls_after += ("addUserScript('ro.layout.forceRelayout();',"
                        " Null, False);\n"
                        )

        # mit JAVASCRIPT_MODE_ENABLED_NO_LAYOUT stünden keine Layout-Infos zur
        # Verfügung; diese werden für die Marginalien derzeit aber noch
        # gebraucht (noch kein float: outer):
        calls_default = '''\
        setEncoding('UTF-8')
        setJavaScriptMode(JAVASCRIPT_MODE_ENABLED)
        # Enable bookmarks in the PDF document
        setAddBookmarks(True)
        setCleanupTool(CLEANUP_NONE)
        setLogLevel(LOG_LEVEL_%(loglevel)s)
        setAppendLog(%(appendlog)r)
        ''' % {'loglevel': debug_active and 'DEBUG' or 'INFO',
               'appendlog': debug_active >= 2,
               }
        message = self.params['context'].getAdapter('message')
        self.reactor.setAddLinks(True)  # siehe Docstring
        ok = ApiFilter(calls_default=calls_default,
                       calls_after=calls_after,
                       log=DEBUG,
                       msg=message,
                       check_methodname=acceptable_method_name
                       )(self.params['pdfreactor_api_calls'],
                         reactor=self.reactor)
        return ok

    @log_or_trace(**updated(lot_kwargs, trace=0))
    def start(self):
        """
        Setze vordefinierte und konfigurierbare API-Aufrufe ab,
        rufe ggf. die Seite ab (um vorab HTML-Textänderungen vorzunehmen)
        und starte die Generierung.
        """
        # Lizenzschlüssel
        self.set_key()

        # Session an PDFreactor weiterreichen, wg. zugriffsbeschränkter Inhalte:
        self.setCookies()
        logger.info('start: setting base_url to %(base_url)r', self.params)
        self.reactor.setBaseURL(self.params['base_url'])

        if not self.doApiCalls():
            self.sendMail('failure')
            logger.error("API-Fehler bei PDF-Erzeugung"
                         "; Generierung abgebrochen")
            return

        e = None
        pdfcontent = None
        htmlcontent = None
        USE_CONTENT = 0
        # Der Thread läuft in derselben Session, in der die Generierung angefordert wurde, oder?
        # message = self.params['context'].getAdapter('message')
        try:
            if USE_CONTENT:
                print '#' * 79
                # print dir(self.reactor)
                # print '#' * 79
                cookies = self.params['cookie']
                pp({'cookies:': cookies,
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
            logger.error("Fehler bei PDF-Erzeugung: %s", str(e))
            logger.exception(e)
        except urllib2.URLError as e:
            logger.error("PDFreactor not available! (%s)", str(e))
            logger.exception(e)
        except Exception as e:
            logger.error("Fehler (%s) bei PDF-Erzeugung: %s",
                    e.__class__.__name__,
                    str(e))
            logger.exception(e)

        finally:
            if pdfcontent is None:
                logger.error('self.reactor is %r', self.reactor)
                try:
                    errtxt = self.reactor.getError()
                    logger.error('PDFreactor error: %s', errtxt)
                except Exception as e:
                    logger.error('PDFreactor error, and getError failed!')
                    logger.exception(e)
                try:
                    logtxt = self.reactor.getLog()
                    logger.error('PDFreactor error log:\n%s', logtxt)
                except Exception as e:
                    logger.error('PDFreactor error, and getLog failed!')
                    logger.exception(e)
                try:
                    self.sendMail('failure')
                    logger.info('failure notification mail sent')
                except Exception as e:
                    logger.error('PDFreactor error, and getLog failed!')
                    logger.exception(e)

            else:
                self.writePDF(pdfcontent)

    # Achtung: der Dateiname hängt nur von UID und Profil-ID ab;
    #          bei wiederholter Generierung muß der Systembenutzer derselbe sein,
    #          oder die Gruppe muß die Schreibberechtigung haben!
    def writePDF(self, content):
        path = self.params['path']
        uid = self.params['brain'].UID
        profile = self.params['export']
        name = uid + "-" + profile + ".pdf"
        fullname = path + name
        logger.info('Save PDF to %(fullname)s ...', locals())
        try:
            with open(fullname, 'w') as f:
                f.write(content)
        except (OSError, IOError) as e:
            logger.exception(e)
            logger.error('Error saving %(fullname)s', locals())
        else:
            self.sendMail('success')

    def sendMail(self, status):
        """
        Auf der URL:object.absolute_url/@@export/sendMail mit params
        """
        logger.info('sendMail(%(status)r) ...', locals())

        # Parameter Dictionary
        params = {'status': status,
                  'etype': 'pdf',
                  }

        try:
            params.update(self.params['cookie'])
            data = urlencode(params)

            # URL aufbau
            base_url = self.params['object_url']
            url = "%s/@@export/sendMail" % base_url
            logger.info('... url = %(url)r', locals())
            logger.info('... data = %(data)r', locals())

            logger.info('sendMail: url=%(url)r', locals())
            req = urllib2.Request(url, data, {})
            logger.info('sendMail: req=%(req)r', locals())
            try:
                urllib2.urlopen(req)
                logger.info('sendMail: URL opened, mail probably sent')
                return True
            except Exception as e:
                #  urllib2.HTTPError?
                logger.error("sendMail: error %(e)r opening URL '%(url)r'!", locals())
                logger.exception(e)
                for k, v in params.items():
                    logger.info('  %(k)s: %(v)r', locals())
        except Exception as e:
            logger.error("sendMail(%(status)r): error %(e)r!", locals())
            logger.exception(e)

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
