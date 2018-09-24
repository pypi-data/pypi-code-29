import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText, ControlButton, ControlLabel
from pybpod_alyx_module.module_api import AlyxModule
from AnyQt.QtWidgets import QLineEdit

from pybpodgui_api.models.project import Project
from pybpodgui_api.models.subject import Subject

class AlyxDetails(AlyxModule, BaseWidget):

    TITLE = 'Subject Details'

    def __init__(self, _subject):
        BaseWidget.__init__(self, self.TITLE)
        AlyxModule.__init__(self)

        self._nickname = ControlText('Nickname:',default = _subject.name)
        self._species = ControlText('Species', default = _subject.alyx_species)
        self._sex = ControlText('Sex:', default = _subject.alyx_species)
        self._birth = ControlText('Birth Date:', default = _subject.alyx_birth_date)
        self._death = ControlText('Death Date:', default = _subject.alyx_death_date)
        self._alive = ControlText('Alive:', default = str(_subject.alyx_alive))
        #self._ = ControlText('', default = )

        self.set_margin(10)

        self._nickname.enabled = False
        self.formset = [
            '_nickname',
            '_species',
            '_sex',
            '_birth',
            '_death',
            '_alive'
        ]