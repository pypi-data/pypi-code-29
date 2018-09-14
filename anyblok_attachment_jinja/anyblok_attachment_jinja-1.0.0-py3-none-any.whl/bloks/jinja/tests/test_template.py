# This file is a part of the AnyBlok / Attachment / Jinja api project
#
#    Copyright (C) 2018 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok.tests.testcase import BlokTestCase
from ..exceptions import TemplateJinjaException


class TestJinja(BlokTestCase):

    def test_html(self):
        template = self.registry.Attachment.Template.Jinja.insert(
            name='test',
            template_path='report-jinja#=#tests/tmpl.jinja2',
            jinja_paths='report-jinja#=#tests',
            contenttype='text/html',
            model='Model.System.Blok',
            filename='mypage.html')
        document = self.registry.Attachment.Document.insert(
            template=template,
            data={'title': 'My page', 'description': 'Hello world !!'}
        )
        get_file = document.get_file()
        wanted = {
            'contenttype': 'text/html',
            'file': (
                b'<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <title>'
                b'My page</title>\n  </head>\n  <body>\n    \nHello world !!'
                b'\n\n  </body>\n</html>'
            ),
            'file_added_at': get_file['file_added_at'],
            'filename': 'mypage.html',
            'filesize': 126,
            'hash': (
                b"\x80]\xb3\xe9j'\x89P\xf4\xedB\xe8\xdc\xce\x0f\xe2\xc2\xb7"
                b'\x8e*;q\xba(\x81\x1c\x17\x1dW\x1e\x02\xf2'
            ),
        }
        self.assertEqual(get_file, wanted)

    def test_pdf(self):
        page = self.registry.Attachment.WkHtml2Pdf.Page.insert(
            label="A4", size="A4")
        wkhtml2pdf = self.registry.Attachment.WkHtml2Pdf.insert(
            label="Custom", page=page)
        template = self.registry.Attachment.Template.Jinja.insert(
            name='test',
            template_path='report-jinja#=#tests/tmpl.jinja2',
            jinja_paths='report-jinja#=#tests',
            wkhtml2pdf_configuration=wkhtml2pdf,
            contenttype='application/pdf',
            model='Model.System.Blok',
            filename='mypage.html')
        document = self.registry.Attachment.Document.insert(
            template=template,
            data={'title': 'My page', 'description': 'Hello world !!'}
        )
        get_file = document.get_file()
        self.assertEqual(get_file['contenttype'], 'application/pdf')
        self.assertTrue(get_file['file'])

    def test_pdf_without_wkhtml2pdf(self):
        with self.assertRaises(TemplateJinjaException):
            self.registry.Attachment.Template.Jinja.insert(
                name='test',
                template_path='report-jinja#=#tests/tmpl.jinja2',
                contenttype='application/pdf',
                model='Model.System.Blok',
                jinja_paths='report-jinja#=#tests'
            )

    def test_bad_jinja_paths(self):
        template = self.registry.Attachment.Template.Jinja.insert(
            name='test',
            template_path='report-jinja#=#tests/tmpl.jinja2',
            contenttype='text/html',
            model='Model.System.Blok',
            jinja_paths='report-jinja#=#tests/tmpl.jinja2'
        )
        document = self.registry.Attachment.Document.insert(
            template=template,
            data={'title': 'My page', 'description': 'Hello world !!'}
        )
        with self.assertRaises(TemplateJinjaException):
            document.get_file()
