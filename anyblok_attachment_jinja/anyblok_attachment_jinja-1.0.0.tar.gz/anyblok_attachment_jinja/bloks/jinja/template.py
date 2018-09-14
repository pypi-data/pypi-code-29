# This file is a part of the AnyBlok / Attachment / Jinja api project
#
#    Copyright (C) 2018 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok import Declarations
from anyblok.column import UUID, Text, Selection, Json
from anyblok.relationship import Many2One
from .exceptions import TemplateJinjaException
import jinja2
from jinja2.sandbox import SandboxedEnvironment
from anyblok_attachment.bloks.report.common import format_path
import os

register = Declarations.register
Attachment = Declarations.Model.Attachment
Mixin = Declarations.Mixin
TYPE = 'jinja'


@Declarations.register(Attachment)
class Template:

    @classmethod
    def get_template_type(cls):
        res = super(Template, cls).get_template_type()
        res.update({TYPE: 'Jinja templating'})
        return res


@Declarations.register(Attachment.Template)
class Jinja(Mixin.WkHtml2Pdf, Attachment.Template):
    """Jinja templating"""
    TYPE = TYPE

    uuid = UUID(
        primary_key=True, nullable=False, binary=False,
        foreign_key=Attachment.Template.use('uuid').options(ondelete='cascade'))
    jinja_paths = Text(nullable=False)
    contenttype = Selection(
        selections={
            'text/html': 'HTML',
            'application/pdf': 'PDF',
        }, default='application/pdf', nullable=False)
    options = Json(default={}, nullable=False)
    wkhtml2pdf_configuration = Many2One(
        model=Declarations.Model.Attachment.WkHtml2Pdf,
        nullable=True)

    def check_flush_validity(self):
        super(Jinja, self).check_flush_validity()
        if self.contenttype == 'application/pdf':
            if not self.wkhtml2pdf_configuration:
                raise TemplateJinjaException(
                    "No WkHtml2Pdf configuration for %r" % self)

    def update_document(self, document, file_, data):
        super(Jinja, self).update_document(document, file_, data)
        document.contenttype = self.contenttype

    def render(self, data):
        if self.contenttype == 'text/html':
            return self.render_html(data)

        return self.render_pdf(data)

    def render_html(self, data):
        jinja_paths = []
        if self.jinja_paths:
            for jinja_path in self.jinja_paths.split(','):
                jinja_path = format_path(jinja_path.strip())
                if not os.path.isdir(jinja_path):
                    raise TemplateJinjaException(
                        "%r must be a folder" % jinja_path)

                jinja_paths.append(jinja_path)

        jinja_env = SandboxedEnvironment(
            loader=jinja2.FileSystemLoader(jinja_paths),
            undefined=jinja2.StrictUndefined,
        )
        parser = self.get_parser()
        if not hasattr(parser, 'serialize_jinja_options'):
            raise TemplateJinjaException(
                (
                    "The parser %r must declare a method "
                    "'serialize_jinja_options' for %r"
                ) % (parser, self)
            )

        options = self.get_parser().serialize_jinja_options(self.options)
        return jinja_env.from_string(self.get_template()).render(
            data=data, str=str, **options).encode('utf-8')

    def render_pdf(self, data):
        html_content = self.render_html(data)
        return self.wkhtml2pdf(html_content)
