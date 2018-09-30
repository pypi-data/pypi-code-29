"""
Utilities for handling assets packaged in a Pakk file while working with Flask.
"""
from mimetypes import guess_type
from flask import send_file, render_template_string, send_from_directory as flask_send_from_directory, render_template as flask_render_template
from werkzeug.exceptions import NotFound
from pakk import Pakk

class PakkTemplate:
    """
    An object relating a pakkfile and a template file expected to be in the pakkfile.
    """
    def __init__(self, pakkfile: Pakk, template_name: str):
        self.pakkfile = pakkfile
        self.template_name = template_name

def send_from_directory(directory, filename, **options):
    """
    A replacement for Flask's send_from_directory that supports pakked files.

    if directory is an instance of a Pakk object, then this method will decrypt the file within the Pakk and
    return the decrypted contents.
    """

    if isinstance(directory, Pakk):
        if directory.has_blob(filename):
            content = directory.get_blob(filename)

            guessed_type = guess_type(filename)
            mimetype = options.get("mimetype")

            if not mimetype:
                mimetype = f"{guessed_type[0]};"
                if not guessed_type[1]:
                    if guessed_type[0] is not None and guessed_type[0].startswith("text/"):
                        mimetype += f" charset=utf-8"
                else:
                    mimetype += f" charset={guessed_type[1]}"

            content.stream.seek(0)

            return send_file(
                content.stream,
                mimetype=mimetype
            )

        return NotFound()

    return flask_send_from_directory(directory, filename, **options)

def render_template(source, **context):
    """
    A replacement for Flask's render_template that supports pakked files.

    if source is an instance of PakkTemplate and source.template_name exists within source.pakkfile under the subpath 'templates', then the pakked file is rendered.

    if source is an instance of PakkTemplate and source.template_name does not exist within source.pakkfile, then source.template_name is
    passed down to flask.render_template as source.

    if source is not an instance of PakkTemplate, then this function defers to flask.render_template

    """
    if isinstance(source, PakkTemplate):

        new_template_name = f"templates/{source.template_name}"
        if source.pakkfile.has_blob(new_template_name):
            blob = source.pakkfile.get_blob(new_template_name)
            data = blob.get_data()
            text = data.decode("utf-8")
            return render_template_string(text, **context)

        return flask_render_template(source.template_name, **context)

    return flask_render_template(source, **context)
