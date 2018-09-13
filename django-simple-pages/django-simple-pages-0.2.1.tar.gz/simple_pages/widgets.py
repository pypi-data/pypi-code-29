"""Widgets for the simple_pages app."""

import json

from django import forms


class CodeMirrorTextarea(forms.Textarea):
    """Textarea using the CodeMirror javascript widget."""

    codemirror = "simple_pages/vendor/codemirror"
    css = [f"{codemirror}/lib/codemirror.css"]
    js = [f"{codemirror}/lib/codemirror.js"]

    def __init__(self, attrs=None, mode=None, config=None):
        """Initialize the widget."""
        super(CodeMirrorTextarea, self).__init__(attrs=attrs)

        self.mode = mode or "html"
        self.config = config or {
            "mode": self.mode,
            "fixedGutters": True,
            "lineNumbers": True,
        }

        if self.mode == "htmlmixed":
            # This module has dependencies that need to be included first.
            modes = [
                f"{self.codemirror}/mode/css.js",
                f"{self.codemirror}/mode/javascript.js",
                f"{self.codemirror}/mode/xml.js",
                f"{self.codemirror}/mode/htmlmixed.js",
            ]
        else:
            modes = [
                f"{self.codemirror}/mode/{self.mode}.js",
            ]

        self.js.extend(modes)

    @property
    def media(self):
        """Return the media required by this widget."""
        return forms.Media(
            css={"all": self.css},
            js=self.js,
        )

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget."""
        default = super(CodeMirrorTextarea, self).render(
            name=name,
            value=value,
            attrs=attrs,
            renderer=renderer,
        )

        script = f"""
            <script type="text/javascript">
               CodeMirror.fromTextArea(
                   document.getElementById("id_{name}"),
                   {json.dumps(self.config)}
               )
            </script>
        """
        return "\n".join([default, script])
