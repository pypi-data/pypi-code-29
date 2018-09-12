import logging

from cliff.command import Command
from jinja2 import (Environment, FileSystemLoader,
                    StrictUndefined, Undefined,
                    make_logging_undefined, select_autoescape)


class Template(Command):
    """Template file(s)"""

    LOG = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Template, self).get_parser(prog_name)
        parser.add_argument('--check-defined',
                            action='store_true',
                            dest='check_defined',
                            default=False,
                            help="Just check for undefined variables")
        parser.add_argument('source',
                            nargs="?",
                            help="input Jinja2 template source",
                            default=None)
        parser.add_argument('dest',
                            nargs="?",
                            help="templated output destination " +
                                 "('-' for stdout)",
                            default=None)
        return parser

    def take_action(self, parsed_args):
        self.LOG.debug('templating file(s)')
        self.app.secrets.read_secrets_and_descriptions()
        template_vars = self.app.secrets.items()
        template_loader = FileSystemLoader('.')
        base = Undefined if parsed_args.check_defined is True \
            else StrictUndefined
        LoggingUndefined = make_logging_undefined(
            logger=self.LOG,
            base=base)
        template_env = Environment(
            loader=template_loader,
            autoescape=select_autoescape(
                disabled_extensions=('txt',),
                default_for_string=True,
                default=True,
            ),
            undefined=LoggingUndefined)
        template = template_env.get_template(parsed_args.source)
        output_text = template.render(template_vars)
        if parsed_args.check_defined is False:
            if parsed_args.dest == "-":
                print(output_text)
            else:
                with open(parsed_args.dest, 'w') as f:
                    f.writelines(output_text)

# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
