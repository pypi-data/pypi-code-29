"""Define a Jupyter Notebook extension to export Notebooks to PDF.

This module takes the selected Jupyter Notebook files and converts
them to a single PDF.
"""

import os
import io
from typing import List, Dict, TYPE_CHECKING, Union

from notebook.base.handlers import IPythonHandler, web, path_regex, FilesRedirectHandler
from notebook.nbconvert.handlers import _format_regex
from nbconvert import PDFExporter
from notebook.utils import url_path_join
from ipython_genutils import text

from pdfrw import PdfWriter, PdfReader
import thermohw

if TYPE_CHECKING:
    from notebook.notebookapp import NotebookWebApplication  # noqa: F401 (typing)

from ._version import __version__  # noqa: F401

thermohw_dir: str = os.path.abspath(os.path.dirname(thermohw.__file__))


def _jupyter_server_extension_paths() -> List[Dict[str, str]]:
    return [{
        "module": "convert_and_download"
    }]


# Jupyter Extension points
def _jupyter_nbextension_paths() -> List[Dict[str, str]]:
    return [dict(
        section="tree",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="convert_and_download",
        # _also_ in the `nbextension/` namespace
        require="convert_and_download/main")]


class DLConvertHandler(IPythonHandler):
    """Handle converting and downloading a set of Notebooks to PDF."""

    SUPPORTED_METHODS = ('GET',)

    @web.authenticated
    def get(self, format: str, path: str):
        """Handle the GET method call."""
        if format != 'pdf':
            self.log.exception('format must be pdf')
            raise web.HTTPError(500, 'format must be pdf')

        self.config.PDFExporter.preprocessors = [thermohw.ExtractAttachmentsPreprocessor]
        self.config.PDFExporter.template_file = os.path.join(thermohw_dir, 'homework.tpl')
        self.config.PDFExporter.filters = {'convert_div': thermohw.convert_div,
                                           'convert_raw_html': thermohw.convert_raw_html}
        self.config.PDFExporter.latex_count = 1

        exporter = PDFExporter(config=self.config, log=self.log)
        exporter.writer.build_directory = '.'

        pdfs = []

        path = path.strip('/').strip()
        paths = path.split('.ipynb')

        for path in paths:
            if not path:
                continue
            path += '.ipynb'
            # If the notebook relates to a real file (default contents manager),
            # give its path to nbconvert.
            ext_resources_dir: Union[str, None]
            basename: str
            os_path: str
            if hasattr(self.contents_manager, '_get_os_path'):
                os_path = self.contents_manager._get_os_path(path)
                ext_resources_dir, basename = os.path.split(os_path)
            else:
                ext_resources_dir = None

            model: Dict[str, str] = self.contents_manager.get(path=path)
            name: str = model['name']
            if model['type'] != 'notebook':
                # not a notebook, redirect to files
                return FilesRedirectHandler.redirect_to_files(self, path)

            nb = model['content']

            self.set_header('Last-Modified', model['last_modified'])

            # create resources dictionary
            mod_date: str = model['last_modified'].strftime(text.date_format)
            nb_title: str = os.path.splitext(name)[0]

            config_dir: str = self.application.settings['config_dir']

            resource_dict: Dict[str, str] = {
                "metadata": {
                    "name": nb_title,
                    "modified_date": mod_date
                },
                "config_dir": config_dir,
            }

            if ext_resources_dir:
                resource_dict['metadata']['path'] = ext_resources_dir

            output: bytes
            try:
                output, _ = exporter.from_notebook_node(
                    nb,
                    resources=resource_dict
                )
            except Exception as e:
                self.log.exception("nbconvert failed: %s", e)
                raise web.HTTPError(500, "nbconvert failed: %s" % e)

            pdfs.append(io.BytesIO(output))

        writer = PdfWriter()
        for pdf in pdfs:
            writer.addpages(PdfReader(pdf).pages)
        bio = io.BytesIO()
        writer.write(bio)
        bio.seek(0)
        output = bio.read()
        bio.close()

        # Force download if requested
        if self.get_argument('download', 'false').lower() == 'true':
            filename = 'final_output.pdf'
            self.set_header('Content-Disposition',
                            'attachment; filename="{}"'.format(filename))

        # MIME type
        if exporter.output_mimetype:
            self.set_header('Content-Type',
                            '{}; charset=utf-8'.format(exporter.output_mimetype))

        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.finish(output)


def load_jupyter_server_extension(nb_server_app: 'NotebookWebApplication') -> None:
    """Call when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    # _format_regex = r"(?P<format>\w+)"
    # path_regex = r"(?P<path>(?:(?:/[^/]+)+|/?))"
    route_pattern = url_path_join(web_app.settings['base_url'],
                                  r"/dlconvert/{fmt_regex}{path_regex}".format(
                                  fmt_regex=_format_regex, path_regex=path_regex))
    web_app.add_handlers(host_pattern, [(route_pattern, DLConvertHandler)])
