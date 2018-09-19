# -*- coding: UTF-8 -*- äöü
"""
unitracc@@export - Browser zum Export über Exportprofile

SCORM-Exporte werden durch den Browser --> courseexport erledigt; dieser
unterstützt bzw. benötigt keinerlei Parameter außer dem Ausgabetypen (weshalb
dafür derzeit keine Exportprofile verwendet werden)
"""

# Standardmodule:
import os
from os.path import normpath, join, getmtime
from os.path import dirname, splitext
import thread
from datetime import datetime
from time import strftime

# Plone/Zope/Dayta:
from AccessControl import Unauthorized
from App.config import getConfiguration
from dayta.browser.public import Interface, BrowserView, implements

# Unitracc-Tools:
from visaplan.plone.tools.forms import tryagain_url, merge_qvars
from visaplan.tools.minifuncs import translate_dummy
from visaplan.tools.minifuncs import makeBool
from visaplan.plone.tools.cfg import get_raw_config
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.profile import StopWatch

# Dieser Browser:
from .pdf_creator import PDFCreator
from .crumbs import OK  # Brotkrümel

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport('export', default='2')
from visaplan.tools.debug import pp, log_or_trace
from visaplan.tools.dicts import updated
from pprint import pformat
sw_kwargs = {'enable': bool(debug_active),  # für StopWatch
             'logger': logger,
             }
lot_kwargs = {'logger': logger,
              'debug_level': debug_active,
              # ggf. mit updated-Funktion übersteuern:
              'trace': 0,
              }


# Konfiguration:
export_cfg = get_raw_config('export')
pdfs_cfg = get_raw_config('pdfs')
EXPORT_VIA_HTTP = 1  # TODO: in pdfs_cfg integrieren

DEBUG('Konfiguration (export): %s', export_cfg)
DEBUG('Konfiguration (pdfs): %s', pdfs_cfg)


class IExport(Interface):

    def make_export(self, profile_id):
        """
        Erstelle den angeforderten Export.
        """

    def viewExportProfile(self):
        """
        Wrapper für neues Profil
        """

    def newExportProfile(self):
        """
        Wrapper für neues Profil
        """

    def addExportProfile(self):
        """
        ein neues Profil anlegen
        """

    def editExportProfile(self):
        """
        Ein Profil editieren
        """

    def updateExportProfile(self):
        """
        Update existing Profile
        """

    def deleteExportProfile(self):
        """
        Profil löschen
        """

    def export(self):
        """
        Exportiere den gewünschten Inhalt in dem gewünschten Typ
        """

    def getFile(self, ftype):
        """
        gib Datei zurück
        """

    def sendMail(self):
        """
        Sende E-Mail an Nutzer mit Erfolgs- oder Fehlermeldung
        """

    def getCookieLines(self):
        """
        Zum Export einer Cookie-Datei, siehe <https://curl.haxx.se/mail/archive-2005-03/0099.html>
        und (gf) templates/cookies.txt.pt
        """

    def _getRawContent(self, obj, ctype, maxdepth=1):
        """
        Gib den Inhalt des Typs <ctype> zurück;
        für "Folder" den der zugeordneten Standardseite.

        obj -- das untersuchte Objekt
        ctype -- 'text' oder 'notes'
        maxdepth -- Abbruchkriterium für Rekursion
        """


