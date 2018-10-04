from traitlets import Unicode, Int, CaselessStrEnum
from ipywidgets import DOMWidget, register, widget_serialization
from ipywidgets.widgets.trait_types import InstanceDict
from ipywidgets.widgets.widget_button import ButtonStyle


@register
class ExecuteButton(DOMWidget):
    _view_name = Unicode('ExecuteButtonView').tag(sync=True)
    _model_name = Unicode('ExecuteButtonModel').tag(sync=True)
    _view_module = Unicode('jupyter-button_execute').tag(sync=True)
    _model_module = Unicode('jupyter-button_execute').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    # Attributes
    button_text = Unicode('Execute next cells', help="The button's caption.").tag(sync=True)
    n_next_cells = Int(1, help="The number of cells to execute.").tag(sync=True)

    button_style = CaselessStrEnum(
        values=['primary', 'success', 'info', 'warning', 'danger', ''], default_value='',
        help="""Use a predefined styling for the button.""").tag(sync=True)

    style = InstanceDict(ButtonStyle).tag(sync=True, **widget_serialization)

