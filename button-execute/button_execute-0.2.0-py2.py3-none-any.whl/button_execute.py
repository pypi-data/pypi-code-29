from traitlets import Unicode, Int, CaselessStrEnum, Bool
from ipywidgets import DOMWidget, register, widget_serialization
from ipywidgets.widgets import CallbackDispatcher
from ipywidgets.widgets.trait_types import InstanceDict
from ipywidgets.widgets.widget_button import ButtonStyle


@register
class ExecuteButton(DOMWidget):
    _view_name = Unicode('ExecuteButtonView').tag(sync=True)
    _model_name = Unicode('ExecuteButtonModel').tag(sync=True)
    _view_module = Unicode('jupyter-button_execute').tag(sync=True)
    _model_module = Unicode('jupyter-button_execute').tag(sync=True)
    _view_module_version = Unicode('^0.2.0').tag(sync=True)
    _model_module_version = Unicode('^0.2.0').tag(sync=True)

    # Attributes
    button_text = Unicode('Execute next cells', help="The button's caption.").tag(sync=True)
    n_next_cells = Int(1, help="The number of cells to execute.").tag(sync=True)
    disabled = Bool(False, help="Disable the button").tag(sync=True)

    button_style = CaselessStrEnum(
        values=['primary', 'success', 'info', 'warning', 'danger', ''], default_value='',
        help="""Use a predefined styling for the button.""").tag(sync=True)

    style = InstanceDict(ButtonStyle).tag(sync=True, **widget_serialization)

    def __init__(self, **kwargs):
        super(ExecuteButton, self).__init__(**kwargs)
        self._click_handlers = CallbackDispatcher()
        self.on_msg(self._handle_button_msg)

    def on_click(self, callback, remove=False):
        """Register a callback to execute when the button is clicked.
        The callback will be called with one argument, the clicked button
        widget instance.
        Parameters
        ----------
        callback: The function to call
        remove: bool (optional)
            Set to true to remove the callback from the list of callbacks.
        """
        self._click_handlers.register_callback(callback, remove=remove)

    def click(self):
        """Programmatically trigger a click event.
        This will call the callbacks registered to the clicked button
        widget instance.
        """
        self._click_handlers(self)

    def _handle_button_msg(self, _, content, buffers):
        """Handle a msg from the front-end.
        Parameters
        ----------
        content: dict
            Content of the msg.
        """
        if content.get('event', '') == 'click':
            self.click()