class Browser(BrowserView):

    implements(IExport)

    # ------------------------------- [ Exportprofile verwalten ... [
    # XXX Siehe http://dev-wiki.unitracc.de/wiki/PDF-Export
    def profilesOverview(self):
        """
        Gib die Profilname das Erstellungsdatum und den Ersteller zurück
        """
        return self.getProfile(all=True)

    def viewExportProfile(self):
        """
        Ein bestimmtes Profil in der Detailansicht anzeigen
        """
        context = self.context
        request = context.REQUEST
        auth = context.getBrowser('authorized')
        auth.authorized('unitracc: Manage Export Profiles')
        pid = request.form.get('pid')
        if not pid:
            return request.response.redirect(request['HTTP_REFERER'])
        profile = self.getProfile(id=pid)
        if not profile:
            return request.response.redirect(request['HTTP_REFERER'])
        return context.restrictedTraverse('edit_export_profile'
                                          )(profile=profile,
                                            view=True)

    def newExportProfile(self):
        """
        Wrapper für neues Profil
        """
        auth = self.context.getBrowser('authorized')
        auth.authorized('unitracc: Manage Export Profiles')
        return self.context.restrictedTraverse('new_export_profile')()

    def editExportProfile(self):
        """
        Ein Profil editieren
        """
        # Siehe --> updateExportProfile
        context = self.context
        auth = context.getBrowser('authorized')
        auth.authorized('unitracc: Manage Export Profiles')
        request = context.REQUEST
        pid = request.form.get('pid')
        if not pid:
            return request.response.redirect(request['HTTP_REFERER'])
        profile = self.getProfile(id=pid)
        if not profile:
            return request.response.redirect(request['HTTP_REFERER'])
        return context.restrictedTraverse('edit_export_profile'
                                          )(profile=profile,
                                            view=False)

    def deleteExportProfile(self):
        """
        Profil löschen

        ToDo: Nicht mehr löschen, sondern nur noch deaktivieren!
        """
        context = self.context
        context.getBrowser('authorized'
                           ).authorized('unitracc: Manage Export Profiles')
        request = context.REQUEST
        redirect = request.response.redirect
        pid = request.form.get('pid')
        msg = context.getAdapter('message')
        _ = context.getAdapter('translate')
        if not pid:
            msg(_('No Profile ID submitted.'),
                'error')
            return redirect(request['HTTP_REFERER'])
        with context.getAdapter('sqlwrapper') as sql:
            where = "WHERE id=%(id)s"
            qdata = {'id': pid}
            msg(_('Profile deleted.'))
            sql.delete("unitracc_export_profile", where, qdata)
            return redirect(request['HTTP_REFERER'])

    def addExportProfile(self):
        """
        ein neues Profil anlegen
        """
        context = self.context

        context.getBrowser('authorized').authorized('unitracc: Manage Export Profiles')

        req = context.REQUEST
        form = req.form

        # Titel inhalte Prüfen
        form_titles = [(x, v) for x, v in form.items() if x.startswith("title_")]
        titles = []
        for items in form_titles:
            k, v = items
            lang = k.split("_")[1]
            if v:
                titles.append((lang, v))
        if not titles:
            msg = context.getAdapter('message')
            msg(""'Please enter a title.')
            return req.response.redirect(req['HTTP_REFERER'])
        # Portal übergeben?
        subportals = form.get('subportal', [])
        if not subportals:
            msg = context.getAdapter('message')
            msg(""'Please select a subportal.')
            return req.response.redirect(req['HTTP_REFERER'])

        creator = context.getBrowser('author').get()
        subs = context.getBrowser('subportal').get()
        creator = creator.getUserId()
        now = datetime.now()
        active = form.get('active', False)
        manual_css = form['manual_css']
        etype_id = int(form.get('etype', '1'))

        if isinstance(subportals, str):
            subportals = [subportals]

        # Profil speichern
        table = "unitracc_export_profile"
        values = {'creator': creator,
                  'active': active,
                  'type_id': etype_id,
                  'manual_css': manual_css,
                  'pdfreactor_api_calls': form.get('pdfreactor_api_calls'),
                  'creation_date': now,
                  'main_template': form.get('main_template', ''),
                  'browser_id': form.get('browser_id', ''),
                  }
        with context.getAdapter('sqlwrapper') as sql:
            id = sql.insert(table, values, returning=["id"]).next()
            title_table = "unitracc_export_profile_titles"

            for title in titles:
                sql.insert(title_table,
                           {'title': title[1],
                            'lang_code': title[0],
                            'profile_id': id['id'],
                            })

            for subportal in subportals:
                subportal_row = sql.select(table="unitracc_subportal",
                                           fields=['id'],
                                           query_data={'uid': subportal},
                                           maxrows=1)
                # Noch kein Subportal vorhanden
                if not subportal_row:
                    new_portal = subs[subportal]
                    subportal_row = sql.insert("unitracc_subportal",
                                               {'uid': subportal,
                                                'subportal': new_portal['title'],
                                                },
                                               returning=['id']).next()
                else:
                    subportal_row = subportal_row[0]

                sql.insert("unitracc_subportal_unitracc_export_profile",
                           {'subportal': subportal_row['id'],
                            'profile': id['id'],
                            })
            pos = 0
            stylesheets = form.get('cssfiles')
            if stylesheets:
                for name in stylesheets:
                    pos += 1
                    sql.insert("unitracc_export_css",
                               {'css_name': name,
                                'load_position': int(pos),
                                'profile_id': id['id'],
                                })

        return context.REQUEST.response.redirect('/manage_export_profiles')

    # ------------------------------ [ Exportprofil ändern ... [
    def updateExportProfile(self):
        """
        Update existing Profile

        ToDo: Profile nicht mehr ändern (Ausnahme: wenn nur die
        Bezeichnung geändert wird), sondern eine Kopie mit neuer Nummer
        anlegen und das Original deaktivieren!
        """
        context = self.context
        context.getBrowser('authorized').authorized('unitracc: Manage Export Profiles')
        redirect = context.REQUEST.response.redirect
        req = context.REQUEST
        form = req.form
        pid = form.get('pid')
        subs = context.getBrowser('subportal').get()
        if not pid:
            return redirect("/manage_profiles")

        if form.get('cancel'):
            return redirect('/@@export/viewExportProfile?pid=%s' % pid)
        form_titles = [(x, v)
                       for x, v in form.items()
                       if x.startswith("title_")
                       ]
        titles = []
        for items in form_titles:
            k, v = items
            lang = k.split("_")[1]
            if v:
                titles.append((lang, v))
        if not titles:
            msg = context.getAdapter('message')
            msg('Please enter a title.')
            return redirect(req['HTTP_REFERER'])

        # Portal übergeben?
        subportals = form.get('subportal', [])
        if not subportals:
            msg = context.getAdapter('message')
            msg('Please select a subportal.')
            return redirect(req['HTTP_REFERER'])



        # Nicht verwendete CSS-Dateien aus Liste löschen


        with context.getAdapter('sqlwrapper') as sql:
            where = "WHERE profile_id=%(pid)s"
            qdata = {'pid': pid}
            #delete old css entrys
            # commit wird durch Kontextmanager geregelt;
            # einzelne Commits sollten unnötig sein:
            sql.delete("unitracc_export_css", where, qdata)
            # Delete Old Titles
            sql.delete("unitracc_export_profile_titles", where, qdata)
            # Delete Subportal entries
            sql.delete("unitracc_subportal_unitracc_export_profile",
                       "WHERE profile=%(pid)s",  # *nicht* profile_id hier :-(
                       qdata)

            update_profile = {'modification_date': datetime.now(),
                              'active': form.get('active', False),
                              'type_id': form.get('etype'),
                              'manual_css': form.get('manual_css'),
                              'pdfreactor_api_calls':
                                    form.get('pdfreactor_api_calls'),
                              'main_template': form.get('main_template', ''),
                              'browser_id': form.get('browser_id', ''),
                              }
            where_profile = "WHERE id=%(pid)s"
            sql.update("unitracc_export_profile",
                       update_profile,
                       where_profile,
                       qdata)
            title_table = "unitracc_export_profile_titles"

            for title in titles:
                sql.insert(title_table,
                           {'title': title[1],
                            'lang_code': title[0],
                            'profile_id': pid,
                            })
            subportals = form.get('subportal', [])
            if isinstance(subportals, str):
                subportals = [subportals]
            for subportal in subportals:
                subportal_row = sql.select(table="unitracc_subportal",
                                           fields=['id'],
                                           query_data={'uid': subportal},
                                           maxrows=1)
                # Noch kein Subportal vorhanden
                if not subportal_row:
                    new_portal = subs[subportal]
                    subportal_row = sql.insert("unitracc_subportal",
                                               {'uid': subportal,
                                                'subportal': new_portal['title'],
                                                },
                                               returning=['id']).next()
                else:
                    subportal_row = subportal_row[0]

                sql.insert("unitracc_subportal_unitracc_export_profile",
                           {'subportal': subportal_row['id'],
                            'profile': pid})
            pos = 0
            for name in form.get('cssfiles', []):
                pos += 1
                sql.insert("unitracc_export_css",
                           {'css_name': name,
                            'load_position': int(pos),
                            'profile_id': pid,
                            })
        msg = context.getAdapter('message')
        _ = context.getAdapter('translate')
        msg(_('Changes saved.'))
        return redirect("/manage_export_profiles")
    # ------------------------------ ] ... Exportprofil ändern ]
    # ------------------------------- ] ... Exportprofile verwalten ]

    # --- Export erstellen -----
    def export(self):
        """
        Exportiere die Dokumente
        """
        context = self.context
        request = context.REQUEST
        form = request.form
        profile_id = form.get('export')
        if profile_id is not None:
            return self.make_export(profile_id)
        message = context.getAdapter('message')
        _ = translate_dummy
        message(_('Please choose an export profile!'),
                "error")
        return request.response.redirect(tryagain_url(request))

    def make_export(self, profile_id):
        """
        Erstelle den angeforderten Export.

        Bei HTML- und XML-Exporten wird derzeit direkt zur entsprechenden View
        umgeleitet;
        bei PDF-Exporten wird die Generierung asynchron angestoßen
        und per Mail eine Benachrichtigung versandt (geht i.d.R. sehr schnell;
        nach kurzer Zeit lohnt es sich meistens schon, die Seite neu zu laden);
        SCORM-Exporte werden ebenfalls sofort erledigt (durch Aufruf der
        export-Methode des scorm-Browsers).

        TO DO:
        - Optional konfigurierbare Templates verwenden (renderzpt-Adapter)
        """
        context = self.context
        pid = int(profile_id)
        profile = self.getProfile(id=pid)
        profile = profile[pid]
        export_type = profile['etype']
        request = context.REQUEST
        def redirect(request, path):
            u = tryagain_url(request,
                             ('pid', # 'suptitle',
                              'etype',
                              ), path)
            return request.response.redirect(u)
        uri = context.getPath()
        logger.info('make_export: type=%(export_type)r\nuri=%(uri)s', locals())
        path_list = context.getPath().split('/')
        # Falls HTML: direkt weiterleiten, da HTML "on the fly" erzeugt wird
        if export_type == "HTML":
            return redirect(request, uri + "/html_view")

        getAdapter = context.getAdapter
        getBrowser = context.getBrowser
        rc = getAdapter('rc')()
        book = getBrowser('book')
        msg = getAdapter('message')
        _ = getAdapter('translate')
        presentation = getBrowser('presentation')

        brain = context.getHereAsBrain()
        is_book = book.isBook(brain)
        is_presentation = presentation.isPresentation(context.UID())
        dir = export_type.lower()
        if dir == "pdf":
            dir = "pdfs"

        self.path = getConfiguration().product_config.get(dir, {})[dir + '_dir'] + os.sep

        if profile['browser_id']:
            logger.info('SCORM?!')
            if profile['browser_id']:
                return getBrowser('scorm').export(pid)

        if export_type == "XML":
            if is_presentation or is_book:
                self._exportStructureXML(brain, profile)
            elif context.portal_type == "UnitraccCourse":
                self._exportCourseXML(brain, profile)
            else:
                self._exportSimpleXML()
            return redirect(request, uri + "/xml_view")

        if export_type == "PDF":
            try:
                if 1:
                    self._exportPDF(brain, profile)
                elif is_presentation or is_book:
                    self._exportStructurePDF(brain, profile)

                elif context.portal_type == "UnitraccCourse":
                    self._exportCoursePDF(brain, profile)
                else:
                    self._exportSimplePDF(brain, profile)
            except NotImplementedError, e:
                msg(str(e), 'error')
            else:
                msg(_('You will be notified via e-mail'
                      ' as soon as the PDF file is generated.'))

        return redirect(request, uri + "/export_view")

    # ------- XML Export ----------- #
    def _exportStructureXML(self, brain, profile):
        profile_id = profile['profile_id']
        uid = brain.UID
        filename = join(self.path,
                        '%(uid)s-%(profile_id)s.xml' % locals())
        context = self.context
        book = context.getBrowser('book')
        tree = context.getBrowser('tree')
        elements = tree.getNavigationWithBrains(brain)
        if book.isBook():
            elements = [{'current': self.context.getHereAsBrain(),
                         'childs': elements,
                         'portal_type': 'book',
                         }]
        xml_content = self.__build_xml__(elements)
        f = open(filename, "w")
        f.write(xml_content)
        f.close()
        return xml_content

    def _exportCourseXML(self, profile):
        profile_id = profile['profile_id']
        context = self.context
        Bcourse = context.getBrowser('unitracccourse')
        elements = Bcourse.get_complete_tree()
        elements = [{'current': self.context.getHereAsBrain(),
                     'childs': elements,
                     'portal_type': self.context.portal_type,
                     }]
        xml_content = self.__build_xml__(elements, True)
        f = open(self.path + context.UID() + ".xml", "w")
        f.write(xml_content)
        f.close()
        return xml_content

    def _exportSimpleXML(self):
        return

    def __build_xml__(self, elements, course=False):
        head = '<objects xmlns:i18n="http://xml.zope.org/namespaces/i18n">\n'
        foot = '</objects>'
        content = ""

        def folder_object(folder_brain):
            folder_object = folder_brain.getObject()
            stage = folder_object.getBrowser('stage')
            objects = [brain.getObject()
                       for brain in stage.getAsBrains('book-start-page',
                                                      folder_object.UID())
                       ]
            if objects:
                page_object = objects[0]
            else:
                page_object = ''
            transform = folder_object.getBrowser('transform')
            folder_fields = folder_object.Schemata()['default'].fields()
            content = ""
            for field in folder_fields:
                name = field.getName()
                if name.lower().find('type') >= 0:
                    continue
                value = str(field.get(folder_object))
                if not value:
                    # TH: keine leeren Werte transformieren ...
                    continue
                    value = ''

                content += "<%s><![CDATA[%s]]></%s>\n" % (name,
                                                          transform.get(value),
                                                          name)
            if page_object:
                content += "<%s>" % page_object.portal_type
                page_fields = page_object.Schemata()['default'].fields()
                for field in page_fields:
                    name = field.getName()
                    if name.lower().find('type') >= 0:
                        continue
                    value = str(field.get(page_object))
                    if not value:
                        # TH: keine leeren Werte transformieren ...
                        continue
                        value = ''

                    content += "<%s><![CDATA[%s]]></%s>\n" % (name,
                                                              transform.get(value),
                                                              name)
                content += "</%s>" % page_object.portal_type
            return content

        def simple_object(element):
            brain = element['current']
            obj = element['current'].getObject()
            transform = obj.getBrowser('transform')

            fields = obj.Schemata()['default'].fields()

            start_tag = "<%s>\n" % element['portal_type']
            end_tag = "</%s>\n" % element['portal_type']
            content = ""
            for field in fields:
                name = field.getName()
                #raus nehmen von internen daten für Folder und Kurse
                if (name.lower().find('type') >= 0
                    or name in ['xml', 'html_left', 'html_right']
                    ):
                    continue
                value = str(field.get(obj))
                if not value:
                    # TH: keine leeren Werte transformieren ...
                    continue
                    value = ''

                content += "<%s><![CDATA[%s]]></%s>\n" % (name,
                                                          transform.get(value),
                                                          name)

            return start_tag + content + end_tag + "\n"

        def structure_object(element):
            start_tag = "<%s>\n" % element['portal_type']
            end_tag = "</%s>\n" % element['portal_type']
            content = ""
            if element['portal_type'] in ['Folder', 'book']:
                content = folder_object(element['current'])
            if element['portal_type'] == 'UnitraccCourse':
                content = simple_object(element)
            for child in element['childs']:
                if child['childs']:
                    content += structure_object(child)
                else:
                    content += simple_object(child)
            return start_tag + content + end_tag + "\n"
        for element in elements:
            if element['childs']:
                content += structure_object(element)
            else:
                content += simple_object(element)

        res = head + content + foot
        res = res.replace('\x0B', ' ')
        return res
    # ------- PDF Export ----------- #

    def getPDF(self):
        """
        Redirect aufs PDF File
        """
        request = self.context.REQUEST
        name = request.form.get('name')
        return request.response.redirect("@@export/getFile?name=%s" % name)

    def getCookieLines(self):
        """
        Zum Export einer Cookie-Datei, siehe <https://curl.haxx.se/mail/archive-2005-03/0099.html>
        und (gf) templates/cookies.txt.pt
        """
        request = self.context.REQUEST
        # ein schnödes dict mit Schlüsseln und Werten:
        cookies = request.cookies
        # pp(('cookies:', cookies.__class__, cookies))
        domain = '.unitracc.de'
        tailmatch = 'TRUE'
        expires = 'Sun, 27 May 2018 14:10:35 GMT'
        secure = 'FALSE'
        path = '/'
        res = []
        for name, value in cookies.items():
            res.append('\t'.join((domain,
                                  tailmatch,
                                  '/',
                                  secure,
                                  expires,
                                  name,
                                  value,
                                  )))
            continue
            print cookie, cookie.__class__

            print dir(cookie)
            print cookie.__module__

            # pp(dict(cookie))
            res.append('\t'.join((cookie['domain'],
                                  cookie['tailmatch'],
                                  cookie['path'],
                                  cookie['secure'],
                                  cookie['expires'],
                                  cookie['name'],
                                  cookie['value'],
                                  )))
        res.append('')
        return '\r\n'.join(res)

    def _commonExportParams(self, brain, profile):
        profile_id = profile['profile_id']
        context = self.context
        request = context.REQUEST
        myDict = request.form.copy()
        url = brain.getURL()
        myDict['base_url'] = context.portal_url()
        myDict['context'] = context
        myDict['cookie'] = request.cookies  # siehe neu: info['PDFcreator']
        myDict['path'] = self.path  # .writePDF; Dateisystem-Präfix
        myDict['brain'] = brain     # .writePDF; für UID
        myDict['object_url'] = url
        items = [('isPDFExport', True),
                 ('pid', profile_id),
                 ]
        suptitle = myDict.pop('subtitle', None)
        if suptitle:
            items.append(('suptitle', suptitle))
        myDict['url'] = merge_qvars(url+'/html_view', items)
        myDict['title'] = brain.Title
        myDict['pdfreactor_api_calls'] = profile['pdfreactor_api_calls']
        if EXPORT_VIA_HTTP:
            for key in ('base_url',
                        'url',
                        'object_url',
                        ):
                val = myDict[key]
                if val.startswith('https://'):
                    val = 'http' + val[5:]
                    myDict[key] = val
                    logger.info('_CEP: changed %(key)r to %(val)r', locals())
                elif 1:
                    logger.info('_CEP: key %(key)r unchanged (%(val)r)')
        if debug_active:
            pp(('@@export._commonExportParams(...) -->', myDict))
        return myDict

    @log_or_trace(**updated(lot_kwargs))
    def _exportPDF(self, brain, profile):
        logger.info('_exportPDF: arguments for creator ...')
        myDict = self._commonExportParams(brain, profile)
        logger.info('_exportPDF: creating creator for %(path)r ...',
                    myDict)
        creator = PDFCreator(myDict)
        logger.info('_exportPDF: starting thread ...')
        tid = thread.start_new_thread(creator.start, ())
        logger.info('_exportPDF: thread id is %(tid)r', locals())

    # -------------------------------- [ mutmaßlich obsolet ... [
    def _exportCoursePDF(self, brain, profile):
        myDict = self._commonExportParams(brain, profile)
        thread.start_new_thread(PDFCreator(myDict).start, ())
        return

    def _exportStructurePDF(self, brain, profile):
        myDict = self._commonExportParams(brain, profile)
        thread.start_new_thread(PDFCreator(myDict).start, ())
        return

    def _exportSimplePDF(self, brain, profile):
        myDict = self._commonExportParams(brain, profile)
        thread.start_new_thread(PDFCreator(myDict).start, ())
        return

        portal_type = self.context.portal_type
        raise NotImplementedError(_('Sorry; PDF export of %(portal_type)s '
                                    'objects is not yet implemented'
                                    ) % locals())
    # -------------------------------- ] ... mutmaßlich obsolet ]

    # ------- SCORM Export --------- #
    def getScorm(self):
        """
        Exportiere das Element als SCORM
        """

    # --- HTML PDF Preview Export -- #
    def getHTML(self, profile_id, isPDFExport=False):
        """
        Exportiere HTML (z. B. als Vorschau für PDF)
        """

        logger.info('getHTML(%(profile_id)r, %(isPDFExport)r ...', locals())
        OK = 1
        try:
            if not isPDFExport:
                self.canExport(True)
            if not profile_id:
                logger.info('getHTML: keine Profil-ID, Abbruch.')
                return ""
            pid = int(profile_id)
            context = self.context
            if not context:
                logger.error('getHTML: kein Kontext, Abbruch.')
                return ""
            form = context.REQUEST.form
            getAdapter = context.getAdapter
            getBrowser = context.getBrowser
            rc = getAdapter('rc')()
            obj_ = rc.lookupObject(context.UID())
            if not obj_:
                uid = context.UID()
                logger.info('getHTML: UID %(uid)r nicht gefunden, Abbruch.')
                return ""
            brain = obj_.getHereAsBrain()
            book = getBrowser('book')
            is_book = book.isBook(brain)
            presentation = getBrowser('presentation')
            is_presentation = presentation.isPresentation(context.UID())
            content = ""

            transform = getBrowser('transform')
            if is_book or is_presentation:
                logger.info('getHTML: exportiere Struktur')
                content = self._exportStructureHTML(brain, pid)
            elif context.portal_type == "UnitraccCourse":
                logger.info('getHTML: exportiere Kurs')
                content = self._exportCourseHTML(brain, pid)
            else:
                logger.info('getHTML: sonstiger Export')
                rawbyname = getAdapter('rawbyname')
                content = rawbyname('text')
            return transform.get(content, True)
        except Exception as e:
            OK = 0
            logger.error('getHTML: %(e)r', e)
            logger.exception(e)
            raise
        finally:
            if OK:
                logger.info('getHTML: OK')

    def _exportStructureHTML(self, brain, pid):
        context = self.context
        tree = context.getBrowser('tree')
        elements = tree.getNavigationWithBrains(brain, excludeFromNav=False)
        css = self.getSelectedCss(pid)
        structure = [{'Title': context.Title(),
                      'current': brain,
                      'level': 1,
                      'portal_type': 'Folder',
                      'childs': [],
                      }]
        structure[0]['childs'] = elements
        self.logStructure('_exportStructureHTML', structure)

        content = context.unrestrictedTraverse('html_main')(
                    title=context.Title(),
                    content=structure,
                    epilogue=None,
                    prologue=None,
                    css=css)
        return content

    def _exportCourseHTML(self, brain, pid):
        context = self.context
        Bcourse = context.getBrowser('unitracccourse')
        with StopWatch('_exportCourseHTML(%(brain)r, %(pid)r)',
                       mapping=locals(),
                       **sw_kwargs) as stopwatch:
            elements = Bcourse.get_complete_tree()
            stopwatch.lap('.. get_complete_tree')
            css = self.getSelectedCss(pid)
            structure = [{'Title': context.Title(),
                          'current': brain,
                          'level': 1,
                          'portal_type': 'UnitraccCourse',
                          'childs': [],
                          }]
            structure[0]['childs'] = elements
            self.logStructure('_exportCourseHTML', structure)
            stopwatch.lap('.. logStructure. Nun html_main() ...')

            content = context.unrestrictedTraverse('html_main')(
                        title=context.Title(),
                        content=structure,
                        epilogue=None,
                        prologue=None,
                        css=css)

            return content

    # ------- E-Mail --------------- #
    def sendMail(self, status=None, etype=None):
        """
        Sende E-Mail an Nutzer mit Erfolgs- oder Fehlermeldung

        Sende E-Mail and Empfänger über Erfolg/Fehler der Erstellung
        des Objektes.
        Diese Methode kann sowohl als URL, als auch als Methode der Klasse
        aufgerufen werden.
        Bei Aufruf als Methode Parameter übergeben
        Bei Aufruf als URL Parameter=Requestparameter
            -status: War der export erfolgreich oder nicht.
                    type:string  values:"success"/"failure"
            -etype: Welchen Typs war der Export
                    type:string values:"pdf"/"xml"/"scorm"...

        """
        context = self.context
        form = context.REQUEST.form
        status = form.get('status', status)
        etype = form.get('etype', etype)

        if not status or not etype:
            logger.error("missing value to send mail")
            return

        _ = context.getAdapter('translate')

        getBrowser = context.getBrowser
        me = getBrowser('author').get()
        url = context.absolute_url() + "/export_view"
        email = me.getEmail()
        kwargs = {'type': etype.upper(),
                  'title': context.Title(),
                  'url': url,
                  'status': status,
                  'user': me.getFirstname() + " " + me.getLastname()}

        subject = _('Your requested %(type)s export') % kwargs

        subportal = getBrowser('subportal')
        from_address = subportal.get_from_address()
        logger.info('sending mail from %(from_address)r to %(email)r ...',
                    locals())

        mail = getBrowser('unitraccmail')
        mail.set('utf-8', 'mail_export_notify', subject, kwargs)
        mail.renderAsPlainText()
        mail.sendMail(from_address, email)
        logger.info('OK: sent mail to %(email)r',
                    locals())
        return mail.email

    @log_or_trace(**updated(lot_kwargs))
    def _getRawContent(self, obj, ctype, maxdepth=1):
        """
        Gib den Inhalt des Typs <ctype> zurück;
        für "Folder" den der zugeordneten Standardseite.

        obj -- das untersuchte Objekt
        ctype -- 'text' oder 'notes'
        maxdepth -- Abbruchkriterium für Rekursion
        """
        try:
            pt = obj.portal_type
            # pp(locals())
            assert maxdepth >= 0, 'maxdepth: %(maxdepth)r' % locals()
            if pt != 'Folder':
                try:
                    if ctype == "text":
                        return obj.getRawText()
                    elif ctype == "notes":
                        return obj.getRawNotes()
                    logger.error('content(%(obj)r): bogus ctype (%(ctype)r)',
                                 locals())
                    return
                except AttributeError as e:
                    logger.error('%(self)r._gRC: obj=%(obj)r, pt=%(pt)r, ctype=%(ctype)r', locals())
                    logger.exception(e)
                    return
                except Exception as e:
                    logger.error('%(self)r._gRC (Hu?!): obj=%(obj)r, pt=%(pt)r, ctype=%(ctype)r', locals())
                    logger.exception(e)
                    return
            if not maxdepth:
                context = self.context
                logger.error('content(%(context)r, %(ctype)r):'
                             ' max. recursion exceeded',
                             locals())
                return
            stage = self.context.getBrowser('stage')
            for brain in stage.getAsBrains('book-start-page', obj.UID()):
                o = brain.getObject()
                if o is not None:
                    return self._getRawContent(o, ctype, maxdepth-1)
                logger.error('no object found for brain %(brain)r',
                             locals())
            logger.error('no start page found for %(obj)r', locals())
        except Exception as e:
            logger.error('%(self)r._gRC(%(obj)r, %(ctype)r, %(maxdepth)r) failed!', locals())
            logger.error('Exception is %(e)r', locals())
            logger.exception(e)

    # --- Diverse Interne Methoden u.a Inhalte wiedergeben, Permission check...
    def getContent(self, obj, ctype):
        """
        Gib Inhalt der Standardview zurück für Folder
        """
        result = self._getRawContent(obj, ctype, 1)
        if result is None:
            return

        transform = obj.getBrowser('transform')
        return transform.get(result)

    def getURL(self):
        """
        Gib die Absolute URL des Objektes zurück.
        Falls Buch gib URL des Toplevelelements
        """
        context = self.context
        book = context.getBrowser('book')
        brain = context.getHereAsBrain()

        if book.isBook():
            brain = book.getBookFolderAsBrain()
        return brain.getURL()

    def canExport(self, withRaise=False):
        """
        Darf Nutzer Objekt exportieren?

        withRaise -- wirf eine Unauthorized-Exception, wenn Export nicht
                     *erlaubt*; es kann dennoch False zurückgegeben werden,
                     wenn der Export zwar erlaubt wäre, aber nicht möglich ist.
        """
        context = self.context
        logger.debug('%(context)r.canExport(%(withRaise)r) ...', locals())
        book = context.getBrowser('book')
        fieldname = 'text'

        try:
            if book.isBook():
                context = book.getBookFolder()
                logger.debug('context --> %(context)r', locals())
            pt = context.portal_type
            if pt not in ('UnitraccCourse', 'Folder'):
                text = self._getRawContent(context, fieldname)
                if text is None:
                    logger.error(
                            '%(context)r (%(pt)s) has no %(fieldname)r',
                            locals())
                    return False

        except Exception as e:
            logger.exception(e)
            return False

        cp = context.getAdapter('checkperm')
        view = cp('View')
        if not view:
            logger.debug('View-Berechtigung fehlt')
            if withRaise:
                raise Unauthorized()
            else:
                return False
        # XXX bisher keinerlei Bezug zum real angeforderten Exporttyp!
        export = cp('unitracc: Export PDF') or \
                 cp('unitracc: Export XML') or \
                 cp('unitracc: Export HTML') or \
                 cp('unitracc: View PDF') or \
                 cp('unitracc: View XML')

        logger.debug('%(context)r.canExport() --> %(export)r', locals())
        if not withRaise:
            return export
        if not export:
            raise Unauthorized()
        return True

    def getExportPermissions(self):
        """
        Was darf der Nutzer (sehen/machen auf Exportseite)
        """
        context = self.context

        cp = context.getAdapter('checkperm')
        view = cp('View')
        if not view:
            return []
        can_edit = cp('Modify portal content')
        export = {
            # Export erfordert Bearbeitungsrechte:
            'pdf_export': can_edit and cp('unitracc: Export PDF'),
            'xml_export': can_edit and cp('unitracc: Export XML'),
            'html_export': can_edit and cp('unitracc: Export HTML'),
            'scorm_export': can_edit and cp('unitracc: Export SCORM'),
            # Für Ansicht reichen Ansichtsrechte:
            'pdf_view': (can_edit or view) and cp('unitracc: View PDF'),
            'xml_view': (can_edit or view) and cp('unitracc: View XML'),
            'scorm_view': (can_edit or view) and cp('unitracc: View SCORM'),
        }
        return export

    def getExportedFiles(self):
        """
        Gib alle exportierten Dateien zurück.
        """
        uid = self.context.UID()
        conf = getConfiguration()
        files = []
        xml_path = conf.product_config.get('xml', {})['xml_dir'] + os.sep
        pdf_path = conf.product_config.get('pdfs', {})['pdfs_dir'] + os.sep
        for rootdir in (xml_path, pdf_path):
            for fn in os.listdir(rootdir):
                if fn.startswith(uid):
                    try:
                        files.append(self._create_fdict_(rootdir, fn))
                    except IndexError as e:
                        logger.error('getExportedFiles: Error adding %(fn)r in %(rootdir)r', locals())
                        logger.exception(e)
        return files

    def _create_fdict_(self, path, fname):
        try:
            _ = self.context.getAdapter('translate')
            filename = normpath(join(path, fname))
            cdate_ts = getmtime(filename)
            cdate = datetime.fromtimestamp(cdate_ts)
            name_, ext = splitext(fname)
            name = name_.split("-")
            ext = ext[1:]

            pid = int(name[1])
            title = _("Unknown name")
            profile = self.getProfile(id=pid)
            if profile:
                act_lang = self.context.getAdapter('langcode')()

                if act_lang in profile[pid]['title'].keys():
                    title = profile[pid]['title'][act_lang]
                else:
                    key = profile[pid]['title'].keys()[0]
                    title = profile[pid]['title'][key]
            url = self.context.absolute_url()
            if ext.lower() == 'pdf':
                url += "/pdf_view?name=" + fname
            if ext.lower() == 'xml':
                url += "/xml_view?pid=%s" % pid
            mydict = {'type': ext.upper(),
                      'title': ext.upper() + " " + title,
                      'name': fname,
                      'pid': pid,
                      'url': url,
                      'created': cdate.strftime("%d.%m.%Y %H:%M"),
                      }
            return mydict
        except IndexError as e:
            pp(('_create_fdict_:', locals()))
            raise

    def getExportProfileTypes(self):
        """
        gib die Werte für die Profile aus DB wieder
        """
        with self.context.getAdapter('sqlwrapper') as sql:
            return sql.select("unitracc_export_type")

    def getExportTypes(self):
        """
        Was darf der Nutzer exportieren?
        """
        types = []
        pdf = self.getProfilesByEtype("PDF")
        xml = self.getProfilesByEtype("XML")
        html = self.getProfilesByEtype("HTML")
        scorm = self.getProfilesByEtype("SCORM")
        perms = self.getExportPermissions()

        if perms.get('pdf_export') and pdf:
            types.append(pdf)
        if perms.get('xml_export') and xml:
            types.append(xml)
        if perms.get('html_export') and html:
            types.append(html)
        if perms.get('scorm_export') and html:
            types.append(scorm)

        return types

    def getFile(self, pid=None, ftype="pdf"):
        """
        Gib den Inhalt der Exportdatei zurück
        """
        self.canExport(True)
        context = self.context
        request = context.REQUEST
        uid = context.UID()
        conf = getConfiguration()
        perms = self.getExportPermissions()
        if ftype == "xml" and (perms['xml_export'] or perms['xml_view']):
            fname = uid + ".xml"
            path = conf.product_config.get('xml', {})['xml_dir'] + os.sep
            fpath = path + uid + "-" + pid + ".xml"
            request.response.setHeader("Content-type", "text/xml")
        if ftype == "pdf" and (perms['pdf_export'] or perms['pdf_view']):
            path = conf.product_config.get('pdfs', {})['pdfs_dir'] + os.sep
            fname = request.get('name')
            fpath = path + fname
            request.response.setHeader("Content-type", "application/pdf")

        try:
            f = open(fpath, "r")
            content = f.read()
            f.close()

        except IOError:
            content = ""
        finally:
            request.response.setHeader('Content-Disposition',
                                'attachment; filename="%s"' % fname)
            return content

    # ------------- Interne Verwaltungsmethoden ------
    def getProfileTitle(self, id):
        """
        Nur den Profiltitel ermitteln
        (noch keine Priorisierung der Sprache;
        es wird der erste vorgefundene nicht-leere Titel genommen)
        """
        context = self.context
        getAdapter = context.getAdapter
        with getAdapter('sqlwrapper') as sql:
            for row in sql.select('unitracc_export_profile_titles',
                                  query_data={'profile_id': id}):
                val = row['title']
                if val:
                    val = val.strip()
                    if val:
                        return val
        _ = getAdapter('translate')
        return _('Profile %s') % id

    def getProfile(self, all=False, id=None):
        """
        Gib ein dict von dicts zurück; Schlüssel der obersten Ebene ist
        unitracc_export_profile.id (eine Ganzzahl).

        all - Wenn True, wird eine übergebene id ignoriert;
              wenn nicht im primären Subportal, werden nur die Exportprofile
              des aktuellen Subportals ausgegeben.
              res[id]['subportal'] ist eine Liste von Namen
        id - Wenn übergeben, werden die Namen der Stylesheets
             im Schlüssel 'css' zurückgegeben;
             res[id]['subportal'] ist eine Liste von UIDs.
        """
        # Siehe neue View: export_profiles_view
        context = self.context
        Bsubportal = context.getBrowser('subportal')
        current_subportal = Bsubportal.get_current_id()

        query_data = {}
        if all:
            assert not id
            default_subportal = Bsubportal._default_uid()
            if current_subportal != default_subportal:
                query_data['uid'] = current_subportal
            SUBPORTAL_FIELD = 'subportal'
        elif id:
            id = int(id)
            query_data['id'] = id
            SUBPORTAL_FIELD = 'uid'
        else:
            # aus Kontinuitätsgründen; der normale Rückgabewert ist ein dict!
            return []

        mydict = {}
        with context.getAdapter('sqlwrapper') as sql:
            result = sql.select('export_profiles_view',
                                query_data=query_data)
            for row in result:
                profile_id = int(row['id'])
                if profile_id not in mydict:
                    mydict[profile_id] = {}
                    entry = mydict[profile_id]
                    entry['profile_id'] = profile_id
                    entry['subportal'] = []
                    entry['title'] = {}
                    # direkt aus unitracc_export_profile:
                    entry['creator'] = row['creator']
                    entry['creation_date'] = row['creation_date'
                                                 ].strftime('%d.%m.%Y %H:%M')
                    entry['active'] = row['active']
                    entry['manual_css'] = row['manual_css']
                    # aus unitracc_export_type:
                    entry['etype'] = row['etype']
                    entry['etype_id'] = row['etype_id']
                    entry['pdfreactor_api_calls'] = row['pdfreactor_api_calls']
                    entry['main_template'] = row['main_template']
                    entry['browser_id'] = row['browser_id']

                else:
                    entry = mydict[profile_id]

                subportal = row[SUBPORTAL_FIELD]
                if subportal not in entry['subportal']:
                    entry['subportal'].append(subportal)
                lang_code = row['lang_code']
                lang_title = row['title']
                if (lang_code
                    and lang_title
                    ):
                    entry['title'][lang_code] = lang_title

            # Nur eine vorhandene <id> (u. a. mit Namen) hat evtl. CSS-Stylesheets:
            if id and id in mydict:
                css_files = sql.select("export_css_view",
                                       query_data={'profile_id': id})
                mydict[id]['css'] = [x['css_name']
                                     for x in css_files
                                     ]
            return mydict

    def getCSS(self):
        context = self.context
        portal = context.getAdapter('portal')()
        css_files = [x.getId() for x in portal.portal_css.getResources()]
        return css_files

    def getProfilesByEtype(self, etype):
        #  Gib alle Profile je nach Exporttyp (XML, PDF, HTML) zurück;
        #  berücksichtige dabei das Subportal
        # TODO: statt komplizierter Logik hier eine SQL-Sicht verwenden!
        # TODO: Einzelaufrufe (pro etype) auflösen
        context = self.context
        sql = context.getAdapter('sqlwrapper')
        sub = context.getBrowser('subportal').get_current_id()
        profile_table = "unitracc_export_profile"
        title_table = "unitracc_export_profile_titles"
        type_table = "unitracc_export_type"
        subportal_export_table = "unitracc_subportal_unitracc_export_profile"
        subportal_table = "unitracc_subportal"
        query = {'tables': ",".join([profile_table, title_table,
                                    type_table, subportal_export_table,
                                    subportal_table])}
        sql_query = "SELECT %(fields)s FROM %(tables)s WHERE %(where)s;"
        where = """%s.etype='%s'
        AND %s.type_id=%s.id
        AND %s.profile_id=%s.id
        AND %s.active='t'
        AND %s.profile=%s.id
        AND %s.uid = '%s'
        AND %s.id = %s.subportal""" % (type_table, etype,
                                      profile_table, type_table,
                                      title_table, profile_table,
                                      profile_table,
                                      subportal_export_table, profile_table,
                                      subportal_table, sub,
                                      subportal_table, subportal_export_table)
        fields = ("%s.id, %s.id as eid, %s.etype, %s.title, %s.lang_code"
                  % (profile_table, type_table, type_table,
                     title_table, title_table,
                     ))

        query['where'] = where
        query['fields'] = fields

        result = sql.query(sql_query % query, {})
        res = {}
        for row in result:
            rid = row['id']

            if not rid in res.keys():
                entry = res[rid] = {}
                entry['titles'] = {}
                entry['etype'] = row['etype']
                entry['eid'] = row['eid']
                code = row['lang_code']
                entry['titles'][code] = row['title']
            else:
                entry = res[rid]
                code = row['lang_code']
                entry['titles'][code] = row['title']

        return res

    def getSelectedCss(self, pid):
        """
        Gib für die übergebene Profil-ID zurück:
        - die zugeordneten Stylesheets ('files')
        - das handgeschriebene Korrektor-Stylesheet ('manual')
        """
        context = self.context
        # TODO: readonly
        with context.getAdapter('sqlwrapper') as sql:
            # FIXME: SQL injection verhindern!
            # Siehe neue Sicht export_css_view
            result = sql.query("""\
            SELECT css_name as name,
                   load_position
              FROM unitracc_export_css
             WHERE profile_id=%s
             ORDER BY load_position;""" % pid, {})
            manual_css = sql.query("""\
            SELECT manual_css
            FROM unitracc_export_profile
            WHERE id=%s""" % pid, {})
            final = {'files': result,
                     'manual': None}
            if manual_css:
                final['manual'] = manual_css[0]
            return final

    def getRawProfile(self, pid, active=True):
        """
        Gib die "rohen" Profildaten zurück
        """
        context = self.context
        # TODO: readonly
        with context.getAdapter('sqlwrapper') as sql:
            # TODO: fetchone
            query_data = {'id': pid}
            if active is not None:
                query_data['active'] = active

            res = sql.select('unitracc_export_profile',
                             query_data=query_data,
                             maxrows=1)  # limit
            if res:
                return res[0]
            else:
                return None

    def logStructure(self, name, data):
        """
        Debugging/Entwicklung:
        protokolliere eine Datenstruktur
        """
        if not debug_active:
            return
        with StopWatch('logStructure(%(name)r, ...)',
                       mapping=locals(),
                       **sw_kwargs) as stopwatch:
            context = self.context
            val = context.REQUEST.form.get('reset_log', '')
            if val:
                reset_log = makeBool(val)
            else:
                reset_log = False
            mode = reset_log and 'w' or 'a'
            timestamp = strftime('%A, %H:%M:%S')
            filename = join(dirname(__file__), '_struct-log.py')
            with open(filename, mode) as fo:
                fo.write('\n\n')
                fo.write('# %s [ %s ... [\n' % (timestamp, name))
                fo.write(pformat(data))
                fo.write('\n')
                fo.write('# %s ] ... %s ]\n' % (timestamp, name))
                fo.write('\n')
            print '*' * 79
            print '*   Struktur geschrieben nach', filename
            logger.info('%(name)s: Struktur geschrieben nach %(filename)s',
                        locals())
